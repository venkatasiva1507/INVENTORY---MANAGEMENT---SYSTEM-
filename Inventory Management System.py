# INVENTORY MANAGEMENT

lst_items = []
quantity = []
price = []
sellingprice = []

username = []
total_bill = []

cart = []
qnt_cart = []

print('*' * 10, 'WELCOME TO ALL IN ONE SHOP', '*' * 10)

while True:
    print('-----SELECT YOUR ROLE-----')
    print('1. OWNER')
    print('2. USER')
    print('3. EXIT')

    ch = input('Enter the role (1/2/3): ')

    # ================= OWNER SECTION =================
    if ch == '1':

        while True:
            print('\n-----OWNER SECTION------')
            print('1. Add items')
            print('2. Remove items')
            print('3. Update items')
            print('4. View inventory')
            print('5. View users details')
            print('6. View report')
            print('7. Total revenue')
            print('8. Exit section')

            s = input('Enter your choice: ')

            # ---------- ADD ITEM ----------
            if s == '1':
                item = input('Enter the item: ')

                if item not in lst_items:
                    qnt = float(input('Enter the quantity: '))
                    rate = float(input('Enter the price: '))
                    selling = float(input('Enter the selling price: '))

                    lst_items.append(item)
                    quantity.append(qnt)
                    price.append(rate)
                    sellingprice.append(selling)

                    print('Your item added successfully')

                else:
                    print(item, 'is already in the inventory')

            # ---------- REMOVE ITEM ----------
            elif s == '2':
                item = input('Enter the item to remove: ')

                if item in lst_items:
                    idx = lst_items.index(item)

                    lst_items.pop(idx)
                    quantity.pop(idx)
                    price.pop(idx)
                    sellingprice.pop(idx)

                    print(item, 'is removed from inventory successfully')

                else:
                    print(item, 'is not in the inventory')

            # ---------- UPDATE ITEM ----------
            elif s == '3':
                item = input('Enter the item to update: ')

                if item in lst_items:
                    idx = lst_items.index(item)

                    qut = input('Do you want to update quantity (yes/no): ')

                    if qut.lower() == 'yes':
                        qnt = float(input('Enter updated quantity: '))
                        quantity[idx] = qnt
                        print('Quantity is updated')

                    rise = input('Do you want to update price (yes/no): ')

                    if rise.lower() == 'yes':
                        rate = float(input('Enter the updated cost price: '))
                        price[idx] = rate
                        print('Price is updated')

                    sell_update = input(
                        'Do you want to update selling price (yes/no): '
                    )

                    if sell_update.lower() == 'yes':
                        selling = float(
                            input('Enter the updated selling price: ')
                        )
                        sellingprice[idx] = selling
                        print('Selling price is updated')

                else:
                    print(item, 'is not in the inventory')

            # ---------- VIEW INVENTORY ----------
            elif s == '4':
                print('\n---------VIEW INVENTORY-------')

                if len(lst_items) == 0:
                    print('No item is in the inventory')

                else:
                    print('ITEM / QUANTITY / PRICE / SELLING PRICE')

                    for i in range(len(lst_items)):
                        print(
                            lst_items[i],
                            '/',
                            quantity[i],
                            '/',
                            price[i],
                            '/',
                            sellingprice[i]
                        )

            # ---------- VIEW USERS ----------
            elif s == '5':
                print('\n---------USERS DETAILS---------')

                if len(username) == 0:
                    print('No customers yet')

                else:
                    for i in range(len(username)):
                        print(username[i], '--', total_bill[i])

            # ---------- VIEW REPORT ----------
            elif s == '6':
                print('\n---------REPORT---------')

                if len(lst_items) == 0:
                    print('No inventory available')

                else:
                    for i in range(len(lst_items)):
                        print(
                            'Item:',
                            lst_items[i],
                            '| Stock:',
                            quantity[i],
                            '| Cost Price:',
                            price[i],
                            '| Selling Price:',
                            sellingprice[i]
                        )

            # ---------- TOTAL REVENUE ----------
            elif s == '7':
                total_revenue = sum(total_bill)

                print('Total revenue of the shop:', total_revenue)

            # ---------- EXIT OWNER ----------
            elif s == '8':
                break

            else:
                print('Incorrect choice')

    # ================= USER SECTION =================
    elif ch == '2':

        user_name = input('Enter your name: ')

        if user_name not in username:
            username.append(user_name)
            total_bill.append(0)

        # Clear previous cart for a new shopping session
        cart = []
        qnt_cart = []

        while True:
            print('\n---------USER SECTION-----------')
            print('1. Add item to cart')
            print('2. Remove item')
            print('3. Modify item')
            print('4. View cart')
            print('5. Total bill')
            print('6. Exit')

            j = input('Enter the section you want: ')

            # ---------- ADD TO CART ----------
            if j == '1':
                item = input('Enter the item you want: ')

                if item in lst_items:

                    qnt = float(input('How much quantity do you want: '))
                    idx = lst_items.index(item)

                    if qnt <= 0:
                        print('Quantity must be greater than zero')

                    elif qnt <= quantity[idx]:

                        if item in cart:
                            cart_idx = cart.index(item)

                            qnt_cart[cart_idx] += qnt
                            quantity[idx] -= qnt

                        else:
                            cart.append(item)
                            qnt_cart.append(qnt)

                            quantity[idx] -= qnt

                        print('Item is added to cart')

                    else:
                        print('Insufficient stock')

                else:
                    print('No item available')

            # ---------- REMOVE FROM CART ----------
            elif j == '2':

                cart_item = input('What item do you want to remove: ')

                if cart_item in cart:

                    idx = cart.index(cart_item)

                    # Return quantity to inventory
                    inventory_idx = lst_items.index(cart_item)
                    quantity[inventory_idx] += qnt_cart[idx]

                    cart.pop(idx)
                    qnt_cart.pop(idx)

                    print('Item is successfully removed from cart')

                else:
                    print('Item is not in this cart')

            # ---------- MODIFY CART ----------
            elif j == '3':

                item = input('Item which you want to modify: ')

                if item in cart:

                    cart_idx = cart.index(item)
                    inventory_idx = lst_items.index(item)

                    old_quantity = qnt_cart[cart_idx]

                    new_quantity = float(
                        input('Enter the new quantity: ')
                    )

                    if new_quantity <= 0:
                        print('Quantity must be greater than zero')

                    else:
                        # Available stock includes the old cart quantity
                        available_stock = (
                            quantity[inventory_idx] + old_quantity
                        )

                        if new_quantity <= available_stock:

                            quantity[inventory_idx] = (
                                available_stock - new_quantity
                            )

                            qnt_cart[cart_idx] = new_quantity

                            print('Cart quantity updated')

                        else:
                            print('Insufficient stock')

                else:
                    print('Item not found in cart')

            # ---------- VIEW CART ----------
            elif j == '4':

                print('\n-------VIEW CART--------')

                if len(cart) == 0:
                    print('Cart is empty')

                else:
                    print('CART / QUANTITY / PRICE')

                    for i in range(len(cart)):
                        item = cart[i]
                        qty = qnt_cart[i]
                        idx = lst_items.index(item)

                        print(
                            item,
                            '/',
                            qty,
                            '/',
                            sellingprice[idx]
                        )

            # ---------- BILL ----------
            elif j == '5':

                if len(cart) == 0:
                    print('Cart is empty')

                else:

                    total = 0

                    print('\n---------BILL---------')
                    print('ITEM / QUANTITY / PRICE / TOTAL')

                    for i in range(len(cart)):

                        item = cart[i]
                        qty = qnt_cart[i]

                        idx = lst_items.index(item)

                        selling_rate = sellingprice[idx]

                        cost = qty * selling_rate

                        total += cost

                        print(
                            item,
                            '/',
                            qty,
                            '/',
                            selling_rate,
                            '/',
                            cost
                        )

                    print('----------------------')
                    print('TOTAL BILL:', total)

                    # Store bill for this user
                    user_idx = username.index(user_name)
                    total_bill[user_idx] += total

                    print('Billing complete!')

                    # Empty cart after billing
                    cart.clear()
                    qnt_cart.clear()

            # ---------- EXIT USER ----------
            elif j == '6':
                break

            else:
                print('Incorrect choice')

    # ================= EXIT SHOP =================
    elif ch == '3':
        print('SHOP IS CLOSED')
        print('THANK YOU, VISIT AGAIN')
        break

    else:
        print('Incorrect role choice')
