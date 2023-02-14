from flask import render_template, request
from app import app
import tkinter as tk
from tkinter import ttk



# top level dialog window to display on the Monitor    
def show_dialog(time, venue, presenter_1, presenter_2):
    root = tk.Tk()
    
    # getting screen size to calculate the center of the screen to display the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (550/2)
    y = (screen_height/2) - (300/2)

    root.geometry("+%d+%d" % (x, y))
    root.geometry("550x300")
    root.wm_attributes("-topmost", 1)
    root.configure(bg='#2d2d2d')
    root.title("OB - Studio Crossover")

    heading = tk.Label(root, text="Please can you respond to the request below", font=("Arial", 16, "bold"), bg='#2d2d2d', fg='#ffffff')
    heading.pack(pady=20)

    label_2 = tk.Label(root, text=f"Crossover Time: {time}", font=("Arial", 13, "bold"), bg='#2d2d2d', fg='red')
    label_2.pack(pady=10)

    label_3 = tk.Label(root, text=f"Venue: {venue}", bg='#2d2d2d', fg='#ffffff')
    label_3.pack(pady=10)
    
    # check if both presenters or one presenter is included to display the label on the window (display nothing if none)
    if presenter_1 != 'None' or presenter_2 != 'None':
        if presenter_1 == 'None':
            label_4 = tk.Label(root, text=f"Presenters: {presenter_2}", bg='#2d2d2d', fg='#ffffff')
            label_4.pack(pady=10)
        if presenter_2 == 'None':
            label_4 = tk.Label(root, text=f"Presenters: {presenter_1}", bg='#2d2d2d', fg='#ffffff')
            label_4.pack(pady=10)
        if presenter_1 != 'None' and presenter_2 != 'None' :
            label_4 = tk.Label(root, text=f"Presenters: {presenter_1} and {presenter_2}", bg='#2d2d2d', fg='#ffffff')
            label_4.pack(pady=10)
        

    style = ttk.Style()
    style.configure('TButton', font=('Arial', 14), background='#3f51b5', foreground='#000000')

    button = ttk.Button(root, text="OK", command=root.destroy)
    button.pack(pady=20)

    root.mainloop()



# the web's home page
@app.route('/')
def index():
    return render_template('index.html')


# if user hit request button on the web, this route is called and it displays the dialog with data from the web form
@app.route('/crossover', methods=('GET', 'POST'))
def crossover():
    if request.method == 'POST':
        time = request.form['time']
        venue = request.form['venue']
        presenter_1 = request.form['presenters']
        presenter_2 = request.form['presenters_2']

        show_dialog(time, venue, presenter_1, presenter_2)

    return render_template('done.html')