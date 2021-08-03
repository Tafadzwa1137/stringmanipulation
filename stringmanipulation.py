# Ask the user how many words they would like to write in
userWords = int(input("How many words would you like to use? "))

words = []
for i in range (userWords):
    newWord = str(input("Please type in a word: "))
    words.append(newWord)

print(words)

def spacedWords():
    for i in words:
        print(i, end=" ")
        
        
def reverseWords():
    reverse = ' '.join(reversed(words))
    print(reverse)
  
def upperRemove():
  new = []
  for i in words:
    upper = i.upper()
    new.append(upper)
    for i in new:
        print(i, end="")
    
def vowels():
  new = []
    for i in words:
        if i != "e" or "i" or "a" or "o" or "u":
            words.pop(i)
        else:
          new = 


spacedWords()
reverseWords()
upperRemove()
