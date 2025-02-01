from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

class FAQAdminForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer': CKEditorWidget(),
            'answer_hi': CKEditorWidget(),
            'answer_bn': CKEditorWidget(),
        }

class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm
    list_display = ('question', 'question_hi', 'question_bn')
    search_fields = ('question', 'question_hi', 'question_bn')

admin.site.register(FAQ, FAQAdmin)
