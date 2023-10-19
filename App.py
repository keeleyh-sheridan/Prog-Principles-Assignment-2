class Product:
    def __init__(self):
        self.code = int(input("Please enter the product code (integer from 1-100): "))
        self.name = input("Please enter the product's name: ")
        self.stockLevel = int(input("Please enter the current stock (integer greater than 0): "))
        self.salePrice = float(input("Please enter the sale prive: "))
        self.manufactureCost = float(input("Please enter the manufacturing cost: "))
        self.monthlyUnits = int(input("Enter the estimated amount of monthly units manufactured"))

product1 = Product()
