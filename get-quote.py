import random
def primary():
  #print("Keep it logically awesome.")

  f = open("C:/Users/hrido\Desktop/git/python-random-quote/quotes.txt")
  quotes = f.readlines()
  f.close()

  last  = len(quotes) - 1
  rnd = random.randint(0, last)
  #print(rnd)
  print(quotes[rnd], quotes[random.randint(0, last)])
  
  #print(quotes)
  

if __name__== "__main__":
  primary()
