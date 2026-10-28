from datetime import date
car_register = {
    "toyotaBZ4X": {
    "brand": "Toyota",
    "model": "Corolla",
    "price": 96_000,
    "year": 2012,
    "month": 8,
    "new": False,
    "km": 163_000
    },

    "pugeot408": {
    "brand": "Pugeot",
    "model": "408",
    "price": 330_000,
    "year": 2019,
    "month": 1,
    "new": False,
    "km": 40_000
    },

    "audiRS3": {
    "brand": "Audi",
    "model": "RS3",
    "price": 473_000,
    "year": 2022,
    "month": 2,
    "new": True,
    "km": 0
    },
}

NEW_CAR_REGISTRATION_FEE = 10783
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000

def print_car_information(car):
    print(f"Brand: {car['brand']}")
    print(f"Model: {car['model']}")
    print(f"Price: {car['price']}")
    print(f"Manufactures: {car['year']}-{car['month']}")

    if car["new"]:
        print(f"Condition: New")
    else:
        print(f"Condition: Used")

print_car_information(car_register["toyotaBZ4X"])

def create_car(car_register, brand, model, price, year, month, new, km):

    addCar = {
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "month": month,
        "new": new,
        "km": km
    }

    #Skapar ett id för nya bilar baserat på brand och model
    carId = brand.lower() + model

    car_register[carId] = addCar

    return addCar

car1 = create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)
print("car_register:", car_register)

def get_car_age(car):
    #Sparar dagens datum
    aDate = date.today() 
    #Detta året - bilens produktionsår
    getYear = aDate.year - car["year"]

    return getYear

print(get_car_age(car_register["pugeot408"]))

def rent_car_monthly_price(car):
    #Variabel som håller på det årliga priset. Bilens pris * 0,4 delat på 12 månader
    monthlyPrice = (car["price"] * RENT_CAR_PERCENTAGE) / 12

    if car["new"]:
        monthlyPrice += RENT_NEW_CAR__FEE

    return round(monthlyPrice, 2)

print(rent_car_monthly_price(car_register["audiRS3"]))

def next_eu_control(car):
    todaysDate = date.today()

    #Produktionsdatum
    carDate = date(car["year"], car["month"], 1)

    #Första eu kontrollen
    euControl = date(carDate.year + 2, carDate.month, 1)

    #While loop som kör fram till vi hittar nästa kontroll
    while euControl < todaysDate:
       euControl = date(euControl.year + 2, euControl.month, 1)
        

    return euControl

print(next_eu_control(car_register["pugeot408"]))

def calculate_total_price(car):

    startPrice = car["price"]
    fee = 0

    #Om ny bil blir fee 10783
    if car["new"]:
        fee = NEW_CAR_REGISTRATION_FEE
    
    #Bil mellan 0-3år får ny fee
    elif 0 <= get_car_age(car) <= 3:
        fee = 6681

    #Bil mellan 4-11år får ny fee
    elif 4 <= get_car_age(car) <= 11:
        fee = 4034

    #Bil mellan 12-29år får ny fee
    elif 12 <= get_car_age(car) <= 29:
        fee = 1729
    
    #Retunerar startpris plus avgiften
    return startPrice + fee

print(calculate_total_price(car_register["pugeot408"]))

class Car:
    def __init__(self, brand, model, price, year, month, new, km):
        self.brand = brand 
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km

    def print_information(self):
        #Denna visar information om bilen
        pass

    def get_age(self):
        #Denna visar bilens ålder
        pass

    def rent_monthly_price(self):
        #Visar hyrpriset på bilen
        pass

    def next_eu_control(self):
        #Visar datum för nästa eu-kontroll
        pass

    def calculate_total_price(self):
        #Visar totalpris för bilen
        pass
    
