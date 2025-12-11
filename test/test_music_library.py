from lib.music_library import *
from unittest.mock import Mock

def test_empty_list_returned_when_initlised():
    library = MusicLibrary()
    assert library.tracks == []
    
def test_list_item_added_when_add_is_used_with_one_track():
    library = MusicLibrary()
    track = Mock()
    track.format = 'Drain You By Nirvana'
    library.add(track.format)
    assert library.tracks == ['Drain You By Nirvana']
    
def test_list_items_added_when_add_is_used_with_two_tracks():
    library = MusicLibrary()
    track1 = Mock()
    track1.format = 'Drain You By Nirvana'
    library.add(track1.format)
    track2 = Mock()
    track2.format = 'Just By Radiohead'
    library.add(track2.format)
    assert library.tracks == ['Drain You By Nirvana', 'Just By Radiohead']
    
def test_search_by_title_with_full_title():
    library = MusicLibrary()
    track = Mock()
    track.format = 'Soma By the Strokes'
    library.add(track.format)
    search = library.search_by_title('Soma')
    assert search == ['Soma By the Strokes']
    
    
def test_search_by_title_with_part_of_title():
    library = MusicLibrary()
    track = Mock()
    track.format = 'Soma By the Strokes'
    library.add(track.format)
    search = library.search_by_title('So')
    assert search == ['Soma By the Strokes']
    
def test_search_by_title_with_full_title_when_multiple_results():
    library = MusicLibrary()
    track1 = Mock()
    track1.format = 'Soma By the Strokes'
    library.add(track1.format)
    track2 = Mock()
    track2.format = 'Soma By not the Strokes'
    library.add(track2.format)
    search = library.search_by_title('Soma')
    assert search == ['Soma By the Strokes', 'Soma By not the Strokes']
    
    
def test_search_by_title_with_part_of_title_when_multiple_results():
    library = MusicLibrary()
    track1 = Mock()
    track1.format = 'Soma By the Strokes'
    library.add(track1.format)
    track2 = Mock()
    track2.format = 'Somewhere I Belong By Linkin Park'
    library.add(track2.format)
    search = library.search_by_title('So')
    assert search == ['Soma By the Strokes', 'Somewhere I Belong By Linkin Park']
    