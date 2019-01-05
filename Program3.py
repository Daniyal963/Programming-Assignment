print("Daniyal Ali","18b-096-CS(A)")
print("Programming Excercise")
print("Question no.3")
#Code
print("Programming excercise Question - 03")
word_1 = str(input("Please enter your string"))
word_1 = word_1.casefold()
rev_1 = reversed(word_1)
if list(word_1) == list(rev_1):
    print("Yes, your string is a palidrome")
else:
    print("Sorry your string is not a palindrome")
