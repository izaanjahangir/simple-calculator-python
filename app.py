from tkinter import Tk, Label, Entry, Button, END

root = Tk()
root.title("Simple calculator")
answer = 0


def handleButtonClick(number):
    previous = str(entryEl.get())
    entryEl.delete(0, END)

    new = previous + str(number)

    entryEl.insert(0, new)


def clear():
    entryEl.delete(0, END)

def resetCalculation():
    clear()
    global answer
    answer = 0

def handlePlusPress():
    operand = entryEl.get()
    global answer

    answer = answer + int(operand)
    clear()


def handleEqualPress():
    handlePlusPress()
    entryEl.insert(0, answer)


entryEl = Entry(root)
entryEl.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

buttonNo1 = Button(root, text="1", command=lambda: handleButtonClick(1))
buttonNo1.grid(row=1, column=0)

buttonNo2 = Button(root, text="2", command=lambda: handleButtonClick(2))
buttonNo2.grid(row=1, column=1)

buttonNo3 = Button(root, text="3", command=lambda: handleButtonClick(3))
buttonNo3.grid(row=1, column=2)

buttonNo4 = Button(root, text="4", command=lambda: handleButtonClick(4))
buttonNo4.grid(row=2, column=0)

buttonNo5 = Button(root, text="5", command=lambda: handleButtonClick(5))
buttonNo5.grid(row=2, column=1)

buttonNo6 = Button(root, text="6", command=lambda: handleButtonClick(6))
buttonNo6.grid(row=2, column=2)

buttonNo7 = Button(root, text="7", command=lambda: handleButtonClick(7))
buttonNo7.grid(row=3, column=0)

buttonNo8 = Button(root, text="8", command=lambda: handleButtonClick(8))
buttonNo8.grid(row=3, column=1)

buttonNo9 = Button(root, text="9", command=lambda: handleButtonClick(9))
buttonNo9.grid(row=3, column=2)

buttonNo0 = Button(root, text="0", command=lambda: handleButtonClick(0))
buttonNo0.grid(row=4, column=0)

buttonEqual = Button(root, text="=", width=10, command=handleEqualPress)
buttonEqual.grid(row=4, column=1, columnspan=2)

buttonAdd = Button(root, text="+", command=handlePlusPress)
buttonAdd.grid(row=5, column=0, pady=(0, 20))

buttonClear = Button(root, text="Clear", width=10, command=resetCalculation)
buttonClear.grid(row=5, column=1, columnspan=2, pady=(0, 20))

root.mainloop()
