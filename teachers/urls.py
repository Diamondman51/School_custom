from django.urls import path

from teachers.serializers import TeacherSignUpSerializer
from teachers.views import TeacherSignUpView, TeacherTokenObtainPairView, TeacherTokenRefreshView

urlpatterns = [
    path('teacher/login/', TeacherTokenObtainPairView.as_view(), name='teacher_token_obtain_pair'),
    path('teacher/refresh/', TeacherTokenRefreshView.as_view(), name='teacher_token_refresh'),
    path('teacher/sign_up/', TeacherSignUpView.as_view(), name='teacher_sign_up'),
]
