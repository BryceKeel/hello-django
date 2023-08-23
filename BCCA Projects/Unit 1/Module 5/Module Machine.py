#Imports
from dataclasses import dataclass


#Module Progress Class
@dataclass
class ModuleProgress:
  current_state: str


#Complete Task function
def complete_task(m: ModuleProgress) -> None:
  if m.current_state == "Introductory Exercises":
    m.current_state = "Project"
  elif m.current_state == "Project":
    m.current_state = "Benchmark"
  else:
      print("Invalid transition.")

#Pass task function
def pass_task(m: ModuleProgress) -> None:
  if m.current_state == "Benchmark":
    m.current_state = "Module Complete"
  else:
      print("Invalid transition.")

#Fail task function
def fail_task(m: ModuleProgress) -> None:
  if m.current_state == "Benchmark":
    m.current_state = "Project"
  else:
      print("Invalid transition.")

#Input helper
def is_valid_input(progress):
  if progress == "Complete" or progress == "Pass" or progress == "Fail" or progress == "q":
    return True
  else:
    return False


#Our code
def main():
  module1 = ModuleProgress("Introductory Exercises")
  failures = 0
  while True:
    print(f"Current State: {module1.current_state}")
    progress = input("> ")
    if is_valid_input(progress):
      if progress == "Complete":
        complete_task(module1)
      elif progress == "Pass":
        pass_task(module1)
        if module1.current_state == "Module Complete":
          print(f"Current State: {module1.current_state}")
          break
      elif progress == "Fail":
        fail_task(module1)
        failures += 1
        if failures >= 3:
          print("You must be removed from Base Camp Coding Academy.")
          break
      elif progress == "q":
        print("You quit Base Camp Coding Academy.")
        break
    else:
      print("Invalid transition.")


#Run our code
if __name__ == "__main__":
  main()