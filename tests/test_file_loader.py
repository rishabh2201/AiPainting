# Unit tests for file_loader.py

from file_loader import FileLoader


def test_get_artist_name():
    text = "DALL·E 2022-07-11 07.31.17 - cool bird wearing glasses in the style of lichtenstein, digital art.png"
    regex = " in the style of "
    expected = "lichtenstein, digital art.png"
    result = FileLoader.get_artist_name(text, regex)
    assert result == expected


def test_get_title_and_artist():
    text = "DALL·E 2022-07-11 07.31.17 - cool bird wearing glasses in the style of lichtenstein, digital art.png"
    preamble_regex = " .* - "
    artist_regex = " in the style of "
    file_extension = "png"
    expected = ("cool bird wearing glasses", "lichtenstein, digital art")
    result = FileLoader.get_title_and_artist(text, preamble_regex, artist_regex, file_extension)
    assert result == expected


def test_remove_text():
    text = "DALL·E 2022-07-11 07.31.17 - cool bird wearing glasses in the style of lichtenstein, digital art.png"
    remove = [", digital art", "in the style of ", "DALL·E "]
    expected = "2022-07-11 07.31.17 - cool bird wearing glasses lichtenstein.png"
    result = FileLoader.remove_text(text, remove)
    assert result == expected