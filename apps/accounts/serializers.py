from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    bank_name = serializers.SerializerMethodField()  # 한글 이름 표시용

    class Meta:
        model = Account
        fields = [# 계좌를 보여주고 등록하고 삭제하는 거니까 이정도만 해도 필수항목이라고 판단함 아마? ㅎ
            'id', 'account_number', 'bank_code', 'bank_name',
            'account_type', 'balance', 'user'
        ]
        read_only_fields = ['user']  # user는 자동으로 넣음

    def get_bank_name(self, obj):
        return obj.get_bank_code_display() # 뱅크 코드 입력시 뱅크 이름이 출력됨 
