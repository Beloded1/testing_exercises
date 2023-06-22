from functions.level_1.three_url_builder import build_url
import pytest


def test__build_url__with_relative_url():
    assert build_url("example.com", "path/to/resource") == "example.com/path/to/resource"


def test__build_url__with_relative_url_and_get_params():
    assert build_url("example.com", "path/to/resource", {"param1": "value1", "param2": "value2"}) == "example.com/path/to/resource?param1=value1&param2=value2"


def test__build_url__with_relative_url_and_empty_get_params():
    assert build_url("example.com", "path", {}) == "example.com/path"


@pytest.mark.parametrize(
    'host_name, relative_url, get_params, expected_result',
    [
        ('example.com', 'path/to/resource', None, 'example.com/path/to/resource'),
        ('example.com', 'path/to/resource', {"param1": "value1", "param2": "value2"}, 'example.com/path/to/resource?param1=value1&param2=value2'),
        ('example.com', 'path', {}, 'example.com/path'),
        ],
        ids=[
            'build_url__with_relative_url',
            'build_url__with_relative_url_and_get_params',
            'build_url__with_relative_url_and_empty_get_params',
        ]

)
def test__build_url(host_name, relative_url, get_params, expected_result):
    assert build_url(host_name, relative_url, get_params) == expected_result
