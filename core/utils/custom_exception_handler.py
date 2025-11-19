import logging

from rest_framework.views import exception_handler


# Logger for exception debugging (using module name)
logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    """
    Custom exception handler to override DRF’s default error response format.

    This function is called whenever DRF catches an exception.
    It transforms the default DRF error response into a consistent structure:

    {
        "success": False,
        "message": <error message or field errors>,
        "detail": <long error message if available>,
        "code": <HTTP status code>,
        "data": {}
    }

    - `exc`     : The exception instance raised.
    - `context` : Additional information, including request and view.

    Process:
    - Let DRF generate its normal error response first.
    - If DRF returns a response, extract and normalize the error messages.
    - Wrap everything into a unified error response structure.
    """

    # Let DRF create the initial error response
    response = exception_handler(exc, context)

    # Only modify if DRF generated an HttpResponse for the exception
    if response is not None:
        errors = []
        message = response.data

        # If DRF returned an empty response.data, reconstruct error messages
        if not message:
            try:
                for field, value in response.data.items():
                    errors.append("{} : {}".format(field, " ".join(value)))
                    message = errors
            except Exception:
                message = response.data
        message_long = getattr(exc, "message_long", "")

        # Build final consistent error response structure
        response.data = {
            "success": False,
            "message": message,
            "detail": message_long,
            "code": response.status_code,
            "data": {},
        }

    return response
