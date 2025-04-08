import time
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from adrf.viewsets import GenericViewSet, ViewSet, ViewSetMixin
from adrf import mixins


from drf_spectacular.utils import extend_schema

from adrf.generics import CreateAPIView
from teachers.models import Course, Group, Teacher
from teachers.serializers import CourseSerializer, GroupSerializer, GroupsSerializer, TeacherSignUpSerializer, TeacherTokenObtainPairSerializer, TeacherTokenRefreshSerializer
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

    def list(self, request, *args, **kwargs):
        course = Course.objects.first()
        for i in range(5):
            print('Timing for ID: ', request.user.id)
            time.sleep(1)
        print(f'{type(course.price)=}-------------------sync--------------------')
        return super().list(request, *args, **kwargs)
    


class CourseView(mixins.DestroyModelMixin, 
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                GenericViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GroupsView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer


class GroupView(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                GenericViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
