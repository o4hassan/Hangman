import random
WORDLIST =open('wordlist.txt','r').readlines()

#this function is being made to store all of the words in wordlist.txt into a list called words... from that list in words we will choose a word at random using random choice
def picked(min_word_length): #the input is the minimum length the word can be
    picked.one=[]
    for word in WORDLIST:
        if '(' or ')' not in word:
            word = word.strip().lower()
        if len(word) >= min_word_length:
            picked.one.append(word)
    picked.one = random.choice(picked.one)

























"""the try and except method kinda works like this:
   try:
       number = int(input()) #so try to make the input an integer, if you can
       if 1<= number <= 25 #if it is an integer check to see if its between 1 and 25 and if it is do...
       
   except:
       print("dsdf") #if it doesn't work then run the except thing."""
       
   
