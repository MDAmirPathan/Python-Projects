import tkinter as tk 
from datetime import date, datetime

counter = 66600
running = False

def counter_label(label):

    def count():
        
        if running:
            global counter
            if counter == 66600:
                display = "Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string
                
            label['text'] = display
            label.after(1000,count)
    
        
            counter += 1
    
    count()
    
    
    
        

def Start(label):
    global running
    running = True
    counter_label(label)
    
    start['state'] = 'disabled'
    stop['state']= 'normal'
    reset['state'] = 'normal'
    

def Stop():
    global running

    start['state'] = 'normal'
    stop['state']= 'disabled'
    reset['state'] = 'normal'
    running = False


def Reset(label):
    global counter
    counter = 66600
    if not running:
        reset['state'] = 'disabled'
        label['text'] = "Welcome"
    else:
        label['text'] = 'Starting...'
        
    


root = tk.Tk()
root.title('Stopwatch')
root.minsize(width = 250 , height= 70)
label = tk.Label(root,fg='green',bg='black',text = 'Welcome',font='Verdona 30 bold')
label.pack()
f = tk.Frame(root)
f.pack(anchor= 'center' ,pady=5)
start = tk.Button(f,text = 'Start',width = 6,command = lambda: Start(label))
start.pack(side= 'left')
stop = tk.Button(f,text = 'Stop',width = 6,state= 'disabled',command= Stop)
stop.pack(side= 'left')
reset = tk.Button(f,text = 'Reset',width =6 ,state= 'disabled',command = lambda:Reset(label))
reset.pack(side= 'left')

root.mainloop()






