from datetime import date

from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import EventForm
from .models import Event


def event_list(request):
    selected_date = request.GET.get("date")

    upcoming_events = Event.objects.filter(date__gte=date.today())
    past_events = Event.objects.filter(date__lt=date.today()).order_by("-date")

    if selected_date:
        upcoming_events = upcoming_events.filter(date=selected_date)
        past_events = past_events.filter(date=selected_date)

    return render(
        request,
        "core/event_list.html",
        {
            "upcoming_events": upcoming_events,
            "past_events": past_events,
            "selected_date": selected_date,
        },
    )


def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)

        if form.is_valid():
            event = form.save()
            messages.success(request, f'Evento "{event.title}" criado com sucesso.')
            return redirect("event_list")
    else:
        form = EventForm()

    return render(request, "core/event_form.html", {"form": form})
