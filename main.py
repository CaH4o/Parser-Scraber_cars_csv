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

def extruct_cars():
    print('extruct cars - to implement')

def extruct_title():
    print('extruct title - to implement')

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
    print(type(cars))
    print(len(cars))
    print(cars[0])
    print(type(cars[0]))
    cars_gallery = load_cars_gallery()
    print(len(cars_gallery))
    print(cars_gallery[0])
    cars_options = load_cars_otions()
    print(len(cars_options))
    print(cars_options[0])

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

