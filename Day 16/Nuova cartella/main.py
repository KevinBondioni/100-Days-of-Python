from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

is_on=True
while is_on:
    selected_product=input(f"What would you like? ({menu.get_items()}):\n\t").lower()
    if selected_product == "off":
        is_on=False
    elif selected_product == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order=menu.find_drink(selected_product)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
            else:
                print("Sorry, that's not enough money. Money refunded")






