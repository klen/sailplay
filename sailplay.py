""" Agnostic API for sailplay.ru """

__version__ = "0.1.1"
__project__ = "sailplay"
__author__ = "Kirill Klenov <horneds@gmail.com>"
__license__ = "BSD"

import logging
import requests as rs
from contextlib import contextmanager
from copy import deepcopy


logger = logging.getLogger('sailplay')
rs_logger = logging.getLogger('requests')


class SailPlayException(Exception):
    pass


class SailPlayAPI(object):

    """ Proxy SailPlay API. """

    def __init__(self, client):
        self.__client = client
        if not self.__client.params.get('token'):
            self.__client.login()
        self.session = []

    def __getattr__(self, name):
        self.session.append(name)
        return self

    def __call__(self, *args, **data):
        """ Call API. """
        url = '/'.join(self.session)
        return self.__client.get(url, data=data)


class SailPlayClient(object):

    """ SailPlay client. """

    api_url = 'https://sailplay.ru/api'

    def __init__(self, pin_code, store_department_id, store_department_key,
                 token=None, silence=False, version='v2', loglevel='INFO'):
        self.params = locals()

    @property
    def token(self):
        return self.params.get('token', '')

    @property
    def credentials(self):
        return dict(
            pin_code=self.params.get('pin_code'),
            store_department_id=self.params.get('store_department_id'),
            store_department_key=self.params.get('store_department_key'),
            token=self.params.get('token'),
        )

    def login(self):
        """ Get API token. """
        json = self.get('login')
        self.params['token'] = json.get('token')
        return json

    def request(self, method, url, data=None):
        """ Request sailplay API. """
        url = "%s/%s/%s/" % (
            self.api_url, self.params.get('version'), url.strip('/'))
        params = dict(self.credentials)

        loglevel = self.params.get('loglevel', 'INFO')
        logger.setLevel(loglevel.upper())
        rs_logger.setLevel(loglevel.upper())

        if data and method == 'GET':
            params.update(data)

        try:
            response = rs.api.request(
                method, url, params=params, data=data)
            response.raise_for_status()
        except rs.HTTPError as exc:
            raise SailPlayException(exc)

        json = response.json()

        if json['status'] == 'error':
            if self.params['silence']:
                logger.error(json['message'])
            else:
                raise SailPlayException(json['message'])

        logger.debug(json)
        return json

    def get(self, *args, **kwargs):
        """ Proxy to method get. """
        return self.request('GET', *args, **kwargs)

    def post(self, *args, **kwargs):
        """ Proxy to method get. """
        return self.request('POST', *args, **kwargs)

    @property
    def api(self):
        """ Return proxy to self client. """
        return SailPlayAPI(client=self)

    @contextmanager
    def ctx(self, **params):
        """ Enter context. """
        _params = deepcopy(self.params)
        try:
            self.params.update(params)
            yield self
        finally:
            self.params = _params

# pylama:ignore=D
