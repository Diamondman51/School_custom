from django.contrib import admin

from teachers.models import Course, Group, ReadMore, Teacher

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['f_id', 'f_username', 'f_email', 'f_is_active', 'f_is_staff', 'f_is_admin']

    def f_id(self, object: Teacher):
        return object.user.id

    def f_username(self, object: Teacher):
        return object.user.username
    
    def f_email(self, object: Teacher):
        return object.user.email
    
    def f_is_active(self, object: Teacher):
        return object.user.is_active
    
    def f_is_staff(self, object: Teacher):
        return object.user.is_staff
    
    def f_is_admin(self, object: Teacher):
        return object.user.is_admin
    

    # def get_list_display(self, request):
    #     return super().get_list_display(request)


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course)
admin.site.register(ReadMore)
admin.site.register(Group)
