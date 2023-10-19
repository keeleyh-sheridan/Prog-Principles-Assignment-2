class Product:
    def __init__(self):
        self.code = int(input("\nPlease enter the product code (integer from 1-100): "))
        self.name = input("Please enter the product's name: ")
        self.stockLevel = int(input("Please enter the current stock (integer greater than 0): "))
        self.salePrice = float(input("Please enter the sale prive: "))
        self.manufactureCost = float(input("Please enter the manufacturing cost: "))
        self.monthlyUnits = int(input("Enter the estimated amount of monthly units manufactured: "))

product = Product()

print(f'''
Welcome to Programming Principles Sample Product Inventory
*******Programming Principles*******
      
Product Code: {product.code}
Product Name: {product.name}

Sale Price: {product.salePrice} CAD
Manufacture Cost: {product.manufactureCost} CAD
Monthly Production: {product.monthlyUnits} units (Approx.)
''')