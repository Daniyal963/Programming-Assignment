print("Daniyal Ali","18b-096-CS(A)")
print("Programming Excercise")
print("Question no.5")
#Code
print("\n\nTable Generation\n")

table = [[row*col for col in range(1,6)] for row in range(1,6)]
for row in range(5):
    print("\n")
    for col in range(5):
        print(table[row][col]," ",end="")
