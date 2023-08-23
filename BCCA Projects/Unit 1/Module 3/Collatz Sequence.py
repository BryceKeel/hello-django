#user input
number = int(input("number: "))
print(number)
#math
while number != 1:
  if number%2 == 0:
    number = number // 2
    print(int(number))
  elif number%2 == 1:
    number = number * 3 + 1
    print(int(number))