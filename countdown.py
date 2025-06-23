import sys, time #sys is a built in python module that provides access to system specific parameters and function.In this context, it allows you work with time related functions.
import sevseg # Import our sevseg.py program.

secondsLeft = int(input("Enter the starting countdown time in seconds: "))

endMessage = input("Enter a message to display at the end of the countdown: ")
try: 
    while True: 
        print('\n'* 60) #clear the screen by printing several newlines
        # 3600 is the number of seconds in an hour
        hours = str(secondsLeft // 3600) # // 3600 cal the num of whole hours remaining. 
        minutes = str((secondsLeft % 3600)// 60) # %3600 calculates the remsining seconds after substracting hours. // 60 cal the num of whole min from those remaining seconds. 
        seconds= str(secondsLeft % 60) # % 60 calculate the remaining seconds after substracting hours and mins.

        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        #Display the digits:
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        if secondsLeft ==0:
            print(endMessage)
            break
            
        print()
        print('press ctrl-C to quit.')

        time.sleep(1) #Insert a one-second pause. normal time delay
        secondsLeft -= 1  #decrease the value of secondsLeft by 1, it sustracts 1 from the current value of secondsLeft and assigns the result back to secondsLeft.
except KeyboardInterrupt:
    print('Countdown')
    sys.exit() # When Ctrl-C is pressed, end the program. 

