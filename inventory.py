

import os


def intro():
    print("******************************************************************")
    print("*                                                                *")
    print("*                                                                *")
    print("*       Welcome to my Stock Inventory Program                    *")
    print("*                                                                *")
    print("*                                                                *")
    print("******************************************************************")
    print("                                                                  ")


def menu():

    user_selected_option = 0

    while user_selected_option != 3:
        print("Select an Option For Inventory Maintenance")
        print("                                          ")
        print("Press 1 To -> Add Stock")
        print("Press 2 To -> Sale Of Items")
        print("Press 3 To -> Quit\n")

        user_selected_option = int(input("Please select option 1-3 from the menu: "))

        if user_selected_option == 1:
            add_stock()
        elif user_selected_option == 2:
            sale_of_items()
        elif user_selected_option == 3:
            print("Good Bye! ")
        else:  # validate selection
            print("That is not a valid option, please type the correct number\n")


def display_stocks():
    print("***********************************************************")
    print("         Available Items In Stock                          ")
    print("***********************************************************")
    f_obj = open("stock.txt")
    for line in f_obj:
        print(line.rstrip())
    f_obj.close()
    print("***********************************************************\n")


def add_stock():

    display_stocks()
    item_name = input("Please enter name of item :")
    unit_price = eval(input("Please enter unit price of item :"))
    quantity = eval(input("Please enter additional quantity of item :"))

    print("{} of price {} and quantity {} has been added".format(item_name, unit_price, quantity))
    print('\n')

    f_obj = open("stock.txt")
    f_obj_new = open("stocknew.txt", "w")

    item_already_exist = 0
    existing_quantity = 0
    for line1 in f_obj:
        arrline = line1.split(":")
        if arrline[0].upper() == item_name.upper():
            item_already_exist = 1
            existing_quantity = arrline[2]
        else:
            f_obj_new.writelines(line1)

    if item_already_exist == 1:
        print("found: " + item_name)
        f_obj_new.writelines("\n" + item_name + ":" + str(unit_price) + ":"
                             + str(quantity + eval(existing_quantity + ':')))
    else:
        f_obj_new.writelines("\n"+item_name+":"+str(unit_price)+":"+str(quantity)+":")

    f_obj_new.close()
    f_obj.close()
    os.remove("stock.txt")
    os.renames("stocknew.txt", "stock.txt")


def sale_of_items():

    display_stocks()

    item_name = input("Please enter name of item :")
    requested_quantity = eval(input("Please enter quantity of item :"))

    print("You purchased {} units of {}".format(requested_quantity, item_name))

    f_obj = open("stock.txt")
    f_obj_new = open("stocknew.txt", "w")
    f_obj_bill = open("bill.txt", "a")
    item_already_exist = 0
    existing_quantity = 0
    existing_unit_price = 0

    for line1 in f_obj:
        arr_line = line1.split(":")
        if arr_line[0].upper() == item_name.upper():
            item_already_exist = 1
            existing_unit_price = arr_line[1]
            existing_quantity = arr_line[2]
        else:
            f_obj_new.writelines(line1)

    if item_already_exist == 1:
        print("found: " + item_name)
        sale_quantity = 0
        if eval(existing_quantity) > requested_quantity:
            sale_quantity = requested_quantity
        else:
            sale_quantity = eval(existing_quantity)
        # Reduce quantity from stock.txt
        new_stock_quantity = eval(existing_quantity) - sale_quantity
        f_obj_new.writelines("\n" + item_name + ":" + str(existing_unit_price) +
                             ":" + str(new_stock_quantity) + ":")
        f_obj_bill.writelines("\n" + item_name + ":" + str(existing_unit_price) +
                              ":" + str(sale_quantity) + ":")
    else:
        print("Requested Item Not Found")

    f_obj_new.close()
    f_obj.close()
    f_obj_bill.close()
    os.remove("stock.txt")
    os.renames("stocknew.txt", "stock.txt")


intro()
menu()
