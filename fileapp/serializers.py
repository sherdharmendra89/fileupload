from rest_framework import serializers
# from .models import User
from .models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(default=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'age', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

# from .models import File

# class FileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = File
#         fields = ('file',)

# from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
