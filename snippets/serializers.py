from rest_framework import serializers

from snippets import models as snippet_models
from users import serializers as user_serializers


class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializer for Snippet objects.

    - Exposes 'created_by' as a nested read-only user representation.
    - Automatically assigns the logged-in user as the creator during creation.
    """

    # Nested read-only representation of the user who created the snippet
    created_by = user_serializers.BasicUserSerializer(read_only=True)

    class Meta:
        model = snippet_models.Snippet
        fields = "__all__"
        read_only_fields = ("created_by",)

    def create(self, validated_data):
        """
        Automatically assign the logged-in user as 'created_by'.
        The client should not send this field.
        """
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)