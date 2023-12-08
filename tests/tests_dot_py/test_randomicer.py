import pytest
from src.randomicer import randomicer

@pytest.mark.randomicer
def test_randomicer_empty():
    playlist = []
    result = randomicer(playlist)
    assert result == []

@pytest.mark.randomicer
def test_randomicer_single_element():
    playlist = [1]
    result = randomicer(playlist)
    assert result == [1]

@pytest.mark.randomicer
def test_randomicer_multiple_elements():
    playlist = [1, 2, 3, 4, 5]
    result = randomicer(playlist)

    assert len(result) == len(playlist)

    for item in playlist:
        assert item in result

    assert result != playlist

@pytest.mark.randomicer
def test_randomicer_duplicates():
    playlist = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    result = randomicer(playlist)

    assert len(result) == len(playlist)

    for item in playlist:
        assert item in result

    assert result != playlist

@pytest.mark.randomicer
def test_randomicer_mixed_types():
    playlist = [1, 'a', 3.14, True, [1, 2, 3]]
    result = randomicer(playlist)

    assert len(result) == len(playlist)

    for item in playlist:
        assert item in result

    assert result != playlist
