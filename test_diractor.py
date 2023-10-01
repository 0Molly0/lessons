def test_library_director_name(library):
    assert library.director.startswith('Mr. ')
