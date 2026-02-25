from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    """Validated contact form used on the contact page."""

    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'company', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_subject(self):
        subject = self.cleaned_data['subject'].strip()
        if len(subject) < 5:
            raise forms.ValidationError('Subject must be at least 5 characters long.')
        return subject
