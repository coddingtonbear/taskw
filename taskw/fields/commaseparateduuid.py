from __future__ import absolute_import

import uuid

from .base import DirtyableList, Field


class CommaSeparatedUUIDField(Field):
    def deserialize(self, value):
        if not value:
            return DirtyableList([])
        return DirtyableList([uuid.UUID(v) for v in value.split(',')])

    def serialize(self, value):
        return ','.join([str(v) for v in value])
