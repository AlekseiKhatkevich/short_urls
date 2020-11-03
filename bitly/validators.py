import uuid
from typing import Any

from django.core import exceptions
from django.utils.deconstruct import deconstructible

from short_urls import error_messages


@deconstructible
class UUIDValidator:
    """

    """
    def __init__(self, version: int):
        self.version = version

    def __call__(self, value: Any):
        try:
            uuid.UUID(str(value), version=self.version)
        except ValueError as err:
            raise exceptions.ValidationError(
                *error_messages.WRONG_UUID,
            ) from err