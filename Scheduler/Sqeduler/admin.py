from django.contrib import admin
from Sqeduler.models import User
from Sqeduler.models import Course
from Sqeduler.models import Enrollment

class CourseAdmin(admin.ModelAdmin):
   fields = (('courseid','section'),'title','days','starttime','endtime')

class EnrollmentInline(admin.StackedInline):
   model = Enrollment
   extra = 6

class UserAdmin(admin.ModelAdmin):
   inlines = [
	EnrollmentInline,
   ]

admin.site.register(User,UserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment)


