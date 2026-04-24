from datetime import date, timedelta

import pytest
from django.contrib.messages import get_messages
from django.urls import reverse

from core.models import Event

pytestmark = pytest.mark.django_db


def test_event_list_page_returns_success_and_uses_expected_templates(client):
    response = client.get(reverse("event_list"))

    assert response.status_code == 200
    template_names = [template.name for template in response.templates if template.name]

    assert "core/event_list.html" in template_names
    assert "base.html" in template_names


def test_event_list_shows_upcoming_events_and_separates_past_events(client):
    past_event = Event.objects.create(
        title="Show Encerrado",
        date=date.today() - timedelta(days=2),
        location="Teatro Municipal",
        description="Evento que já aconteceu.",
    )
    upcoming_event = Event.objects.create(
        title="Festival de Primavera",
        date=date.today() + timedelta(days=3),
        location="Praça Central",
        description="Evento que ainda vai acontecer.",
    )

    response = client.get(reverse("event_list"))
    content = response.content.decode()

    assert response.status_code == 200
    assert list(response.context["upcoming_events"]) == [upcoming_event]
    assert list(response.context["past_events"]) == [past_event]
    assert "Próximos eventos" in content
    assert "Eventos anteriores" in content
    assert "Festival de Primavera" in content
    assert "Show Encerrado" in content


def test_event_list_can_filter_by_specific_date(client):
    filtered_event = Event.objects.create(
        title="Feira Gastronômica",
        date=date.today() + timedelta(days=5),
        location="Mercado Público",
    )
    Event.objects.create(
        title="Encontro Literário",
        date=date.today() + timedelta(days=7),
        location="Biblioteca",
    )

    response = client.get(reverse("event_list"), {"date": filtered_event.date.isoformat()})

    assert response.status_code == 200
    assert list(response.context["upcoming_events"]) == [filtered_event]
    assert list(response.context["past_events"]) == []
    assert response.context["selected_date"] == filtered_event.date.isoformat()


def test_event_list_shows_empty_state_when_no_events_match_filter(client):
    response = client.get(reverse("event_list"), {"date": "2099-12-31"})

    assert response.status_code == 200
    assert "Nenhum evento encontrado" in response.content.decode()
    assert list(response.context["upcoming_events"]) == []
    assert list(response.context["past_events"]) == []


def test_event_create_page_returns_success_and_uses_expected_template(client):
    response = client.get(reverse("event_create"))

    assert response.status_code == 200
    template_names = [template.name for template in response.templates if template.name]

    assert "core/event_form.html" in template_names
    assert "Crie um novo evento" in response.content.decode()


def test_event_create_persists_event_redirects_and_shows_success_message(client):
    response = client.post(
        reverse("event_create"),
        data={
            "title": "Cinema ao ar livre",
            "date": (date.today() + timedelta(days=10)).isoformat(),
            "location": "Parque da Cidade",
            "description": "Sessão aberta com filmes brasileiros.",
        },
        follow=True,
    )

    messages = [message.message for message in get_messages(response.wsgi_request)]

    assert response.status_code == 200
    assert response.redirect_chain == [(reverse("event_list"), 302)]
    assert Event.objects.filter(title="Cinema ao ar livre").exists()
    assert 'Evento "Cinema ao ar livre" criado com sucesso.' in messages


def test_event_create_with_invalid_data_returns_form_errors(client):
    response = client.post(
        reverse("event_create"),
        data={
            "title": "Abc",
            "date": (date.today() + timedelta(days=1)).isoformat(),
            "location": "Centro Cultural",
            "description": "Título inválido para teste.",
        },
    )

    assert response.status_code == 200
    assert Event.objects.count() == 0
    assert "Use pelo menos 4 caracteres no título do evento." in response.content.decode()
