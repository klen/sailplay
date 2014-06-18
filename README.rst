API sailplay.ru
###############

.. _description:

Python client for API sailplay.ru

.. _badges:

.. image:: https://secure.travis-ci.org/klen/sailplay.png?branch=master
    :target: http://travis-ci.org/klen/sailplay
    :alt: Build Status

.. image:: https://coveralls.io/repos//sailplay/badge.png?branch=master
    :target: https://coveralls.io/r/klen/sailplay
    :alt: Coverals

.. image:: https://pypip.in/d/sailplay/badge.png
    :target: https://pypi.python.org/pypi/sailplay

.. image:: https://badge.fury.io/py/sailplay.png
    :target: http://badge.fury.io/py/sailplay

.. _documentation:

**Docs are available at https://sailplay.readthedocs.org/. Pull requests
with documentation enhancements and/or fixes are awesome and most welcome.**

.. _contents:

.. contents::

.. _requirements:

Requirements
=============

- python >= 2.6

.. _installation:

Installation
=============

**sailplay** could be installed using pip: ::

    pip install sailplay

.. _usage:

Usage
=====

.. _bugtracker:

Initialize API client
---------------------
You should have `pin`, `store_department_id` and `store_department_key` from
the service.

::

    from sailplay import SailPlayClient

    client = SailPlayClient(pin, store_department_id, store_department_key)

Additional params
-----------------
::

    client = SailPlayClient(
        pin, store_department_id, store_department_key,
        token="token-here", # Set token manually (default "")
        silence=True,       # Dont fail on API errors (default False)
        loglevel="debug",   # Set log level (default INFO)
    )


Get API token
-------------

.. note:: Not required. Client will get token automatically on API requests.

::

    client.login()
    print client.token


Working with api
----------------

Sailplay have nice and easy syntax. Just have a look: ::

    # Get events list  http://sailplay.ru/api/v2/events/list/
    client.api.events.list()

    # Create a new user http://sailplay.ru/api/v2/users/add/?...
    client.api.users.add(user_phone='...', first_name='...', last_name='...')

    # Get info about user http://sailplay.ru/api/v2/users/info/?...
    client.api.users.info(user_phone='...')

    # Create purchase http://sailplay.ru/api/v2/purchases/new/?...
    client.api.purchases.new(**params)

    # And etc. I hope you make decision how the client works :)


For now client chooses API version automaticaly.


Context manager
---------------

You could redefine the client settings in context: ::

    with client.ctx(silence=True):
        # Errors will not be raised here
        client.api.users.add(user_phone='...', first_name='...', last_name='...')


Raw api request
---------------

You could make raw request to sailplay API: ::

    client.request(method='GET', url='/users/info', data={...})


Have a nice codding!


Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/klen/sailplay/issues


.. _contributing:

Contributing
============

Development of starter happens at github: https://github.com/klen/sailplay


Contributors
=============

* klen_ (Kirill Klenov)

.. _license:

License
=======

Licensed under a `BSD license`_.

.. _links:

.. _BSD license: http://www.linfo.org/bsdlicense.html
.. _klen: http://klen.github.com/
