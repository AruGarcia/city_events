# City Events

City Events is a Django web application for discovering and publishing local events with a cleaner product feel than a default CRUD app. The project started as a simple Django setup and was evolved into a more polished event agenda with responsive UI, environment-based settings, automated tests, and CI support.

## Project Overview

This project was built as a portfolio-style exercise focused on two goals:

1. delivering a useful local events experience
2. showing solid Django engineering practices

The current product allows users to:

- browse upcoming events
- review past events in a separate section
- filter events by date
- publish new events through a styled form
- receive success feedback after creating an event

## Product Direction

The interface was redesigned to feel closer to a lightweight product than a scaffolded admin-style page. The UI now uses:

- Bootstrap 5 for responsive layout and spacing
- custom CSS organized in `core/static/core/css/styles.css`
- clearer UX writing focused on user benefit
- event cards with faster visual scanning
- dedicated list and create screens

The homepage messaging was also updated to emphasize user value:

> Discover events in your city with ease.

## What Was Implemented

### 1. Django Project Structure

- split settings by environment:
  - `config/settings/base.py`
  - `config/settings/development.py`
  - `config/settings/production.py`
- local entrypoints use `config.settings.development`
- environment variables are loaded with `django-environ`

### 2. Event Management Features

- `Event` model with:
  - title
  - date
  - location
  - description
- default ordering by date
- list view for event discovery
- create view for publishing new events
- future and past events displayed separately
- date-based filtering on the main page
- success message after event creation

### 3. Frontend Improvements

- responsive layout with Bootstrap 5
- external stylesheet instead of inline CSS
- portfolio-style product presentation
- reusable base template
- improved form labels, placeholders, and calls to action

### 4. Validation and UX

- minimum title length validation
- optional description field
- clearer form microcopy
- confirmation feedback after successful submission

### 5. Testing and Quality

- `pytest`
- `pytest-django`
- `pytest-cov`
- `ruff`
- GitHub Actions workflow for linting and tests

The test suite currently covers:

- app registration
- settings behavior
- model ordering and string representation
- form widget configuration and validation
- list page rendering
- date filtering
- empty state behavior
- event creation flow
- success messaging

## Tech Stack

- Python 3.12
- Django 6
- Bootstrap 5
- django-environ
- pytest / pytest-django / pytest-cov
- Ruff
- uv
- GitHub Actions

## Local Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd city_events
```

### 2. Install dependencies

```bash
uv sync --all-groups
```

### 3. Create your environment file

Create a `.env` file with:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 4. Apply migrations

```bash
uv run python manage.py migrate
```

### 5. Run the development server

```bash
uv run python manage.py runserver
```

## Running Quality Checks

Lint:

```bash
uv run ruff check .
```

Format check:

```bash
uv run ruff format --check .
```

Tests:

```bash
uv run pytest
```

Coverage:

```bash
uv run pytest --cov=core --cov=config --cov-report=term-missing
```

## Test Status

Latest verified local result:

- 15 tests passing
- 96% total coverage

## Repository Highlights

Key files:

- `core/models.py`
- `core/views.py`
- `core/forms.py`
- `core/templates/base.html`
- `core/templates/core/event_list.html`
- `core/templates/core/event_form.html`
- `core/static/core/css/styles.css`
- `core/tests/`
- `.github/workflows/ci.yml`

## Engineering Notes

This repository demonstrates:

- migration from default Django scaffolding to a structured project baseline
- separation of development and production settings
- UI improvement with product-oriented copy and responsive layout
- test-driven stabilization of new features
- practical project organization for a portfolio-ready Django app

## Next Steps

Planned improvements that would make the project more complete:

- event detail page with slug-based URLs
- text search
- image uploads for events
- event categories
- edit and delete flows
- PostgreSQL option for production
- production deployment configuration

## Author Goal

This project is meant to showcase the ability to:

- design and improve a Django product beyond boilerplate
- structure a maintainable backend/frontend workflow
- apply testing, CI, and environment-based configuration
- turn a simple CRUD into something closer to a real portfolio case
