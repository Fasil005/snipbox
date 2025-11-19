from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    """
    Custom JSON renderer that ensures all API responses follow a consistent format.

    This renderer expects the view or exception handler to return a dictionary 
    containing a "success" key when the response is already structured.

    - If "success" exists → response is already formatted → return as-is.
    - If "success" is missing → wrap the response in a success structure.
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Override DRF's default render method to control the final API response structure.

        Parameters:
            data (dict or list): The raw response data from the view/serializer.
            accepted_media_type (str): The media type requested (JSON by default).
            renderer_context (dict): Metadata such as request, response, view.

        Logic:
        - Try accessing data["success"].
        - If success key exists:
              → Response is already wrapped, so return as-is.
        - If success key doesn't exist (KeyError or any exception):
              → Assume success, wrap the data into a standard structure:
                {
                    "success": True,
                    "detail": "Success",
                    "code": <status_code>,
                    "data": <original data>
                }
        """

        response_data = data
        try:
            if not data["success"]:
                response_data = data
        except Exception:
            response_data = {
                "success": True,
                "detail": "Success",
                "code": renderer_context["response"].status_code,
                "data": data,
            }

        # Let JSONRenderer handle the actual serialization to JSON bytes
        response = super(CustomJSONRenderer, self).render(
            response_data, accepted_media_type, renderer_context
        )

        return response
