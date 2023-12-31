from django.urls import path

from courses.apps import CourseConfig
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentsListAPIView, SubscriptionListAPIView, SubscriptionCreateAPIView, \
    SubscriptionDestroyAPIView, PaymentCreateAPIView, PaymentRetrieveAPIView, PaymentSuccessAPIView

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('subscription/', SubscriptionListAPIView.as_view(), name='subscription_list'),
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),

    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
    path('payments/create/', PaymentCreateAPIView.as_view(), name='payments_create'),
    path('payments/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payments_detail'),
    path('payments/success/', PaymentSuccessAPIView.as_view(), name='payments_success'),
] + router.urls
