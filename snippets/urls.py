from django.urls import path

from snippets import views as snippet_views


urlpatterns = [
    path(
        "",
        snippet_views.SnippetsAPIView.as_view(),
        name="snippets-view"
    ),
    path(
        "<int:id>/",
        snippet_views.SnippetDetailedAPIView.as_view(),
        name="snippet-detailed-view"
    ),

    path(
        "tags/",
        snippet_views.TagsAPIView.as_view(),
        name="tags-list"
    ),
    path(
        "tags/<int:id>/",
        snippet_views.TagDetailedAPIView.as_view(),
        name="snippets-by-tags"
    )
]
