from Tkinter import *

from newspapers import get_article

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

# try to get rid of this global
article = None
save_button = None

root = Tk()
top = Frame(root)
S = Scrollbar(root)
T = Text(root)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
text = "WELCOME TO PYNEWS\n"
T.insert(END, text)
T.config(yscrollcommand=S.set,state=DISABLED)

R = Text(root)
R.pack()

def quit_click():
    #T.insert(END, "This is an addition to the test")
    root.destroy()
    
def save_click():
    input = R.get("1.0", END)
    file = open("responses.txt", 'a')
    file.write(article.title + '\n')
    file.write(article.url + '\n')
    file.write(input + '\n\n')
    file.close()
    R.delete("1.0", END)
    
def next_click():
    T.config(state=NORMAL)
    global article
    article = get_article()
    new_text = str(article)
    T.delete("1.0", END)
    T.insert(END, new_text)
    T.config(state=DISABLED)

    global save_button
    if save_button is None:
        save_button = Button(root, text='Save', command=save_click)
        save_button.pack(in_=bottom, side=TOP)

bottom = Frame(root)
bottom.pack(side=BOTTOM)
    
Button(root, text='Next', command=next_click).pack(in_=bottom, side=TOP)
Button(root, text='Quit', command=quit_click).pack(in_=bottom, side=BOTTOM)
root.title("PyNews!")
center(root)
root.mainloop()
