from typing import Tuple, List, Optional
#distance
def distance(interval: Tuple[int, int]) -> int:
  return abs(interval[0] - interval[1])
#rise
def rise(pos1: Tuple[float, float], pos2: Tuple[float, float]) -> float:
  return pos2[1] - pos1[1]
#run
def run(pos1: Tuple[float, float], pos2: Tuple[float, float]) -> float:
  return pos2[0]-pos1[0]
#max and min
def max_and_min(nums: List[int]) -> Optional[Tuple[int,int]]:
  if not nums:
    return None
  else:
    return max(nums), min(nums)
#find greater
def find_greater(nums: List[float], threshold: float) -> Optional[Tuple[int, float]]:
  if not nums:
    return None
  for i, num in enumerate(nums):
    if num > threshold:
      return i, num
  return None

#main
def main():
  ...
if __name__=='__main__':
  main()