class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    

class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty
        self.isWarranty = True

class Groceries(Product):
    def __init__(self, name, price, quantity, expiry):
        super().__init__(name, price, quantity)
        self.expiry = expiry
        self.isWarranty = False

class Cart:
    def __init__(self):
        self.cart = {}
    
    def addItem(self, product):
        self.cart[product] = True
        print(f'{product.quantity} {product.name}(s) added to shopping cart')
    
    def getItem(self, name):
        for product in self.cart:
            if(product.name == name):
                return product
        
        return None
    
    def removeItem(self, name):
        isRemoved = False
        for product in self.cart:
            if(product.name == name):
                self.cart[product]  = False
                isRemoved =  True
        
        if not isRemoved:
            print(f'Entered product name does not exist in cart')
        
    def viewCart(self):
        if len(self.cart) == 0:
            print(f'Empty Shopping Cart')
            return
        
        print(f'Current Shopping Cart:')
        for product in self.cart:
            if self.cart[product] and product.isWarranty:
                print(f'{product.name} - Price: ${round(product.price, 2)}, Quantity: {product.quantity}, Warranty: {product.warranty} months')
            
            if self.cart[product] and not product.isWarranty:
                print(f'{product.name} - Price: ${round(product.price, 2)}, Quantity: {product.quantity}, Expiry Date: {product.expiry}')
    
    def totalCost(self):
        if len(self.cart) == 0:
            print(f'Empty Shopping Cart')
            return
        
        total = 0
        for product in self.cart:
            if self.cart[product]:
                total += product.cost

        print(f'Total Cost: ${round(total, 2)}')

cart = Cart()
choice = int(input())
while choice != 6 :
    if choice == 1:
        cart.addItem(Electronics(input(), float(input()), int(input()), int(input())))
    if choice == 2:
        cart.addItem(Groceries(input(), float(input()), int(input()), float(input())))
    if choice == 3:
        cart.removeItem(input())
    if choice == 4:
        cart.viewCart()
    if choice == 5:
        cart.totalCost()
    choice = int(input())

print("Exit")