import tkinter as tk
# import networking as network

LARGE_FONT = ("Verdana", 12)


class mainGUI(tk.Tk):
    def __init_(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = startPage(container, self)

        self.frames[startPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(startPage)
        print("sdfsdf init")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def qf():
    print("you did it")


class startPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        #button1 = tk.Button(self, text="Visit Page 1", command=qf)
        #button1.pack()
        #print("dfsdf startpage")

print("sdfsdf")
app = mainGUI()
print("sdfsdf2")
app.mainloop()
print("sdfsdf3")