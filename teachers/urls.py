from django.urls import path
from rest_framework.routers import DefaultRouter

from teachers.views import CourseView, CoursesView, GroupsView, TeacherSignUpView, TeacherTokenObtainPairView, TeacherTokenRefreshView

router = DefaultRouter()

router.register('courses', CoursesView, basename='courses')
router.register('course', CourseView, basename='course')
router.register('groups', GroupsView, basename='groups')

urlpatterns = [
    path('auth/login/', TeacherTokenObtainPairView.as_view(), name='teacher_token_obtain_pair'),
    path('auth/refresh/', TeacherTokenRefreshView.as_view(), name='teacher_token_refresh'),
    path('auth/sign_up/', TeacherSignUpView.as_view(), name='teacher_sign_up'),

] + router.urls
