# Beyza Nur Deliktaş
# Global AI Hub - Akbank Python Bootcamp
# **** Pizza Order System ****

import csv
import datetime


class Pizza:
    def __init__(self, description, cost):
        self._description = description
        self._cost = cost

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._cost


class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic pizza", 10.0)


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita pizza", 12.0)


class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Turkish pizza", 15.0)


class PlainPizza(Pizza):
    def __init__(self):
        super().__init__("Plain pizza", 20.0)


class Decorator():
    def __init__(self, description, cost):
        self._description = description
        self._cost = cost

    def get_cost(self):
        return self._cost

    def get_description(self):
        return self._description


class Olive(Decorator):
    def __init__(self):
        super().__init__("Olive", 2.25)


class Mushroom(Decorator):
    def __init__(self):
        super().__init__("Mushroom", 1.5)


class GoatCheese(Decorator):
    def __init__(self):
        super().__init__("Goat Cheese", 3.0)


class Meat(Decorator):
    def __init__(self):
        super().__init__("Meat", 3.5)


class Onion(Decorator):
    def __init__(self):
        super().__init__("Onion", 1.25)


class Corn(Decorator):
    def __init__(self):
        super().__init__("Corn", 1.5)


class PizzaMenu:
    def print_menu(self):
        # Read the menu from the file
        with open("Menu.txt", "r") as f:
            menu = f.read()

        # Display the menu on the screen
        print(menu)

    def select_pizza(self):
        while True:
            try:
                choice = int(input("\nPlease enter the number of the pizza you want to select:(1-4)"))
                if choice < 1 or choice > 4:
                    raise ValueError
                else:
                    if choice == 1:
                        pizza = ClassicPizza().get_description()
                        pizza_cost = ClassicPizza().get_cost()
                        break
                    if choice == 2:
                        pizza = MargheritaPizza().get_description()
                        pizza_cost = ClassicPizza().get_cost()
                        break
                    if choice == 3:
                        pizza = TurkishPizza().get_description()
                        pizza_cost = ClassicPizza().get_cost()
                        break
                    if choice == 4:
                        pizza = PlainPizza().get_description()
                        pizza_cost = ClassicPizza().get_cost()
                        break
            except ValueError:
                print("\nPlease make a valid choice.")
        return pizza, pizza_cost


class SauceMenu:

    def select_sos(self):
        sauces = []
        sauce_number = 0
        sauce_cost = 0

        # boolean appointment to prevent re-election
        olive_isSelected = False
        mushroom_isSelected = False
        goatCheese_isSelected = False
        meat_isSelected = False
        onion_isSelected = False
        corn_isSelected = False

        while True:
            try:
                choice = int(
                    input("\nPlease enter the desired sauce number you want to add (if you don't want sauce type 0): "))

                if (choice < 11 and choice != 0) or choice > 16:
                    raise ValueError

                else:
                    if choice == 11:
                        if olive_isSelected:
                            choice = input(
                                "\nYou've already chosen this sauce! Please enter another sauce number you want to add "
                                "(if that's enough type 0): ")
                        else:
                            olive_isSelected = True
                            sauce_number += 1
                            sauce = Olive().get_description()
                            sauces.append(sauce)
                            sauce_cost += Olive().get_cost()

                    if choice == 12:
                        if mushroom_isSelected:
                            choice = input(
                                "\nYou've already chosen this sauce! Please enter another sauce number you want to add "
                                "(if that's enough type 0): ")

                        else:
                            olive_isSelected = True
                            sauce = Mushroom().get_description()
                            sauces.append(sauce)
                            sauce_cost += Mushroom().get_cost()
                            sauce_number += 1

                    if choice == 13:
                        if goatCheese_isSelected:
                            choice = input(
                                "\nYou've already chosen this sauce! Please enter another sauce number you want to add "
                                "(if that's enough type 0): ")
                        else:
                            olive_isSelected = True
                            sauce = GoatCheese().get_description()
                            sauces.append(sauce)
                            sauce_cost += GoatCheese().get_cost()
                            sauce_number += 1

                    if choice == 14:
                        if meat_isSelected:
                            choice = input(
                                "\nYou've already chosen this sauce! Please enter another sauce number you want to add "
                                "(if that's enough type 0): ")
                        else:
                            olive_isSelected = True
                            sauce = Meat().get_description()
                            sauces.append(sauce)
                            sauce_cost += Meat().get_cost()
                            sauce_number += 1

                    if choice == 15:
                        if onion_isSelected:
                            choice = input(
                                "\nYou've already chosen this sauce! Please enter another sauce number you want to add "
                                "(if that's enough type 0): ")
                        else:
                            olive_isSelected = True
                            sauce = Onion().get_description()
                            sauces.append(sauce)
                            sauce_cost += Onion().get_cost()
                            sauce_number += 1

                    if choice == 16:
                        if corn_isSelected:
                            choice = input(
                                "\nYou've already chosen this sauce! Please enter another sauce number you want to add "
                                "(if that's enough type 0): ")
                        else:
                            olive_isSelected = True
                            sauce = Corn().get_description()
                            sauces.append(sauce)
                            sauce_cost += Corn().get_cost()
                            sauce_number += 1

                    if choice == 0:
                        break

            except ValueError:
                print("\nPlease make a valid choice.")

        if sauce_number != 0:
            print(f"\nYou chose {sauce_number} sauce!")

        if sauce_number == 0:
            print("\nYou chose 0 sauce. Are you alien or something?")

        return sauces, sauce_cost, sauce_number


if __name__ == '__main__':
    pizzaMenu = PizzaMenu()
    pizzaMenu.print_menu()
    pizza, pizza_cost = pizzaMenu.select_pizza()
    print(f"\nSelected pizza: {pizza}, Price: {pizza_cost} $")

    sauce_menu = SauceMenu()
    sauces, sauce_cost, sauce_number = sauce_menu.select_sos()
    print(f"\nSelected sauces: {sauces}, Price: {sauce_cost} $")

    cost = sauce_cost + pizza_cost

    # Getting the data from costumer
    name = input("\nEnter your name: ")
    ID_no = input("\nEnter your ID: ")
    cc_no = input("\nEnter your credit card number: ")
    cc_cvv = input("\nEnter your CVV: ")
    description = input("\nAdd description of order if you want: ")
    time = datetime.datetime.now()

    # Setting the mm.dd.yyy format
    formatted_time = time.strftime("%m.%d.%Y")

    # Writing the data of orders to Orders.Database.csv
    with open('Orders_Database.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(["Name: " + name, "ID: " + ID_no, "Credit Card Number: " + cc_no, "CVV: " + cc_cvv, "Pizza: " + str(pizza), "Sauces: " + str(sauces), "Decription: " + description, "Price: " + cost, "Order Time: " + formatted_time])

    print(f"\nYour order has been successfully received. Total fee: {cost} $.")