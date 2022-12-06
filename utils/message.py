from enum import Enum


class ToastMessageText(Enum):
    ### Success Respone toast message ###
    SUCCESS_UPLOAD = "با موفقیت ذخیره شد."
    SUCCESS_SAVE_ITEM = "با موفقیت ذخیره شد."
    SUCCESS_UPDATE_SAVE = ".تغییرات با موفقیت ذخیره شد"
    ### Bad request input ###
    AUTHENTICATION_NOT_PROVIDE = "Forbidden"
    FORMAT_FILE_NOT_ACCEPTABLE = "فرمت وردی صحیح نمی باشد."
    ITEM_NOT_FOUND = "موردی یافت نشد."
    ENTER_CORRECT_DATA = "مقادیر ورودی را چک نمایید."
    DUPLICATE_DATA = "داده ای با این مشحصات قبلا ثبت شده است."
    ### Service Error ###
    SERVICE_ERROR = "مشکلی رخ داده دوباره تلاش کنید"
    SERVICE_CONNECTION_FAIL = "مشکلی در برقراری ارتباط رخ داده است"
