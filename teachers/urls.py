from django.urls import path
from rest_framework.routers import DefaultRouter

from teachers.views import CourseView, CoursesView, TeacherSignUpView, TeacherTokenObtainPairView, TeacherTokenRefreshView

router = DefaultRouter()

router.register('courses', CoursesView, basename='courses')
router.register('course', CourseView, basename='course')

urlpatterns = [
    path('login/', TeacherTokenObtainPairView.as_view(), name='teacher_token_obtain_pair'),
    path('refresh/', TeacherTokenRefreshView.as_view(), name='teacher_token_refresh'),
    path('sign_up/', TeacherSignUpView.as_view(), name='teacher_sign_up'),
    
] + router.urls
