from django.db import models


class Snippet(models.Model):
    """Model representing a code snippet."""

    # Relationship Fields
    created_by = models.ForeignKey(
        'auth.User',
        related_name='snippets',
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        'snippets.Tag',
        related_name='snippets',
        blank=True
    )

    # String Fields
    title = models.CharField(max_length=100)
    notes = models.TextField()

    # DateTime
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Model representing a tag for categorizing snippets."""

    # String Fields
    title = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.title