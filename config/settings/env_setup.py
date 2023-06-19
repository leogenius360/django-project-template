

import logging
from pathlib import Path
from pydantic import (
    BaseSettings,
    PostgresDsn,
    EmailStr,
    HttpUrl,
)


logger = logging.getLogger(__name__)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 12-factor-app best practice: all logging goes to the console
# https://12factor.net/logs
# https://docs.djangoproject.com/en/3.2/topics/logging/#examples
LOGGING_CONFIG = None
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"}
    },
    "handlers": {
        "console": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}
import logging.config  # pylint: disable=ungrouped-imports, wrong-import-position, wrong-import-order

logging.config.dictConfig(LOGGING)

# 12-factor-app best practice: all configuration is stored in the environment
#
# Use pydantic with run-time type coercion & validation
# https://docs.pydantic.dev/latest/usage/settings/
class SettingsFromEnvironment(BaseSettings):
    """Defines environment variables with their types and optional defaults"""

    # postgresql
    DATABASE_URL: PostgresDsn
    DATABASE_SSL: bool = True

    # Django settings
    SECRET_KEY: str
    DEBUG: bool = False
    DEBUG_TEMPLATES: bool = False
    USE_SSL: bool = False
    ALLOWED_HOSTS: list

    class Config:  # pylint: disable=too-few-public-methods
        """Defines configuration for pydantic environment loading"""

        env_file = str(BASE_DIR / ".env")
        case_sensitive = True

# if __name__ == "__main__":
config = SettingsFromEnvironment()