from tkinter import *
from googletrans import Translator,LANGUAGES


root = Tk()
root.geometry("540x654")
root.title("GOOGLE TRANSLATOR PROJECT")
root.config(background="darkblue")
label = Label(root,text = "Translator"
              ,font=('Atma',40,'bold')
              ,fg="yellow"
              ,bg="dark blue")
label.pack(pady=20)
wid = 30
fnt = "Atma",20,"bold"
ent = Entry()
ent.config(font=fnt
           ,fg = "black"
           ,bg = "white"
           ,width=wid)
ent.pack(pady=20)

entr = Entry()
entr.config(font=fnt
           ,fg = "black"
           ,bg = "white"
           ,width=wid)
entr.pack(pady=20)
select = StringVar()
select.set("select languages")
drop = OptionMenu(root,select,*LANGUAGES.values())
drop.config(font= ("Atma",10),fg="black",bg="white",width=wid)
drop.pack(pady=20)


def translated_text():
    text = ent.get()
    if text and select.get()!="Select Langauage":
        translator = Translator()
        translated = translator.translate(text,dest = select.get())
        entr.delete(0,END)
        entr.insert(0,translated.text)
    

button = Button(root,text = "Translate",font=("Atma",10,"bold"),bg="orange",command=translated_text)
button.pack(pady=20)




root.mainloop()