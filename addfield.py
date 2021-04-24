import Tkinter as tk
import arcpy



def addfield():
    input_layer = e1.get()
    field_name = e2.get()
    arcpy.AddField_management(input_layer,field_name,"TEXT")

master = tk.Tk()
master.geometry("300x300")
tk.Label(master, 
         text="Layin yolu").grid(row=0)
tk.Label(master, 
         text="Sutunun adi").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


tk.Button(master, 
          text='Add Field', command=addfield).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()
