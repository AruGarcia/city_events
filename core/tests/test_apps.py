from django.apps import apps


def test_core_app_config_is_registered():
    app_config = apps.get_app_config("core")

    assert app_config.name == "core"
    assert app_config.verbose_name == "Core"
