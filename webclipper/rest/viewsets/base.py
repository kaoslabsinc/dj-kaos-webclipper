from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializers import *
from ...models import *


class BaseWebClipViewSet(
    viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated,)
    queryset = WebClip.objects.select_related(
        'owner',
    ).all()
    serializer_class = WebClipSerializer
    lookup_field = 'uuid'
    search_fields = (
        'page_url',
        'page_title',
    )
    filterset_fields = (
        'owner',
    )


__all__ = [
    'BaseWebClipViewSet',
]
