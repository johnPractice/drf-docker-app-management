from django.db import models
import uuid


class BaseModel(models.Model):
    """
    Base model for inheritance another models.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    @classmethod
    def retrive_by_id(cls: models.Model, id: uuid.uuid4):
        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None

    class Meta:
        abstract = True
