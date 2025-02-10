# define the manu of our restaurant

menu = {
    'pizza': 50,
    'burger': 40,
    'pasta': 60,
    'french fries': 30,
    'sandwich': 20,
    'coke': 20,
    'coffee': 10,
    'tea': 10,
    'ice cream': 15,
    'cake': 20
    
}

# Greet msg for the customer

print('Welcome to our restaurant')

# Display the menu

print('Pizza:50\nBurger:40\nPasta:60\nFrench Fries:30\nSandwich:20\nCoke:20\nCoffee:10\nTea:10\nIce Cream:15\nCake:20')

order_total = 0

# Take the order from the customer

item_1 = input('Enter the item you want to order: ')
if item_1 in menu:
    order_total += menu[item_1]
    print(f'{item_1} added to your cart')
    
else:
    print(f'Sorry, {item_1} is not available in our restaurant')
    
    
another_item = input('Do you want to order another item? (yes/no): ')
if another_item == 'yes':
    item_2 = input('Enter the item you want to order: ')
    if item_2 in menu:
        order_total += menu[item_2]
        print(f'{item_2} added to your cart')
        
    else:
        print(f'Sorry, {item_2} is not available in our restaurant')
        
print(f'Your total bill is {order_total}')