from rest_framework import serializers

from users.models import User


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'bio', 'location', 'last_activity', 'last_login'
        )


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for registration contractor user
    """
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'email', 'first_name', 'last_name', 'password1', 'password2', 'bio', 'location'
        )
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'bio': {'required': False},
            'location': {'required': False},
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({
                'detail': 'Password one does not match password two'
            })
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password1')
        del validated_data['password2']
        email = validated_data.pop('email')
        user = User.objects.create(email=email, **validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user
