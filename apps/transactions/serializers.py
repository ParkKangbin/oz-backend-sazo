from rest_framework import serializers
from apps.transactions.models import (
    TransactionHistory,
    TRANSACTION_IO_TYPE_CHOICES,
    TRANSACTION_METHOD_CHOICES,
)


class TransactionSerializer(serializers.ModelSerializer):
    # ModelSerializer는 필드를 별도로 선언하지 않으면 Meta 클래스에서 지정한 모델의 필드를 읽어와서 해당 필드 타입이 맞는지 유효성 검증을 실행합니다.
    # 하지만 Choice 필드의 경우 모델에서는 CharField로 지정하기 때문에 문자열인지만 확인하지 우리가 정한 선택지에 해당하는지는 검사하지 않습니다.
    # 따라서 별도로 ChoiceField로 지정하여 선택지에 맞게 데이터가 들어왔는지 검사하는 것입니다.
    io_type = serializers.ChoiceField(choices=TRANSACTION_IO_TYPE_CHOICES)  
    transaction_type = serializers.ChoiceField(choices=TRANSACTION_METHOD_CHOICES)

    class Meta:
        model = TransactionHistory
        fields = [
            "id",
            "account",
            "amount",
            "balance_after_transaction",
            "description",
            "io_type",
            "transaction_type",
            "transaction_date",
            "transaction_update",
        ]
        read_only_fields = [
            "id",
            "transaction_date",
            "transaction_update",
            "balance_after_transaction",
        ]

    def create(self, validated_data): # validated_data는 데이터 검증이 된 데이터들만 모임
        account = validated_data["account"]       # 거래할 계좌 가져오기
        amount = validated_data["amount"]         # 거래 금액 가져오기
        io_type = validated_data["io_type"]       # 입금/출금 여부 가져오기

        current_balance = account.balance           # 현재 계좌 잔액 확인

        # 입금이면 잔액에 더하기, 출금이면 빼기 (잔액 부족 시 에러 발생)
        if io_type == "DEPOSIT":
            new_balance = current_balance + amount
        elif io_type == "WITHDRAW":
            if current_balance < amount:
                raise serializers.ValidationError("잔액이 부족합니다.")
            new_balance = current_balance - amount
        else:
            raise serializers.ValidationError("입출금 유형이 올바르지 않습니다.")

        # 거래 이후 잔액을 기록해둠 (조회 시 보여주기 위함)
        validated_data["balance_after_transaction"] = new_balance

        # 거래내역 DB에 저장
        transaction = TransactionHistory.objects.create(**validated_data)

        # 계좌 잔액도 실제로 반영
        account.balance = new_balance
        account.save()

        return transaction

    def update(self, instance, validated_data):  
        # 금액이나 입출금 방향은 수정 불가. 설명과 거래 방식만 변경 가능
        instance.description = validated_data.get("description", instance.description)
        instance.transaction_type = validated_data.get("transaction_type", instance.transaction_type)
        instance.save()
        return instance