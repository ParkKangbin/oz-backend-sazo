from rest_framework import serializers
from apps.users.models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email","nickname","name","password","phone_number"]

    def create(self,validated_data):
        data = validated_data
        pure_password = data.pop("password")
        user = CustomUser(**data)

        user.set_password(pure_password)
        user.save()
        return user
    
