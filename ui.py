from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface():
    """docstring for QuizInterface."""
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"SCORE: {self.quiz.score}",
                                 bg=THEME_COLOR,
                                 fg="white",
                                 font=("Arial", 12))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300,
                             height=250,
                             bg="white",
                             highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="test",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20,
                                                           "italic"),width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, rowspan=2,pady=50)

        true_button_img = PhotoImage(file="./images/true.png")
        false_button_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_button_img,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(column=0, row=3)
        self.false_button = Button(image=false_button_img,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(column=1, row=3)

        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
            self.score_label.config(text= f"SCORE: {self.quiz.score}")
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
        
    def true_pressed(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
            
    def false_pressed(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
            
            