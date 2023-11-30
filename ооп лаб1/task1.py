from typing import Union

# TODO Написать 3 класса с документацией и аннотацией типов
class Box:
    """
    класс коробка
    аргументы:
        bool lock открыт или закрыт
        str gift подарок, который лежитвнутри
    методы:
        change_lock открывает / закрывает коробку
        islock узнать открыта / закрыта
        see_gift посмотреть подарок внутри
        get_gift -> str получить переменную gift
    примеры:
        >>> box1 = Box(True, 'свеча')
        >>> box1.islock()
        Бокс закрыт
        >>> box1.change_lock()
        >>> box1.see_gift()
        В боксе лежит свеча
        >>> box1.get_gift()
        'свеча'
    """
    def __init__(self, lock: bool, gift: str):
        #объявление переменных
        if not isinstance(lock, bool):
            raise TypeError
        self.lock = lock             #является ли коробка закрытой или нет
        if not isinstance(gift, str):
            raise TypeError
        self.gift = gift       #содержимое коробки

    def change_lock(self):
        #открываем/закрываем бокс
        self.lock = not self.lock

    def islock(self):
        #узнем открыт ли бокс
        if self.lock:
            print("Бокс закрыт")
        else:
            print("Бокс открыт")

    def see_gift(self):
        #смотрим подарок если бокс открыт
        if self.lock:
            print("Сначала откройте бокс")
        else:
            print(f"В боксе лежит {self.gift}")

    def get_gift(self) -> str:
        """
        метод получения значения, нужен для инкапсуляции,
        сделал чтобы показать анотации что возвращает метод
        """
        return self.gift

class Lamp:
    def __init__(self, glow: bool, brightness: float, temperature: int):
        #инициализация
        if not isinstance(glow, bool):
            raise TypeError
        self.glow = glow     #светится или нет
        if not isinstance(brightness, float):
            raise TypeError
        if not 0<=brightness<=1:
            raise ValueError
        self.brightness = brightness   #яркость
        if not isinstance(temperature, (int, float)):
            raise TypeError
        if not 2000<=temperature<=6000:
            raise ValueError
        self.temperature = temperature    #температура

    def switch(self):
        #переключатель лампы
        ...

    def change_brightness(self):
        #меняем яркость
        ...

class Card():
    def __init__(self, name: str, pin: int, balance: Union[int,float]):
        #инициализация
        self.name = name    #имя владельца
        self.pin = pin      #пинкод
        self.balance = balance      #баланс карты

    def valid(self, pin_input: int):
        #валидация пароля
        ...

    def plus_balance(self, cash: Union[int,float]):
        #пополнение баланса
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    box1 = Box(True, 'свеча')
    box1.islock()
    import doctest
    doctest.testmod()


