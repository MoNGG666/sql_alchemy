from app import app, db, Genre, Book
with app.app_context():
    # Создание жанров
    fiction = Genre(name='Fiction')
    scifi = Genre(name='Science Fiction')
    db.session.add(fiction)
    db.session.add(scifi)
    db.session.commit()

    # Создание книг
    book1 = Book(title='The Great Novel', author='John Doe', genre_id=1, is_read=True)
    book2 = Book(title='Space Odyssey', author='Arthur Clark', genre_id=2)
    db.session.add(book1)
    db.session.add(book2)
    db.session.commit()