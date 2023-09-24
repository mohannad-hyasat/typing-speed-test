import tkinter as tk
reps = 0
n = 60




def stop_test(event: bool):
    if event:
        calculate_speed(60-n)


def calculate_speed(secs):
    correct_c = 0
    og_sentence = str(sentence.cget('text'))
    player = player_input.get()
    words = og_sentence.split(' ')
    try:
        for s in range(len(player)):
            if og_sentence[s] == player[s]:
                correct_c += 1
        cpm = round((correct_c * 60) / secs)
        wpm = round(cpm / len(words))
        accuracy = round((correct_c/len(og_sentence)) * 100)
        cpm_score.config(text=f'{cpm}')
        wpm_score.config(text=f'{wpm}')
        acc_score.config(text=f'{accuracy}%')
    except:
        cpm_score.config(text=f'0')
        wpm_score.config(text=f'0')
        acc_score.config(text=f'0')


def countdown(t):
    global n
    player_input.get()
    if len(str(sentence.cget('text'))) > len(player_input.get()) and n > 0:
        n = t
        window.after(1000, countdown, t-1)
    else:
        n = t
        calculate_speed(60-n)


def start_timer(event:bool):
    global reps
    reps += 1
    if event and reps < 2:
        countdown(n)

window = tk.Tk()
window.title('Typing speed test')
window.config(padx=100, pady=100, bg='#252B48')

title = tk.Label(text='Lets see how fast you can type :)', font=("Courier", 36, 'bold'), fg='#F7E987', bg='#252B48', pady=50)
sentence = tk.Label(text='you have to Type THIS really fast', font=("Courier", 32), fg='#F7E987', bg='#252B48', pady=50)
player_input = tk.Entry(width=50, font=("Courier", 32), fg='#F7E987', bg='#252B48', border=True)
player_input.bind('<KeyRelease>', start_timer)
player_input.bind('<Return>', stop_test)

cpm_label = tk.Label(text='CPM score', font=("Courier", 24), fg='#F7E987', bg='#252B48', pady=50)
wpm_label = tk.Label(text='WPM score', font=("Courier", 24), fg='#F7E987', bg='#252B48', pady=50)
acc_label = tk.Label(text='Accuracy', font=("Courier", 24), fg='#F7E987', bg='#252B48', pady=50)

cpm_score = tk.Label(text='-', font=("Courier", 24), fg='#F7E987', bg='#252B48', pady=50)
wpm_score = tk.Label(text='-', font=("Courier", 24), fg='#F7E987', bg='#252B48', pady=50)
acc_score = tk.Label(text='-', font=("Courier", 24), fg='#F7E987', bg='#252B48', pady=50)


title.grid(row=0, column=1)
sentence.grid(row=1, column=1)
player_input.grid(row=2,column=1)
cpm_label.grid(row=3, column=0)
wpm_label.grid(row=3, column=1)
acc_label.grid(row=3, column=2)
cpm_score.grid(row=4, column=0)
wpm_score.grid(row=4, column=1)
acc_score.grid(row=4, column=2)

window.mainloop()

