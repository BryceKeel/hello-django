print("""How's My Grade Looking?

Class: BCCA

Assignments:

| Assignment                  | Weight |
|-----------------------------| ------ |
| I1 - Hello World!           | 10%    |
| I2 - Say My Name!           | 10%    |
| I3 - Age Is A Number        | 10%    |
| I4 - Can I Take Your Order? | 10%    |
| P1 - Squishing Bugs         | 15%    |
| P2 - How's My Grade Looking?| 15%    |
| B1 - Unit 1 Benchmark       | 30%    |
""")

grade_so_far = 0
points_availible_so_far = 0

i1 = int(input("What grade did you get in I1 - Hello World! [0-100]: "))
grade_so_far += i1 / 100 * 10
points_availible_so_far += 10
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_availible_so_far + grade_so_far}")

i2 = int(input("What grade did you get in I2 - Say My Name! [0-100]: "))
grade_so_far += i2 / 100 * 10
points_availible_so_far += 10
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_availible_so_far + grade_so_far}")

i3 = int(input("What grade did you get in I3 - Age Is A Number [0-100]: "))
grade_so_far += i3 / 100 * 10
points_availible_so_far += 10
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_availible_so_far + grade_so_far}")

i4 = int(input("What grade did you get in I4 - Can I Take Your Order? [0-100]: "))
grade_so_far += i4 / 100 * 10
points_availible_so_far += 10
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_availible_so_far + grade_so_far}")

p1 = int(input("What grade did you get on P1 - Squishing Bugs [0-100]: "))
grade_so_far += p1 / 100 * 15
points_availible_so_far += 15
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_availible_so_far + grade_so_far}")

p2 = int(input("What grade did you get on P2 - How's My Grade Looking? [0-100]: "))
grade_so_far += p2 / 100 * 15
points_availible_so_far += 15
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_availible_so_far + grade_so_far}")

b1 = int(input("What grade did you get on B1 - Unit 1 Benchmark [0-100]: "))
grade_so_far += b1 / 100 * 30
points_availible_so_far += 30
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {100 - points_availible_so_far + grade_so_far}")