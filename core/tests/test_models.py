from datetime import date, timedelta

import pytest

from core.models import Event

pytestmark = pytest.mark.django_db


def test_event_string_representation_returns_title():
    event = Event(title="Feira de Inverno")

    assert str(event) == "Feira de Inverno"


def test_event_model_orders_by_date_ascending():
    later_event = Event.objects.create(
        title="Evento de Amanhã",
        date=date.today() + timedelta(days=1),
        location="Parque Central",
    )
    earlier_event = Event.objects.create(
        title="Evento de Hoje",
        date=date.today(),
        location="Praça Central",
    )

    events = list(Event.objects.all())

    assert events == [earlier_event, later_event]
