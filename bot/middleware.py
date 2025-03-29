import atexit
import asyncio
from bot.views import DeleteHook, SetHook

class LifecycleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        asyncio.create_task(self.startup())  # Use async task instead of sync call
        print('Middleware initialized')

    def __call__(self, request):
        response = self.get_response(request)
        return response

    async def startup(self):  # Make it async
        await SetHook.start()  # Use await instead of async_to_sync
        print('Middleware started')

    async def shutdown(self):
        await DeleteHook.start()  # Use await instead of async_to_sync
        print('Middleware shutdown')

# Register the shutdown function properly
atexit.register(lambda: asyncio.run(LifecycleMiddleware.shutdown(LifecycleMiddleware)))  
