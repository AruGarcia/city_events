from django.urls import reverse


def test_home_page_returns_success(client):
    response = client.get(reverse("home"))

    assert response.status_code == 200


def test_home_page_uses_expected_template(client):
    response = client.get(reverse("home"))

    assert response.status_code == 200
    template_names = [template.name for template in response.templates if template.name]

    assert "core/home.html" in template_names
    assert "base.html" in template_names


def test_home_page_displays_expected_content(client):
    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert "Hello World com Django" in response.content.decode()
