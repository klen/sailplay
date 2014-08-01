import pytest


def test_base():
    from sailplay import SailPlayClient, SailPlayException

    client = SailPlayClient('wrong', 'api', 'params')

    client.params['token'] = 1
    assert client.api.users.add.session == ['users', 'add']
    assert client.api.users['custom-vars'].session == ['users', 'custom-vars']

    with pytest.raises(SailPlayException):
        client.login()

# pylama:ignore=D
