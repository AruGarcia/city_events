from django import forms
from django.core.exceptions import ValidationError

from .models import Event


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "title": "Ex.: Feira de artesanato no centro",
            "location": "Ex.: Praca da Matriz",
            "description": "Conte em poucas linhas o que acontece no evento.",
        }

        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control ce-form-control"
            if name in placeholders:
                field.widget.attrs["placeholder"] = placeholders[name]

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 4:
            raise ValidationError("Use pelo menos 4 caracteres no título do evento.")
        return title

    class Meta:
        model = Event
        fields = ["title", "date", "location", "description"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "title": "Título do evento",
            "date": "Data do evento",
            "location": "Local (ex: Praça Central)",
            "description": "Descrição (opcional)",
        }
