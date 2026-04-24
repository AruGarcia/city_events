import importlib
import sys

import environ
import pytest
from django.core.exceptions import ImproperlyConfigured


def reload_settings_module(monkeypatch, module_name, env_vars):
    monkeypatch.setattr(environ.Env, "read_env", lambda *args, **kwargs: None)

    for key in ("DEBUG", "SECRET_KEY", "ALLOWED_HOSTS"):
        monkeypatch.delenv(key, raising=False)

    for key, value in env_vars.items():
        monkeypatch.setenv(key, value)

    sys.modules.pop(module_name, None)
    return importlib.import_module(module_name)


def test_development_settings_use_env_values(monkeypatch):
    module = reload_settings_module(
        monkeypatch,
        "config.settings.development",
        {
            "DEBUG": "False",
            "SECRET_KEY": "dev-secret-key",
            "ALLOWED_HOSTS": "127.0.0.1,localhost,testserver",
        },
    )

    assert module.DEBUG is False
    assert module.SECRET_KEY == "dev-secret-key"
    assert module.ALLOWED_HOSTS == ["127.0.0.1", "localhost", "testserver"]


def test_production_settings_require_secret_key(monkeypatch):
    with pytest.raises(ImproperlyConfigured, match="SECRET_KEY must be set in production."):
        reload_settings_module(
            monkeypatch,
            "config.settings.production",
            {
                "ALLOWED_HOSTS": "city-events.example.com",
            },
        )


def test_production_settings_use_env_values(monkeypatch):
    module = reload_settings_module(
        monkeypatch,
        "config.settings.production",
        {
            "DEBUG": "False",
            "SECRET_KEY": "prod-secret-key",
            "ALLOWED_HOSTS": "city-events.example.com,api.city-events.example.com",
        },
    )

    assert module.DEBUG is False
    assert module.SECRET_KEY == "prod-secret-key"
    assert module.ALLOWED_HOSTS == [
        "city-events.example.com",
        "api.city-events.example.com",
    ]
    assert module.SESSION_COOKIE_SECURE is True
    assert module.CSRF_COOKIE_SECURE is True
    assert module.X_FRAME_OPTIONS == "DENY"
