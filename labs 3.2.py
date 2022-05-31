##secret_number = 777
##
##print(
##"""
##+================================+
##| Welcome to my game, muggle!    |
##| Enter an integer number        |
##| and guess what number I've     |
##| picked for you.                |
##| So, what is the secret number? |
##+================================+
##""")
##
##var = int(input("Enter a number: "))
##
##while var != secret_number:
##    print("Ha ha! You're stuck on my loop!")
##    var = int(input("Enter a number: "))
##
##print("Well done, muggle! You are free now.")    

#=============================================
##import time
##
##for i in range(5):
##    print(i+1,"Mississippi")
##    time.sleep(1)
##print("Ready or not, here I come!")

#=============================================
##var = str(input("Enter a word: "))

##while var != "chupacabra":
##    print("That is not the correct word, you are stuck in the loop")
##    var = input("Enter a word: ")
##    if var == "chupacabra":
##        print("you have succesfully left the loop")
##        break

#=============================================
##user_word = input("Insert a word: ")
##user_word = user_word.upper()

##for letter in user_word:
##    if letter == "A":
##        continue
##    elif letter == "E":
##        continue
##    elif letter =="I":
##        continue
##    elif letter =="O":
##        continue
##    elif letter =="U":
##        continue
##print(letter)

#=============================================
##user_word = input("Insert a word: ")
##user_word = user_word.upper()

##wordWithoutVowels = ""

##for letter in user_word:
##    if letter == "A":
##        continue
##    elif letter == "E":
##        continue
##    elif letter =="I":
##        continue
##    elif letter =="O":
##        continue
##    elif letter =="U":
##        continue
##    else:
##        wordWithoutVowels = wordWithoutVowels + letter
##        
##print(wordWithoutVowels)

#=============================================
##blocks = int(input("Enter the number of blocks: "))
##
##height = 0
##while blocks > height:
##    height += 1
##    blocks -= height
##
##print("The height of the pyramid:", height)

#=============================================
##n =  int(input("Enter a positive number"))
##
##steps = 0
##
##
##while n!= 1:
##    if n % 2 == 0:
##        n = n / 2
##    elif n % 2 == 1:
##        n = (n * 3) + 1
##    steps += 1
##    print(int(n))
##
##print("steps: ",steps)

#=============================================
###ex1
##for i in range(0, 11):
##    if i % 2 != 0:
##        print(i)
###ex2
##x = 1
##while x < 11:
##    if x % 2 != 0:
##        print(x)
##    x += 1
##
###ex3
##for ch in "john.smith@pythoninstitute.org":
##    if ch == "@":
##        break
##    print(ch, end="")
    
#ex4
##for digit in "0165031806510":
##    if digit == "0":
##        print("x", end="")
##        continue
##    print(digit, end="")    
