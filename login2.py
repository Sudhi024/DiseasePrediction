from tkinter import *
import sqlite3
from tkinter import messagebox

from registration1 import *
from disease2 import *

class User_Login:
# root = Tk()
 def __init__(self,root):
  self.root= root
  root.title("Login Form")
  root.geometry('300x250') 
  #Button(root, text='Reset',width=20,bg='brown',fg='white',command=validation).place(x=180,y=430)
  # Centering Root Window on Screen

  w = 300 # width for the Tk root
  h = 250 # height for the Tk root

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

  self.Uid=StringVar()
  self.Pswd=StringVar()
  self.label_0 = Label(self.root, text="Login Form",width=20,font=("Courier New", 20, "bold"),bg='#98fb98',fg='red')
  self.label_0.place(x=20,y=13)
  self.label_4 = Label(self.root, text="User Id",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_4.place(x=15,y=50)
  self.entry_4 = Entry(self.root,textvar=self.Uid)
  self.entry_4.place(x=75,y=50)
  self.label_5 = Label(self.root, text="Password",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_5.place(x=15,y=100)
  self.entry_5 = Entry(self.root,textvar=self.Pswd,show='*')
  self.entry_5.place(x=75,y=100)

  Button(self.root, text='Login',width=10,bg='brown',fg='white',command=self.database).place(x=30,y=150)
  Button(self.root, text='Cancel',width=10,bg='brown',fg='white',command=self.close_window).place(x=120,y=150)
 

  Button(self.root, text='Reset',width=10,bg='brown',fg='white',command=self.df1).place(x=30,y=200)
  Button(self.root, text='SignUp',width=10,bg='brown',fg='white',command=self.regis).place(x=120,y=200)

 def regis(self):
  from registration1 import regist

  #Do the work done by the main of registration.py
  #Destroy current window
  self.close_window()
  #Open new window
  newroot = Tk()
  application = regist(newroot)
  newroot.mainloop()



 def close_window (self): 
    self.root.destroy()

 def df1(self):
  exp=''
  self.Uid.set(exp)
  self.Pswd.set(exp)

   
 def validation(self):
  uid1=self.Uid.get()
  pswd1=self.Pswd.get()
  ip=len(uid1) != 0 and len(pswd1) != 0
  return ip

 def checkuserpsw(self,userdet,pswd):
  cu=1
  cu1=0
  conn = sqlite3.connect('DiseasePred.db')
  c = conn.cursor()
  # select only the field "username" from the table
  c.execute("SELECT Username,Password FROM Register where Username=?", (userdet,)) 
  # build a set with all names, from the results given as [('name1',), ('name2',), ('name3',)]
  vall=c.fetchall();
  vall = dict(vall)
  #print(vall)

  if userdet in vall: 
   if vall[userdet]==pswd :
     #print("Password Matching")
     return cu
   else:
     #print("Password NOT Matching")
     return cu1
  else:
    messagebox.showinfo("Status","User id does not exist")

 def database(self):
  uid1=self.Uid.get()
  pswd1=self.Pswd.get()
  conn = sqlite3.connect('DiseasePred.db')
  with conn:
   cursor=conn.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS Register(Name TEXT,Email TEXT,Phno TEXT,Username TEXT,Password TEXT)')

  ip1=self.validation()   
  if ip1 ==1:
   if self.checkuserpsw(uid1,pswd1) == 1:
    messagebox.showinfo("Status", "Login Sucessful")
    
    # Do the work done by the main of registration.py
    #Destroy current window
    self.root.destroy()
    #Open new window
    newroot = Tk()
    application = DiseasePred(newroot)
    newroot.mainloop()
   else:
    messagebox.showinfo("Status", "Invalid PSW")
    self.df1() 
  else:
   messagebox.showinfo("Status", "All fields are mandatory")

if __name__ == '__main__':

 root = Tk()
 #root = Tk()
 application=User_Login(root)
 
 root.mainloop()





