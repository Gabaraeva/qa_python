import pytest
from main import BooksCollector


class TestBooksCollector:

    # Тесты для add_new_book
    def test_add_new_book_single_book_added(self):
        collector = BooksCollector()
        collector.add_new_book("Маленький принц")
        assert "Маленький принц" in collector.books_genre

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.add_new_book("1984")
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize("invalid_name", [
        "",
        "Очень длинное название книги, которое явно превышает лимит в сорок символов"
    ])
    def test_add_new_book_invalid_name_not_added(self, invalid_name):
        collector = BooksCollector()
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.books_genre

    # Тесты для set_book_genre
    def test_set_book_genre_valid_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Роман")
        assert collector.get_book_genre("Война и мир") == ""

    # Тесты для get_book_genre
    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"

    def test_get_book_genre_returns_empty_for_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Без жанра")
        assert collector.get_book_genre("Без жанра") == ""

    # Тесты для get_books_genre
    def test_get_books_genre_returns_all_books(self):
        collector = BooksCollector()
        books = {
            "Преступление и наказание": "Детективы",
            "Война и мир": "",
            "1984": "Фантастика"
        }

        for book in books:
            collector.add_new_book(book)
            if books[book]:
                collector.set_book_genre(book, books[book])

        assert collector.get_books_genre() == books

    # Тесты для get_books_with_specific_genre
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.add_new_book("Сияние")
        collector.add_new_book("Зеленая миля")
        collector.set_book_genre("Оно", "Ужасы")
        collector.set_book_genre("Сияние", "Ужасы")
        collector.set_book_genre("Зеленая миля", "Драма")

        assert sorted(collector.get_books_with_specific_genre("Ужасы")) == ["Оно", "Сияние"]

    # Тесты для get_books_for_children
    def test_get_books_for_children_returns_child_friendly_books(self):
        collector = BooksCollector()
        child_books = ["Карлсон", "Незнайка на луне"]
        adult_books = ["Дракула", "Оно"]

        for book in child_books + adult_books:
            collector.add_new_book(book)

        collector.set_book_genre("Карлсон", "Мультфильмы")
        collector.set_book_genre("Незнайка на луне", "Фантастика")
        collector.set_book_genre("Дракула", "Ужасы")
        collector.set_book_genre("Оно", "Ужасы")

        result = collector.get_books_for_children()
        assert len(result) == 2
        for book in child_books:
            assert book in result
        for book in adult_books:
            assert book not in result

    # Тесты для избранного
    def test_add_book_in_favorites_added_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Алиса в стране чудес")
        collector.add_book_in_favorites("Алиса в стране чудес")
        assert "Алиса в стране чудес" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book("Моби Дик")
        collector.add_book_in_favorites("Моби Дик")
        collector.add_book_in_favorites("Моби Дик")
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_removed_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Три мушкетера")
        collector.add_book_in_favorites("Три мушкетера")
        collector.delete_book_from_favorites("Три мушкетера")
        assert "Три мушкетера" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_all_favorites(self):
        collector = BooksCollector()
        favorites = ["Книга 1", "Книга 2", "Книга 3"]
        for book in favorites:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        assert collector.get_list_of_favorites_books() == favorites

    def test_get_list_of_favorites_books_empty_returns_empty_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
  
