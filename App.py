import random

#Class for managing user interaction
class Application:
    #Method for recieving a positive input from the user
    def positiveInput(self, message, type):
        num = float(input(message))
        while num < 0:
            print("Value must be greater than 0")
            num = float(input(message))

        if type == "int":
            return round(num, 2)
        else:
            return num

    #Method for receiving all needed values from the user
    def userInput(self):
        code = self.positiveInput("\nPlease enter the product code (integer from 1-100): ", "int")
        while code > 100:
            print("Value must be an integer from 1-100")
            code = self.positiveInput("\nPlease enter the product code (integer from 1-100): ", "int")
        name = input("Please enter the product's name: ")
        stockLevel = self.positiveInput("Please enter the current stock (integer greater than 0): ", "int")
        salePrice = self.positiveInput("Please enter the sale price: ", "float")
        manufactureCost = self.positiveInput("Please enter the manufacturing cost: ", "float")
        monthlyUnits = self.positiveInput("Enter the estimated amount of monthly units manufactured: ", "int")

        return code, name, stockLevel, salePrice, manufactureCost, monthlyUnits
    
    #Method for printing monthly stock statements
    def monthlyStatement(self, month, monthlyUnits, unitsSold, stockLevel):
        print(f'''Month {month}
|    Manufactured: {monthlyUnits}
|    Sold: {unitsSold} units
|    Stock: {stockLevel}''')
        
    #Method for printing initial stock statement and a welcome message
    def stockStatement(self, code, name, price, cost, monthlyUnits):
        print(f'''
Welcome to Programming Principles Sample Product Inventory
*******Programming Principles*******

Product Code: {code}
Product Name: {name}

Sale Price: {price} CAD
Manufacture Cost: {cost} CAD
Monthly Production: {monthlyUnits} units (Approx.)
''')
    def printFinalProfit(self, profit):
        print(f"Net profit: ${round(profit, 2)}CAD")

#Class for managing productsand storing related attributes 
class Product:
    #Constructor
    def __init__(self, code, name, stockLevel, salePrice, manufactureCost, monthlyUnits):
        self.__code = code
        self.__name = name
        self.__stockLevel = stockLevel
        self.__salePrice = salePrice
        self.__manufactureCost = manufactureCost
        self.__monthlyUnits = monthlyUnits

    #Getters
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
    
    #Setters
    def setStockLevel(self, newStock):
        self.__stockLevel = newStock

#Create objects
app = Application()
product = Product(*app.userInput())

#Print stock statement
app.stockStatement(product.getCode(), product.getName(), product.getSalePrice(), product.getManufactureCost(), product.getMonthlyUnits())

#Variables for loop calculations
monthlyCost = product.getMonthlyUnits() * product.getManufactureCost()
unitsSold = 0
totalUnitsSold = 0
#For loop that calculates how many units have been manufactured and sold, updating the total stock and profits
for i in range(1, 13):
    unitsSold = product.getMonthlyUnits() + random.randrange(-10, 10)
    
    if product.getMonthlyUnits() - unitsSold < 0 and product.getStockLevel() < abs(product.getMonthlyUnits() - unitsSold):
        unitsSold = product.getStockLevel()
        product.setStockLevel(0)
        
    else:
        product.setStockLevel(product.getStockLevel() + (product.getMonthlyUnits() - unitsSold))

    totalUnitsSold += unitsSold

    app.monthlyStatement(i, product.getMonthlyUnits(), unitsSold, product.getStockLevel())

#Print final profit
profit = (product.getSalePrice() * totalUnitsSold) - (product.getMonthlyUnits() * 12 * product.getManufactureCost())
app.printFinalProfit(profit)