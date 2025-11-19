from django.contrib.auth import get_user_model

from rest_framework import serializers

# Get the active User model (supports custom user models too)
User = get_user_model()


class BasicUserSerializer(serializers.ModelSerializer):
    """
    Serializer for representing minimal user information.
    Includes user ID and full name.
    """

    # Custom method field to return the user's full name
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "name")

    def get_name(self, obj):
        """
        Returns the full name of the user.
        If the first or last name is missing, Django automatically handles it.
        """
        return obj.get_full_name()