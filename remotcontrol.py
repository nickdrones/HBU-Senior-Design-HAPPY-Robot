from tkinter import *
from socket import *      # Import necessary modules

top = Tk()   # Create a top window
top.title('Drive Control')

HOST = '172.17.75.175'    # Server IP address
PORT = 21567
BUFSIZ = 255             # buffer size
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # Create a socket
tcpCliSock.connect(ADDR) # Connect with the server

# =============================================================================
# The function is to send the command forward to the server, so as to make the 
# car move forward.
# ============================================================================= 
def forward_fun(event):
    print('forward')
    tcpCliSock.send(bytes("f", 'utf8'))

def backward_fun(event):
    print('backward')
    tcpCliSock.send(b"b")

def left_fun(event):
    print('left')
    tcpCliSock.send(b"l")

def right_fun(event):
    print('right')
    tcpCliSock.send(b"r")

def stop_fun(event):
    print('stop')
    tcpCliSock.send(b"s")

def i_said_stop(event):
        print('STOP!!!')
        tcpCliSock.send('stop')
        
Btn0 = Button(top, width=5, text='Forward')
Btn1 = Button(top, width=5, text='Backward')
Btn2 = Button(top, width=5, text='Left')
Btn3 = Button(top, width=5, text='Right')
Btn4 = Button(top, width=5, text='STOP')

Btn0.grid(row=0,column=1)
Btn1.grid(row=2,column=1)
Btn2.grid(row=1,column=0)
Btn3.grid(row=1,column=2)
Btn4.grid(row=1,column=1)

Btn0.bind('<ButtonPress-1>', forward_fun)  # When button0 is pressed down, call the function forward_fun().
Btn1.bind('<ButtonPress-1>', backward_fun)
Btn2.bind('<ButtonPress-1>', left_fun)
Btn3.bind('<ButtonPress-1>', right_fun)
Btn4.bind('<ButtonPress-1>', i_said_stop)

Btn0.bind('<ButtonRelease-1>', stop_fun)   # When button0 is released, call the function stop_fun().
Btn1.bind('<ButtonRelease-1>', stop_fun)
Btn2.bind('<ButtonRelease-1>', stop_fun)
Btn3.bind('<ButtonRelease-1>', stop_fun)
Btn4.bind('<ButtonRelease-1>', stop_fun)

top.bind('<KeyPress-a>', left_fun)   # Press down key 'A' on the keyboard and the robot will turn left.
top.bind('<KeyPress-d>', right_fun) 
top.bind('<KeyPress-s>', backward_fun)
top.bind('<KeyPress-w>', forward_fun)
top.bind('<KeyRelease-a>', stop_fun) # Release key 'A' and the robot will stop.
top.bind('<KeyRelease-d>', stop_fun)
top.bind('<KeyRelease-s>', stop_fun)
top.bind('<KeyRelease-w>', stop_fun)


def changeSpeed(ev=None):
	global spd
	spd = speed.get()/2 #Divide % by 2 so 100% (full speed) is sent as 50. Explanation for reason in usage manual
	print('sendData = %s' % spd)
	tcpCliSock.send(spd+"x")  # Send the speed data to the server(Raspberry Pi)

label = Label(top, text='Speed:', fg='red')  # Create a label
label.grid(row=6, column=0)                  # Label layout

speed = Scale(top, from_=0, to=100, orient=HORIZONTAL, command=changeSpeed)  # Create a scale from 0 to 100
speed.set(50)
speed.grid(row=6, column=1)

def main():
	top.mainloop()

if __name__ == '__main__':
	main()
