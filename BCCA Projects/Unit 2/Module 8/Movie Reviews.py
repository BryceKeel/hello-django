from typing import List
from dataclasses import dataclass


@dataclass
class Review:
  score: int
  view: str


#  word statur
def word_status() -> None:
  word = input("Enter a word: ")
  reviews = review_list()
  print(f"{word} appears {word_count(word, reviews)} times.")
  print(
    f"The average score for reviews containing the word {word} is {averages(word, reviews)}"
  )


# phrase directive
def phrase_directive() -> None:
  reviews = review_list()
  phrase = input("Enter a phrase you want to find the average score of: ")
  score = phrase_build(phrase, reviews)
  print(f"The average score of words in that phrase is {score:.4f}")
  print(f"The overall sentiment of that phrase is {compute(score,reviews)}\n")


# file directive
def file_directive() -> None:
  reviews = review_list()
  file = input("Enter the name of a file with words you want to score: ")
  try:
    words = load_path(file)
    print(
      f"The most positive word, with a score of {most_positive(words, reviews)}\n"
    )
    print(
      f"The most negative word, with a score of {most_negative(words, reviews)}\n"
    )
  except FileNotFoundError:
    print("This file is nonexistent")


# averages
def averages(word: str, reviews: List[Review]) -> float:
  score = 0
  count = 0
  for review in reviews:
    if word in review.view:
      score += review.score
      count += 1
  try:
    average_score = score / count
  except ZeroDivisionError:
    average_score = 0.0
  return average_score


#word count
def word_count(word: str, reviews: List[Review]) -> int:
  count = 0
  for review in reviews:
    if word in review.view:
      count += 1
  return count


#review list
def review_list() -> List[Review]:
  reviews = []
  with open("scored-reviews.txt", "r") as f:
    for line in f:
      rating, text = line.split(' ', 1)
      reviews.append(Review(int(rating), text.strip()))
  return reviews


#phrase build
def phrase_build(phrase: str, reviews: List[Review]) -> float:
  words = phrase.split(' ')
  score = 0
  count = 0
  for word in words:
    score += averages(word, reviews)
    count += 1
  try:
    average_score = score / count
  except ZeroDivisionError:
    average_score = 0.0
  return average_score


#compute
def compute(score: float, reviews: List[Review]) -> str:
  sent = ""
  if score >= 0 and score < 1.99:
    sent = "Negative"
  elif score >= 1 and score < 2.01:
    sent = "Somewhat Negative"
  elif score >= 2 and score < 3:
    sent = "Neutral"
  elif score >= 3 and score < 4:
    sent = "Somewhat Positive"
  elif score == 4:
    sent = "Positive"
  else:
    sent = "Error"
  return sent


#load path
def load_path(file) -> List:
  words = []
  with open(f"{file}.txt", "r") as f:
    for line in f:
      words.append(line.strip())
  return words


#most postitive
def most_positive(words, reviews) -> str:
  scores = []
  for i in words:
    score = (averages(i, reviews))
    scores.append(score)
  for i in words:
    if averages(i, reviews) == max(scores):
      best_word = i
  return f"{max(scores)} is {best_word}"


#most negative
def most_negative(words, reviews) -> str:
  scores = []
  for i in words:
    score = (averages(i, reviews))
    scores.append(score)
  for i in words:
    if averages(i, reviews) == min(scores):
      worst_word = i
  return f"{min(scores)} is {worst_word}"


#Main
def main() -> None:
  review_list()
  while True:
    directive = input(
      "[word] stats, [phrase] stats, [file] stats, or [quit]> ").lower()
    if directive == "word":
      word_status()
    elif directive == "phrase":
      phrase_directive()
    elif directive == "file":
      file_directive()
    elif directive == "quit":
      break
    else:
      print("Invalid action")


#dunder
if __name__ == "__main__":
  main()
