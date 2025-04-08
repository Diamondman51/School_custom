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

class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'f_lang', 'price', 'teacher']

    def f_name(self, object: Group):
        return object.name

    def f_lang(self, object: Group):
        return object.get_lang_display()

    def f_price(self, object: Group):
        return object.price


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']

    def f_price(self, object: Course):
        print(f'{type(object.price)=}')
        return f'{object.price:,}'


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(ReadMore)
admin.site.register(Group, GroupAdmin)
