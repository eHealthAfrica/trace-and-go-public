from __future__ import absolute_import

from celery import shared_task
from django.conf import settings
import importlib


def load_class(full_class_string):
    """
    dynamically load a class from a string
    """

    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    func_str = class_data[-1]

    module = importlib.import_module(module_path)
    return getattr(module, func_str)


sms_func = load_class(settings.SMS_BACKEND)


@shared_task
def send_sms(to, message):
    return sms_func(to, message)


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
