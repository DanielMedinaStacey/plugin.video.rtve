import json
import urllib2 as url


class Listings:

    base_url = 'http://www.rtve.es/api/'

    def __init__(self, base_url):
        assert isinstance(base_url, str)
        self.base_url = base_url

    def _fetch_json_string_from_url(self, url_target):
        request = url.Request(url_target)
        connection = url.urlopen(request)
        response = connection.read()
        connection.close()
        return response


    def _get_content_from_json(self, json_string):
        parser = json.JSONDecoder(None)
        content = parser.decode(json_string)
        return content


    def _get_items_from_content(self, content):
        return content['page']['items']


    def _get_fields_from_items(self, field, items):
        return map(lambda item: item[field], items)

    def fetch_categories(self):

        full_url = self.base_url + 'agrupadores.json'

        json_string = self._fetch_json_string_from_url(full_url)
        content = self._get_content_from_json(json_string)
        items = self._get_items_from_content(content)
        categories = self._get_fields_from_items('name', items)
        return categories
