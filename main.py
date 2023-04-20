import csv
from tabulate import tabulate

def load_file(file_path):
    result = []
    with open(file_path, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row)
    return result


def load_cars():
    file_path = './src/cars-av-by_card.csv'
    return load_file(file_path)


def load_cars_gallery():
    file_path = './src/cars-av-by_card_gallery.csv'
    return load_file(file_path)


def load_cars_otions():
    file_path = './src/cars-av-by_card_options.csv'
    return load_file(file_path)


def extruct_cars(cars):
    result = {}
    for car in cars:
        result[car["card_id"]] = car
    return result

def extruct_title(cars):
    for car in cars:
        str = car["title"]
        # type, brand
        type = str.split()[0]
        brand = str.split()[1]
        str = str.split(" ", 2)[2]
        # year, location
        year = str.split(".")[0][-6:-2]
        location = str.split(".")[1][3:]
        str = str.split(".")[0][:-8]
        # plases
        plases = ""
        if 'мест' in str:
            plases = str.split("мест")[0][-2:-1]
            str = str.split("мест")[0][:-4]
        # model, restailing, no
        str = str.replace(" · ", "%").replace(" (", "%").replace(")", "%")
        column = len(str.split("%"))
        if column == 1:
            model = str.split("%")[0]
            restailing = ""
            no = ""
        if column == 2:
            model = str.split("%")[0]
            restailing = str.split("%")[1]
            no = ""
        if column == 3:
            model = str.split("%")[0]
            restailing = str.split("%")[1]
            no = str.split("%")[2]
        car["title"] = {
            "base": car["title"],
            "type": type, "brand": brand, "model": model, "restailing": restailing,
            "no": no, "plases": plases, "year": year,  "location": location
        }
    return cars


def extruct_description(cars):
    for car in cars:
        str = car["description"]
        # year, transmission
        year = str[:4]
        transmission = str.split(", ")[1]
        str = str.split(", ", 2)[2]
        # engine, fuel
        is_engine_empty = ' л' not in str.split(",")[0]
        if is_engine_empty:
            engine = ""
            fuel = str.split(", ")[0]
            str = str.split(", ", 1)[1]
        else:
            engine = str.split(", ")[0]
            fuel = str.split(", ")[1]
            str = str.split(", ", 2)[2]
        # mileage, power_reserve
        str = str.replace(" | ", "%")
        is_power_reserve = 'запас хода' in str.split("%")[0]
        if is_power_reserve:
            power_reserve = str.split("%")[0].split(", ")[0][11:]
            mileage = str.split("%")[0].split(", ")[1]
        else:
            power_reserve = ""
            mileage = str.split("%")[0]
        str = str.split("%")[1]
        # drive_unit, color
        drive_unit = str.split(", ")[1]
        color = ""
        if len(str.split(", ")) == 3:
            color = str.split(", ")[2]
        str = str.split(",")[0]
        # body, number_of_doors
        is_doors = 'дв.' in str
        if is_doors:
            body = str[:-6]
            number_of_doors = str[-5:-4]
        else:
            body = str
            number_of_doors = ""

        car["description"] = {
            "base": car["description"],
            "year": year, "transmission": transmission, "engine": engine, "fuel": fuel,
            "power_reserve": power_reserve, "mileage": mileage, "body": body,
            "number_of_doors": number_of_doors, "drive_unit": drive_unit, "color": color
        }
    return cars


def extruct_comment():
    print('extruct comment - to implement')


def add_cars_gallery_to_cars(cars, car_gallery):
    for row in car_gallery:  # 'card_id', 'ind', 'url', 'scrap_date'
        id = row["card_id"]
        if id in cars:
            if "gallery" in cars[id]:
                cars[id]["gallery"].append(row)
            else:
                cars[id]["gallery"] = [row]
    return cars

def add_cars_options_to_cars(cars, cars_options):
    for row in cars_options: # 'card_id', 'category', 'item', 'scrap_date'
        id = row["card_id"]
        if id in cars:
            if "options" in cars[id]:
                cars[id]["options"].append(row)
            else:
                cars[id]["options"] = [row]
    return cars


def aplly_filter(cars):
    result = {}
    for id in cars:
        filter_1 = cars[id]["labels"] == 'VIN'
        filter_2 = cars[id]["title"]["brand"] == 'Geely'
        filter_3 = cars[id]["description"]["fuel"] == 'бензин'
        is_added = filter_1 and filter_2 and filter_3
        if is_added:
            result[id] = cars[id]
    return result


def show_cars(cars):
    headers = ["id", "price", "brand", "model", "year", "transmission", "engine", "mileage", "body", "images", "options"]
    data = []
    for id in cars:
        data.append([
            cars[id]["card_id"],
            cars[id]["price_primary"],
            cars[id]["title"]["brand"],
            cars[id]["title"]["model"],
            cars[id]["description"]["year"],
            cars[id]["description"]["transmission"],
            cars[id]["description"]["engine"],
            cars[id]["description"]["mileage"],
            cars[id]["description"]["body"],
            len(cars[id]["gallery"]) if "gallery" in cars[id] else 0,
            len(cars[id]["options"]) if "options" in cars[id] else 0,
        ])

    print(tabulate(data, headers=headers))


if __name__ == '__main__':
    ## Load
    cars = load_cars()
    cars_gallery = load_cars_gallery()
    cars_options = load_cars_otions()
    ## Transformation
    cars = extruct_title(cars)
    cars = extruct_description(cars)
    # extruct_comment()
    cars = extruct_cars(cars)
    cars = add_cars_gallery_to_cars(cars, cars_gallery)
    cars = add_cars_options_to_cars(cars, cars_options)
    ##
    cars = aplly_filter(cars)
    show_cars(cars)
