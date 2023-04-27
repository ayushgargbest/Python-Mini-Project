import random
n=random.randint(1,50)
name=input("Enter your name:")
marks=0
count=0
i=0
print("On every correct answer you will get 10 marks\nOn every wrong answer your marks will be reduced by 1\nYou have 10 attempts.... Good Luck!")
while(i<10):
    l=0
    print(f"Guess your {i+1} attempt")
    l=int(input())
    if l==n:
        marks+=10
        count+=1
        print(f"Congrats {name} You won!! \nYour marks={marks}")
        break
    elif l<n:
        print("Too small")
        marks-=1
    elif l>n:
        print("Too large")
        marks-=1
    i+=1    
if count==0:
    print(f"Sorry {name} you have lost")
