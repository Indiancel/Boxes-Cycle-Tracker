import tkinter as tk


pressed_buttons = []

def button_pressed(button_name):
    global pressed_buttons
    if button_name in pressed_buttons:

        reset_count()
    else:

        pressed_buttons.append(button_name)
        

        buttons[button_name].config(bg="red", fg="black")


def reset_count():
    global pressed_buttons
    pressed_buttons.clear()
    

    for button in buttons.values():
        button.config(bg="white", fg="black")

window = tk.Tk()
window.title("Button Counter")
window.geometry("300x500")  
window.resizable(False, False)  


window.configure(bg="gray")


button_frame = tk.Frame(window, bg="gray") 
button_frame.pack(pady=20)  


button_names = ["PHD", "POWER", "AK74", "CLAYMORE", "MULE KICK", "SICKLE", "PAP", "FIRST ROOM"]
buttons = {}

for name in button_names:
    button = tk.Button(button_frame, text=name, padx=10, pady=10, font=("Arial", 14), bg="white", fg="black", width=20,
                       command=lambda n=name: button_pressed(n))  
    button.pack(pady=5)  
    buttons[name] = button 


reset_button = tk.Button(window, text="RESET", command=reset_count, font=("Arial", 14), bg="red", fg="white", width=20)
reset_button.pack(pady=10)


window.mainloop()
