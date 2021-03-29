# Python
import os
import json
import pycodestyle
from urllib.parse import urlencode

# Django
from django.test import TestCase
from django.conf import settings
from django.urls import reverse as rev

# Project
from .utils import get_files_for_checking


def reverse(url, params=None, **kwargs):
    """
    :param url:
    :param params: dict
    :return: full_url: full_url
    """
    return rev(url, **kwargs) + '?' + urlencode(params or {})


class ViewSetTestCase(object):
    def _list(self, filters=None, kwargs=None):
        filters = filters or {}
        kwargs = kwargs or {}

        headers = kwargs.pop('headers', {})
        method = kwargs.pop('method', 'list')

        url = reverse(self.url % method, filters, kwargs=kwargs)
        response = self.client.get(url, **headers)
        return response

    def _retrieve(self, kwargs):
        kwargs = kwargs or {}

        headers = kwargs.pop('headers', {})
        method = kwargs.pop('method', 'detail')

        url = reverse(self.url % method, kwargs=kwargs)
        response = self.client.get(url, **headers)
        return response

    def _create(self, data=None, kwargs=None, params=None):
        params = params or {}
        kwargs = kwargs or {}
        data = data or {}

        headers = kwargs.pop('headers', {})
        method = kwargs.pop('method', 'list')

        url = reverse(self.url % method, params=params, kwargs=kwargs)
        response = self.client.post(url, data, **headers)

        return response

    def _update(self, kwargs, data=None, partial=False):
        data = data or {}

        headers = kwargs.pop('headers', {})
        method = kwargs.pop('method', 'detail')

        url = reverse(self.url % method, kwargs=kwargs)
        if partial:
            response = self.client.patch(url, data, **headers)
        else:
            response = self.client.put(url, data, **headers)
        return response

    def _destroy(self, kwargs):
        kwargs = kwargs or {}

        headers = kwargs.pop('headers', {})
        method = kwargs.pop('method', 'detail')

        url = reverse(self.url % method, kwargs=kwargs)
        response = self.client.delete(url, **headers)
        return response


class PyCodeStyleTest(TestCase):
    def test_check_files(self):
        """Test that we conform to PEP-8."""
        app_dir = os.path.join(settings.BASE_DIR, 'apps')
        source = get_files_for_checking(app_dir)

        total_errors = 0
        messages = ''
        for item in source:
            style = pycodestyle.StyleGuide(quite=True)
            result = style.check_files([item])
            if result.total_errors:
                total_errors += result.total_errors
                message = '%s:%s:%s %s' % (
                    item,
                    result.counters['physical lines'],
                    result.counters['logical lines'],
                    json.dumps(result.messages, sort_keys=True, indent=4)
                )
                messages += '\n' + message

        self.assertEqual(0, total_errors, messages)
