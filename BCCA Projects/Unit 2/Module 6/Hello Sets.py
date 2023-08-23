#average
def average(array) -> None:
  total = len(set(array))
  hite = sum(set(array))
  print(hite / int(total))

        
  
# Do not touch code below
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)