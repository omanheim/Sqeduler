from django.contrib import admin
from Sqeduler.models import User
from Sqeduler.models import Course
from Sqeduler.models import Enrollment

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Enrollment)
