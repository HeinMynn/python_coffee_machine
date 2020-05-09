class CoffeeMachine:
  def __init__(self):
    self.have_water = 400
    self.have_milk = 540
    self.have_coffee_beans = 120
    self.have_cups = 9
    self.have_money = 550
    self.main_action()

  def fill_coffee(self):
    self.have_water += int(input("Write how many ml of water do you want to add:"))
    self.have_milk += int(input("Write how many ml of milk do you want to add:"))
    self.have_coffee_beans += int(input("Write how many grams of coffee beans do you want to add:"))
    self.have_cups += int(input("Write how many disposable cups of coffee do you want to add:"))
    self.main_action()

  def buy_coffee(self):
    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    if coffee_type == 'back':
      self.main_action()
    else:
      coffee_type = int(coffee_type)

    if coffee_type == 1:
      if self.have_water >= 250 and self.have_coffee_beans > 16 and self.have_cups > 0:
        self.have_water = self.have_water - 250
        self.have_coffee_beans = self.have_coffee_beans - 16
        self.have_cups = self.have_cups - 1
        self.have_money = self.have_money + 4
        print("I have enough resources, making you a coffee!")
        self.main_action()
      else:
        print("Sorry, not enough resources")
        self.main_action()

    elif coffee_type == 2:
      if self.have_water >= 350 and self.have_milk >= 75 and self.have_coffee_beans > 20 and self.have_cups > 0:
        self.have_water = self.have_water - 350
        self.have_milk = self.have_milk - 75
        self.have_coffee_beans = self.have_coffee_beans - 20
        self.have_cups = self.have_cups - 1
        self.have_money = self.have_money + 7
        print("I have enough resources, making you a coffee!")
        self.main_action()
      else:
        print("Sorry, not enough resources")
        self.main_action()
    elif coffee_type == 3:
      if self.have_water >= 200 and self.have_milk >= 100 and self.have_coffee_beans > 12 and self.have_cups > 0:
        self.have_water = self.have_water - 200
        self.have_milk = self.have_milk - 100
        self.have_coffee_beans = self.have_coffee_beans - 12
        self.have_cups = self.have_cups - 1
        self.have_money = self.have_money + 6
        print("I have enough resources, making you a coffee!")
        self.main_action()
      else:
        print("Sorry, not enough resources")
        self.main_action()

  def remaining(self):
    print("The coffee machine has:")
    print(self.have_water, "of water")
    print(self.have_milk, "of milk")
    print(self.have_coffee_beans, "of coffee beans")
    print(self.have_cups, "of disposable cups")
    print(self.have_money, "of money")
    self.main_action()

  def main_action(self):
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == 'exit':
        return
    else:
        self.do_action(action)
    
    
  def do_action(self, action):
    if action == 'buy':
        self.buy_coffee()
    elif action == 'fill':
        self.fill_coffee()
    elif action == 'take':
        print("I gave you", self.have_money)
        self.have_money = 0
        self.main_action()
    elif action == 'remaining':
        self.remaining()
    else:
        print("I don't understand! Choose again.")
        self.main_action()

my_coffee = CoffeeMachine()
