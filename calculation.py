import sqlite3

from tkinter import messagebox
import sys
class clculation:
    def __index__(self):
        self.list_nane = []
        return

    def creattabel(self):
        one = sqlite3.connect("one.db")
        cursor = one.cursor()

        cursor.execute("CREATE TABLE billnum(billnum)")
        one.commit()
        one.close()

    def string_upper_converter(self, string):
        string_list = string.split(" ")
        string_upper = ""
        for word in string_list:
            if type(word) == str and word != "":
                word_fist = f"{word[0]}".upper()
            elif word!="":
                word_fist = word[0]
            else:
                word_fist=""
            string_upper = f"{string_upper}{word_fist}{word[1:]} "
        return string_upper

    def openfile(self):
        one = sqlite3.connect("one.db")
        cursor = one.cursor()
        cursor.execute("INSERT INTO billnum VALUES(200)")
        one.commit()
        one.close()

    def shownum(self):
        one = sqlite3.connect("one.db")
        cursor = one.cursor()
        cursor.execute("SELECT * FROM billnum WHERE oid=1")
        num = cursor.fetchall()

        for num in num:
            num = num[0]
            num = 1 + num
        one.commit()
        one.close()
        return num

    def replace(self, num):
        num = num.split(" ")
        one = sqlite3.connect("one.db")
        cursor = one.cursor()
        try:
            cursor.execute(F"""UPDATE billnum SET billnum= {num[0]} WHERE oid=oid""")
        except sqlite3.OperationalError:
            comma = '\''
            messagebox.showerror(f"{str(sys.exc_info()).split(comma)[1]}", f"{str(sys.exc_info()).split(',')[1]}{str(sys.exc_info()).split(',')[2]}")
            return 1


        one.commit()
        one.close()
        return 0

    def time(self):
        global datetime, date
        import datetime
        datetime_1 = datetime.datetime.now()
        datetime_1 = str(datetime_1)
        date = datetime_1[0:10]
        time = datetime_1[11:19]
        time = time.replace(":", "")
        date_r = ""
        for date_list in date.split("-"):
            date_r = date_list + date_r

        date_1 = date.replace("-", "")
        return f"{date_r}{time}"

    def num2words(self, num):
        under_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                    'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        above_100 = {100: 'Hundred', 1000: 'Thousand', 100000: 'Lack', 10000000: 'Crore'}

        if num < 20:
            return under_20[num]

        if num < 100:
            return tens[(int)(num / 10) - 2] + ('' if num % 10 == 0 else ' ' + under_20[num % 10])

        # find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550
        pivot = max([key for key in above_100.keys() if key <= num])

        return self.num2words((int)(num / pivot)) + ' ' + above_100[pivot] + (
            '' if num % pivot == 0 else ' ' + self.num2words(num % pivot))

    def show(self):
        oid = input("enter a oid num: ")

        one = sqlite3.connect("one.db")
        cursor = one.cursor()
        cursor.execute(f"SELECT * FROM data WHERE oid=:oid",
                       {"oid": oid}
                       )
        value = cursor.fetchall()
        list = ["invoicenum", "date", "gst", "gstin"]
        xyz = 0

    def gemometry(self, pdf):
        pdf.line(100, 10, 100, 800)
        pdf.line(200, 10, 200, 800)
        pdf.line(300, 10, 300, 800)
        pdf.line(400, 10, 400, 800)
        pdf.line(500, 10, 500, 800)
        pdf.line(600, 10, 600, 800)
        pdf.line(700, 10, 700, 800)
        pdf.line(800, 10, 800, 800)
        pdf.line(900, 10, 900, 800)

        pdf.line(10, 100, 500, 100)
        pdf.line(10, 200, 500, 200)
        pdf.line(10, 300, 500, 300)
        pdf.line(10, 400, 500, 400)
        pdf.line(10, 500, 500, 500)
        pdf.line(10, 600, 500, 600)
        pdf.line(10, 700, 500, 700)
        pdf.line(10, 800, 500, 800)
        pdf.line(10, 900, 500, 900)
