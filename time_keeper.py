'''
Python and TKinter App that displays current time, with buttons to mark clock in and clock out times
Will save those times on button press to csv file

'''
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
from time import strftime
from datetime import datetime
from datetime import date
from csv import * 


win=tkinter.Tk(screenName=None,  baseName=None,  className='time_keeper',  useTk=1) #creating the main window and storing the window object in 'win'

#Setting the Tkinter window icon
img = PhotoImage(file='icon.gif') #Having this setting without the full path breaks the code in visual studio, but the actual executable is fine
win.iconphoto(True, img)
win.resizable(width=False, height=False) #Keeping the window from being resizable

#We create the widgets here
win.geometry('500x450') #setting the size of the window
win.title("Time Keeper") #Main Window title
main_lst=[] #This is where the entry boxes store the data

#Date and time widget for clock
def my_time():
    time_string = strftime('%H:%M:%S %p \n %A \n %x') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) #time delay of 1000 milliseconds 
	
my_font=('times',25,'bold') #display size and style
alt_font=('times', 12, 'bold') #alt font size for labels
#Formatting block for the clock
l1=tkinter.Label(win,font=my_font,bg='yellow')
l1.grid(row=1, column=4)

current_date = date.today() #Pulling current date for usage in the entry box autopopulation, needs formatted in the acutal function

'''
This is for the clock in button and function
Shows an alert box on button click showing system time on click
also changes a label to show last action and time
same for the clock out button further down
'''
def clock_in(): #function of the button
    date_ent.delete(0,END) #This block of deletes wipes the entry boxes to allow clean new data on each button press
    time_ent.delete(0,END)
    type_ent.delete(0,END)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") #Grabbing time and date to update the label with
    label_clock_in = Label(win,font=alt_font, text="Clocked in at "+ current_time) #Display clock in time
    label_clock_in.place(x=10, y=100)
    tkinter.messagebox.showinfo("Complete","You clocked in at "+ current_time) #Display pop up box with same info
    #This block is for autopopulating the entry boxes with the pulled info
    date_ent.insert(0, current_date.strftime("%m/%d/%y")) #Pulls the date from current_date function and formats it
    time_ent.insert(0, current_time) #Pulls current time in UTC, could use formatting, not sure how
    type_ent.insert(0, "In") #Displays In since this is for the clock in button       
btn=Button(win,text="Clock In", width=10,height=5,command=clock_in)
btn.grid(row=1,column=0)

#This is for the clock out button and function descibing in comment block above
def clock_out(): #function of the button
    date_ent.delete(0,END) #This block of deletes wipes the entry boxes to allow clean new data on each button press
    time_ent.delete(0,END)
    type_ent.delete(0,END)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") #Grabbing time and date to update the label with
    label_clock_in = Label(win,font=alt_font, text="Clocked out at "+ current_time) #Display clock out time 
    label_clock_in.place(x=10, y=100)
    tkinter.messagebox.showinfo("Completed","You clocked out at "+ current_time) #Display pop up box with same info
    date_ent.insert(0, current_date.strftime("%m/%d/%y")) #Pulls the date from current_date function and formats it
    time_ent.insert(0, current_time) #Pulls current time in UTC, could use formatting, not sure how
    type_ent.insert(0, "Out") #Displays Out since this is for the clock out button       
btn=Button(win,text="Clock Out", width=10,height=5,command=clock_out)
btn.grid(row=1,column=1)
'''
All the following is to set up entry fields to put the relevant info in and add it to a list
and save to csv
'''
#Function adds the data in the entry boxes to a list
def Add():
   lst=[date_ent.get(),time_ent.get(),type_ent.get()]
   main_lst.append(lst)
   messagebox.showinfo("Information","Data added")

#Function to save the file
def Save():
   with open('time_keeper_export-%s.csv'%datetime.now().strftime('%Y-%m-%d'),"w") as file: #Will save the file with timestamp in same folder
      Writer=writer(file)
      Writer.writerow(["Date","Time","Type"])
      Writer.writerows(main_lst)
      messagebox.showinfo("Information","Saved succesfully")

#Clears the entry fields
def Clear():
   date_ent.delete(0,END)
   time_ent.delete(0,END)
   type_ent.delete(0,END)

#Gui formatting
# 3 labels, 3 buttons,3 entry fields
date_lbl=Label(win,text="Date: ",padx=20,pady=10)
time_lbl=Label(win,text="Time: ",padx=20,pady=10)
type_lbl=Label(win,text="In or Out: ",padx=20,pady=10)

date_ent=Entry(win,width=30,borderwidth=3)
time_ent=Entry(win,width=30,borderwidth=3)
type_ent=Entry(win,width=30,borderwidth=3)

save=Button(win,text="Save",padx=20,pady=10,command=Save)
add=Button(win,text="Add",padx=20,pady=10,command=Add)
clear=Button(win,text="Clear",padx=18,pady=10,command=Clear)
Exit=Button(win,text="Exit",padx=20,pady=10,command=win.quit)

date_lbl.grid(row=7,column=0)
time_lbl.grid(row=8,column=0)
type_lbl.grid(row=9,column=0)

date_ent.grid(row=7,column=1)
time_ent.grid(row=8,column=1)
type_ent.grid(row=9,column=1)
save.grid(row=20,column=1,columnspan=2)
add.grid(row=21,column=1,columnspan=2)
clear.grid(row=22,column=1,columnspan=2)
Exit.grid(row=23,column=1,columnspan=2)
#End Gui formatting

my_time() #loop for the time clock to keep updating
win.mainloop() #running the loop that works as a trigger
#These last 2 statements were part of some copied code, not sure what if anything they do- commented them out for now, no effect it seems
#print(lst)
#print(main_lst)