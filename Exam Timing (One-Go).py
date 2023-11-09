#Exam Timing (One Go)
#Q = Question
import time
import sys
#Subroutine to time exam questions
def countdown(QAmount):
    #This procedure runs the function of displaying a countdown
    for i in range(0, QAmount):
        QAmount = QAmount - 1
        QTime = int(input("Enter the total number of marks in the paper/How much time you need for all questions:\n"))
        Time = QTime * 60
        #Converts the time into seconds

        start = input("To start the timer, press enter. To quit, type 'q':\n")
        #Allows the user to be prepared before the timer for each question begins
        
        if start == "":
            print(QTime, "mins")
            while Time > 0:
                #Loops until the Time (in seconds) hits zero
                mins, secs = divmod(Time, 60)
                #divmod returns a quotient and a remainder (when the two inputs are integers)
                #quotient = The result of dividing two numbers
                
                timer = '{:02d}:{:02d}'.format(mins, secs)
                #'{;02d}', '02' displays a number in a two-digit form "00"
                #The letter 'd' displays a number in decimal form
                
                print(timer, end="\r \n")
                #The letter \r shifts your mouse cursor back to the beginning of a string/line
                #In this case, the cursor shifts to a new line
                
                time.sleep(1)
                #Waits one second before starting the countdown
                
                Time -= 1
                #The code under this while loop displays the countdown to the user

        elif start == "q" or start == "Q" or start != "":
            print("Goodbye :)")
            sys.exit()
            #Stops running the program
                   
    print("\nYOU HAVE REACHED THE END OF THE PAPER\n")

    print("Next Paper?...\n")

# Main Program
# Allows the user to input the total number of marks in the paper

print("""'Question Countdown'
PLEASE READ!
This tool allows you to complete a full exam paper in one go, by
entering the number of marks in the paper.

You may enter a slightly higher time (if you feel that it is needed)\n""")

QAmount = int(input("Enter the number of questions in the exam:\n"))
# Function call
while QAmount > 0:
    countdown(int(QAmount))
