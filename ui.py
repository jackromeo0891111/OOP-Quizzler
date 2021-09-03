from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.main_text = self.canvas.create_text(150, 125, text="test test test test", font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.label = Label(text="Score :0", bg=THEME_COLOR, fg="white", padx=20, pady=20)
        self.label.grid(column=1, row=0)

        right_image = PhotoImage(file="./images/true.png")
        wrong_image = PhotoImage(file="./images/false.png")
        self.right_button = Button(image=right_image, highlightthickness=0)
        self.wrong_button = Button(image=wrong_image, highlightthickness=0)
        self.right_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)

        self.window.mainloop()

