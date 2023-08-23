def vowels_in_phrase(vowels):
  vowels += 1
  return vowels

def main():
  phrase = input("Phrase: ").lower()
  vowels = 0
  a = 0
  e = 0
  i = 0
  o = 0
  u = 0

  if "a" in phrase:
    a = vowels_in_phrase(vowels)
  if "e" in phrase:
    e = vowels_in_phrase(vowels)
  if "i" in phrase:
    i = vowels_in_phrase(vowels)
  if "o" in phrase:
    o = vowels_in_phrase(vowels)
  if "u" in phrase:
    u = vowels_in_phrase(vowels)

  vowels = a + e + i + o + u
  total = vowels * 250
  print(f"That's a ${total} phrase")

if __name__ == "__main__":
  main()