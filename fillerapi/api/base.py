import requests
from requests.compat import urljoin
from django.http import HttpResponse
from fillerapi.constants import BASE_URL


class FillerAPI(object):
    @staticmethod
    def _get_request_headers():
        headers = {
            'Accept': 'application/json',
        }
        return headers

    def _request_get(self, path, params=None, url=BASE_URL):
        url = urljoin(url, path)
        headers = self._get_request_headers()
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return HttpResponse(response)

    def _request_post(self, path, data=None, params=None, url=BASE_URL):
        url = urljoin(url, path)
        headers = self._get_request_headers()
        response = requests.post(url, json=data, params=params, headers=headers)
        response.raise_for_status()
        return HttpResponse(response)

    def _request_put(self, path, data=None, params=None, url=BASE_URL):
        url = urljoin(url, path)
        headers = self._get_request_headers()
        response = requests.put(url, json=data, params=params, headers=headers)
        response.raise_for_status()
        return HttpResponse(response)

    def _request_delete(self, path, params=None, url=BASE_URL):
        url = urljoin(url, path)
        headers = self._get_request_headers()
        response = requests.delete(url, params=params, headers=headers)
        response.raise_for_status()
        return HttpResponse(response)
