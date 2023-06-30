import tempfile
from unittest.mock import patch

from functions.level_2.four_lines_counter import count_lines_in


def test__count_lines_in__if_get_file_with_text_lines_and_comments_return_file_with_only_text_lines():
    with tempfile.NamedTemporaryFile(mode='w') as temp_file:
        temp_file.write('Text line 1\n')
        temp_file.write('Text line 2\n')
        temp_file.write('# Comment line\n')
        temp_file.write('Text line 3\n')

        with patch('functions.level_2.four_lines_counter.open', create=True) as mock_open:
            mock_file_handler = mock_open.return_value.__enter__.return_value
            mock_file_handler.readlines.return_value = [
                'Text line 1\n',
                'Text line 2\n',
                '# Comment line\n',
                'Text line 3\n'
            ]
            result = count_lines_in(temp_file.name)
            mock_open.assert_called_once_with(temp_file.name, 'r')
            assert result == 3


def test__count_lines_in__if_filepath_is_not_exist():
    filepath = '\path\noneexist\text.txt'
    assert count_lines_in(filepath) == None    


def test__count_lines_in__if_get_file_with_comment_lines_only_return_zero():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write('# Comment line 1\n')
        temp_file.write('# Comment line 2\n')
        filepath = temp_file.name

    result = count_lines_in(filepath)
    assert result == 0


def test__count_lines_in__if_get_empty_file_return_zero():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        filepath = temp_file.name
    result = count_lines_in(filepath)
    assert result == 0