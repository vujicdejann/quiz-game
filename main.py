__author__ = "Vujic Dejan"

from tkinter import *
from tkinter import messagebox as mb
import json

class QuizGame:
    def __init__(self):
        # Set variable for default value of question number
        self.question_number = 0

        # Set integer type for selected opions
        self.selected_options = IntVar()

        # Set radio buttons for current questions
        self.radio_option = self.create_options()

        # Define number of guestion
        self.data_size = len(question)

        # Set default counter of correct answers
        self.correct = 0

        # Call functions
        self.create_widgets()
        self.create_options()
        self.options()

    def create_widgets(self):
        # Create title description
        title = Label(frame, text = "Welcome to the Quiz Game! Let's begin", bg = "#012f3b", fg = "#ffffff",
                      font = ("Helvetica", 20, "bold"), width = 50)
        title.place(x = 0, y = 0.5)

        # Create question label
        question_number = Label(frame, text = question[self.question_number], font = ("Helvetica", 14, "bold"),
                                bg = "#065569", fg = "#ffffff")
        question_number.place(x=50, y=120)

        # Create buttons
        next_button = Button(frame, text = "Next question", font=("Helvetica", 24, "bold"), highlightbackground = "green",
                             command=self.next_button)
        next_button.place(x=120, y=320)

        quit_button = Button(frame, text = "Quit game", font=("Helvetica", 24, "bold"), highlightbackground = "red", command=frame.destroy)
        quit_button.place(x = 330, y = 320)

    def create_options(self):
        # Create radio buttons
        option_list = []
        position = 160
        
        # Set selected options in list and create radio buttons
        while len(option_list) < 4:
            radio_button = Radiobutton(frame, text=" ", variable=self.selected_options, value=len(option_list) + 1,
                                       font=("Helvetica", 14), bg="#065569", fg="#ffffff")
            option_list.append(radio_button)
            radio_button.place(x=100, y=position)
            position += 30

        return option_list

    def options(self):
        i = 0
        self.selected_options.set(0)
        
        for option in options[self.question_number]:
            self.radio_option[i]['text'] = option
            i += 1

    def check_answers(self, question_number):
        # Check answer is correct or worng
        if self.selected_options.get() == answer[self.question_number]:
            return True

    def results(self):
        # Calc correct and wrong answers
        count = self.data_size - self.correct
        correct = "Correct answers: ", self.correct
        wrong = "Wrong answers: ", count
        
        # Calc percentage
        score = int(self.correct / self.data_size * 100)
        result = "Score: ", score, "%"
        
        # Show info 
        mb.showinfo("Result: ", f"{result}\n{correct}\n{wrong}")
    
    # Next button logic
    def next_button(self):
        if self.check_answers(self.question_number):
            self.correct += 1

        self.question_number += 1

        if self.question_number == self.data_size:
            self.results()
            frame.destroy()

        else:
            self.create_widgets()
            self.options()


if __name__ == "__main__":
    # Configure gui 
    frame = Tk()
    frame.geometry("600x400")
    frame.resizable(width=False, height=False)
    frame.title("Quiz Game")
    frame.config(bg="#065569")

    # Get data from json file
    with open("data.json", "r") as question_file:
        data = json.load(question_file)

    # Set the values
    question = (data['question'])
    options = (data['options'])
    answer = (data['answer'])
    
    # Start game
    application = QuizGame()
    frame.mainloop()
