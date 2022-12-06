from rest_framework import status
from utils.message import ToastMessageText
from rest_framework.exceptions import APIException


# 4xx exception
class NotFoundItem(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ToastMessageText.ITEM_NOT_FOUND.value


# service exception
class ServiceException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = ToastMessageText.SERVICE_ERROR.value


class DockerApiException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = ToastMessageText.SERVICE_ERROR.value
