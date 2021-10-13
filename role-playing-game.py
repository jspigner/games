# Create a class (Player) 
# Add parameters (self, name) 
# Create more classes and use Player as the parent class (Computer, User)
# Define some functions (respond, greet) 

class Player:
  def __init__(self, name):
    self.name = name

class Computer(Player):
  def __init__(self):
    super().__init__("NPC")

  def respond(self, player):
    print("Hello", player.name, "I am", self.name)

class User(Player):
  def __init__(self, name, level):
    super().__init__(name)
    self.level = level

  def greet(self):
    print("Hi! What is your name?")

computer = Computer()
user = User("User", 1)
user.greet()
computer.respond(user)
