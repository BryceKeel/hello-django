from dataclasses import dataclass


@dataclass
#defining the class
class UserPreference:
  shape: str
  input_unit: str
  output_unit: str
  input_amount: int
  output_amount: int


up = UserPreference("", "", "", 0, 0)


def inch_conversion(input_amount, output_unit):
  if up.output_unit == 'Yard':
    return round(up.input_amount / 36, 2)
  elif up.output_unit == "Centimeter":
    return round(up.input_amount * 2.54, 2)
  elif up.output_unit == "Feet":
    return round(up.input_amount / 12, 2)
  elif up.output_unit == "Meter":
    return round(up.input_amount / 39.3700787, 2)


def yard_conversion(input_amount, output_unit):
  if up.output_unit == 'Inch':
    return up.input_amount * 36



  
  elif up.output_unit == 'Feet':
    return up.input_amount * 3
  elif up.output_unit == 'Centimeter':
    return round(up.input_amount * 91.44, 2)
  elif up.output_unit == 'Meter':
    return round(up.input_amount * 1.0936133, 2)


def centimeter_conversion(input_amount, output_unit):
  if up.output_unit == 'Inch':
    return round(up.input_amount / 2.54, 2)
  elif up.output_unit == 'Feet':
    return round(up.input_amount / 30.48, 2)
  elif up.output_unit == 'Yard':
    return round(up.input_amount / 91.44, 2)
  elif up.output_unit == 'Meter':
    return round(up.input_amount / 100, 2)


def feet_conversion(input_amount, output_unit):
  if up.output_unit == 'Inch':
    return up.input_amount * 12
  elif up.output_unit == 'Centimeter':
    return up.input_amount * 30.48
  elif up.output_unit == 'Yard':
    return round(up.input_amount / 3, 2)
  elif up.output_unit == 'Meter':
    return round(up.input_amount / 3.2808399, 2)


def meter_conversion(input_amount, output_unit):
  if up.output_unit == 'Inch':
    return round(up.input_amount * 39.37007870, 2)
  elif up.output_unit == 'Centimeter':
    return up.input_amount * 100
  elif up.output_unit == 'Yard':
    return round(up.input_amount * 1.0936133, 2)
  elif up.output_unit == 'Feet':
    return round(up.input_amount * 3.2808399, 2)


def two_dimensional(shape):
  if up.shape == 'Rectangle':
    rec_length = float(input("What is the length? "))
    rec_width = float(input("What is the width? "))
    rec_area = rec_length * rec_width
    return round(rec_area, 2)
  elif up.shape == 'Triangle':
    tri_base = float(input("What is the length of the base? "))
    tri_height = float(input("What is the height? "))
    tri_total = tri_base * tri_height
    tri_area = round(tri_total / 2, 2)
    return tri_area
  elif up.shape == 'Square':
    square_side = float(input("What is the length of a side? "))
    square_area = round(square_side**2, 2)
    return square_area
  elif up.shape == 'Circle':
    circle_radius = float(input("What is the radius? "))
    pi = 3.14
    circle_area = circle_radius * pi
    return round(circle_area, 2)
  elif up.shape == "Trapezoid":
    base_one = float(input("What is the length of the first base? "))
    base_two = float(input("What is the length of the second base? "))
    trap_height = int(input("What is the height? "))
    combined_bases = base_one + base_two
    trap_total = combined_bases / 2
    trap_area = trap_total * trap_height
    return round(trap_area, 2)


def three_dimensional(shape):
  if up.shape == "Pyramid":
    pyra_length = float(input("What is the length of the base? "))
    pyra_width = float(input("What is the width of the base? "))
    pyra_height = float(input("What is the height of the pryamid? "))
    pyra_total = pyra_length * pyra_width * pyra_height
    pyra_area = pyra_total / 3
    return round(pyra_area, 2)
  elif up.shape == "Rectangular Prism":
    recp_length = float(input("What is the length? "))
    recp_width = float(input("What is the width? "))
    recp_height = float(input("What is the height? "))
    recp_area = recp_height * recp_length * recp_width
    return round(recp_area, 2)
  elif up.shape == "Sphere":
    sphere_radius = float(input("What is the radius? "))
    pi = 3.14
    radius_total = sphere_radius**3
    sphere_area = pi * radius_total * 4 / 3
    return round(sphere_area, 2)
  elif up.shape == "Trapezoidal Prism":
    trap_prism_base_one = float(
      input("What is the length of the first base? "))
    trap_prism_base_two = float(
      input("What is the length of the second base? "))
    trap_prism_base_total = trap_prism_base_one + trap_prism_base_two
    trap_prism_height = float(input("What is the measure of the height? "))
    trap_prism_length = float(input("What is the length of the prism? "))
    trap_prism_total = trap_prism_height * trap_prism_length * trap_prism_base_total
    trap_prism_area = trap_prism_total / 2
    return round(trap_prism_area, 2)
  elif up.shape  == "Cube":
    cube_length = float(input("What is the length of a side? "))
    cube_volume = cube_length ** 3
    return cube_volume




def main():
  need_area_or_conversion = input("Do you need to [convert] units or find the [area] / [volume] of a shape? ")
  if need_area_or_conversion == "convert":
    up.input_unit = input("\n\n\nWhat is your initial unit?\n Available options include:\n- Inch\n- Yard\n- Centimeter\n- Feet\n- Meter\n> ").title()
    up.input_amount = int(input("What is the value of the length? ").title())
    up.output_unit = input("What unit are you converting to? ").title()
    if up.input_unit == "Inch":
      print(inch_conversion(up.input_amount, up.output_unit))
    elif up.input_unit == 'Yard':
      print(yard_conversion(up.input_amount, up.output_unit))
    elif up.input_unit == "Centimeter":
      print(centimeter_conversion(up.input_amount, up.output_unit))
    elif up.input_unit == "Feet":
      print(feet_conversion(up.input_amount, up.output_unit))
    elif up.input_unit == "Meter":
      print(meter_conversion(up.input_amount, up.output_unit))

  elif need_area_or_conversion == "area" or need_area_or_conversion == "volume":
    up.shape = up.shape = input("What is the desired shape?\n Available options include:\n- Pyramid\n- Triangle\n- Rectangle\n- Rectangular Prism\n- Sphere\n- Circle\n- Trapezoid\n- Trapezodial Prism\n- Square\n- Cube\n> ").title()
    if up.shape == "Triangle":
      print(two_dimensional("Triangle"))
    elif up.shape == "Pyramid":
      print(three_dimensional("Pyramid"))
    elif up.shape == "Rectanlge":
      print(two_dimensional("Rectangle"))
    elif up.shape == "Rectangular Prism":
      print(three_dimensional("Rectangular Prism"))
    elif up.shape == "Sphere":
      print(three_dimensional("Sphere"))
    elif up.shape == "Cirlce":
      print(two_dimensional("Circle"))
    elif up.shape == "Trapezoid":
      print(two_dimensional("Trapezoid"))
    elif up.shape == "Trapezoidal Prism":
      print(three_dimensional("Trapezoidal Prism"))
    elif up.shape == "Square":
      print(two_dimensional("Square"))
    elif up.shape == "Cube":
      print(three_dimensional("Cube"))

if __name__ == '__main__':
  main()
