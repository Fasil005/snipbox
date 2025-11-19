from rest_framework import serializers

from snippets import models as snippet_models

class TagSlugField(serializers.SlugRelatedField):
    """
    Custom SlugRelatedField for Tag objects.
    Allows passing tag titles as plain strings and ensures:
    - Existing tags are reused
    - Missing tags are automatically created
    """

    def to_internal_value(self, data):
        """
        Convert incoming tag name to a Tag instance.
        DRF normally expects the slug to already exist, but we override this
        so new tags can be created on the fly.
        """
        # Normalize the incoming value (remove extra spaces)
        slug = str(data).strip()
        
        obj, _ = snippet_models.Tag.objects.get_or_create(title=slug)
        return obj