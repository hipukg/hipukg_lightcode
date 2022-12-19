from rest_framework import  serializers
from .models import MyUser

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, write_only=True, required=True)

    class Mate:
        model = MyUser
        fields = ['email', 'username', 'password', 'password2']
        def validate(self, attrs):
            pass1 = attrs.get('password')
            pass2 = attrs('password2')

            if pass1 != pass2:
                raise serializers.ValidationError('парол не совпадает')
            return  attrs
        def create(self, validated_data):
            user =  MyUser.objects.create_user(**validated_data)
            return  user