# Stdlib
import json
import os
import io
import uuid
from urllib.parse import urlencode
from contextlib import contextmanager
from time import monotonic

# Pypi: requests
import requests

# Django
from django.http import HttpResponse
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.urls import reverse
from django.core.cache import cache
from django.conf import settings


def rev(url, params=None, **kwargs):
    """
    :param url:
    :param params: dict
    :return: full_url: full_url
    """
    return reverse(url, **kwargs) + '?' + urlencode(params or {})


def url_with_params(url, params={}):
    """
    :param url:
    :param params: dict
    :return: full_url: full_url
    """
    return reverse(url) + '?' + urlencode(params)


def url_with_pk(url, pk):
    return reverse(url, kwargs={'pk': pk})


def timezone_fix(str_date):
    date = parse_datetime(str_date)
    date_timezone = timezone.localtime(date)
    return str(date_timezone).replace(' ', 'T')


def get_files_for_checking(start_path):
    source_files = []
    for root, dirs, files in os.walk(start_path, topdown=True):
        for file in files:
            if file.endswith('.py') and not root.endswith('migrations'):
                source_files.append('%s/%s' % (root, file))
    return source_files
