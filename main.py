from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

''' to do
Menu
off
report 
order drink
'''

#objects
coffee_mach = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

#variables
list = (menu.get_items()).split("/")
is_on = True

while is_on == True:

  choice = (input(f"\nwhat would you like? {menu.get_items()}\n")).lower()
  
  if choice == "off":
      is_on = False
  elif choice == "report":
    print ("\n")
    coffee_mach.report()
    money.report()
    print ("\n")
  elif choice in list:
    drink = menu.find_drink(choice)
    
    if coffee_mach.is_resource_sufficient(drink) is True: 
      print ("\n")
      print (f"That will cost: ${drink.cost}")
      print ("\n")
      if money.make_payment(drink.cost) == True:
        print ("\n")
        coffee_mach.make_coffee(drink)
        print ("\n")
  else:
    print ("\n")
    print ("That't not a valid choice \n")









