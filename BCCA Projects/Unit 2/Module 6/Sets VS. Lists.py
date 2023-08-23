from typing import List,Set
import time
# Uncomment the appropriate line to run your program against the desired file.
# VOTES_FILE = "votes.txt"
# VOTES_FILE = "unique-votes-10k.txt"
VOTES_FILE = "unique-votes-25k.txt"

def load_votes() -> List[str]:
    votes = []
    with open(VOTES_FILE) as votes_file:
        for line in votes_file:
            votes.append(line)
    return votes


def number_of_candidates(votes: List[str]) -> int:
    # Change this function to maintain the candidates as a set instead of a list.
    candidates = set()
    for vote in votes:
        if vote not in candidates:
            candidates.add(vote)
    return len(candidates)

def main() -> None:
  start = time.time()
  votes = load_votes()
  print(number_of_candidates(votes))
  end = time.time()
  print(end - start)

if __name__ == "__main__":
    main()