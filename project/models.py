from django.db import models
from django.core.cache import cache
from ckeditor.fields import RichTextField
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]

    question = models.TextField()
    answer = RichTextField()

    # Translations
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def translate_text(self, text, dest_language):
        """Translates text using Google Translate API."""
        try:
            translated_text = translator.translate(text, dest=dest_language).text
            return translated_text
        except Exception:
            return None  # Return None if translation fails

    def get_translated_question(self, language_code):
        """Retrieve translated question with caching and fallback."""
        cache_key = f"faq_{self.id}_question_{language_code}"
        translated_question = cache.get(cache_key)

        if not translated_question:
            translated_question = getattr(self, f'question_{language_code}', None) or self.question
            cache.set(cache_key, translated_question, timeout=3600)  # Cache for 1 hour

        return translated_question

    def save(self, *args, **kwargs):
        """Automatically translate question before saving."""
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi') or self.question
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, 'bn') or self.question

        super().save(*args, **kwargs)

        # Invalidate cache on save
        for lang in ['en', 'hi', 'bn']:
            cache.delete(f"faq_{self.id}_question_{lang}")

    def __str__(self):
        return self.question
