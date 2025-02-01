from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer

# Create your views here.
from django.db.models import F

class FAQListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')

        faqs = FAQ.objects.all().values(
            'id', 
            'question', 'question_hi', 'question_bn',
            'answer', 'answer_hi', 'answer_bn'
        )

        for faq in faqs:
            faq['translated_question'] = faq.get(f'question_{lang}', faq['question'])
            faq['translated_answer'] = faq.get(f'answer_{lang}', faq['answer'])

        return Response(faqs, status=status.HTTP_200_OK)

