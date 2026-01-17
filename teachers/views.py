from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import CreateAPIView
from rest_framework import mixins

from drf_spectacular.utils import extend_schema

from rest_framework.generics import CreateAPIView
from teachers.models import Course, Teacher
from teachers.serializers import CourseSerializer, TeacherSignUpSerializer, TeacherTokenObtainPairSerializer, TeacherTokenRefreshSerializer
# Create your views here.


class TeacherTokenObtainPairView(TokenObtainPairView):
    serializer_class = TeacherTokenObtainPairSerializer


class TeacherTokenRefreshView(TokenRefreshView):
    serializer_class = TeacherTokenRefreshSerializer
    @extend_schema(
        request=TeacherTokenRefreshSerializer,
        responses={
            200: {
                "type": "object",
                "properties": {
                    "access": {"type": "string", "description": "JWT Access Token"},
                    "refresh": {"type": "string", "description": "JWT Refresh Token"},
                    "role": {"type": "string", "description": "User role: 'teacher' or 'not_teacher'"}
                },
                "example": {
                    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI...",
                    "refresh": "dGVzdC1yZWZyZXNoLXRva2Vu...",
                    "role": "teacher"
                }
            }
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TeacherSignUpView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSignUpSerializer


class CoursesView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseView(mixins.DestroyModelMixin, 
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                GenericViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
