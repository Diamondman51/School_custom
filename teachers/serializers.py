from attr import fields
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from authentication.models import User
from teachers.models import Teacher


class TeacherTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Custom claims for Teacher
        if hasattr(user, 'teacher_profile'):
            token['role'] = 'teacher'
        else:
            raise ValueError("Not a teacher.")
        return token


class TeacherTokenRefreshSerializer(TokenRefreshSerializer):
    pass


class TeacherSignUpSerializer(ModelSerializer):
    # username = serializers.CharField()
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    phone = serializers.CharField(source='user.phone')
    password = serializers.CharField(source='user.password', write_only=True)
    profile_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Teacher
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password', 'profile_image']
    

    def create(self, validated_data):
        try:
            user_data = validated_data.pop('user')
            
            teacher_data = {
                'profile_image': validated_data.pop('profile_image'),
            }

            password = user_data.pop('password')
            user = User.objects.create(**user_data)
            user.set_password(password)
            user.save()
            teacher = Teacher.objects.create(user=user, **teacher_data)
            teacher.save()
            return teacher
        except Exception as e:
            raise serializers.ValidationError(str(e))