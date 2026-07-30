class KlashAIError(Exception):
    """Base exception for KlashAI."""

    pass


class NotFoundError(KlashAIError):
    """Resource not found."""

    pass


class UnauthorizedError(KlashAIError):
    """Unauthorized access."""

    pass
