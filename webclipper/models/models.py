from building_blocks.models import HasUUID
from django.conf import settings
from django.db import models

from .abstracts import AbstractWebClip


class WebClip(
    HasUUID,
    AbstractWebClip
):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)


__all__ = [
    'WebClip',
]
