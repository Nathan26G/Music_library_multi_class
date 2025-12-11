from lib.track import *

def test_title_is_set_when_initalised():
    track = Track('Teddy Picker', 'Arctic Monkeys')
    assert track.title == 'Teddy Picker'
    
def test_artist_is_set_when_initalised():
    track = Track('Teddy Picker', 'Arctic Monkeys')
    assert track.artist == 'Arctic Monkeys'
    
def test_format_returns_correct_string():
    track = Track('Go With The Flow', 'Queens of the Stone Age')
    formated = track.format()
    assert formated == 'Go With The Flow By Queens of the Stone Age'