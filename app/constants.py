"""
Application-wide constants.

This module contains immutable values shared across the application.
"""

from typing import Final, Literal

# Application
APP_NAME: Final[str] = "Enterprise AI Prediction Platform"

# API
API_PREFIX: Final[str] = "/api"
API_VERSION: Final[str] = "v1"

# Health Status
HealthStatus = Literal["healthy", "unhealthy"]

DEFAULT_HEALTH_STATUS: Final[HealthStatus] = "healthy"