import pytest
from main import BooksCollector

def test_add_new_book():
    collector = BooksCollector()
    collector.add_new_book("Маленький принц")
    assert "Маленький принц" in collector.books_genre

def test_cant_add_same_book_twice():
    collector = BooksCollector()
    collector.add_new_book("1984")
    collector.add_new_book("1984")
    assert len(collector.books_genre) == 1

def test_set_book_genre():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

def test_cant_set_invalid_genre():
    collector = BooksCollector()
    collector.add_new_book("Война и мир")
    collector.set_book_genre("Война и мир", "Роман")
    assert collector.get_book_genre("Война и мир") == ""

# Позитивная проверка для get_book_genre
def test_get_book_genre_for_book_without_genre():
    collector = BooksCollector()
    collector.add_new_book("Без жанра")
    assert collector.get_book_genre("Без жанра") == ""

def test_get_books_with_specific_genre():
    collector = BooksCollector()
    collector.add_new_book("Оно")
    collector.add_new_book("Сияние")
    collector.set_book_genre("Оно", "Ужасы")
    collector.set_book_genre("Сияние", "Ужасы")
    assert collector.get_books_with_specific_genre("Ужасы") == ["Оно", "Сияние"]

def test_get_books_for_children():
    collector = BooksCollector()
    collector.add_new_book("Карлсон")
    collector.add_new_book("Дракула")
    collector.set_book_genre("Карлсон", "Мультфильмы")
    collector.set_book_genre("Дракула", "Ужасы")
    assert "Карлсон" in collector.get_books_for_children()
    assert "Дракула" not in collector.get_books_for_children()

def test_add_book_to_favorites():
    collector = BooksCollector()
    collector.add_new_book("Алиса в стране чудес")
    collector.add_book_in_favorites("Алиса в стране чудес")
    assert "Алиса в стране чудес" in collector.get_list_of_favorites_books()

def test_cant_add_to_favorites_twice():
    collector = BooksCollector()
    collector.add_new_book("Моби Дик")
    collector.add_book_in_favorites("Моби Дик")
    collector.add_book_in_favorites("Моби Дик")
    assert len(collector.get_list_of_favorites_books()) == 1

def test_delete_book_from_favorites():
    collector = BooksCollector()
    collector.add_new_book("Три мушкетера")
    collector.add_book_in_favorites("Три мушкетера")
    collector.delete_book_from_favorites("Три мушкетера")
    assert "Три мушкетера" not in collector.get_list_of_favorites_books()

# Позитивная проверка для get_books_genre
def test_get_books_genre_returns_correct_dict():
    collector = BooksCollector()
    collector.add_new_book("Книга1")
    collector.set_book_genre("Книга1", "Фантастика")
    assert collector.get_books_genre() == {"Книга1": "Фантастика"}

# Позитивная проверка для get_list_of_favorites_books
def test_get_list_of_favorites_books_initially_empty():
    collector = BooksCollector()
    assert collector.get_list_of_favorites_books() == []

# Исправленный тест для недопустимых имен
@pytest.mark.parametrize("name", ["", "Очень длинное название книги, которое явно больше сорока символов"])
def test_cant_add_book_with_invalid_name(name):
    collector = BooksCollector()
    collector.add_new_book(name)
    assert name not in collector.get_books_genre()
