from django.urls import path
from .views import FAQListAPIView

urlpatterns = [
    path('api/faqs/', FAQListAPIView.as_view(), name='faq-list'),
]
