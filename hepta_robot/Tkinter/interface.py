# coding: utf-8
import os
from tkinter import *
from tkinter import messagebox
import sys
import subprocess as sub
import tkinter
import tkinter.font as font

def Destination():
    global point_input
    point_input = e1.get()
    print(point_input)
    sub.run(['python', '/home/chames/catkin_ws/src/pfe_robot/move_alone/test_nav.py','-p', point_input])
    messagebox.showinfo('Destination', 'Destination reached successfully!')

def boutonFourreTout():

    fenetre.destroy()

    return(0)


fenetre = Tk()
fenetre.geometry('500x500')
fenetreBackground=PhotoImage(file = "/home/chames/catkin_ws/src/pfe_robot/hepta_robot/Tkinter/hepta.png")
#bg = PhotoImage(file = "/home/chames/catkin_ws/src/pfe_robot/hepta_robot/Tkinter/hepta.png")
canvas1 = Canvas( fenetre, width = 400,
                 height = 400)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 1, 0, image = fenetreBackground, 
                     anchor = "nw")
fenetre.title("Hepta Software Solution")
myFont = font.Font(family='Batang')
myFont2 = font.Font(family='Vani', size=30 )

label = Label(fenetre,font=myFont2, text="Hepta ROS")
label.pack()
zone_1 = Frame(fenetre, bg='black')
zone_1.pack(fill=Y, padx=0,pady=90)
zone_2 = Frame(fenetre, bg='black')
zone_2.pack(fill=Y, padx=10,pady=5)

bt1 = Button(zone_1,font = myFont, text="Hepta SLAM", fg="blue", bg="#5dbb00", command = lambda: sub.call('/home/chames/catkin_ws/src/pfe_robot/scripts/SLAM_hepta.sh'))
bt2 = Button(zone_1,font = myFont, text="MAP SAVER", fg="blue", bg='#5dbb00',  command = lambda: sub.run(['rosrun', 'map_server','map_saver' ,'-f', 'SimpleMap']))
bt3 = Button(zone_1,font = myFont,text="RUN", fg="white", bg='#BBBB99', command = lambda: sub.call('/home/chames/catkin_ws/src/pfe_robot/scripts/GO_hepta.sh'))
bt4 = Button(zone_1, text="Emergency Stop", fg="black", bg="red", command = lambda : sub.call('rosnode kill -a ', shell=True) )
Label(fenetre, text="Table number").pack(side=LEFT, fill=X, ipady=30, padx=2,pady=3)
e1 = Entry(fenetre)
e1.pack(side=LEFT, fill=Y, ipady=10, padx=10,pady=10)
btn=Button(fenetre,text="Destination", fg="white",bg="#bbbb00", command= Destination)
btn.pack(fill=Y, padx=30,pady=15)
bt1.pack(side=LEFT, fill=Y, ipady=30, padx=10,pady=10)
bt2.pack(side=RIGHT, fill=Y, ipady=30, padx=10,pady=10)
bt3.pack(side=LEFT, fill=Y, ipady=30, padx=10,pady=10)
bt4.pack(fill=X, ipady=30,padx=10,pady=10)
btn.pack(side= LEFT, padx=30,pady=15)


button1=tkinter.Button(zone_2, text="Table 1", fg="white",bg="#bbbb00",command = lambda:sub.run(['python', '/home/chames/catkin_ws/src/pfe_robot/move_alone/test_nav.py','-p', '2']))
button1.grid(row=1,column=0, padx=5, pady=5)

button2=tkinter.Button(zone_2, text="Table 2", fg="white",bg="#bbbb00",command = lambda:sub.run(['python', '/home/chames/catkin_ws/src/pfe_robot/move_alone/test_nav.py','-p', '3']))
button2.grid(row=1,column=1, padx=5, pady=5)

button3=tkinter.Button(zone_2, text="Table 3", fg="white",bg="#bbbb00",command = lambda:sub.run(['python', '/home/chames/catkin_ws/src/pfe_robot/move_alone/test_nav.py','-p', '4']))
button3.grid(row=1,column=2, padx=5, pady=5)

button4=tkinter.Button(zone_2, text="Table 4", fg="white",bg="#bbbb00",command = lambda:sub.run(['python', '/home/chames/catkin_ws/src/pfe_robot/move_alone/test_nav.py','-p', '5']))
button4.grid(row=2,column=0, padx=5, pady=5)

button5=tkinter.Button(zone_2, text="Table 5", fg="white",bg="#bbbb00",command = lambda:sub.run(['python', '/home/chames/catkin_ws/src/pfe_robot/move_alone/test_nav.py','-p', '6']))
button5.grid(row=2,column=1, padx=5, pady=5)

button6=tkinter.Button(zone_2, text="Table 6", fg="white",bg="#bbbb00",command = lambda:sub.run(['python', '/home/chames/catkin_ws/src/pfe_robot/move_alone/test_nav.py','-p', '7']))
button6.grid(row=2,column=2, padx=5, pady=5)

button7=tkinter.Button(zone_2, text="Parc", fg="white",bg="#bbbb00",command = lambda:sub.run(['python', '/home/chames/catkin_ws/src/pfe_robot/move_alone/test_nav.py','-p', '1']))
button7.grid(row=3,column=1, padx=5, pady=5)


fenetre.mainloop()