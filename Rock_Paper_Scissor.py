import random
comp=0
user=0
for i in range(1,4):
    arr=["rock","paper","scissor"]
    a=random.randint(0,2)
    c_choice=arr[a]
    #print(c_choice)

    u_choice=input("Enter choice:").lower()
    if u_choice not in arr:
        print("invalid choice")
    else:
        if c_choice=="rock" and u_choice=="scissor":
            print("computer won")
            comp+=1
        elif u_choice=="rock" and c_choice=="paper":
            print("computer won")
            comp+=1
        elif u_choice=="paper" and c_choice=="scissor":
            print("computer won")
            comp+=1
        elif c_choice==u_choice:
            print("DRAW MATCH")
        else:
            print("user won")
            user+=1
        print(f"comp:{comp},user:{user}")
if user>comp:
    print("user won")
elif comp>user:
    print("computer won")
else:
    print("draw")
        
