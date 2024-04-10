import sqlite3
from tkinter import *
from tkinter import messagebox, ttk

from PIL import Image, ImageTk


class productClass:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1222x620+300+125")
        self.root.title("Inventory Control System | Developed by Aditee,Aayush,Tanaya")
        self.root.config(bg="white")
        self.root.focus_force()

        #=========ALL VARIABLES
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_pid=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()




        product_Frame=Frame(self.root,bd=2, relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450, height=480)
        
        title=Label(product_Frame,text="Product Details",font=("Footlight MT Light",18),bg="#0f4d7d",fg="white").pack(side=TOP, fill=X)
        lbl_product_name=Label(product_Frame,text="Name",font=("Footlight MT Light",18),bg="white").place(x=30, y=110)
        lbl_price=Label(product_Frame,text="Price",font=("Footlight MT Light",18),bg="white").place(x=30, y=160)
        lbl_quantity=Label(product_Frame,text="Quantity",font=("Footlight MT Light",18),bg="white").place(x=30, y=210)
        lbl_status=Label(product_Frame,text="Status",font=("Footlight MT Light",18),bg="white").place(x=30, y=260)


        txt_name=Entry (product_Frame,textvariable=self.var_name,font=("Footlight MT Light",15),bg='lightyellow').place(x=150, y=110, width=200)
        txt_price=Entry (product_Frame,textvariable=self.var_price,font=("Footlight MT Light",15),bg='lightyellow').place(x=150, y=160, width=200)
        txt_qty=Entry (product_Frame,textvariable=self.var_qty,font=("Footlight MT Light",15),bg='lightyellow').place(x=150, y=210, width=200)

        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Available","Unavailable"),state='readonly',justify=CENTER,font=("Footlight MT Light",15))
        cmb_status.place(x=150, y=260, width=200)
        cmb_status.current(0)


        #Button
        btn_add=Button(product_Frame,text="Save",command=self.add,font=("Footlight MT Light",15),bg="#9505E3",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("Footlight MT Light",15),bg="#9505E3",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("Footlight MT Light",15),bg="#9505E3",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("Footlight MT Light",15),bg="#9505E3",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)
   


        #Search Frame
        SearchFrame=LabelFrame(self.root,text="Search Product",font=("Footlight MT Light",12),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #Options
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Name","Pid","Price"),state='readonly',justify=CENTER,font=("Footlight MT Light",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("Footlight MT Light",15),bg="#D3F4FB")
        txt_search.place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("Footlight MT Light",15),bg="#9505E3",fg="white",cursor="hand2")    
        btn_search.place(x=435,y=7,width=150,height=30)


        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(p_frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        
        self.product_table.heading("pid",text="PID")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="Qty")
        self.product_table.heading("status",text="Status")
        
        self.product_table["show"]="headings"

        self.product_table.column("pid",width=60)
        self.product_table.column("name",width=150)
        self.product_table.column("price",width=90)
        self.product_table.column("qty",width=150)
        self.product_table.column("status",width=70)
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()


    
    
    


    def add(self):
        con=sqlite3.connect(database=r'ics.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product where name=?",(self.var_name.get(),))
            cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
            cur.execute("Select * from product where price=?",(self.var_price.get(),))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","Product already available", parent=self.root)
            else:
                cur.execute("Insert into product (name , price , qty , status ) values(?,?,?,?)",(
                                            self.var_name.get(),
                                            self.var_price.get(),
                                            self.var_qty.get(),   
                                            self.var_status.get(),
                                            ))
                con.commit()
                messagebox.showinfo("Success","Product added successfully!",parent=self.root)
                self.show()    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    

    def show(self):
        con=sqlite3.connect(database=r'ics.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_name.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.var_status.set(row[4])
                                              

    def update(self):
        con=sqlite3.connect(database=r'ics.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select product",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ID")
                else:
                    cur.execute("Update product set name=?,price=?,qty=?,status=? where pid=?",(
                                                self.var_name.get(),
                                                self.var_price.get(),
                                                self.var_qty.get(),                                            
                                                self.var_status.get(),
                                                self.var_pid.get()
                          
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product updated successfully!",parent=self.root)
                    self.show()    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ics.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select product from the list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid PID")
                else:
                    op=messagebox.askyesno("Confirmation","Do you wish to confirm deletion?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("","Product deleted successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def clear(self):
        self.var_pid.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Select")

        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ics.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input is required",parent=self.root)

            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)

                else:
                    messagebox.showerror("Error","No record found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)







if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()