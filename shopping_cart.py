# Exercises
# Exercise 1 - Turn the shopping cart program from yesterday into an object-oriented program¶

text = {
    'divider': '=~' * 30,
    'main':'ADD / DELETE / VIEW / QUIT: ',
    'show_options': ['show', 's'],
    'add_options': ['add', 'a'],
    'delete_options': ['delete', 'd'],
    'quit_options': ['quit', 'q']
}

class ShoppingCart():
    
    def __init__(self, items):
        self.items = items
        
    def show_items(self):
        print("You Have items in your bag!!!")
        print(text['divider'])
        
        for item in self.items:
            print(f'{item} in your shopping bag.')
            print(text['divider'])
    
        
    def add_items(self):
        products = str(input('What would you like to add to your cart?: '))
        amount = int(input('Quantity: '))
        print(f"X{amount} {products} added to your shopping cart.")
        self.items.append(products)
        
        
    def delete_items(self):
        products = str(input('What would you like to remove to your cart?: '))
        amount = int(input('Quantity: '))
        self.items.remove(products)
        print(f"X{amount} {products} removed from you shopping cart.")   
        

    

shopping_cart = ShoppingCart([])


def main():
    while True:
        response = input('What do you want to do? add/delete/show or QUIT: ')
        
        if response in text['quit_options']:
            shopping_cart.show_items()
            print('Thanks for shopping!')
            break
        elif response in text['add_options']:
            shopping_cart.add_items()
            
        elif response in text['show_options']:
            shopping_cart.show_items()
        
        elif response in text['delete_options']:
            shopping_cart.delete_items()
            
main()


### Exercise 2 - Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.

class PythonString():

    def __init__(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())
