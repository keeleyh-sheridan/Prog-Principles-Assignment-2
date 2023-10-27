import random

class Application:
    def positiveInput(self, message, type):
        num = float(input(message))
        while num < 0:
            print("Value must be greater than 0")
            num = float(input(message))

        if type == "int":
            return round(num, 2)
        else:
            return num

    def userInput(self):
        code = self.positiveInput("\nPlease enter the product code (integer from 1-100): ", "int")
        name = input("Please enter the product's name: ")
        stockLevel = self.positiveInput("Please enter the current stock (integer greater than 0): ", "int")
        salePrice = self.positiveInput("Please enter the sale price: ", "float")
        manufactureCost = self.positiveInput("Please enter the manufacturing cost: ", "float")
        monthlyUnits = self.positiveInput("Enter the estimated amount of monthly units manufactured: ", "int")

        return code, name, stockLevel, salePrice, manufactureCost, monthlyUnits

class Product:
    def __init__(self, code, name, stockLevel, salePrice, manufactureCost, monthlyUnits):
        self.__code = code
        self.__name = name
        self.__stockLevel = stockLevel
        self.__salePrice = salePrice
        self.__manufactureCost = manufactureCost
        self.__monthlyUnits = monthlyUnits

    def getCode(self):
        return self.__code
    def getName(self):
        return self.__name
    def getStockLevel(self):
        return self.__stockLevel
    def getSalePrice(self):
        return self.__salePrice
    def getManufactureCost(self):
        return self.__manufactureCost
    def getMonthlyUnits(self):
        return self.__monthlyUnits
    
    def setStockLevel(self, newStock):
        self.__stockLevel = newStock

product = Product(*Application.userInput())

print(f'''
Welcome to Programming Principles Sample Product Inventory
*******Programming Principles*******

Product Code: {product.getCode()}
Product Name: {product.getName()}

Sale Price: {product.getSalePrice()} CAD
Manufacture Cost: {product.getManufactureCost()} CAD
Monthly Production: {product.getMonthlyUnits()} units (Approx.)
''')

monthlyCost = product.getMonthlyUnits() * product.getManufactureCost()
unitsSold = 0
totalUnitsSold = 0
#For loop that calculates how many units have been manufactured and sold, updating the total stock and profits
for i in range(1, 13):
    unitsSold = product.getMonthlyUnits() + random.randrange(-10, 10)
    
    product.setStockLevel(product.getStockLevel() + (product.getMonthlyUnits() - unitsSold))

    totalUnitsSold += unitsSold

    print(f'''Month {i}
|    Manufactured: {product.getMonthlyUnits()}
|    Sold: {unitsSold} units
|    Stock: {product.getStockLevel()}''')
    
profit = (product.getSalePrice() * totalUnitsSold) - (product.getMonthlyUnits() * 12 * product.getManufactureCost())
print(f"Net profit: ${round(profit, 2)}CAD")