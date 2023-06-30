from functions.level_2.five_extra_fields import (
    fetch_app_config_field, fetch_extra_fields_configuration)


def test__fetch_extra_fields_configuration__get_without_config_return_empty_dict(mock_config_parser):
    mock_config_parser.return_value.get.return_value = None
    result = fetch_extra_fields_configuration('config.ini')
    expected_result = {}
    assert result == expected_result


def test__fetch_extra_fields_configuration__get_app_config_field_with_value_return_value(mock_config_parser):
    mock_config_parser.__getitem__.return_value = {'field_name': 'value'}
    result = fetch_app_config_field('config.ini', 'field_name')
    expected_result = 'value'
    assert result == expected_result


def test__fetch_extra_fields_configuration__get_app_config_field_without_value_return_none(mock_config_parser):
    mock_config_parser.__getitem__.return_value = {}
    result = fetch_app_config_field('config.ini', 'field_name')
    expected_result = None
    assert result == expected_result
