from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.generics import CreateAPIView
from teachers.models import Teacher
from teachers.serializers import TeacherSignUpSerializer, TeacherTokenObtainPairSerializer, TeacherTokenRefreshSerializer
# Create your views here.

class TeacherTokenObtainPairView(TokenObtainPairView):
    serializer_class = TeacherTokenObtainPairSerializer


class TeacherTokenRefreshView(TokenRefreshView):
    serializer_class = TeacherTokenRefreshSerializer


class TeacherSignUpView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSignUpSerializer
