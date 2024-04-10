from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from product import productClass
import sqlite3
from tkinter import messagebox
import time
class IMS:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1400x700+0+0")
        self.root.title("Inventory Control System | Developed by Aditee,Aayush,Tanaya")
        self.root.config(bg="white")
        
        #Title
        self.icon_title=PhotoImage(file="Images/logo.png")
        title=Label(self.root,text="Inventory Control System",image=self.icon_title,compound=LEFT,font=("Footlight MT Light",40),bg="#281c7c",fg="white").place(x=0,y=0,relwidth=1,height=70)

        #Intro line
        self.intro=Label(self.root,text="Welcome to Inventory Control System !  |   This system has been developed by Team Aditee, Aayush, Tanaya",font=("Footlight MT Light",15),bg="#4a93f9",fg="white")
        self.intro.place(x=0,y=70,relwidth=1,height=30)

        #Left Menu
        self.MenuLogo=Image.open("Images/Menu.png")
        self.MenuLogo=self.MenuLogo.resize((250,250),Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE)
        LeftMenu.place(x=0,y=102,width=300,height=660)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        #Menu & Functionalities
        self.icon_side=PhotoImage(file="Images/pointer.png")     

        lbl_menu=Label(LeftMenu,text="Menu",font=("Footlight MT Light",20,"bold"),bg="#4a93f9",fg="white").pack(side=TOP,fill=X)
        
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=25,anchor="w",font=("Footlight MT Light",20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=25,anchor="w",font=("Footlight MT Light",20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",command=root.destroy,image=self.icon_side,compound=LEFT,padx=25,anchor="w",font=("Footlight MT Light",20,"bold"),bg="white",fg="black",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #Functionality Counters
        self.lbl_employee=Label(self.root,text="Total Employees\n[ 0 ]",bd=5,relief=RIDGE,bg="#0000FF",fg="white",font=("Footlight MT Light",20,"bold"))
        self.lbl_employee.place(x=550,y=130,height=250,width=400)

        self.lbl_product=Label(self.root,text="Total Products\n[ 0 ]",bd=5,relief=RIDGE,bg="#A020F0",fg="white",font=("Footlight MT Light",20,"bold"))
        self.lbl_product.place(x=550,y=400,height=250,width=400)

        #Footer
        lbl_footer=Label(self.root,text="Inventory Control System | DBMS Project\n Artificial Intelligence & Data Science",font=("Footlight MT Light",13),bg="#281c7c",fg="white").pack(side=BOTTOM,fill=X)

        self.update_content()
#=================================================================================================================================================================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
    
#=======================new========================
    
    def update_content(self):
        con=sqlite3.connect(database=r'ics.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n[{str(len(employee))}]')

            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[{str(len(product))}]')
           
    
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    


if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()