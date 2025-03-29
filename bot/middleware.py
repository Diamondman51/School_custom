import atexit

from bot.views import DeleteHook, SetHook
from asgiref.sync import async_to_sync

class LifecycleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.startup()

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def startup(self):
        async_to_sync(SetHook.get)()

    def shutdown(self):
        async_to_sync(DeleteHook.get)()

atexit.register(LifecycleMiddleware.shutdown)