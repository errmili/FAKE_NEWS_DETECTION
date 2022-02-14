from joblib import dump, load
import requests
from bs4 import BeautifulSoup
#from wordcloud import WordCloud as wc
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import re
#from PIL import Image,ImageTk
#import pickle

#loading the model
Predict_news = load('pipeline.sav') 

#function for load the file
def callback():
    global name
    name = filedialog.askopenfilename()
    lien1.insert(0,name)

#function for predict the text enter
def generate_text():
    try:
        if param1.get("1.0","end").strip()=="":
            a=1/0
        labelTextSET.set("the news is ----> " + findlabel(param1.get("1.0","end")))
    except:
        labelTextSET.set('We have an error :( !!')

#function for predict the file enter
def generate_word():
    try:
        global file
        file = open(name,'r', encoding='utf-8').read()
        labelTextSET.set("the news is ----> "+findlabel(file))

    except:
        labelTextSET.set('We have an error :( !!')

#function for predict the Url enter
def generate_url():
    try:
        page = requests.get(url_web.get())
        html = BeautifulSoup(page.text, 'html.parser')
        text_html = html.findAll('p')
        text = str([str(p.getText()) for p in text_html])
        text = re.sub('\'' ,'', text)
        labelTextSET.set("the news is ----> " + findlabel(text))
    except:
        labelTextSET.set('We have an error :( !!')

#function for excutation  
def findlabel(newtext):
    y_pred1 = Predict_news.predict([newtext])
    return y_pred1[0]

#4 function for delete the ........
def master_destroy():
    root.destroy()
    labelTextSET.set("")
    
def e1_delete():
    lien1.delete(0,END)
    labelTextSET.set("")
    
def e1_delete1():
    param1.delete("1.0","end")
    labelTextSET.set("")

def e1_delete2():
   URL.delete(0,END)
   labelTextSET.set("")
        
# interface tkinter 
root = tkinter.Tk()
root.geometry("660x550")
root.config(bg="#e1e4e8")
root.title('FAKE NEWS')

#label = tkinter.Label(root, text="FAKE NEWS",font=('arial',14,'italic'))
#label.place(x=200,y=5)

Text = tkinter.Button(text=" Predict the text !!",command=generate_text,font=('arial',10,'bold'),bg="#282696",fg="#ffffff",width=60)
Text.place(x=10,y=124)

b_erase=tkinter.Button(root,text=" Erase the text  ",font=('arial',10,'bold'),bg="#d61c1c",fg="#ffffff",command=e1_delete1)
b_erase.place(x=520,y=124)

label = tkinter.Label(root, text="Put your text here for predict : ",font=('arial',10,'italic'),bg="#e1e4e8")
label.place(x=10,y=5)

nword = tkinter.StringVar(value='')
param1=tkinter.Text(root,height=5)
#param1 = tkinter.Entry(root, textvariable = nword,width=80)
param1.place(x=10,y=30)

label = tkinter.Label(root, text="Select your file to predict : ",font=('arial',10,'italic'),bg="#e1e4e8")
label.place(x=10,y=168)
lien1 = tkinter.Entry(root,width=81)
lien1.place(x=10,y=193)

labelTextSET = StringVar()
labelError = tkinter.Label(root, textvariable=labelTextSET,bg="#e1e4e8",font=('arial',14,'italic'))
labelError.place(x=250,y=420)

openFile = tkinter.Button(text="  File Open   ",font=('arial',10,'bold'),bg="#0bba37",fg="#ffffff",width=11,command=callback)
openFile.place(x=520,y=185)

Generate = tkinter.Button(text="Predict the file !!", command=generate_word,font=('arial',10,'bold'),bg="#282696",fg="#ffffff",width=60)
Generate.place(x=10,y=220)

b_erase=tkinter.Button(root,text=" Erase the file ", command=e1_delete,font=('arial',10,'bold'),bg="#d61c1c",fg="#ffffff")
b_erase.place(x=520,y=220)

label = tkinter.Label(root, text="Put your URL to predict : ",font=('arial',10,'italic'),bg="#e1e4e8")
label.place(x=10,y=260)
url_web = tkinter.StringVar()
URL = tkinter.Entry(root,textvariable = url_web,width=81)
URL.place(x=10,y=285)

Text = tkinter.Button(text=" Predict the URL !!",command=generate_url,font=('arial',10,'bold'),bg="#282696",fg="#ffffff",width=60)
Text.place(x=10,y=312)

b_erase=tkinter.Button(root,text=" Erase the URL  ",font=('arial',10,'bold'),bg="#d61c1c",fg="#ffffff",command=e1_delete2)
b_erase.place(x=520,y=312)

b_quit_destroy=Button(root, text="Quit application", command=master_destroy,font=('arial',10,'bold'),bg="#d61c1c",fg="#ffffff")
b_quit_destroy.place(x=520,y=500)

root.mainloop()