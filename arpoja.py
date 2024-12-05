import random

giver = ["Hanna", "Eero", "Annu", "Pepe", "Reijo", "Sylvi"]
receiver = ["Hanna", "Eero", "Annu", "Pepe", "Reijo", "Sylvi"]

def arpoja(giver, receiver):
    while True:
      random.shuffle(receiver)
      if not any(giver[i] == receiver[i] for i in range(len(giver))):
          break
    for i in range(len(giver)):
        print(giver[i], "ostaa lahjan henkilölle", receiver[i])

if __name__ == "__main__":
    arpoja(giver, receiver)
