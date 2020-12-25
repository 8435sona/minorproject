from tkinter import*
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Shopping Bill Software")
        bg_color="#074463"
        title=Label(self.root,text="Shopping Bill Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #*******Variables*******
        #*******Cosmetics*******
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()
        #*******Grocery*******
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #*******Vegetable*******
        self.potato=IntVar()
        self.garlic=IntVar()
        self.tomato=IntVar()
        self.onion=IntVar()
        self.coriander=IntVar()
        self.ginger=IntVar()

        #*******Total Product Price & Tax Variables*******
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.vegetable_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.vegetable_tax=StringVar()

        #*******Customer*******
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        self.search_bill=StringVar()
        

        #******Customer Details Frame*******
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)


        #*******Cosmetics Frame*******
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_wash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_Wash_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_gel_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_gel_txt=Entry(F2,width=10,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_lotion_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_lotion_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        
        #*******Grocery Frame*******
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #*******Vegetables*******
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Vegetables",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        v1_lbl=Label(F4,text="Potato",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        v1_txt=Entry(F4,width=10,textvariable=self.potato,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        v2_lbl=Label(F4,text="Garlic",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        v2_txt=Entry(F4,width=10,textvariable=self.garlic,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        v3_lbl=Label(F4,text="Tomato",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        v3_txt=Entry(F4,width=10,textvariable=self.tomato,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        v4_lbl=Label(F4,text="Onion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        v4_txt=Entry(F4,width=10,textvariable=self.onion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        v5_lbl=Label(F4,text="Coriander",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        v5_txt=Entry(F4,width=10,textvariable=self.coriander,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        v6_lbl=Label(F4,text="Ginger",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        v6_txt=Entry(F4,width=10,textvariable=self.ginger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #*******Bill Area*******
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #*******Button Frame*******
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=325,height=140)
        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Vegetable Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.vegetable_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.grocery_tax,bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Vegetable Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.vegetable_tax,bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=720,width=605,height=105)

        total_btn=Button(btn_F,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=11,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        Gbill_btn=Button(btn_F,text="Generate Bill",bg="cadetblue",fg="white",bd=2,pady=15,width=11,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)





root=Tk()
obj=Bill_App(root)
root.mainloop()
