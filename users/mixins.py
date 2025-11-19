from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404


class UserOwnedViewMixin:
    """
    View mixin for Django REST Framework API views that enforces ownership.

    This mixin provides automatic filtering and permission checking for views:
    - Filters queryset to return only objects owned by authenticated user
    - Raises 403 Forbidden if user tries to access object they don't own
    - Raises 404 Not Found if the object doesn't exist at all

    Usage:
        class MyAPIView(UserOwnedViewMixin, generics.ListCreateAPIView):
            queryset = MyModel.objects.all()
            owner_field = "created_by"  # Optional: defaults to "created_by"
    """

    owner_field = "created_by"

    def get_queryset(self):
        """
        Filter queryset to return only objects owned by authenticated user.

        Returns:
            QuerySet: Filtered queryset containing only user's objects
        """
        queryset = super().get_queryset()
        user = self.request.user

        if not user.is_authenticated:
            return queryset.none()

        filter_kwargs = {self.owner_field: user}
        return queryset.filter(**filter_kwargs)

    def get_object(self):
        """
        Retrieve and validate object ownership.

        First checks base queryset (before filtering) to see if object exists.
        If object exists but belongs to another user, raises 403 Forbidden.
        If object doesn't exist, lets DRF raise 404 Not Found.
        If object exists and belongs to the user, returns it.

        Returns:
            Model instance: The requested object if user owns it

        Raises:
            PermissionDenied: If user doesn't own the requested object (403)
            Http404: If the object doesn't exist at all (404)
        """
        # Get base queryset before filtering
        # (call super().get_queryset() to bypass our filtering)
        queryset = super().get_queryset()

        # Use same lookup logic as DRF's GenericAPIView.get_object()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {
            self.lookup_field: self.kwargs[lookup_url_kwarg]
        }

        # Try to get object from unfiltered queryset
        # This will raise 404 if the object doesn't exist
        obj = get_object_or_404(queryset, **filter_kwargs)

        # Validate ownership and raise 403 if unauthorized
        # This ensures users get 403 (Forbidden) instead of 404 (Not Found)
        # when trying to access another user's object
        owner = getattr(obj, self.owner_field, None)
        if owner != self.request.user:
            raise PermissionDenied(
                "You do not have permission to access this resource."
            )

        return obj
