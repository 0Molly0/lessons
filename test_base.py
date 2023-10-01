class TestLibraryAddress:

    def test_library_address(self, library):
        assert library.address == 'Sadova, 14'


class TestLibraryBooks:
    books_inner = ['aaa', 'bbb']

    def test_books_again(self, library):
        # assert library.books == []
        assert library.books == self.books_inner

    def test_library_books(self, library, books):
        assert library.books == []
        library.books.extend(books)
        assert library.get_random_book() in self.books_inner
