import csv

class Car:
    def __init__(
            self,
            name=None,
            year=None,
            body_type=None,
            engine=None,
            doors=None,
            sits=None,
            transmission=None,
            speed=None,
            consumption=None,
            brand=None,
    ):
        self.name = name
        self.year = year
        self.body_type = body_type
        self.engine = engine
        self.doors = doors
        self.sits = sits
        self.transmission = transmission
        self.speed = speed
        self.brand = brand
        self.consumption = consumption  # 10 л на 100 км

    def get_fuel_consume(self, range_):
        if self.consumption is not None:
            return self.consumption / 100 * range_
        else:
            return None

    def compare(self, another_car):
        print("name", self.name, another_car.name, sep=" | ")
        print("year", self.year, another_car.year, sep=" | ")
        print("body_type", self.body_type, another_car.body_type, sep=" | ")
        print("engine", self.engine, another_car.engine, sep=" | ")
        print("doors", self.doors, another_car.doors, sep=" | ")
        print("sits", self.sits, another_car.sits, sep=" | ")
        print("transmission", self.transmission, another_car.transmission, sep=" | ")
        print("speed", self.speed, another_car.speed, sep=" | ")
        print("consumption", self.consumption, another_car.consumption, sep=" | ")

    def __str__(self):
        return self.name


def load_csv():
    filename = "/home/hasan/german_cars.csv"
    with open(filename) as f:
        csv_reader = csv.DictReader(f)
        return csv_reader.fieldnames, list(csv_reader)


def get_year(date_string: str) -> int:

    year_number = int(date_string.split("-")[1])
    if year_number > 22:
        return 1900 + year_number
    else:
        return 2000 + year_number


def load_car(car_data: dict) -> Car:
    car = Car(
        name=car_data["Full car name"],
        year=get_year(car_data["Model series launch date"]),  # Mar-19
        body_type=car_data['Body type'],
        engine=car_data['Displacement (ccm)'],
        brand=car_data["Brand"],
    )
    return car


fieldnames, data = load_csv()

cars = []
for dict_obj in data:
    car_obj = load_car(dict_obj)
    cars.append(car_obj)

print(cars)
car = cars[0]
print(car)
