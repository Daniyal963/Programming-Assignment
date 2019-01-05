print("Daniyal Ali","18b-096-CS(A)")
print("Programming Excercise")
print("Question no.2")
#Code
a = int(input("Please enter your 1st term :"))
d = int(input("Please enter the common difference :"))
n = int(input("Please enter the desired nth term :"))
seq = a+(n-1)*d
print("the"+" "+str(n)+"the term is :", seq)
cont  = input(("Continue? = ",))
while cont == "yes":
    n = int(input("\nenter another desired nth term :"))
    seq = a+(n-1)*d
    print("the"+" "+str(n)+"th term is :", seq)
    cont = input("continue? =",)
    if cont == "no":
        break
