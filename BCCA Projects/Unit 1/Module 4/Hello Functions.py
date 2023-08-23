#hello world
def say_hello():
  return("Hello World!")
  #hey  name
def hey_you(name):
  return(f"Hello {name}!")
#age in 2050
def age_in_2050(year):
  return (2050 - year)
#can i take your order
def can_i_take_your_order(burger,fries,drink):
  burgercost = 4.50 * burger
  friescost = 1.50 * fries
  drinkscost = 1.00 * drink
  total = burgercost + friescost + drinkscost
  return(total)
  