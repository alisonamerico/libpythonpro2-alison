import pytest
from unittest.mock import Mock
from libpythonpro2 import github_api


@pytest.fixture
def avatat_url():
    resp_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/13425415?v=4'
    resp_mock.json.return_value = {
        'avatar_url': url,
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original


def test_buscar_avatar(avatat_url):
    url = github_api.buscar_avatar('alisonamerico')
    assert avatat_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('alisonamerico')
    assert 'https://avatars0.githubusercontent.com/u/13425415?v=4' == url
