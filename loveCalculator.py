

# the love calculator
print("Welcome to the Love Calculator")
name1 = input("What is your name \n")
name2 = input("What is your name \n")

name1 = name1.lower()
name2 = name2.lower()

#The part True of the Letters

print(f"T occures {name1.count('t')} time")
print(f"R occures {name1.count('r')} time")
print(f"U occures {name1.count('u')} time")
print(f"E occures {name1.count('e')} time")
print(f"L occures {name1.count('l')} time")
print(f"O occures {name1.count('o')} time")
print(f"V occures {name1.count('v')} time")
print(f"E occures {name1.count('e')} time")

totalName1 = (int((name1.count('t')) + 
                  (name1.count('r')) + 
                  (name1.count('u')) + 
                  (name1.count('e')) +
                  (name1.count('l')) + 
                  (name1.count('o')) +
                  (name1.count('v')) +
                  (name1.count('e'))))

print(f"Total : {totalName1}")
print("")

#The part Love of the Letters

print(f"T occures {name2.count('t')} time")
print(f"R occures {name2.count('r')} time")
print(f"U occures {name2.count('u')} time")
print(f"E occures {name2.count('e')} time")
print(f"L occures {name2.count('l')} time")
print(f"O occures {name2.count('o')} time")
print(f"V occures {name2.count('v')} time")
print(f"E occures {name2.count('e')} time")

totalName2 = (int((name2.count('t')) + 
                  (name2.count('r')) + 
                  (name2.count('u')) + 
                  (name2.count('e')) +
                  (name2.count('l')) + 
                  (name2.count('o')) +
                  (name2.count('v')) +
                  (name2.count('e'))))

print(f"Total : {totalName2}")
print("")

#Change int to str
trueLoveResult = (str(totalName1) + str(totalName2))


#rechange str to int
loveScore = int(trueLoveResult)

#and the last part
if 10 <= loveScore <= 100:
  print(f"Your score is {loveScore}, you got together like coke and mentos")

  if 40 <= loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together")

else:
  print(print(f"Your score is {loveScore}"))
