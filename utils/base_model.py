from django.db import models
import uuid
from utils.http_exception import ServiceException
import logging


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

    @staticmethod
    def delete_item(db_instancs: models.Model):
        try:
            db_instancs.is_deleted = True
            db_instancs.save()
        except Exception as e:
            logging.error(e)
            raise ServiceException()

    class Meta:
        abstract = True
