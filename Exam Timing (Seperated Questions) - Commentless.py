#Exam Timing (Seperate Questions) (Commentless)
import time
import sys
def countdown(QAmount):
    while QAmount > 0:
        for i in range(0, QAmount):
            QAmount = QAmount - 1
            QTime = int(input("Enter the number of marks for question {}/ The amount of time you need for question {} (at least 1 min)\n".format(i+1, i+1)))
            Time = QTime * 60
            start = input("To start the timer, press enter. To quit, type 'q':\n")
            if start == "":
                if Time == 60:
                    print(QTime, "min")
                else:    
                    print(QTime, "mins")
                while Time > 0:
                    mins, secs = divmod(Time, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(timer, end="\r \n")
                    time.sleep(1)
                    Time -= 1
            elif start == "q" or start == "Q" or start != "":
                    print("Goodbye :)")
                    sys.exit()

    print("\nYOU HAVE REACHED THE END OF THE PAPER\n")

print("""'Question Countdown'
This tool allows you to enter the number of exam questions in a paper,
and the amount of marks needed for each question (1 min per mark).

You may require more time to complete a question than that stated by the
number of marks, which is why this program allows you to enter the amount
of time you believe is needed.

This timer can only be used for completing one question at a time. Complete
one question, then after the time for one question has reached 0:00,
mark the question, write down the total score for that question, then,
write down the time needed to complete the next question.

Repeat this process until you've reached the end of the paper.

EACH QUESTION MUST BE AT LEAST 1 MIN LONG

BEGIN\n""")

QAmount = int(input("Enter the number of questions in the exam:\n"))
while QAmount > 0:
    countdown(int(QAmount))
