from django.test import TestCase
import pytest
from django.core.cache import cache
from .models import FAQ

@pytest.mark.django_db
class TestFAQModel:

    def test_faq_creation(self):
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework for Python."
        )
        assert faq.question == "What is Django?"
        assert faq.answer == "Django is a web framework for Python."

    def test_auto_translation(self):
        faq = FAQ.objects.create(question="Hello, how are you?")
        assert faq.question_hi is not None  # Ensure translation is generated
        assert faq.question_bn is not None

    def test_get_translated_question(self):
        faq = FAQ.objects.create(
            question="What is Redis?",
            question_hi="रेडिस क्या है?",
            question_bn="রেডিস কি?"
        )
        assert faq.get_translated_question('hi') == "रेडिस क्या है?"
        assert faq.get_translated_question('bn') == "রেডিস কি?"
        assert faq.get_translated_question('en') == "What is Redis?"

    def test_cache_translations(self):
        faq = FAQ.objects.create(question="What is caching?")
        cache_key = f"faq_{faq.id}_question_hi"
        
        # Check if cache is empty initially
        assert cache.get(cache_key) is None  

        # Fetch translation (this should store in cache)
        faq.get_translated_question('hi')
        assert cache.get(cache_key) is not None  # Now it should be cached

