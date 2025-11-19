from django.shortcuts import get_object_or_404

from rest_framework import generics

from snippets import models as snippet_models
from snippets import serializers as snippet_serializers
from users.mixins import UserOwnedViewMixin


class SnippetsAPIView(UserOwnedViewMixin, generics.ListCreateAPIView):
    """
    API endpoint to list all snippets belonging to the authenticated user
    or create a new snippet.
    
    GET: Returns a list of snippets owned by the current user
    POST: Creates a new snippet for the current user
    """

    queryset = snippet_models.Snippet.objects.all()
    serializer_class = snippet_serializers.SnippetSerializer


class SnippetDetailedAPIView(
    UserOwnedViewMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    """
    API endpoint to retrieve, update, or delete a specific snippet.
    
    Only snippets owned by the authenticated user are accessible.
    
    GET: Retrieve a specific snippet by ID
    PUT: Update a specific snippet by ID
    PATCH: Partially update a specific snippet by ID
    DELETE: Delete a specific snippet by ID
    """

    queryset = snippet_models.Snippet.objects.all()
    serializer_class = snippet_serializers.SnippetSerializer
    lookup_field = "id"


class TagsAPIView(generics.ListAPIView):
    """
    API endpoint to list all available tags.
    
    Useful for showing tag options to the user.
    
    GET: Returns a list of all tags in the system
    """

    queryset = snippet_models.Tag.objects.all()
    serializer_class = snippet_serializers.TagsSerializers


class TagDetailedAPIView(generics.ListAPIView):
    """
    API endpoint to list all snippets belonging to the authenticated user
    that are associated with a specific tag.
    
    GET: Returns snippets filtered by tag ID for the current user
    """

    serializer_class = snippet_serializers.SnippetSerializer

    def get_queryset(self):
        # Get the tag based on URL param: /api/tags/<id>/
        tag = get_object_or_404(snippet_models.Tag, pk=self.kwargs["id"])

        return snippet_models.Snippet.objects.filter(
            created_by=self.request.user,
            tags=tag
        )
