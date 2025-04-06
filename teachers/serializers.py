import re
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from adrf.serializers import ModelSerializer
from rest_framework import serializers

from authentication.models import User
from teachers.models import Course, Teacher

LANG_CHOICES = (
    ("1", "UZ"),
    ("2", "RU"),
    ("3", "EN"),
)

class TeacherTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Custom claims for Teacher
        if hasattr(user, 'teacher_profile'):
            token['role'] = 'teacher'
        else:
            token['role'] = 'not_teacher'
        return token
    
    def validate(self, attrs):
        attrs = super().validate(attrs=attrs)
        attrs['role'] = 'teacher'
        return attrs
    

class TeacherTokenRefreshSerializer(TokenRefreshSerializer):
    async def validate(self, attrs):
        data = super().validate(attrs)
        if hasattr(self, 'teacher_profile'):
            data['role'] = 'teacher'
            return data
        else:
            data['role'] = 'not_teacher'
            return data
        

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
    

    async def create(self, validated_data):
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
    
    async def validate_phone(self, value):
        regex = re.compile(r'^\+998\d{9}$')
        f_value = value[4:]
        if not regex.fullmatch(value):
            raise serializers.ValidationError(f'Phone number must start with +998, after contains 9 digits not {len(f_value)}')
        return value


class CourseSerializer(ModelSerializer):
    # langs = serializers.ListField(child=serializers.ChoiceField(choices=LANG_CHOICES))  # ✅ Fix here
    class Meta:
        model = Course
        fields = '__all__'
