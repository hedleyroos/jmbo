import logging

from django.utils import encoding
from photologue.models import PhotoSize
from six import python_2_unicode_compatible


logger = logging.getLogger("logger")

logger.info("Patching PhotoSize.name max_length")
PhotoSize._meta.get_field("name").max_length = 255


# TODO: remove and see what breaks
logger.info("Patching python_2_unicode_compatible for backward compatibility for unmaintained modules")
encoding.python_2_unicode_compatible = python_2_unicode_compatible
