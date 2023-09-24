count = 0 #count to get the score
a = input("1. What is the capital of France? \n")
b = input("2.What is the capital of China? \n")
c = input("3. What is the capital of India? \n")
d = input("4. What is the capital of the United States? \n")
e = input("5. What is the capital of Japan? \n") #questions with user input

answer = "correct"
answer2 = "wrong call"

if a == "Paris" : #to find out the correct answer and to add score
    count += 1
    if b == "Beijing":
        count +=1
        if c == "New Delhi" :
            count+=1
            if d == "Washington":
                count+=1
                if e == "Tokyo":
                    count+=1
else:
    print(answer2)
Total_correct = count  #total score calculation
print("SCORE",Total_correct)
if Total_correct>=3: #final report
    print("Doing Good.....keep Trying")
elif Total_correct==5:
    print("Verygood Keep it up")
else:
    print("BetterLuck Next Time")