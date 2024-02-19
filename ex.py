from tkinter import *
gui = Tk()
gui.geometry("800x220")
gui.configure(background="gray", highlightbackground="black") 

toplabel = Label(gui, text="Atbash GUI", font=("Arial", 15), bg ="white", fg = "black")
toplabel.place(x=280, y=20)
toplabel.pack(fill=X)

def encrypt(*args):
    ciphertext.delete(0.0, 'end')
    p = plaintext.get(0.0, 'end')
    k = ""
    for i in range(len(p)):
        if p[i]!=" " and p[i]!='\n' and p[i]!="\t":
            if ord(p[i]) in range(97,123):
                k += chr(96 + 26-(ord(p[i])-97))
            elif ord(p[i]) in range(65,91):
                k += chr(64 + 26-(ord(p[i])-65))
            else:
                k += p[i]
        else:
            k += p[i]
    ciphertext.insert(0.0, k)
  
def decrypt(*args):
    plaintext.delete(0.0, 'end')
    c = ciphertext.get(0.0, 'end')
    k=""
    for i in range(len(c)):
        if c[i]!=" " and c[i]!='\n'and c[i]!="\t":
            if ord(c[i]) in range(97,123):
                k += chr(96 + 26-(ord(c[i])-97))
            elif ord(p[i]) in range(65,91):
                k += chr(64 + 26-(ord(c[i])-65))
            else:
                k += c[i]
        else:
            k += c[i]
    plaintext.insert(0.0, k)

plabel = Label(gui, text="Text", bg="white", fg="gray20", relief="flat")
plabel.place(x=30, y=50)

plaintext = Text(gui, height = 6, width=43, bg = "snow", fg="black", relief="flat", highlightthickness="2px")
plaintext.place(x=30, y=80)
plaintext.bind('<Any-KeyRelease>', encrypt)

clabel = Label(gui, text="Cipher", bg="white", fg="gray20", relief="flat")
clabel.place(x=410, y=50)

ciphertext = Text(gui, height = 6, width=43, bg = "snow", fg="black", relief="flat", highlightthickness="2px")
ciphertext.place(x=410, y=80)
ciphertext.bind('<Any-KeyRelease>', decrypt)

gui.mainloop()
