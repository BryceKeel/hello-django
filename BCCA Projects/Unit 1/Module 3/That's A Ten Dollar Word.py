#start
phrase = input("Phrase: ").lower()
total = 0
#Math
while True:
  if 'a' in phrase:
    total += 250
  if 'e' in phrase:
    total += 250
  if 'i' in phrase:
    total += 250
  if 'o' in phrase:
    total += 250
  if 'u' in phrase:
    total += 250
  break
#final
print(f"That's a ${total} phrase.")