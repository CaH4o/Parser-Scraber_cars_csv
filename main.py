import csv

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

def add_cars_gallery_to_cars():
    print('add cars gallery to cars - to implement')

def add_cars_options_to_cars():
    print('add cars options to cars - to implement')

def aplly_filter():
    print('aplly filter - to implement')

def show_cars():
    print('show_cars - to implement')

if __name__ == '__main__':
    cars = load_cars()
    # load_cars_gallery()
    # load_cars_otions()
    cars_gallery = load_cars_gallery()
    cars_options = load_cars_otions()
    cars = extruct_title(cars)
    cars = extruct_description(cars)
    # extruct_comment()
    cars = extruct_cars(cars)
    # add_cars_gallery_to_cars()
    # add_cars_options_to_cars()
    # aplly_filter()
    # show_cars()

    print(cars["101410920"]["description"])
