#Exam-Timing (One-Go) (Commentless)
import time
import sys
def countdown():
    QTime = int(input("Enter the total number of marks in the paper:\n"))
    Time = QTime * 60
    start = input("To start the timer, press enter. To quit, type 'q':\n")
    if start == "":
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
This tool allows you to complete a full exam paper in one go, by
entering the number of marks in the paper.

You may enter a slightly higher time (if you feel that it is needed)\n""")

countdown()
