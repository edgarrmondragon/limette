"""Common exceptions."""


class LimeSurveyError(Exception):
    """Basic exception raised by LimeSurvey."""

    def __init__(self, message: str) -> None:  # noqa:: ANN101
        """Create a generic error for the LimeSurvey RPC API.

        Args:
            message: Exception message. By default none, and a generic message is used.
        """
        super(LimeSurveyError, self).__init__(message)


class LimeSurveyStatusError(LimeSurveyError):
    """Exception raised when LimeSurvey responds with an error status."""


class LimeSurveyApiError(LimeSurveyError):
    """Exception raised when LimeSurvey responds with a non-null error."""
