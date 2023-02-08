from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    #longbreak min(8..)
    if reps%8 == 0:
        count_down(2*6)
        start_timer()
    #work min(1 3 5 7..)
    if reps%2 == 1:
        count_down(1*25)
        start_timer()
    #shortbreak min(2 4 6..)
    else:
        count_down(1*5)
        start_timer()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute = math.floor(count/60) # return the biggest integer
    second = count%60
    if second < 10:     # print the second to 2 number
        second = f"0{second}"
    canvas.itemconfig(timer_label, text=f"{minute}:{second}")
    if count>0:
        window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

#timer Labels
label1 = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
label1.grid(row=0, column=1)

canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image = tomato_img)
timer_label = canvas.create_text(100, 112, text = '00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

#start Button
button1 = Button(text="Start", command=start_timer)
button1.grid(row=2, column=0)

#check label
label2 = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, 'bold'))
label2.grid(row=3, column=1)

#reset button
def action2():
    print("Do some2thing")

button2 = Button(text="Reset", command=action2)
button2.grid(row=2, column=2)

window.mainloop()