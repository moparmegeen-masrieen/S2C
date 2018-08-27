import threading
from queue import Queue
import time
from tkinter import *

print_lock = threading.Lock()
q = Queue()

def printer(worker):
    time.sleep(0.5)
    with print_lock:
    print(threading.current_thread().name, worker)

def finder():
    while True:
        worker = q.get()
        printer(worker)
        q.task_done()

for i in range(10):
    threads = threading.Thread(target = finder)
    threads.deamon = True
    threads.start()

print('Threads created')

for job in range(20):
    q.put(job)

q.join()
print('Jobs assigned to threads')
print('The jobs are done')

class form1(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('Thread window')
        self.pack(fill=BOTH, expand=1)
        Thread_Button = Button(self, text='Thread print', command=threading)
        Thread_Button.place(x=0, y=0)
        label = Label(self, text=threading)
        label.place(x=100, y=100)

app = Tk()
app.geometry('600x400')
window = form1(app)
app.mainloop()
window = form1(app)
