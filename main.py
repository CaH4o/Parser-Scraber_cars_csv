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
        #'Продажа Geely Emgrand II, 2023 г. в Минске'
        # type, brand, model, restailing, no, plases, year, location
        base = car["title"].replace(" · ", "%").replace(".", "%")
        type = car["title"].split()[0]
        brand = car["title"].split()[1]
        model = base.split("%")[0][base.find(brand) + len(brand) + 1:]
        restailing = "1" # car["title"].split("·")[1]
        no = "1" #car["title"].split("·")[2].spleat(",")[0]
        plases = "plases"
        year = car["title"].split(".")[0][-6:-2]
        location_type = car["title"].split(".")[0][-1:]
        location = car["title"].split(".")[1][3:]
        car["title"] = {"type": type, "brand": brand, "model": model, "restailing": restailing, "no": no,
                        "plases": plases, "year": year, "location_type": location_type,  "location": location,
                        "base": base}
    return cars

def extruct_description():
    print('extruct description - to implement')

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
    cars_gallery = load_cars_gallery()
    cars_options = load_cars_otions()
    cars = extruct_title(cars)
    cars = extruct_cars(cars)
    #print(cars["103779165"])
    print(cars["104190182"])

    # extruct_cars()
    # extruct_title()
    # extruct_description()
    # extruct_comment()
    # load_cars_gallery()
    # add_cars_gallery_to_cars()
    # load_cars_otions()
    # add_cars_options_to_cars()
    # aplly_filter()
    # show_cars()

