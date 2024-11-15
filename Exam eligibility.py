n=int(input("Enter number of school days"))
a=int(input("Enter amount of days attended"))
for i in range(1, n+1):
    p=(a/n)*100

    if p>= 75:
        print("Can do the exam")
    else:
        print("Can't do the exam")