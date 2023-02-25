from tkinter import *
import sqlite3
import pandas as pd
from time import sleep
import numpy as np
from tkinter import messagebox
from resultform import *

class DiseasePred:
# root = Tk()
 def __init__(self,root):
  self.root= root
  root.title("Symptoms Form")
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

  self.var = StringVar()
  self.var.set('')
  self.var1 = StringVar()
  self.var1.set('Output')
  self.alg1=""  


  # TRAINING DATA dataframe1 --------------------------------------------------------------------------------

  listItems=[]
  dataframe1 = pd.read_csv("Training.csv")
  for col in dataframe1.columns: 
   listItems.append(col)
  listItems.pop(-1)
  self.disease=dataframe1.prognosis.unique()
  res = {val : idx for idx, val in enumerate(self.disease)}
  #print(res)
  dataframe1.replace({'prognosis':res},inplace=True)
  #print(dataframe1)
  self.l1=listItems
  self.X11= dataframe1[self.l1] #train symptoms
  self.y11 = dataframe1[["prognosis"]] #test disaease
  np.ravel(self.y11)
 


 # TESTING DATA df -------------------------------------------------------------------------------------
  dataframe2 = pd.read_csv("Testing.csv")
  dataframe2.replace({'prognosis':res},inplace=True)
  self.X_test= dataframe2[self.l1]
  self.y_test = dataframe2[["prognosis"]]
  np.ravel(self.y_test)



  self.l2=[]
  for x in range(0,len(self.l1)):
    self.l2.append(0)
  #--------------------------------------------------GUI-TKINTER-------------------------------------------------------
  self.label_0 = Label(self.root, text="Disease Prediction from Symptoms",width=35,font=("Courier New", 16, "bold"),bg='#98fb98',fg='red')

  self.label_0.place(x=50,y=30)

  self.label_00 = Label(self.root, text=" using ML Algorithms.",width=20,font=("Courier New", 16, "bold"),bg='#98fb98',fg='red')

  self.label_00.place(x=100,y=70)

  self.label_1 = Label(self.root, text="Symptoms Choice",width=15,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_1.place(x=40,y=130)
  self.label_1 = Label(self.root, text="Selected Symptoms",width=20,font=("bold", 10),bg='#98fb98', anchor='w')
  self.label_1.place(x=300,y=130)
  
  self.LB =Listbox(self.root,selectmode=EXTENDED )
  # self.listBox.pack( side = LEFT, expand = YES, fill = BOTH,padx = 5, pady = 5 )
  self.LB.place( x=20,y=180)

  self.copyButton = Button( self.root,text = ">>>", command = self.additemtoLB )
 # self.copyButton.pack( side = LEFT, padx = 5, pady = 5 )
  self.copyButton.place( x=200,y=200 )

  self.copyButton1 = Button( self.root,text = "<<<", command = self.additemtoLB1 )
 # self.copyButton.pack( side = LEFT, padx = 5, pady = 5 )
  self.copyButton1.place( x=200,y=260 )
  
  self.chosen = Listbox(root,selectmode=EXTENDED) 
  #self.chosen.pack( side = LEFT, expand = YES, fill = BOTH,padx = 5, pady = 5 )
  self.chosen.place( x=280,y=180 )




  self.lbl1 = Label(self.root, textvariable = self.var,width=35,font=("Courier New", 13, "bold"),bg='#98fb98',fg='red',anchor='w')
  self.lbl1.place( x=100,y=370 )
  Button(self.root, text='Submit',width=15,bg='brown',fg='white',command=self.ApplyAlgorithm).place(x=50,y=400)
  Button(self.root, text='Result',width=15,bg='brown',fg='white',command=self.logform).place(x=200,y=400)
  Button(self.root, text='Exit',width=15,bg='brown',fg='white',command=self.close_window).place(x=350,y=400)
  
  self.lbl2 = Label(self.root, text="",width=80,font=("Courier New", 9, "bold"),bg='#98fb98',fg='red',anchor='w')
  self.lbl2.place( x=50,y=450 )
  temp_list =  listItems.copy()
  temp_list.sort(key=str.lower)
  for item in temp_list:
    self.LB.insert(END, item)
# ------------------------------------ALGORITHM------------------------------------------------------------------

 def DecisionTree(self):

    from sklearn import tree
    e4 = self.chosen.get(0, 'end')
    e4=list(e4)
    #print(e4)
    
    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(self.X11,self.y11)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score,precision_score,classification_report,confusion_matrix,average_precision_score
    y_pred=clf3.predict(self.X_test)
    print("accuracy_score :", accuracy_score(self.y_test, y_pred))
    print("precision_score :", precision_score(self.y_test, y_pred,average = None))
    #print('classification_report',classification_report(self.y_test, y_pred))
    #mat =
   # print('confusion_matrix :',confusion_matrix(self.y_test, y_pred))
    #sensitivity = mat[]
    #print("accuracy_score : ", accuracy_score(self.y_test, y_pred,normalize=False))
    # -----------------------------------------------------
    psymptoms = e4

    for k in range(0,len(self.l1)):
        # print (k,) symptoms cross check  with all symptoms dataset
        for z in psymptoms:
            if(z==self.l1[k]):
                self.l2[k]=1

    inputtest = [self.l2] 
    predict = clf3.predict(inputtest)
    print(predict)
    predicted=predict[0]
    print(predicted)
    h='no'
    for a in range(0,len(self.disease)):
        if(predicted == a):
            h='yes'
            break

    lblout=self.var1.get()
    if (h=='yes'):
        lblout=lblout+","+self.disease[a]
        self.var1.set(lblout)
        
    else:
        lblout=lblout+","+"Not Found"
        self.var1.set(lblout)
      

 def randomforest(self):
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(self.X11,np.ravel(self.y11))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score,precision_score,classification_report,confusion_matrix,average_precision_score
    y_pred=clf4.predict(self.X_test)
    print("accuracy_score :",accuracy_score(self.y_test, y_pred))
    print("precision_score :", precision_score(self.y_test, y_pred,average = None))
   # print("classification_report :",classification_report(self.y_test, y_pred))
    #print('confusion_matrix :',confusion_matrix(self.y_test, y_pred))
    #print("accuracy_score :",accuracy_score(self.y_test, y_pred,normalize=False))
    # -----------------------------------------------------
    e4 = self.chosen.get(0, 'end')
    e4=list(e4)
    psymptoms = e4
    
    for k in range(0,len(self.l1)):
        for z in psymptoms:
            if(z==self.l1[k]):
                self.l2[k]=1

    inputtest = [self.l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(self.disease)):
        if(predicted == a):
            h='yes'
            break
    lblout=self.var1.get()
    if (h=='yes'):
        lblout=lblout+","+self.disease[a]
        self.var1.set(lblout)
        
    else:
        lblout=lblout+","+"Not Found"
        self.var1.set(lblout)
       


 def NaiveBayes(self):
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(self.X11,np.ravel(self.y11))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score,precision_score,classification_report,confusion_matrix,average_precision_score
    y_pred=gnb.predict(self.X_test)
    print("accuracy_score :",accuracy_score(self.y_test, y_pred))
    print("precision_score :", precision_score(self.y_test, y_pred,average = None))
    #print('classification_report',classification_report(self.y_test, y_pred))
    #print('confusion_matrix :',confusion_matrix(self.y_test, y_pred))
    #print("accuracy_score :",accuracy_score(self.y_test, y_pred,normalize=False))
    # -----------------------------------------------------
    e4 = self.chosen.get(0, 'end')
    e4=list(e4)
    psymptoms = e4
    for k in range(0,len(self.l1)):
        for z in psymptoms:
            if(z==self.l1[k]):
                self.l2[k]=1

    inputtest = [self.l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(self.disease)):
        if(predicted == a):
            h='yes'
            break
    lblout=self.var1.get()
    if (h=='yes'):
        lblout=lblout+","+self.disease[a]
        self.var1.set(lblout)
    else:
        lblout=lblout+","+"Not Found"
        self.var1.set(lblout)
      
# ------------------------------------ALGORITHM FINISH------------------------------------------------------------------
 
 def ApplyAlgorithm( self ):
  if self.var.get()=='Finish':
   exp=''
   self.var1.set(exp)
  sleep(0) # Need this to slow the changes down
  self.var.set('Check Symptoms')
  self.root.update_idletasks()
  sleep(0) # Need this to slow the changes down
  self.var.set('')
  self.root.update_idletasks()
  sleep(0) # Need this to slow the changes down
  self.var.set('Check Symptoms')
  self.root.update_idletasks()
  sleep(0) # Need this to slow the changes down
  self.var.set('')
  self.root.update_idletasks()
  sleep(0) # Need this to slow the changes down
  self.var.set('Check Symptoms')
  self.root.update_idletasks()
  # self.DecisionTree()
  
  listchose=self.chosen.get(0, 'end')
  listchose=list(listchose)
  countitem=len(listchose)
  if countitem>0:

   sleep(0) # Need this to slow the changes down
   self.var.set('Apply Algorithm1')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('Apply Algorithm1')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('Apply Algorithm1')
   self.root.update_idletasks()
   self.DecisionTree()

   sleep(0) # Need this to slow the changes down
   self.var.set('')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('Apply Algorithm2')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('Apply Algorithm2')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('Apply Algorithm2')
   self.randomforest()

   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('Apply Algorithm3')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('Apply Algorithm3')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('Apply Algorithm3')
   self.NaiveBayes()
   self.alg1=self.var1.get()
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('')
   self.root.update_idletasks()
   sleep(0) # Need this to slow the changes down
   self.var.set('Finish')
   self.root.update_idletasks()
  else:
   messagebox.showinfo("Status", "Select Any Symptoms.")

 
 def additemtoLB( self ):
  sel = self.LB.curselection()
  for index in sel[::-1]:
   self.chosen.insert(END, self.LB.get(index))
   self.LB.delete(index)

 def additemtoLB1( self ):
  sel = self.chosen.curselection()
  for index in sel[::-1]:
   self.LB.insert(END, self.chosen.get(index))
   self.chosen.delete(index)

 def logform(self):
  if self.var.get()=='Finish':
   from resultform import result_form
   self.root.destroy()
   newroot = Tk()
   application = result_form(newroot,self.alg1)
   newroot.mainloop()
  else:
   messagebox.showinfo("Status", "First execute Algorithms.Click Submit")

  
 def close_window (self): 
    self.root.destroy()


if __name__ == '__main__':

 root = Tk()

 application=DiseasePred(root)
 #root.geometry('500x500') 
 root.mainloop()





