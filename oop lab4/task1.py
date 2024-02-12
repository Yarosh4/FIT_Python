class Car:
    """
    Класс: автомобиль
    аргументы:
        mark - марка
        model - модель автомобиля
        is_auto_trans - установлена ли акпп
        engine - установленный двигатель
    методы:
        swap_transmision - замена трансмиссии на противополжную
        swap_engine - замена двигателя
    """
    def __init__(self, mark: str, model: str, is_auto_trans: bool, engine: str):
        if not isinstance(mark, str) or not isinstance(model, str) or not isinstance(engine, str):
            raise TypeError("Марка/модель/двигатель должна быть формата str")
        self.__mark = mark   #приватный тип т.к. не стоит менять марку и модель
        self.__model = model
        self.engine = engine
        if not isinstance(is_auto_trans, bool):
            raise TypeError("Должно быть значение типа bool. True для Акпп и False для Мкпп")
        self.__is_auto_trans = is_auto_trans

    def swap_transmision(self) -> None:
        """Свап трансмиссии на противоположную"""
        self.__is_auto_trans = not self.__is_auto_trans

    def swap_engine(self, swapped_engine: str) -> None:
        """Замена двигателя на swapped_engine"""
        if not isinstance(swapped_engine, str):
            raise TypeError("Двигатель должен быть типом str")
        self.engine = swapped_engine

    def __str__(self):
        return f"Марка {self.__mark}. Модель {self.__model}"

    def __repr__(self):
        return f"{self.__class__.__name__}(mark={self.__mark!r}, model={self.__model!r}, is_auto_trans={self.__is_auto_trans})"


class FreightCar(Car):
    """
    Класс: грузовой автомобиль
    Аргументы:
        аргументы базового класса
        lifting_capacity - грузоподъемность
    Методы:
        swap_transmision - наследован от базового класса
        swap_engine - перегружен, т.к. появляется условие по объему двигателя
    """
    def __init__(self, mark: str, model: str, is_auto_trans: bool, engine: str, lifting_capacity: int):
        super().__init__(mark, model, is_auto_trans, engine)
        if not isinstance(lifting_capacity, int):
            raise TypeError("Грузоподъемность должна быть целочисленной")
        if lifting_capacity <= 0:
            raise ValueError("Грузоподъемнотсь должна быть больше 0")
        self.lifting_capacity = lifting_capacity

    def swap_engine(self, swapped_engine: str, v_engine: float) -> None:
        if not isinstance(swapped_engine, str):
            raise TypeError("Двигатель должен быть типом str")
        if not isinstance(v_engine, float):
            raise TypeError("Объем двигателя должен быть float")
        if v_engine < 3.0:
            raise ValueError("Объема двигателя недостаточно для грузового автомобиля")
        self.engine = swapped_engine

    def __repr__(self):
        return f"{self.__class__.__name__}(mark={self._Car__mark!r}, model={self._Car__model!r}, is_auto_trans={self._Car__is_auto_trans}, engine={self.engine}, lifting_capacity={self.lifting_capacity})"

if __name__ == "__main__":
    # Write your solution here
    truck = FreightCar("Gaz", "21", True, "dvs-1", 2000)
    print(truck.__repr__())
    truck.swap_transmision()
    truck.swap_engine("dvs-2", 4.0)
    print(truck.__repr__())
