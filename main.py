import csv
from tabulate import tabulate
import sys

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
        year = int(str[:4])
        transmission = str.split(", ")[1]
        str = str.split(", ", 2)[2]
        # engine, fuel
        is_engine_empty = ' л' not in str.split(",")[0]
        if is_engine_empty:
            engine = 0
            fuel = str.split(", ")[0]
            str = str.split(", ", 1)[1]
        else:
            engine = int(str.split(", ")[0][:1]) * 1000 + int(str.split(", ")[0][2:3]) * 100
            fuel = str.split(", ")[1]
            str = str.split(", ", 2)[2]
        # mileage, power_reserve
        str = str.replace(" | ", "%")
        is_power_reserve = 'запас хода' in str.split("%")[0]
        if is_power_reserve:
            power_reserve = str.split("%")[0].split(", ")[0][11:]
            mileage = int(str.split("%")[0].split(", ")[1].replace(" ", "")[:-2])
        else:
            power_reserve = ""
            mileage = int(str.split("%")[0].replace(" ", "")[:-2])
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


def extruct_comment(cars):
    for car in cars:
        car["comment"] = car["comment"].split("|")
    return cars

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
    filters = str(sys.argv)
    filter_year_from = "2012"
    filter_year_to = ""
    filter_brand = "NISSAN"
    filter_model = "X-TRAIL"
    filter_price_from = ""
    filter_price_to = "" #8000
    filter_transmission = "механика"
    filter_mileage = "" #10000
    filter_body = "внедорожник"
    filter_engine_from = "1600"
    filter_engine_to = "2000"
    filter_fuel = "дизель"
    filter_exchange = "yes"
    filter_keywords = "сигнализация"
    filter_labels = "VIN"

    for i in range(len(sys.argv)):
        # —year_from
        if "—year_from" in filters[i]:
            i = i + 1
            filter_year_from = filters[i]
            continue
        # —year_to
        if "—year_to" in filters[i]:
            i = i + 1
            filter_year_to = filters[i]
            continue
        # —brand
        if "—brand" in filters[i]:
            i = i + 1
            filter_brand = filters[i]
            continue
        # —model
        if "—model" in filters[i]:
            i = i + 1
            filter_model = filters[i]
            continue
        # —price_from
        if "—price_from" in filters[i]:
            i = i + 1
            filter_price_from = filters[i]
            continue
        # —price_to (8000)
        if "—price_to" in filters[i]:
            i = i + 1
            filter_price_to = filters[i]
            continue
        # —transmission
        if "—transmission" in filters[i]:
            i = i + 1
            filter_transmission = filters[i]
            continue
        # —mileage
        if "—mileage" in filters[i]:
            i = i + 1
            filter_mileage = filters[i]
            continue
        # —body
        if "—body" in filters[i]:
            i = i + 1
            filter_body = filters[i]
            continue
        # —engine_from
        if "—engine_from" in filters[i]:
            i = i + 1
            filter_engine_from = filters[i]
            continue
        # —engine_to
        if "—engine_to" in filters[i]:
            i = i + 1
            filter_engine_to = filters[i]
            continue
        # —fuel
        if "—fuel" in filters[i]:
            i = i + 1
            filter_fuel = filters[i]
            continue
        # —exchange
        if "—exchange" in filters[i]:
            i = i + 1
            filter_exchange = filters[i]
            continue
        # —keywords
        if "—keywords" in filters[i]:
            i = i + 1
            filter_keywords = filters[i]
            continue
        # —keywords
        if "—labels" in filters[i]:
            i = i + 1
            filter_labels = filters[i]
            continue


    result = {}
    for id in cars:
        if filter_year_from != "":
            if int(filter_year_from) > cars[id]["description"]["year"]:
                continue
        if filter_year_to != "":
            if int(filter_year_to) < cars[id]["description"]["year"]:
                continue
        if filter_brand != "":
            if filter_brand.lower() != cars[id]["title"]["brand"].lower():
                continue
        if filter_model != "":
            if filter_model.lower() not in cars[id]["title"]["model"].lower():
                continue
        # if filter_price_from != "":
        #     if int(filter_price_from) > cars[id]["price_secondary"]:
        #         continue
        # if filter_price_to != "":
        #     if int(filter_price_to) < cars[id]["price_secondary"]:
        #         continue
        if filter_transmission != "":
            if filter_transmission != cars[id]["description"]["transmission"]:
                continue
        # if filter_mileage != "":
        #     if filter_mileage != cars[id]["description"]["mileage"]:
        #         continue
        if filter_body != "":
            if filter_body != cars[id]["description"]["body"]:
                continue
        if filter_engine_from != "":
            if int(filter_engine_from) > cars[id]["description"]["engine"]:
                continue
        if filter_engine_to != "":
            if int(filter_engine_to) < cars[id]["description"]["engine"]:
                continue
        if filter_fuel != "":
            if filter_fuel != cars[id]["description"]["fuel"]:
                continue
        if filter_exchange != "":
            if filter_exchange == "yes" and "Обмен не интересует" in cars[id]["exchange"]:
                continue
            if filter_exchange == "no" and "Возможен обмен" in cars[id]["exchange"][:14]:
                continue
        if filter_keywords != "":
            words = filter_keywords.split(", ")
            is_not_present = True
            for word in words:
                if is_not_present == False:
                    break
                for option in cars[id]["options"]:
                   if word.lower() in option["category"].lower() or word.lower() in option["item"].lower():
                        is_not_present = False
                        break
            if is_not_present:
                continue
        if filter_labels != "":
            if filter_labels != cars[id]["labels"]:
                continue
        result[id] = cars[id]
    return result


def show_cars(cars):
    headers = ["id", "price", "brand", "model", "year", "transmission", "engine", "mileage", "body", "images", "options"]
    data = []
    print(f"Found # {len(cars)} cars. You can see details below:")
    for id in cars:
        data.append([
            cars[id]["card_id"],
            cars[id]["price_secondary"],
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
    cars = extruct_comment(cars)
    cars = extruct_cars(cars)
    cars = add_cars_gallery_to_cars(cars, cars_gallery)
    cars = add_cars_options_to_cars(cars, cars_options)
    ##
    cars = aplly_filter(cars)
    show_cars(cars)
    print(f"\n{cars}")