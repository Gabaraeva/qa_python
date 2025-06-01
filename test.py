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

@pytest.mark.parametrize("name", ["", "Очень длинное название книги больше сорока символов"])
def test_cant_add_book_with_invalid_name(name):
    collector = BooksCollector()
    collector.add_new_book(name)
    assert name not in collector.books_genre
def test_get_book_genre_positive():
    collector = BooksCollector()
    collector.add_new_book("Мастер и Маргарита")
    collector.set_book_genre("Мастер и Маргарита", "Фантастика")
    assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"

def test_get_books_genre_positive():
    collector = BooksCollector()
    collector.add_new_book("Преступление и наказание")
    collector.add_new_book("Война и мир")
    collector.set_book_genre("Преступление и наказание", "Детективы")
    expected = {
        "Преступление и наказание": "Детективы",
        "Война и мир": ""
    }
    assert collector.get_books_genre() == expected

def test_get_list_of_favorites_books_positive():
    collector = BooksCollector()
    books = ["Книга 1", "Книга 2", "Книга 3"]
    for book in books:
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
    assert collector.get_list_of_favorites_books() == books