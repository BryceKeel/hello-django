#takes name
def main():
    name = input("Name: ")
  #prints in dry erase board
    with open("dry-erase-board.txt","w") as namefile:
      namefile.write(name + " wuz here")
      namefile.close()
if __name__ == "__main__":
  main()
