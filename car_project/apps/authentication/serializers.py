from rest_framework import serializers

from django.contrib.auth import authenticate


from .models import  User

class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(
        min_length=8,
        write_only = True
    )

    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields =  ['email', 'username', 'password', 'token']


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):


    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(max_length=255)
    username= serializers.CharField(read_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields =  ['email', 'username', 'password', 'token']

    def validate(self, data):
        email =data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('email is required to login')

        if password is None:
            raise serializers.ValidationError('passowrd is required')

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('user with this email and password noy found')


        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }
