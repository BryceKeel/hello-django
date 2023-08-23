from typing import Dict


#input students
def input_students() -> Dict[str, bool]:
  students = {}
  print("Please provide the students names and then q to quit")
  while True:
    student = input("> ")
    if student == "q":
      if len(students) == 0:
        print("No students were provided. ")
        quit()
      else:
        break
    else:
      students[student] = False

  return students


#actions
def input_action() -> str:
  print("[check] sign ins, [sign] in, or [q]uit:")
  action = input("> ")
  if action in ["check", "sign", "quit"]:
    return action


#checkins
def print_checkins(students: Dict[str, bool]) -> None:
  for student in students:
    if students[student] == True:
      check_in = "Y"
    else:
      check_in = "N"
    print(f"{student}: {check_in}")


#signin
def sign_in(students: Dict[str, bool]) -> None:
  person = input("> ")
  if person in students:
    students[person] = True
  else:
    print("student not found")


#main
def main() -> None:
  students = input_students()

  while True:
    action = input_action()
    if action == "check":
      print_checkins(students)
    elif action == "sign":
      sign_in(students)
    elif action == "quit":
      break
    else:
      print("Please choose a valid action.")


#dunder
if __name__ == "__main__":
  main()
