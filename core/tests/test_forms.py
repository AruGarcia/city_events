from datetime import date

from core.forms import EventForm


def test_event_form_uses_bootstrap_classes_placeholders_and_labels():
    form = EventForm()

    assert form.fields["title"].widget.attrs["class"] == "form-control ce-form-control"
    assert form.fields["title"].widget.attrs["placeholder"] == "Ex.: Feira de artesanato no centro"
    assert form.fields["location"].widget.attrs["placeholder"] == "Ex.: Praca da Matriz"
    assert form.fields["description"].widget.attrs["placeholder"] == (
        "Conte em poucas linhas o que acontece no evento."
    )
    assert form.fields["description"].label == "Descrição (opcional)"


def test_event_form_rejects_titles_shorter_than_four_characters():
    form = EventForm(
        data={
            "title": "Abc",
            "date": date.today().isoformat(),
            "location": "Praça Central",
            "description": "Evento curto.",
        }
    )

    assert form.is_valid() is False
    assert form.errors["title"] == ["Use pelo menos 4 caracteres no título do evento."]
