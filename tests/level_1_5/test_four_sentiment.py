from functions.level_1_5.four_sentiment import check_tweet_sentiment
import pytest

@pytest.mark.parametrize(
    'text, good_words, bad_words, expected_result',
    [
        ('This text with only good words', ['good', 'best', 'perfect'], ['bad', 'scary', 'terrible'], 'GOOD'), 
        ('This text with only perfect words', ['good', 'best', 'perfect'], ['bad', 'scary', 'terrible'], 'GOOD'), 
        ('This text with only best words', ['good', 'best', 'perfect'], ['bad', 'scary', 'terrible'], 'GOOD'), 
    ]
)
def test__check_tweet_sentiment__return_good_when_only_good_words_found(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected_result



@pytest.mark.parametrize(
    'text, good_words, bad_words, expected_result',
    [
        ('This text with only bad words', ['good', 'best', 'perfect'], ['bad', 'scary', 'terrible'], 'BAD'), 
        ('This text with only scary words', ['good', 'best', 'perfect'], ['bad', 'scary', 'terrible'], 'BAD'), 
        ('This text with only terrible words', ['good', 'best', 'perfect'], ['bad', 'scary', 'terrible'], 'BAD'), 
    ]
)
def test__check_tweet_sentiment__return_bad_when_only_bad_words_found(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected_result


@pytest.mark.parametrize(
    'text, good_words, bad_words, expected_result',
    [
        ('This text with good and bad words', ['good', 'best', 'perfect'], ['bad', 'scary', 'terrible'], None), 
        ('This text with good best and bad scary words', ['good', 'best', 'perfect'], ['bad', 'scary', 'terrible'], None), 
        ('This text with good best perfect and bad scary  terrible words', ['good', 'best', 'perfect'], ['bad', 'scary', 'terrible'], None), 
    ]
)
def test__check_tweet_sentiment__return_none_when_equal_good_and_bad_words_found(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected_result


def test__check_tweet_sentiment__return_none_when_no_good_and_bad_words_found():
    text = 'This text without needed words'
    good_words = ['good', 'best', 'perfect']
    bad_words = ['bad', 'scary', 'terrible']
    assert check_tweet_sentiment(text, good_words, bad_words) == None