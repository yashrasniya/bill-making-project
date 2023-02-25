from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from reportlab.pdfgen import canvas
import calculation
from tkinter.ttk import *
import sqlite3, json, subprocess, sys, os


class Summit:
    def __init__(self, e1, e2, e3, e4, e5, e5_1, e6, e6_1, v_1, v_2, root, list_name):
        self.one = sqlite3.connect("one.db")
        self.cursor = self.one.cursor()
        self.entry_1 = e1
        self.entry_2 = e2
        self.entry_3 = e3
        self.entry_4 = e4
        self.entry_5 = e5
        self.entry_5_1 = e5_1
        self.entry_6 = e6
        self.entry_6_1 = e6_1

        self.cal = calculation.clculation()
        self.datetime = self.cal.time()

        self.list_name = list_name
        self.v_1 = v_1
        self.v_2 = v_2
        self.root = root
        self.ent_1 = self.entry_1.get()
        self.pdf = canvas.Canvas(f"{self.ent_1}-{self.entry_3.get()}{self.datetime}.pdf")

        self.pdf.drawImage('pdf_3.jpg', 0, 00, width=595.276, height=841.89)
        self.cal.replace(self.entry_1.get())

        self.ent_2 = self.entry_2.get().upper()
        self.ent_3 = self.entry_3.get().upper()
        self.ent_4 = self.entry_4.get().upper()
        self.ent_5 = self.entry_5.get().upper()
        self.ent_6 = self.entry_6.get().upper()
        self.ent_5_1 = self.entry_5_1.get().upper()
        self.ent_6_1 = self.entry_6_1.get().upper()

        try:
            self.cursor.execute("""CREATE TABLE histry_profile_4(invoice_num,address ,gst_num ,gst_pursanyage,name,date,product)
            """)
            self.cursor.execute("""CREATE TABLE histry_data(invoice_num,address ,gst_n um ,gst_pursanyage,name,date,product)
                        """)
        except:
            return
        finally:

            for name, qui, rate, size, list,quantity_types in self.list_name:
                with open("histry.txt", "a") as file:
                    file.write(f"\n"
                               f"                  Invoice No.      {self.ent_1} \n"
                               f"                    Invoic date    {self.ent_2} \n"
                               f"                    Name           {self.ent_3}\n"
                               f"                    addres         {self.ent_4} \n"
                               f"                    gst_in%          {self.ent_5} \n"
                               f"                    state          {self.ent_6} \n"
                               f"                    gstin          {self.ent_5_1}\n"
                               f"                    state code     {self.ent_6_1}\n"
                               f"                    name fo the pro{name}\n"
                               f"                    qui            {qui}\n"
                               f"                    rate           {rate}\n"
                               f"                    size           {size} {list[1:]}"
                               f"---------------------------------------------------------")

            self.papa = 1
            try:
                self.gst = int(self.ent_5)
                self.papa += 1
            except:
                messagebox.showerror("ERROR", "ENTER IN VALUE IN GST BOX#")
            if self.papa == 2:

                self.pdf.setFontSize(9)
                self.ent_3 = self.ent_3.upper()
                self.pdf.drawString(130, 622, self.ent_1)
                self.pdf.drawString(130, 610, self.ent_2)
                self.pdf.drawString(90, 575, self.ent_3)
                self.pdf.setFontSize(9)
                if len(self.ent_4) > 38:
                    ent_4_1 = self.ent_4[0:38]
                    ent_4_2 = self.ent_4[38:]
                    self.pdf.drawString(90, 560, ent_4_1)
                    if len(ent_4_2) > 38:
                        self.pdf.setFontSize(7)
                    self.pdf.drawString(90, 548, ent_4_2)
                    self.pdf.setFontSize(9)
                else:
                    self.pdf.drawString(90, 560, self.ent_4)

                self.pdf.drawString(90, 528, self.ent_5_1)
                self.pdf.drawString(90, 515, self.ent_6)
                self.pdf.drawString(250, 510, self.ent_6_1)
                self.pdf.drawString(129, 600, "UTTARAKHAND")
                self.pdf.drawString(250, 600, "05")

                self.prooses()

    def prooses(self):
        y = 452
        num = 1
        totel = 0
        for list, qty, rate, size, list_sq, list_qun in self.list_name:

            rate_type = ""
            quantity = ""
            for types in list_sq[1:]:
                rate_type += f" {types} "
            for types in list_qun[1:]:
                quantity += f"{types}"
            amount = size * (qty * rate)
            totel += amount
            qty = str(qty)
            rate = str('%.2f' % rate)
            num_1 = str(num)
            self.pdf.drawString(55, y, str(num))
            if len(list) > 60:
                list_1 = list[0:40]
                list_2 = list[40:]
                self.pdf.drawString(80, y, list_1)
                y -= 15
                self.pdf.drawString(80, y, list_2)
                if len(f"{qty} {quantity}") > 11:
                    self.pdf.setFontSize(7)
                self.pdf.drawString(372, y, f"{qty} {quantity}")
                self.pdf.setFontSize(9)
                if len(f"{rate}/-{rate_type}") > 11:
                    self.pdf.setFontSize(7)
                self.pdf.drawString(427, y, f"{rate}/-{rate_type}")
                self.pdf.setFontSize(9)
                self.pdf.drawString(482, y, f"{str('%.0f' % amount)}/-")

            else:
                self.pdf.drawString(80, y, list)
                if len(f"{qty} {quantity}") > 11:
                    self.pdf.setFontSize(7)
                self.pdf.drawString(372, y, f"{qty} {quantity}")
                self.pdf.setFontSize(9)
                if len(f"{rate}/-{rate_type}") > 11:
                    self.pdf.setFontSize(7)
                self.pdf.drawString(427, y, f"{rate}/-{rate_type}")
                self.pdf.setFontSize(9)
                self.pdf.drawString(482, y, f"{str('%.0f' % amount)}/-")

            y -= 15
            num += 1

        self.pdf.drawString(482, 190, f"{str('%.0f' % totel)}/-")

        gst_va = totel * (self.gst / 100)
        all_totel = int(round(totel + gst_va))

        all_totel_str = str("%.0f" % all_totel)
        print("'%.0f'" % gst_va)
        gst_va_str = str("%.0f" % gst_va)
        self.pdf.drawString(482, 150, f"{gst_va_str} /-")
        self.pdf.drawString(482, 130, f"{all_totel_str} /-")

        word = self.cal.num2words(all_totel)
        if len(word + "only") > 44:
            word_1 = word.split(" ")[0:6]
            n = ""
            for word_1 in word_1:
                n = n + " " + word_1 + " "
            word_2 = word.split(" ")[6:]
            m = ""
            for word_2 in word_2:
                m = m + " " + word_2 + " "
            self.pdf.drawString(175, 173, f"{n} ")
            if len(word_1) > 60:
                self.pdf.setFontSize(7)
            self.pdf.drawString(50, 156, f"{m} only")
        else:

            self.pdf.drawString(180, 173, f"{word} only")
        self.add(gst_va)

        list_mane = json.dumps(self.list_name)
        self.cursor.execute(
            f"""INSERT INTO histry_profile_4 VALUES (:invoice_num,:address,:gst_num ,:gst_in_num,:name,:invoice_date,:product)""",
            {"invoice_num": self.ent_1,
             "address": self.ent_4,
             "gst_num": self.ent_5_1,
             "gst_in_num": self.ent_5,
             "name": self.ent_3,
             "invoice_date": self.ent_2,
             "product": list_mane})
        self.one.commit()
        self.one.close()

        if self.papa == 2:

            num=calculation.clculation.replace(calculation.clculation(), self.ent_1)
            if num==1:
                return

            jaja = filedialog.askdirectory()
            if jaja== "":
                messagebox.showerror("ERROR", " Give directory!")
                return
            try:
                os.chdir(jaja)
                self.pdf.save()
                self.root.destroy()

                subprocess.Popen(f"{self.ent_1}-{self.entry_3.get()}{self.datetime}.pdf")
            except:
                print(str(sys.exc_info()))
                return
        else:
            return

    def add(self, gst):
        gst_va_haff = gst / 2
        gst_va_haff_str = str("%.0f" % gst_va_haff)

        gst = int(self.ent_5)
        gst_div = gst / 2
        gst_str = str(gst_div)
        gst_str = str(gst / 2)
        print(gst_str)
        self.pdf.drawString(160, 202, f"{gst_va_haff_str}")
        self.pdf.drawString(90, 202, f"{gst_va_haff_str}")
        self.pdf.drawString(113, 216, f"{gst_str}")
        self.pdf.drawString(183, 216, f"{gst_str}")


class Show:
    def __init__(self, e1, e2, e3, e4, e5, e5_1, e7, e8, e8_1, e9, oid):
        self.entry_1 = e1

        self.entry_2 = e2
        self.entry_3 = e3
        self.entry_4 = e4
        self.entry_5 = e5
        self.entry_5_1 = e5_1
        self.entry_7 = e7
        self.entry_8 = e8
        self.entry_8_1 = e8_1
        self.entry_9 = e9
        self.entry_oid = oid
        self.histryshow()

    def histryshow(self):
        m = 0
        oid = self.entry_oid.get()

        one = sqlite3.connect("one.db")
        cursor = one.cursor()
        cursor.execute(f"SELECT oid FROM histry_profile_4 ")
        number = cursor.fetchall()

        if not f"{oid}," in f"{str(number)}":
            messagebox.showerror("ERROR", "ENTER IN VALUE IN oid num BOX#")
            return
        else:
            m += 1

        cursor.execute(f"SELECT * FROM histry_profile_4 WHERE oid=:oid",
                       {"oid": oid}
                       )
        value = cursor.fetchall()
        self.entry_1.delete(0, last=1000)
        self.entry_4.delete(0, last=1000)
        self.entry_5_1.delete(0, last=1000)
        self.entry_5.delete(0, last=1000)
        self.entry_3.delete(0, last=1000)
        self.entry_2.delete(0, last=1000)
        for value in value:
            self.entry_4.insert(0, value[1])
            self.entry_5_1.insert(0, value[2])
            self.entry_5.insert(0, value[3])
            self.entry_3.insert(0, value[4])
            self.entry_2.insert(0, value[5])

        row = 1
        num = 1
        try:
            joky = json.loads(value[6])
            self.root_1 = Tk()
            size = "200"
            if len(json.loads(value[6])) > 5:
                size = str(200 + (20 * len(json.loads(value[6]))))
            self.root_1.geometry(f"200x{size}")

            m += 1
            label_show = Label(self.root_1, text="S.No")
            label_show_1 = Label(self.root_1, text="Name")

            label_show_2 = Label(self.root_1, text="Qty")
            label_show_3 = Label(self.root_1, text="Rate")
            label_show_4 = Label(self.root_1, text="size")
            label_show.grid(row=0, column=0)
            label_show_1.grid(row=0, column=1)
            label_show_2.grid(row=0, column=2)
            label_show_3.grid(row=0, column=3)
            label_show_4.grid(row=0, column=4)
            list_k = 0
            for ks in json.loads(value[6]):
                print(ks)
                label = Button(self.root_1, text=f"{num}",command=lambda index=num-1: self.happy(joky,index))
                label.grid(row=row, column=0)
                label = Label(self.root_1, text=f"{ks[0]}")
                label.grid(row=row, column=1)
                label = Label(self.root_1, text=f"{ks[1]}")
                label.grid(row=row, column=2)
                label = Label(self.root_1, text=f"{ks[2]}")
                label.grid(row=row, column=3)
                label = Label(self.root_1, text=f"{ks[3]}")

                label.grid(row=row, column=4)
                row += 1
                list_k += 1
                num += 1
        except:
            messagebox.showerror("ERROR", "ENTER IN VALUE IN oid num BOX#")
            return
        label_show_4 = Label(self.root_1, text="Num:-")
        label_show_4.grid(row=row, column=0)

        self.entry_rate = Entry(self.root_1)
        self.entry_rate.grid(row=row, column=1, columnspan=5)
        but = Button(self.root_1, text="show", command=lambda: self.happy(joky))
        but.grid(row=row + 1, column=1)
        one.commit()
        one.close()
        if m == 2:
            self.root_1.mainloop()

    def happy(self, value,index=None):

        print(value)
        try:
            if index is None:
                get = int(self.entry_rate.get()) - 1
            else:
                get=index

            print(get)
            if len(value) < get:
                messagebox.showerror("ERROR", "ENTER WRITE VALUE")

            self.entry_7.delete(0, 1000)
            self.entry_8.delete(0, 1000)
            self.entry_8_1.delete(0, 1000)
            self.entry_9.delete(0, 1000)

            self.entry_7.insert(0, str(value[get][0]))
            self.entry_8.insert(0, str(value[get][1]))
            self.entry_9.insert(0, str(value[get][2]))
            self.entry_8_1.insert(0, str(value[get][3]))




        except TypeError:
            messagebox.showerror("ERROR", "ENTER WRITE VALUE")
        finally:
            self.root_1.destroy()
import tkinter as tk
class showing_all_data:
    def __init__(self,e1, e2, e3, e4, e5, e5_1, e7, e8, e8_1, e9, oid,root):
        self.entry_1 = e1

        self.entry_2 = e2
        self.entry_3 = e3
        self.entry_4 = e4
        self.entry_5 = e5
        self.entry_5_1 = e5_1
        self.entry_7 = e7
        self.entry_8 = e8
        self.entry_8_1 = e8_1
        self.entry_9 = e9
        self.entry_oid = oid
        self.root=root
        self.main()

    def main2(self):
        one = sqlite3.connect("one.db")
        cursor = one.cursor()
        try:
            cursor.execute(f"SELECT * FROM histry_profile_4 " )

            self.value = cursor.fetchall()
        except:
            self.value=[]


    def printing_value_in_entryBox(self,value,root):
        f1 = tk.Frame(root).grid(row=16, column=3,columnspan=2)
        canvas = tk.Canvas(f1, borderwidth=0, background="#ffffff",height=100,width=290)
        frame = tk.Frame(canvas, background="#ffffff")
        vsb = tk.Scrollbar(f1, orient="vertical", command=canvas.yview, width=20)
        canvas.configure(yscrollcommand=vsb.set)

        # vsb.pack(side="right", fill="y")
        vsb.grid(row=16, column=2, sticky='NSW')
        # canvas.pack(side="left", fill="both", expand=True)
        canvas.grid(row=16, column=0,columnspan=2)
        canvas.create_window((4, 4), window=frame, anchor="nw")

        frame.bind("<Configure>", lambda event, canvas=canvas: self.onFrameConfigure(canvas))
        num=1
        column=1
        row=1
        b=[i for i in value[:6]]
        b.append("All")
        c=Combobox(frame,value=b)
        c.grid(row=0,column=1)
        c.bind('<<ComboboxSelected>>',lambda x:self.headChange(c.get(),value[:6]))
        print(value[:5])
        for ks in json.loads(value[6]):
            print(ks,"ks")

            label = Button(frame, text=f"{ks[0]}",width=20, command=lambda index=num - 1: self.changing_all_values(value, index))
            label.grid(row=row, column=column)
            if column%4==0:
                row=row+1
            row=row+1
            num=num+1
    def headChange(self,value,list):

        entry_array=[ self.entry_1,
        self.entry_4,
        self.entry_5_1,
        self.entry_5,
        self.entry_3,
        self.entry_2
    ]
        k=0
        if value=="All":
            for i in entry_array:
                i.delete(0, last=1000)
                i.insert(0,list[k] )
                k+=1
            return
        index = list.index(value)
        entry_array[index].delete(0,last=1000)
        entry_array[index].insert(0,value)
    def changing_all_values(self,full_arry,index_number):
        self.entry_1.delete(0, last=1000)
        self.entry_4.delete(0, last=1000)
        self.entry_5_1.delete(0, last=1000)
        self.entry_5.delete(0, last=1000)
        self.entry_3.delete(0, last=1000)
        self.entry_2.delete(0, last=1000)
        self.entry_7.delete(0, 1000)
        self.entry_8.delete(0, 1000)
        self.entry_8_1.delete(0, 1000)
        self.entry_9.delete(0, 1000)


        self.entry_4.insert(0, full_arry[1])
        self.entry_5_1.insert(0, full_arry[2])
        self.entry_5.insert(0, full_arry[3])
        self.entry_3.insert(0, full_arry[4])
        self.entry_2.insert(0, full_arry[5])
        full_arry=json.loads(full_arry[6])
        self.entry_7.insert(0, str(full_arry[index_number][0]))
        self.entry_8.insert(0, str(full_arry[index_number][1]))
        self.entry_9.insert(0, str(full_arry[index_number][2]))
        self.entry_8_1.insert(0, str(full_arry[index_number][3]))

    def populate(self,frame_, row,v,root):
        '''Put in some fake data'''
        tk.Button(frame_,text=f"{str(self.value[v][0])[0:10]} {self.value[v][4]}",width=40,command=lambda x=self.value[v]:self.printing_value_in_entryBox(x,root)).grid(row=row[-1], column=0)
        row.append(row[-1] + 1)

    def onFrameConfigure(self,canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))
    def main(self):

        f = tk.Frame(self.root).grid(row=15, column=3,columnspan=2)
        canvas = tk.Canvas(f, borderwidth=0, background="#ffffff",height=200,width=260)
        frame = tk.Frame(canvas, background="#ffffff")
        vsb = tk.Scrollbar(f, orient="vertical", command=canvas.yview, width=20)
        canvas.configure(yscrollcommand=vsb.set)

        # vsb.pack(side="right", fill="y")
        vsb.grid(row=15, column=2,columnspan=1 ,sticky='NSW',padx=25)
        # canvas.pack(side="left", fill="both", expand=True)
        canvas.grid(row=15, column=2,columnspan=2,padx=20,rowspan=2)
        canvas.create_window((4, 4), window=frame, anchor="nw")

        frame.bind("<Configure>", lambda event, canvas=canvas: self.onFrameConfigure(canvas))
        row = [1]
        # tk.Button(f, command=lambda: self.populate(frame, row), text="press").grid(row=4)
        self.main2()
        for v in range(len(self.value)):
            self.populate(frame, row,v,self.root)

# e1, e2, e3, e4, e5, e5_1, e7, e8, e8_1, e9, oid=0,0,0,0,0,0,0,0,0,0,0
# jaj=showing_all_data(e1, e2, e3, e4, e5, e5_1, e7, e8, e8_1, e9, oid)
