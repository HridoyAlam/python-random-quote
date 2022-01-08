def primary():
  #print("Keep it logically awesome.")

  f = open("C:/Users/hrido\Desktop/git/python-random-quote/quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])
  #print(quotes)
  

if __name__== "__main__":
  primary()
