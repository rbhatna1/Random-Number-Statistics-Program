import random,statistics

def space(): #To make it look good and have proper demarcations
    print()
    print("**********************************************************")
    print()

def generate():
    global tuple1
    n=int(input("Enter the number of random terms to be generated"))
    tuple1=()
    for a in range(n):
        b=random.randrange(1,10000)
        tuple1=tuple1+(b,)
    print(tuple1)
    space()
    
def show(n):
    space()
    print("The numbers are:")
    for a in n:
        print(a,end=" ")
    space()

def stat(n):
    space()
    print("The mean of the following list is:",statistics.mean(n))
    print("The median of the following list is:",statistics.median(n))
    n=list(n)
    b=n.sort()
    b=tuple(n)
    print("The sorted list is:",b)
    space()
    
choice=0

while choice!=4:
    print("Choose from one of the following options")
    print("1)to generate n numbers of random numbers")
    print("2)To show the numbers of the list")
    print("3)To show the mean,median and the sorted tuple")
    print("4)Enter the 4th choice to exit the loop")
    choice=int(input("Enter the choice"))
    
    if choice==1:
        generate()
        
    elif choice==2:
        n=eval(input("Enter the list"))
        show(n)
        
    elif choice==3:
        n=eval(input("Enter the tuple"))
        stat(n)