from tkinter import *

def select():
    select = "인도 도시 중 " + str(r.get()) + "를 선택했습니다."
    show.config(text = select)

top = Tk()
top.geometry("300x200")

r = IntVar()
lb = Label(text="인도 도시 중 어떤거 선택?")
lb.pack()

r1 = Radiobutton(top, text="1. Maharashtra", variable=r, value=1, command=select)
r1.pack(anchor = W)

r2 = Radiobutton(top, text="2. Karnataka", variable=r, value=2, command=select)
r2.pack(anchor = W)

r3 = Radiobutton(top, text="3. Andhra Pradesh", variable=r, value=3, command=select)
r3.pack(anchor = W)

show = Label(top)
show.pack()

top.mainloop()
