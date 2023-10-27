import random

class Product:
    def __init__(self):
        self.__code = int(input("\nPlease enter the product code (integer from 1-100): "))
        self.__name = input("Please enter the product's name: ")
        self.__stockLevel = int(input("Please enter the current stock (integer greater than 0): "))
        self.__salePrice = float(input("Please enter the sale prive: "))
        self.__manufactureCost = float(input("Please enter the manufacturing cost: "))
        self.__monthlyUnits = int(input("Enter the estimated amount of monthly units manufactured: "))

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

product = Product()

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
|    Manufactured: {product.monthlyUnits}
|    Sold: {unitsSold} units
|    Stock: {product.stockLevel}''')
    
profit = (product.getSalePrice() * totalUnitsSold) - (product.getMonthlyUnits() * 12 * product.getManufactureCost())
print(f"Net profit: ${round(profit, 2)}CAD")