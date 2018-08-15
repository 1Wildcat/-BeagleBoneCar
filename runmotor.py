import rcpy.motor as motor
from rcpy.motor import motor2
from rcpy.motor import motor3
import curses, time

def input_char(message):
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        while True:
            ch = win.getch()
            if ch in range(32, 127): break
            time.sleep(0.05)
    except: raise
    finally:
        curses.endwin()
    return chr(ch)

def forward(duty):
    motor2.set(duty)
    motor3.set(-duty)
def stop():
    motor2.set(0)
    motor3.set(0)
def reverse(duty):
    motor2.set(-duty)
    motor3.set(duty)
def right(duty):
    motor2.set(duty)
    motor3.set(duty)
def left(duty):
    motor2.set(-duty)
    motor3.set(-duty)
def trn_left(duty):
    motor2.set(duty)
    motor3.set(-duty+0.1)
def trn_right(duty):
    motor2.set(duty+0.1)
    motor3.set(-duty)


#def reverse():
duty = list(range(1,11))
duty_index = 0
speed = duty[duty_index]/10
while(1):

    input1 = input_char('w = forward\n s = reverse\n a = left\n d = right\n i = inc speed\n k = dec speed\n other keys = stop\n')
    if(input1 == 'w'):
        forward(speed)
    elif(input1 == 's'):
        reverse(speed)
    elif(input1 == 'q'):
        left(speed)
    elif(input1 == 'e'):
        right(speed)
    elif(input1 == 'a'):
        trn_left(speed)
    elif(input1 == 'd'):
        trn_right(speed)

    elif(input1 == 'i'):
        if(duty_index < 9):
            duty_index = duty_index + 1
            speed = (duty[duty_index])/10 
    elif(input1 == 'k'):
        if(duty_index > 0):
            duty_index = duty_index - 1
            speed = (duty[duty_index])/10
    else:
        stop()
