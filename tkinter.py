import tkinter as tk

def showText():
  myText.delete(0,"end")
  myText.insert(0,"Hello there!")

def kBye():
  myText.delete(0,"end")
  myText.insert(0,"K bye")

myWindow = tk.Tk()
myWindow.title("My Window")
myWindow.geometry("400x200")
myLabel = tk.Label(myWindow, text = "My Label")
myLabel.pack()
myButton = tk.Button(myWindow, text = "Click here!", command=showText)
myButton.pack()
myButton2 = tk.Button(myWindow, text = "Goodbye!" , command=kBye)
myButton2.pack()
myText = tk.Entry(myWindow)
myText.pack()
myWindow.mainloop()
