from libpythonpro2 import github_api
from unittest.mock import Mock


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'avatar_url': 'https://avatars0.githubusercontent.com/u/13425415?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('alisonamerico')
    assert 'https://avatars0.githubusercontent.com/u/13425415?v=4' == url
