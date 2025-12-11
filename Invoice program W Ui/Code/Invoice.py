from PyQt5.QtWidgets import *
from Code.Buttons import connect_buttons_Invoice
import subprocess,mimetypes,smtplib,os
from email.message import EmailMessage
from pathlib import Path
from Code.PDF_Creator import create_invoice_pdf as pdf_make
from tkinter import *
from tkinter import messagebox
import time

all_clean = []

class Invoice(QDialog):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        self.personal_data = []
        self.selected_clean = []
        connect_buttons_Invoice(self)
        self.validate_create()
        self.validate_delete()
        self.validate_client()
        if os.path.exists("Personal\Personal_data.txt") != True:
            messagebox.showinfo("Enter User Info","Please go to admin tab and enter your information")
            self.ui.tabWidget.setCurrentIndex(2)
        else:
            with open("Personal\Personal_data.txt","r") as personal_data_list:
                for i in personal_data_list:
                    self.personal_data.append(i.replace("\n",""))
        print(self.personal_data)            
        

    def Add_clean(self):
        clean = []
        clean.append(str(len(all_clean)))
        clean.append(self.ui.Client_Box.currentText())
        clean.append(self.ui.No_Hrs_Box.currentText())
        clean.append(self.ui.calendarWidget.selectedDate().toString("dd/MM/yyyy"))
        clean.append(self.ui.Description.currentText())
        all_clean.append(clean)
        self.validate_create()
        
    def select_clean(self,row,col):
        self.selected_clean = []
        for column in range(self.ui.Day_table.columnCount()):
            element = self.ui.Day_table.item(row,column)
            self.selected_clean.append(element.text())
        self.validate_delete()
            
    def validate_delete(self):
        self.ui.Delete_Day.setEnabled(len(self.selected_clean) > 0)

    def validate_create(self):
        self.ui.Preview.setEnabled(len(all_clean) > 0)
        self.ui.Send.setEnabled(len(all_clean) > 0)

    def validate_client(self):
        self.ui.Add_Clean.setEnabled(self.ui.Client_Box.currentIndex() != -1)
                
    def update_table(self):
        self.ui.Day_table.setRowCount(len(all_clean))
        if len(all_clean) == 1:
            nocol = 0
            for element in all_clean[0]:
                item = QTableWidgetItem(str(element))
                self.ui.Day_table.setItem(0,nocol,item)
                nocol +=1
        elif len(all_clean) > 1:
            norow = 0
            for row in all_clean:
                nocol = 0
                for element in row:
                    field = QTableWidgetItem(str(element))   
                    self.ui.Day_table.setItem(norow,nocol,field)
                    nocol+=1
                norow+=1
        if len(all_clean) != 0:
            self.ui.Client_Box.setDisabled(True)
        else:
            self.ui.Client_Box.setDisabled(False)

    def delete_day(self):
        all_clean.remove(self.selected_clean)
        self.selected_clean = []
        self.validate_delete()
        self.update_table()
        self.validate_create()

    def read_txt_file_line(self,file,line_num):
        line_num = line_num-1 # corrects index (0=1st line)
        with open(file,) as file_content:
            for i, line in enumerate(file_content):
                if i == line_num:
                    return line
                elif i > line_num:
                    break
        file_content.close()

    def invoice_make(self):
        client_info = []
        x = 0
        with open("Clients/"+str(all_clean[0][1])+"/Base_"+str(all_clean[0][1]),"r") as client_base: # with open client/client_txt
            for i in client_base:
                if x == 6:
                    rate = i
                    break
                client_info.append(i.replace("\n",""))
                x += 1
        client_base.close()
        clients  = os.listdir("Clients/"+str(all_clean[0][1]))
        invoice_number = len(clients)
        file_path = os.path.abspath("Clients/"+str(all_clean[0][1])+"/Invoice_"+str(invoice_number)+".pdf")
        pdf_make("Clients/"+str(all_clean[0][1])+"/Invoice_"+str(invoice_number)+".pdf",client_info,invoice_number,rate,all_clean)
        if self.sender().objectName() == "Preview":
            os.startfile(file_path)
            time.sleep(0.5)
            os.remove(file_path)
        else:
            return file_path

    def send_invoice(self):
        Inovice_path = Path(self.invoice_make())
        msg = EmailMessage()
        msg['From'] = self.personal_data[5]
        msg['To'] = "aaronvdpijll@gmail.com" 
        msg['Subject'] = self.personal_data[11]
        msg.set_content(self.personal_data[12])
        smtp_server = ' '
        smtp_port = 587
        smtp_username = self.personal_data[5]
        smtp_password = ' '
        mime_type, _ = mimetypes.guess_type(Inovice_path)
        mime_type = mime_type or "application/octet-stream"
        main_type, sub_type = mime_type.split('/')
        with open(Inovice_path, 'rb') as file:
            msg.add_attachment(file.read(),
                            maintype=main_type,
                            subtype=sub_type,
                            filename=Inovice_path.name)
        file.close()
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls() 
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        server.close()