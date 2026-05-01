import time
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
#Welcome
print("Welcome to the Quiz")
user=input("Enter your name: ")
clear()
print("Hello, ",user)

#Start
consent=input("Do you want to start the game? Y?N\n").upper()
if consent != 'Y':
    quit()
print("Okay, Let's Play!")
print("Loading...")
time.sleep(1)


#Presenting Questions 
with open("question_bank.txt","r") as q:
    score=0

    for i in range(1,11):
        #heading
        clear()
        print("\t\tQuiz Game\t\tScore: ",score)
        print("\nQuestion Number ",i)
        question=""

        #Print Question and Options & take a response
        for i in range(1,3):
            question+=q.readline()
        response=input(f"{question}Your Answer: ").upper()

        #result
        answer=q.readline().strip()
        if response == answer:
           score+=1
           print("Correct Answer! Now your score is: ",score)
        else:
           print("Incorrect Answer! Your score remains at: ",score)
        print("\n Please wait while the next question is being loaded!")

        time.sleep(2)
clear()

#end
print("\t\t\tGame Over")
print("\t\t    Your Score : ",score)
again=input("\n\nDo you want to play again?Y/N\n").strip().upper()
if again == "Y":
    print("Loading again, Please wait....")
else:
    print("Quitting....")
time.sleep(2)
