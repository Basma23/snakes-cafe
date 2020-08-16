print('''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
**********
Wings
Cookies
Spring Rolls
------------
************
Entrees
-------
*******
Salmon
Steak
Meat Tornado
A Literal Garden
----------------
****************
Desserts
--------
********
Ice Cream
Cake
Pie
---
***
Drinks
------
******
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************''')
menu = [
    {
        "plate": "Appetizers",
        "items": [
            "Wings",
            "Cookies",
            "Spring Rolls"
        ],
    },
    {
        "plate": "Entrees",
        "items": [
            "Salmon",
            "Steak",
            "Meat Tornado"
            "A Literal Garden"
        ],
    },
    {
        "plate": "Desserts",
        "items": [
            "Ice Cream",
            "Cake",
            "Pie"
        ],
    },
    {
        "plate": "Drinks",
        "items": [
            "Coffee",
            "Tea",
            "Unicorn Tears"
        ],
    },
]
for order in range(4):
    print(menu[order]["plate"])
    for orderType in range(len(menu[order]["items"])):
        print(menu[order]["items"][orderType])
orders = []
takingOrders = input()
# while takingOrders!= 'quit':
if takingOrders != 'quit':
    orders.append(takingOrders)
    numberOfOrders = orders.count(takingOrders)
    print("** %d orders of %s have been added to your meal **" %(numberOfOrders, takingOrders))
elif takingOrders == 'quit':
    print('Anything else')
    print("** %d orders of %s have been added to your meal **" %(numberOfOrders, takingOrders))
