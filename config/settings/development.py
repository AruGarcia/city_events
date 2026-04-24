"""Development settings."""

import environ

from .base import *  # noqa: F403

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, ""),
    ALLOWED_HOSTS=(list, ["127.0.0.1", "localhost"]),
)
environ.Env.read_env(BASE_DIR / ".env")  # noqa: F405

DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")
