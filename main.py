import datetime

# декоратор для вывода времени запуска функции, введенных параметров и результата вычисления
def log(func):
    def wrapper(distance_km):
        result = func(distance_km) # вызов функции с расстоянием в километрах
        print(f"{datetime.datetime.now()} - расстояние: {distance_km} км, стоимость: ${result:.2f}") # вывод времени, расстояния и стоимости
        return result
    return wrapper

# функция для расчета стоимости поездки на такси
@log # применение декоратора для функции
def taxi_fare(distance_km):
    distance_m = distance_km * 1000  # переводим расстояние из километров в метры
    base_fare = 4.00 # базовый тариф
    per_meter_fare = 0.25 / 140  # стоимость за метр
    total_fare = base_fare + per_meter_fare * distance_m # общая стоимость
    return total_fare

# пользовательский ввод расстояния поездки
distance_km = float(input("Введите расстояние поездки в километрах: "))

# расчет стоимости и вывод результата
fare = taxi_fare(distance_km) # вызов функции с пользовательским вводом
print(f"Стоимость поездки на {distance_km} км составляет ${fare:.2f}") # вывод итоговой стоимости поездки
