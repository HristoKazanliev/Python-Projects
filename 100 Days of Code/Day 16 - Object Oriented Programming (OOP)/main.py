from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_working = True

while is_working:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_working = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        efficient = coffee_maker.is_resource_sufficient(drink)
        if efficient:
            can_pay = money_machine.make_payment(drink.cost)
            if can_pay:
                coffee_maker.make_coffee(drink)

