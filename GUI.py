from tkinter import *


# raises frame; puts first frame entry into second frame label
def raise_frame_for(frame):
    global labellist
    labellist = []
    global result
    result = entry1.get()
    if 40 > len(result) > 0:
        print(len(result))
        create_under_labels(result)
        frame.tkraise()
        print(result)
        entry1.delete(0, END)
    else:
        label_too_large.config(text="Entry too large (40 character max)")
        print(len(result))
    return


def create_under_labels(word):
    global blank
    blank = IntVar()
    blank.set(' ')
    global under
    under = IntVar()
    under.set(' __')
    y = 0
    for x in range(len(word)):
        if x < 20:
            if word[x] == ' ':
                labellist.append(Label(second_frame, textvariable=blank).place(relx=find_relx(x), rely=0.56, anchor=CENTER))
            else:
                labellist.append(Label(second_frame, textvariable=under).place(relx=find_relx(x), rely=0.56, anchor=CENTER))
        else:
            if word[x] == ' ':
                labellist.append(Label(second_frame, textvariable=blank).place(relx=find_relx(y), rely=0.56, anchor=CENTER))
            else:
                labellist.append(Label(second_frame, textvariable=under).place(relx=find_relx(y), rely=0.6, anchor=CENTER))
                y = y + 1
#problem with higher count letter words has to do with y and find relx probably with the result//2 calc

def find_relx(x):
    print(result)
    print(len(result) // 2)
    print(x)
    if x == (len(result) // 2):
        rx = 0.5
        print(rx)
        return (rx)
    elif x < (len(result) // 2):
        nx = 0.5 - (((len(result) // 2) - x) * 0.04)
        print(nx)
        return nx
    elif x > (len(result) // 2):
        px = 0.5 + ((x - (len(result) // 2)) * 0.04)
        print(px)
        return px


def create_letter_labels(word):
    for x in range(len(word)):
        if x > 30:
            labellist.append(Label(second_frame, text="").place(relx=0.1 * x, rely=0.6, anchor=CENTER))
        else:
            labellist.append(Label(second_frame, text="").place(relx=0.1, rely=0.62, anchor=CENTER))
    return labellist


# changes the frame
def raise_frame_bac(frame):
    entry2.delete(0, END)
    frame.tkraise()
    clear = ' '
    under.set('')
    blank.set('')
    label_too_large.config(text=" ")
    # spacelist[:] = []
    guesslabel.config(text=" ")
    guesslist[:] = []


# if guessed correctly turns an underline into a letter
guesslist = []


def change_underline():
    letter = entry2.get()
    lisr = list(result)
    if len(letter) == 1 and letter not in guesslist:
        guesslist.append(letter)
        entry2.delete(0, END)
        for x in range(len(result)):
            if letter == lisr[x]:
                break
            # else:
            # turn show in the guessed wrong section
        guesslabel.config(text="")


root = Tk()
root.title('Hangman')
root.geometry("500x400")

second_frame = Frame(root)
second_frame.place(x=0, y=0, width=500, height=500)

first_frame = Frame(root)
first_frame.place(x=0, y=0, width=500, height=500)

label_question = Label(first_frame, text="What word would you like your opponent to guess?")
label_question.place(relx=0.5, rely=0.3, anchor=CENTER)

label_too_large = Label(first_frame, text="")
label_too_large.place(relx=0.5, rely=0.45, anchor=CENTER)

entry1 = Entry(first_frame, width=20)
# entry1.focus()
entry1.place(relx=0.5, rely=0.4, anchor=CENTER)

button_1 = Button(first_frame, text="Next", command=lambda: raise_frame_for(second_frame)).place(x=220, y=250)

label_guess = Label(second_frame, text="Guess a letter:")
label_guess.place(relx=0.2, rely=0.7, anchor=CENTER)

entry2 = Entry(second_frame)
# entry2.focus()
entry2.place(relx=0.5, rely=0.7, anchor=CENTER)

button_2 = Button(second_frame, text="Back", command=lambda: raise_frame_bac(first_frame)).place(x=10, y=10)

button_3 = Button(second_frame, text="Guess", command=lambda: change_underline())
button_3.place(relx=0.78, rely=0.7, anchor=CENTER)

wordlabel = Label(second_frame, text="")
wordlabel.place(relx=0.5, rely=0.6, anchor=CENTER)

guesslabel = Label(second_frame, text="")
guesslabel.place(relx=0.5, rely=0.585, anchor=CENTER)

root.mainloop()

# "h  e   l   l  o"
# 3 behind every l and 2 behind every other letter

# def move_entry():
# result = entry1.get()
# label_update_guess.config(text=result)
# entry1.delete(0, END)


# button_3 = Button(first_frame, text="change label", command=move_entry()).place(x=15, y=15)

# label_update_guess = Label(first_frame)
# label_update_guess.place(relx=0.5, rely=0.4, anchor=CENTER)

# underlines = StringVar()
# underlines.set("\u0332  " * len(entry1.get()))

# button_3 = Button(second_frame, text="Back", command=lambda: print_underlines()).place(x=50, y=50)


# button_1.place(relx=0.5, rely=0.6, anchor=CENTER)

# def checkToNewWindow() :
# letters = entry1.get()
# if len(letters) > 0 :
# game_window()


# prints the underlines that show the opposing player how many letters are in the word
# word = input("What word would you like to opponent to guess? ")


# print('\u0332  ' * len(word))


# print('\u0332  \u0332a \u0332a \u0332u \u0332z \u0332z \u0332z');


# def displayHangman(event):
#     print(" ______")
#     print(" |   \|");
#     print(" O    |");
#     print("/|\   |            You have already guessed:");
#     print(" |    |");
#     print("/ \   |");
#     print("      |");
#     print("   ___|___");
#     print("");
#
# weight_lbs = input("What is your weight in pounds? ");
# weight_kg = float(weight_lbs)/2.2
# print(int(weight_kg))
# input("what is your favorite color? ");
# print("mosh likes blue");


# def game_window() :
# game = Tk()
# game.title("Hangman")
# game.geometry('500x500')

# game.mainloop()

# Changes frame and updates label
# def raise_frame_update(frame) :
#     letters = entry1.get()
#     if len(letters) > 0:
#         frame.tkraise()
#         label_update_guess.config(text=letters)
#         entry1.delete(0, END)

# def show_the_underlines() :
#     letters = entry1.get()
#     string_to_display = '\u0332  ' * len(letters)
#     label_update_guess("text") = string_to_display


# def print_underlines() :
#     letters = entry1.get()
#     print('\u0332  ' * len(letters))

################################################################################

'''

#creates a list of spaces from an entry that vary in length
longletters = ['t', 'i', 'f', 'j', 'l']
def space_list():
    spaclist = []
    print(result)
    for x in range(len(result)):
        if result[x] in longletters:
            spaclist.append('__')
        else:
            spaclist.append('__')
    for i in spaclist:
        print(i)
        return spaclist

#creates a list of all the locations of a letter in a space list
def calc_space_poss(letter1):
    total = 0
    totallist = []
    for x in result:
        if x in longletters:
            total = total + 2
        else:
            total = total + 2
        if x == letter1:
            totallist.append(total)
    return totallist


'''

'''
#turns an entry into a string of underlines
def turn_to_underlines(word):
    char = [char for char in word]
    ul = ""
    if len(char) > 30:
        ul = "Error Too Large"
    else:
        for x in char:
            if x == " ":
                ul += " "
            else:
                ul += " __"
    return ul
'''
