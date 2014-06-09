import pytest


def test_base():
    from sailplay import SailPlayClient, SailPlayException

    client = SailPlayClient(
        'wrong', 'api', 'params'
    )

    with pytest.raises(SailPlayException):
        client.login()

# pylama:ignore=D
