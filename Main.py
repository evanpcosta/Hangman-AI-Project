import app as app

from GUI import *

class APP:

    root = Tk()
    root.title('Hangman')
    root.geometry("500x400")

    global third_frame
    third_frame = Frame(root)
    third_frame.place(x=0, y=0, width=500, height=500)

    global second_frame
    second_frame = Frame(root)
    second_frame.place(x=0, y=0, width=500, height=500)

    global first_frame
    first_frame = Frame(root)
    first_frame.place(x=0, y=0, width=500, height=500)

    global label_question
    label_question = Label(first_frame, text="What word would you like your opponent to guess?")
    label_question.place(relx=0.5, rely=0.3, anchor=CENTER)

    global label_too_large
    label_too_large = Label(first_frame, text="")
    label_too_large.place(relx=0.5, rely=0.45, anchor=CENTER)

    global entry1
    entry1 = Entry(first_frame, width=20)
    entry1.place(relx=0.5, rely=0.4, anchor=CENTER)

    global button_1
    button_1 = Button(first_frame, text="Next", command=lambda: raise_frame_for())
    button_1.place(x=220, y=250)
    root.bind('<Return>', lambda event: raise_frame_for())
    button_1.focus_set()

    global label_guess
    label_guess = Label(second_frame, text="Guess a letter:")
    label_guess.place(relx=0.2, rely=0.7, anchor=CENTER)

    global entry2
    entry2 = Entry(second_frame)
    entry2.place(relx=0.5, rely=0.7, anchor=CENTER)

    button_2 = Button(second_frame, text="Back", command=lambda: raise_frame_bac(first_frame)).place(x=10, y=10)

    button_3 = Button(second_frame, text="Guess", command=lambda: change_underline())
    button_3.place(relx=0.78, rely=0.7, anchor=CENTER)

    global dashlabel1
    dashlabel1 = Label(second_frame, text=" ")
    dashlabel1.place(relx=0.89, rely=0.52, anchor=CENTER)

    global dashlabel2
    dashlabel2 = Label(second_frame, text=" ")
    dashlabel2.place(relx=0.89, rely=0.59, anchor=CENTER)

    global lostlabel
    lostlabel = Label(Main.third_frame, text="")
    lostlabel.place(relx=0.5, rely=0.45, anchor=CENTER)

    Main.lostlabel.config(text=" You Lost ")
    button2 = Button(Main.third_frame, text="Restart", command=lambda: raise_frame_bac(Main.first_frame))
    button2.place(relx=0.5, rely=0.5, anchor=CENTER)

    root.mainloop()