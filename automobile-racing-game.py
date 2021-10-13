# Create a class (Automobile) 
# Add functions (go, stop) 
# Create more classes in Automobile (Motorcycle, Racecar) 
# Add functions in each class (wheelie, reverse, goto100) 
# Create instances (Motorcycle(), Racecar()) and store then in variables

class Automobile:
  def go(self):
    print('Racing forward')

  def stop(self):
    print('Stopping')

class Motorcycle(Automobile):
  def wheelie(self):
    print('Popping a wheelie')

class Racecar(Automobile):
  def reverse(self):
    print('Reversing')

  def goTo100(self):
    print('Increasing to 100 mph')

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.wheelie()
racecar = Racecar()
racecar.goTo100()
