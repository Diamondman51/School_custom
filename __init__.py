# import os
# import sys
# import django

# # Setup Django environment
# sys.path.append(r'E:/School_custom/core')  # Add your Django project directory to the Python path
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # Use the correct settings module
# django.setup()

# from rest_framework_simplejwt.tokens import AccessToken


# token = AccessToken('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwMjAwMDk1LCJpYXQiOjE3NDAxOTg5OTksImp0aSI6ImY1MmU4MTA1MzNiZjRlODA5YmNhMTJmMGIxYWI2ZDU4IiwidXNlcl9pZCI6MX0.Ul9fN_ZeX1iUGy8ozmvJ5Oe873Ej6fWyOiO7RfjpICM"')
# print(token.payload)


from asgiref.sync import async_to_sync

class S:
    async def get(self):
        print('hello')
        return {'hook': True}

    @classmethod
    async def start(cls):
        await cls.get(cls)

s = async_to_sync(S.start)()