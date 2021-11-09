import pytest

from app import app


@pytest.fixture
def mock_request():
    return


def test_get_200():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert '<form' in response.data.decode()


@pytest.mark.parametrize('zipcode,expected_result', [
    ('12525', ('John J. Faso',)),
    ('97206', ('Earl Blumenauer', 'Kurt Schrader')),
    ('78712', ('Roger Williams',)),
])
def test_post_data(zipcode, expected_result):
    """
    Given a zipcode associated to one or more districts, assert that after the form
    submits, the rendered page includes the name of the representative(s).
    """
    client = app.test_client()
    response = client.post('/', data={'zipcode': zipcode})
    assert response.status_code == 200
    rendered_result = response.data.decode()
    for expected_result in expected_result:
        assert expected_result in rendered_result


@pytest.mark.parametrize('zipcode', [
    '00000', '11111', 'aaaaa'
])
def test_post_zipcode_not_found(zipcode):
    """
    Given either an invalid zipcode or a zipcode that isn't present in the zipcode-districts.json
    file, assert we return a message to the user that the zipcode was not found.
    """
    client = app.test_client()
    response = client.post('/', data={'zipcode': zipcode})
    assert response.status_code == 200
    assert f'The zipcode {zipcode} could not be found.' in response.data.decode()
