from django.urls import path

from .views import BotView, DeleteHook, SetHook


urlpatterns = [
    path('set_webhook/', SetHook.as_view(), name='set_webhook'),
    path('del_webhook/', DeleteHook.as_view(), name='del_webhook'),
    path('hook/', BotView.as_view(), name='post_hook'),
]