class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"
    @property
    def name(self):
        return self._name
    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        """Устанавливает количество страниц в книге."""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    super(Book).__str__()
    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages}'



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        """Устанавливает длительность аудиозаписи."""
        if not isinstance(duration, float):
            raise TypeError("Длительность аудиозаписи должна быть типа float")
        if duration <= 0:
            raise ValueError("Длительность аудиозаписи должна быть положительным числом")
        self.duration = duration

    super(Book).__str__()
    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration in minutes={self.duration}'

paper_book = PaperBook("Про Федота-стрельца, удалого молодца", "Филатов", 130)
print(paper_book)
print(repr(paper_book))
audio_book = AudioBook("I Am Zlatan Ibrahimović", " Zlatan Ibrahimović, David Lagercrantz", 621.5)
print(audio_book)
print(repr(audio_book))