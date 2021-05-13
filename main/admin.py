from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from main.resources import StudentResource
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


class UserAdmin(UserAdmin):
    inlines = (UserInline,)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    fields = ('name', 'salary', )
    list_display = ('name', 'salary', )
    list_filter = ('name', 'salary', )

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'middle_name', 'date_of_birth', 'number', 'group', )
    list_display = ('name', 'surname', 'middle_name', 'date_of_birth', 'number', 'group', )
    list_filter = ('name', 'surname', 'middle_name', 'date_of_birth', 'number', 'group', )




@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'image', )
    list_display = ('title', 'description', 'image', )
    list_filter = ('title', 'description', 'image', )

@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )
    list_filter = ('name', )

@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    fields = ('fk_student', 'fk_discipline', 'fk_homework_check', )
    list_display = ('fk_student', 'fk_discipline', 'fk_homework_check', )
    list_filter = ('fk_student', 'fk_discipline', 'fk_homework_check', )

@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    fields = ('fk_discipline', 'fk_userprofile', 'fk_group_name', )
    list_display = ('fk_discipline', 'fk_userprofile', 'fk_group_name', )
    list_filter = ('fk_discipline', 'fk_userprofile', 'fk_group_name', )

#@admin.register(Attendance)
#class AttendanceAdmin(admin.ModelAdmin):
#    fields = ('fk_student', 'fk_discipline', 'date_of_visit', 'presence', )
#    list_display = ('fk_student', 'fk_discipline', 'date_of_visit', 'presence', )
#    list_filter = ('fk_student', 'fk_discipline', 'date_of_visit', 'presence', )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Homework)
admin.site.register(Homework_check)
admin.site.register(Group_name)
admin.site.register(Attendance)



resource_class = StudentResource
