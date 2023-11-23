from django.contrib import admin

from courses.models import Course, Lesson, Payments, Subscription

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Payments)
admin.site.register(Subscription)
