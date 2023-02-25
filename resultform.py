from tkinter import *
import sqlite3
import re 
from tkinter import messagebox
import pandas as pd
from disease2 import * 

class result_form:
# root = Tk()
 def __init__(self,root,algg):
  self.root= root
  root.title("Result")
  root.geometry('500x500')
  #Button(root, text='Reset',width=20,bg='brown',fg='white',command=validation).place(x=180,y=430)
  # Centering Root Window on Screen

  w = 500 # width for the Tk root
  h = 500 # height for the Tk root

  # get screen width and height
  ws = root.winfo_screenwidth() # width of the screen
  hs = root.winfo_screenheight() # height of the screen

  # calculate x and y coordinates for the Tk root window
  x = (ws/2) - (w/2)
  y = (hs/2) - (h/2)


  root["bg"] = '#98fb98'
  # set the dimensions of the screen 
  # and where it is placed
  root.geometry('%dx%d+%d+%d' % (w, h, x, y))
  fgcol='#581845'
  fgcol1='#BB33FF'
  fgcol2='#191970'
  dataframe1 = pd.read_csv("suggest.csv",header=None)


  print(algg)
  dislist=algg.split(',')
  print(dislist)
  adis1=dislist[1]
  adis2=dislist[2]
  adis3=dislist[3]
  print(adis1)
  print(adis2)
  print(adis3)
  idxx=dataframe1[dataframe1[0]==adis1].index[0]
  print(idxx)

  sugg1=dataframe1[1][idxx]

  idxx1=dataframe1[dataframe1[0]==adis2].index[0]
  sugg2=dataframe1[1][idxx1]
  
  idxx2=dataframe1[dataframe1[0]==adis3].index[0]
  sugg3=dataframe1[1][idxx2]

  self.d1=StringVar()
  self.d1.set(dislist[1])
  self.d2=StringVar()
  self.d2.set(dislist[2])
  self.d3 =StringVar()
  self.d3.set(dislist[3])
  
  self.s1=StringVar()
  self.s1.set(sugg1)
  
  self.s2=StringVar()
  self.s2.set(sugg2)

  self.s3=StringVar()
  self.s3.set(sugg3)

  #print(self.d1.get())
  #print(self.d2.get())
  #print(self.d3.get())
  self.label_0 = Label(self.root, text="Disease Prediction",width=20,font=("Courier New", 20, "bold"),bg='#98fb98',fg='brown')
  self.label_0.place(x=150,y=53)

  self.label_1 = Label(self.root, text="Disease",width=20,font=("Courier New", 10, "bold"),bg='#98fb98',fg=fgcol)
  self.label_1.place(x=120,y=100)

  self.label_2 = Label(self.root, text="Suggestion",width=20,font=("Courier New", 10, "bold"),bg='#98fb98',fg=fgcol)
  self.label_2.place(x=300,y=100)
  
  self.label_3 = Label(self.root, text="Decision Tree",width=20,font=("bold", 10),bg='#98fb98', anchor='w',fg=fgcol)
  self.label_3.place(x=30,y=140)

  self.label_4 = Label(self.root, text="Random Forest",width=20,font=("bold", 10),bg='#98fb98', anchor='w',fg=fgcol)
  self.label_4.place(x=30,y=180)

  self.label_5 = Label(self.root, text="Naive Bayes",width=20,font=("bold", 10),bg='#98fb98', anchor='w',fg=fgcol)
  self.label_5.place(x=30,y=220)

  self.label_6 = Label(self.root, textvariable = self.d1,width=30,font=("Courier New", 10, "bold"),bg='#98fb98',fg=fgcol1,anchor='w')
  self.label_6.place(x=120,y=140)

  self.label_7 = Label(self.root,textvariable = self.s1,width=20,font=("Courier New", 10, "bold"),bg='#98fb98',fg=fgcol2,anchor='w')
  self.label_7.place(x=300,y=140)
  self.label_8 = Label(self.root, textvariable = self.d2,width=30,font=("Courier New", 10, "bold"),bg='#98fb98',fg=fgcol1,anchor='w')
  self.label_8.place(x=120,y=180)
  self.label_9 = Label(self.root,textvariable = self.s2,width=20,font=("Courier New", 10, "bold"),bg='#98fb98',fg=fgcol2,anchor='w')
  self.label_9.place(x=300,y=180)
  self.label_10 = Label(self.root, textvariable = self.d3,width=30,font=("Courier New", 10, "bold"),bg='#98fb98',fg=fgcol1,anchor='w')
  self.label_10.place(x=120,y=220)
  self.label_11 = Label(self.root,textvariable = self.s3,width=20,font=("Courier New", 10, "bold"),bg='#98fb98',fg=fgcol2,anchor='w')
  self.label_11.place(x=300,y=220)

  Button(self.root, text='Back',width=15,bg='brown',fg='white',command=self.df1).place(x=180,y=280)
  Button(self.root, text='Exit',width=15,bg='brown',fg='white',command=self.logform).place(x=180,y=320)

 def logform(self):
  self.root.destroy()

 def df1(self):

  from disease2 import DiseasePred
  self.root.destroy()
  #Open new window
  newroot = Tk()
  application = DiseasePred(newroot)
  newroot.mainloop() 

 def validation(self):
  name1=self.Name.get()
  email=self.Email.get()
  phno1=self.Phno.get()
  uid1=self.Uid.get()
  pswd1=self.Pswd.get()
  valemail=self.checkemail(email)
  ip=len(name1) != 0 and len(email) != 0 and len(phno1) != 0 and len(uid1) != 0 and len(pswd1) != 0 and valemail=="Valid Email"
  return ip

 def checkemail(self,email):  
  regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

  # pass the regualar expression and the string in search() method 
  if(re.search(regex,email)):  
   return "Valid Email"
       
  else:  
   return "Invalid Email"
      

 def checkuser(self,userdet):
  cu=1
  cu1=0
  conn = sqlite3.connect('DiseasePred.db')
  c = conn.cursor()
  # select only the field "username" from the table
  c.execute("SELECT Username FROM Register where Username=?", (userdet,)) 
  #c.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
  # build a set with all names, from the results given as [('name1',), ('name2',), ('name3',)]
  names = {name[0] for name in c.fetchall()}
  #for n in c.fetchall():
  if userdet in names: 
   return cu
  else:
   return cu1

 def database(self):
  name1=self.Name.get()
  email=self.Email.get()
  phno1=self.Phno.get()
  uid1=self.Uid.get()
  pswd1=self.Pswd.get()
  conn = sqlite3.connect('DiseasePred.db')
  with conn:
   cursor=conn.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS Register(Name TEXT,Email TEXT,Phno TEXT,Username TEXT,Password TEXT)')

  ip1=self.validation()   
  if self.checkuser(uid1) == 1:
   messagebox.showinfo("Status", "User Exists")            
  else:
   if ip1==1:
    cursor.execute('INSERT INTO Register VALUES(?,?,?,?,?)',(name1,email,phno1,uid1,pswd1))
    conn.commit()
    messagebox.showinfo("Status", "Registration successful")
    self.df1() 
   else:
    messagebox.showinfo("Status", "All fields are mandatory and Give Correct Values.")

if __name__ == '__main__':

 root = Tk()
 dataa=''
 application=result_form(root,dataa)
 #root.geometry('500x500') 
 root.mainloop()





