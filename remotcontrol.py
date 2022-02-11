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
    tcpCliSock.send(bytes("forward", 'utf8'))

def backward_fun(event):
    print('backward')
    tcpCliSock.send(bytes("backward", 'utf8'))

def left_fun(event):
    print('left')
    tcpCliSock.send(bytes("left", 'utf8'))

def right_fun(event):
    print('right')
    tcpCliSock.send(bytes("right", 'utf8'))

def stop_fun(event):
    print('stop')
    tcpCliSock.send(bytes("stop", 'utf8'))

def i_said_stop(event):
    print('STOP!!!')
    tcpCliSock.send(bytes("stop", 'utf8'))
        
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


def main():
	top.mainloop()

if __name__ == '__main__':
	main()
