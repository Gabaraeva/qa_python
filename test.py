import pytest
from main import BooksCollector

# Позитивные и негативные проверки добавления книг
@pytest.mark.parametrize(
    'name, valid',
    [
        ('', False),          # Негативный: пустое имя
        ('A', True),          # Позитивный: 1 символ
        ('A' * 40, True),     # Позитивный: 40 символов
        ('A' * 41, False),    # Негативный: 41 символ
        (None, False)         # Негативный: None вместо имени
    ]
)
def test_add_new_book_name_length(name, valid):
    collector = BooksCollector()
    collector.add_new_book(name)
    assert (name in collector.books_genre) is valid

# Негативная проверка дублирования книг
def test_add_new_book_duplicate():
    collector = BooksCollector()
    collector.add_new_book('Дубликат')
    collector.add_new_book('Дубликат')  # Негативная: повторное добавление
    assert len(collector.books_genre) == 1

# Позитивные и негативные проверки установки жанра
@pytest.mark.parametrize(
    'book_added, genre, expected_genre',
    [
        (True, 'Фантастика', 'Фантастика'),    # Позитивный
        (True, 'Неизвестный', ''),             # Негативный: несуществующий жанр
        (False, 'Фантастика', None),           # Негативный: книга не существует
        (True, '', '')                         # Негативный: пустой жанр
    ]
)
def test_set_book_genre(book_added, genre, expected_genre):
    collector = BooksCollector()
    book_name = 'Книга'
    if book_added:
        collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == expected_genre

# позитивная проверка для get_book_genre
def test_get_book_genre_positive():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.set_book_genre('Книга', 'Фантастика')
    assert collector.get_book_genre('Книга') == 'Фантастика'

#  позитивная проверка для get_books_genre
def test_get_books_genre_positive():
    collector = BooksCollector()
    books = {
        'Книга1': 'Фантастика',
        'Книга2': 'Комедии',
        'Книга3': ''   # без жанра
    }
    for name, genre in books.items():
        collector.add_new_book(name)
        if genre:  # если жанр не пустой, устанавливаем
            collector.set_book_genre(name, genre)
    assert collector.get_books_genre() == books

# Негативная проверка получения книг по несуществующему жанру
def test_get_books_with_specific_genre_invalid():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    assert collector.get_books_with_specific_genre('Несуществующий') == []

# Позитивная и негативная проверки детских книг
def test_get_books_for_children():
    collector = BooksCollector()
    collector.add_new_book('Мультик')
    collector.add_new_book('Ужастик')
    collector.add_new_book('Детектив')
    collector.add_new_book('Без жанра')
    collector.set_book_genre('Мультик', 'Мультфильмы')
    collector.set_book_genre('Ужастик', 'Ужасы')
    collector.set_book_genre('Детектив', 'Детективы')
    
    children_books = collector.get_books_for_children()
    assert 'Мультик' in children_books       # Позитивная (без рейтинга)
    assert 'Ужастик' not in children_books   # Негативная (возрастной рейтинг)
    assert 'Детектив' not in children_books  # Негативная (возрастной рейтинг)
    assert 'Без жанра' not in children_books # Негативная (жанр не установлен)

# Негативные проверки добавления в избранное
def test_add_book_in_favorites_invalid():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.add_book_in_favorites('Несуществующая')  # Негативная: нет в коллекции
    collector.add_book_in_favorites('Книга')
    collector.add_book_in_favorites('Книга')  # Негативная: дублирование
    assert collector.get_list_of_favorites_books() == ['Книга']

# Негативная проверка удаления несуществующей книги из избранного
def test_delete_book_from_favorites_invalid():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.add_book_in_favorites('Книга')
    collector.delete_book_from_favorites('Несуществующая')  # Негативная
    assert 'Книга' in collector.get_list_of_favorites_books()

# Явная позитивная проверка для get_list_of_favorites_books
def test_get_list_of_favorites_books_positive():
    collector = BooksCollector()
    collector.add_new_book('Книга1')
    collector.add_new_book('Книга2')
    collector.add_book_in_favorites('Книга1')
    collector.add_book_in_favorites('Книга2')
    assert collector.get_list_of_favorites_books() == ['Книга1', 'Книга2']

# Позитивная и негативная проверки удаления из избранного
def test_delete_book_from_favorites():
    collector = BooksCollector()
    collector.add_new_book('Книга1')
    collector.add_new_book('Книга2')
    collector.add_book_in_favorites('Книга1')
    collector.add_book_in_favorites('Книга2')
    
    collector.delete_book_from_favorites('Книга1')  # Позитивная
    assert 'Книга1' not in collector.get_list_of_favorites_books()
    assert 'Книга2' in collector.get_list_of_favorites_books()
    
    collector.delete_book_from_favorites('Несуществующая')  # Негативная
    assert len(collector.get_list_of_favorites_books()) == 1
