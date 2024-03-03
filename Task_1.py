# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

class Automobile:
    """Класс, описывающий автомобили"""
    def __init__(self, model: str, price: float):
        self.model = model    # краткое название машины (Ford Focus)
        self.price = price   # примерная стоимость в млн руб
    def __str__(self):
        return f'{self.__class__.__name__}({self.model}, {self.price} млн руб.)'
    def year_release(self):
        ...
Auto1 = Automobile("Kia Rio", 2.1)
print(Auto1.model)
print(Auto1)
print(Automobile.__doc__)

class PerviyKlaS:
    ''' Класс описывающий творчество Артема Франка'''
    def __init__(self, album: str, track: str, plays: float):
        self.album = album    # Название альбома ($ieg Kla$)
        self.track = track    # Название трека (Первый Первый)
        self.plays = plays    # Число прослушиваний в млн (3.5)
    def __str__(self):
        return f'{self.__class__.__name__}({self.album}: {self.track} ({self.plays} млн прослушиваний)'
    def sum_plays(self):
        ...    # складывание числа прослушиваний

track1 = PerviyKlaS("$ieg Kla$", "От заката до восхода", 2.2)
print(track1.album)
print(track1)
print(PerviyKlaS.__doc__)

class Liverpool:
    ''' Класс, описывающий игроков ФК Ливерпуль, Дарвина Нуньеза'''
    def __init__(self, name: str, matches: int, goals: int, assists: int):
        self.name = name
        self.matches = matches    # Число сыгранных матчей
        self.goals = goals    # Забитые голы
        self.assists = assists    # Отданные голевые передачи
    def __str__(self):
        return f'{self.name}- принял участие в {self.matches} матчах, забил {self.goals} голов' \
               f' и отдал {self.assists} голевых передач)'
    def increase_goals(self):
        ...    # увеличение забитых голов, если игрок отличился в матче
    def increase_assists(self):
        ...    # увеличение отданных голевых передач, если игрок отличился в матче

player1 = Liverpool("Дарвин Нуньез", 25, 10, 17)
print(player1.goals)
print(Liverpool.__doc__)