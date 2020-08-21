def snakes_cafe():
    print('''
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    ************************************* 
    What would you like to order? **
    ***********************************
    ''')
    menu_list = [
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

    items = ["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]
    orders = []
    entering = input()
    while entering != 'quit':
        if entering in items:
            orders.append(entering)
            number_of_order = orders.count(entering)
            print("** %d order of %s have been added to your meal **" %(number_of_order, entering))
        else:
                print('Sorry, the meal that you ordered is not on our menu, anything else?')
    
        entering = input()

if __name__ == "__main__":
    print(snakes_cafe())


