class FoodOrderingSystem:

    def __init__(self):
        self.orders = []
        self.menu()

    def menu(self):
        """
        This function is used to display the menu option to the user.
        It shows the message and the type of option present.
        """
        user_input = int(input("""
Hello, I hope you have a great day! please give your order.

1. Chinese      2. North Indian     3. South Indian     4. Deserts      5. Drinks       6. Exit.

Please Enter your choice :- """))

        if user_input == 1:
            self.chinese()
        elif user_input == 2:
            self.northIndian()
        elif user_input == 3:
            self.southIndian()
        elif user_input == 4:
            self.deserts()
        elif user_input == 5:
            self.drinks()
        elif user_input == 6:
            self.finalOrder()

    def order(self):
        """
        This function is used to take and display the order of the user.
        It takes the order of from the user and displays it to the user to recheck the order so that they can conform it.
        """
        print(f"Your order is {self.orders}")
        self.menu()


    def finalOrder(self):
        if len(self.orders) != 0:
            print(f"Your order is {self.orders} will be serverd shortly.")
        else:
            print("Sorry, you have not ordered any order.")


    def chinese(self):
        """
        This function will display the chinese food present in the restaurant menu and take will take the user order and show it to them.
        """
        user_input = int(input("""
CHINESE FOOD ITEMS :- 
1. Spring Rolls     2. Singapore Noodles        3. Manchurian       4. Chilli Paneer        5. Chilli Patato        6. Back to menu

Please Enter your choice :- """))

        if user_input == 1:
            self.orders.append("Spring Rolls")
            self.order()
        if user_input == 2:
            self.orders.append("Singapore Noodles")
            self.order()
        if user_input == 3:
            self.orders.append("Manchurian")
            self.order()
        if user_input == 4:
            self.orders.append("Chilli Paneer")
            self.order()
        if user_input == 5:
            self.orders.append("Chilli Patato")
            self.order()
        elif user_input == 6:
            self.menu()




    def northIndian(self):
        user_input = int(input("""
NORTH INDIAN FOOD ITEMS :- 
1. Matar Paneer     2. Paneer Tikka        3. Naan       4. Aloo Paratha        5. Daal Makhani     6. Back to menu.

Please Enter your choice :- """))
        if user_input == 1:
            self.orders.append("Matar Paneer")
            self.order()
        elif user_input == 2:
            self.orders.append("Paneer Tikka")
            self.order()
        elif user_input == 3:
            self.orders.append("Naan")
            self.order()
        elif user_input == 4:
            self.orders.append("Aloo Paratha")
            self.order()
        elif user_input == 5:
            self.orders.append("Daal Makhani")
            self.order()
        elif user_input == 6:
            self.menu()



    def southIndian(self):
        user_input = int(input("""
SOUTH INDIAN FOOD ITEMS :- 
1. Idle     2. Masala Dosa        3. Plain Dosa       4. Vada        5. Biryani     6. Back to menu.

Please Enter your choice :- """))
        if user_input == 1:
            self.orders.append("Idle")
            self.order()
        elif user_input == 2:
            self.orders.append("Masala Dosa")
            self.order()
        elif user_input == 3:
            self.orders.append("Plain Dosa")
            self.order()
        elif user_input == 4:
            self.orders.append("Vada")
            self.order()
        elif user_input == 5:
            self.orders.append("Biryani")
            self.order()
        elif user_input == 6:
            self.menu()


    def deserts(self):
        user_input = int(input("""
DESERTS FOOD ITEMS :- 
1. Kheer     2. Rasgula        3. Gajar Ka Halwa       4. Kulfi        5. Jalebi     6. Back to menu.

Please Enter your choice :- """))
        if user_input == 1:
            self.orders.append("Kheer")
            self.order()
        elif user_input == 2:
            self.orders.append("Rasgula")
            self.order()
        elif user_input == 3:
            self.orders.append("Gajar Ka Halwa")
            self.order()
        elif user_input == 4:
            self.orders.append("Kulfi")
            self.order()
        elif user_input == 5:
            self.orders.append("Jalebi")
            self.order()
        elif user_input == 6:
            self.menu()


    def drinks(self):
        user_input = int(input("""
DESERTS FOOD ITEMS :- 
1. Masala Chai     2. Lassi        3. Chocolate Shake       4. Mango Shake        5. Cocktail     6. Back to menu.

Please Enter your choice :- """))
        if user_input == 1:
            self.orders.append("Masala Chai")
            self.order()
        elif user_input == 2:
            self.orders.append("Lassi")
            self.order()
        elif user_input == 3:
            self.orders.append("Chocolate Shake")
            self.order()
        elif user_input == 4:
            self.orders.append("Mango Shake")
            self.order()
        elif user_input == 5:
            self.orders.append("Cocktail")
            self.order()
        elif user_input == 6:
            self.menu()





ordering_system = FoodOrderingSystem()