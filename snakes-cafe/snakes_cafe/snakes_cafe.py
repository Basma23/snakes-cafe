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

    ***********************************
    ** What would you like to order? **
    ***********************************
    ''')

    items = ['Wings', 'Cookies', 'Spring Rolls',
             'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden',
             'Ice Cream', 'Cake', 'Pie',
             'Coffee', 'Tea', 'Unicorn Tears']

    order = []

    userOrder = input('> ').title()

    while userOrder.lower() != 'quit':
        if userOrder in items:
            order.append(userOrder)
            numberOfDishs = order.count(userOrder)
            if numberOfDishs == 1:
                print('** %d order of %s have been added to your meal **' %
                      (numberOfDishs, userOrder))
            if numberOfDishs > 1:
                print('** %d orders of %s have been added to your meal **' %
                      (numberOfDishs, userOrder))
        else:
            print('Sorry, your order is not in the menu, anything else?')
        userOrder = input('> ').title()

    print('Your order is: ' + ', '.join(order) + '.')


if __name__ == '__main__':
    print(snakes_cafe())
