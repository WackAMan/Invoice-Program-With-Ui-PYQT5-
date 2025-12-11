import os
from PyQt5.QtWidgets import *
from Code.Buttons import connect_buttons_client
from pathlib import Path

class Client(QDialog):
    def __init__(self,ui):
        super().__init__()
        print(ui,"ui")
        self.ui = ui
        self.selected_clean = []
        connect_buttons_client(self)    
        self.refresh_combos()

    def refresh_combos(self):
        self.ui.Client_Box.clear()
        self.ui.edit_client_dropdown.clear()
        with open("Personal\Client_List.txt","r") as client_list:
            lines = client_list.readlines()
            for line in lines:
                line = line.replace("\n","")
                self.ui.Client_Box.addItem(line)
                self.ui.edit_client_dropdown.addItem(line)
        self.ui.Client_Box.setCurrentIndex(-1)
        self.ui.edit_client_dropdown.setCurrentIndex(-1)
        
    def goto_add_client(self):
        self.ui.Client_pages.setCurrentIndex(0)
        self.add_client_valid()
    
    def goto_edit_client(self):
        self.ui.Client_pages.setCurrentIndex(1)

    def goto_add_delete_client(self):
        self.ui.Client_pages.setCurrentIndex(2)

    def presence_check(self,widgets):
        valid = []
        if isinstance(widgets,list):
            for i in widgets:
                if len(i.toPlainText()) > 0:
                    valid.append(1)
                else:
                    valid.append(0)
        else:
            if len(i.toPlainText()) > 0:
                valid.append(1)
            else:
                valid.append(0)
        return all(valid)

    def add_client_valid(self):
        widgets = [self.ui.full_name_txt,self.ui.address_txt,self.ui.town_txt,
                   self.ui.country_txt,self.ui.postcode_txt,self.ui.email_txt,self.ui.wage_txt]
        if self.presence_check(widgets) == True:
            self.ui.add_client_btn.setEnabled(True)
        else: 
            self.ui.add_client_btn.setEnabled(False)

    def add_client(self):
        client_info = []
        widgets = [self.ui.full_name_txt,self.ui.address_txt,self.ui.town_txt,
                   self.ui.country_txt,self.ui.postcode_txt,self.ui.email_txt,self.ui.wage_txt]
        for i in widgets:
            client_info.append(i.toPlainText())
            i.setText("")
        client_name = client_info[0]
        client_folder = Path("Clients/"+str(client_name))
        client_folder.mkdir(parents=True, exist_ok=True)
        with open("Clients/"+str(client_name)+"/Base_"+str(client_name),"w") as client_file:
            for i in client_info:
                client_file.writelines(i+"\n")
        client_file.close()
        with open("Personal\Client_List.txt","a") as client_list:
            client_list.write(client_name)
        self.refresh_combos()

    def client_remove_add_select(self):
        self.ui.add_delete_client.clear()
        clients = []
        if self.ui.delete_client_rb.isChecked():
            path = "Personal\Client_List.txt"
        else:
            path = "Personal\Deleted_Client_list.txt"
        with open(path,"r") as client_list:
            for i in client_list:
                i = i.replace("\n","")
                clients.append(i)
        for i in clients:
            self.ui.add_delete_client.addItem(i)

    def confirm_delete(self):
        if self.ui.add_client_rb.isChecked():
            self.finalise_add_remove(False)
        else:
            self.finalise_add_remove(True)

    def finalise_add_remove(self,Delete):
        new_client_list = []
        Moved_client = ""
        selected_client_line = self.ui.add_delete_client.currentText()
        if Delete == True: # if delete is true delete from the client list text file and add to deleted client files
            Adding_file = "Personal\Deleted_Client_list.txt"
            deleting_file = "Personal\Client_List.txt"
        else:
            Adding_file = "Personal\Client_List.txt"
            deleting_file = "Personal\Deleted_Client_list.txt"
        with open(deleting_file,"r") as Client_List:
            Lines = Client_List.readlines()
            for Line in Lines:
                Line = Line.replace("\n","")
                if Line == selected_client_line and selected_client_line != "": 
                    Moved_client = Line
                else:
                    new_client_list.append(Line)
        if Moved_client != "":
            with open(Adding_file,"a") as Adding_file:
                Adding_file.write(Moved_client+"\n")
            Adding_file.close()
            print(Moved_client)
            with open(deleting_file,"r") as Deleting_File:
                lines = Deleting_File.readlines()
            Deleting_File.close()
            with open(deleting_file,"w") as Deleting_File:
                for client in new_client_list:
                    Deleting_File.write(client+"\n")
            Deleting_File.close()
            self.client_remove_add_select()
            self.refresh_combos()

    def edit_client_widgets(self):
        client_edit = self.ui.edit_client_dropdown.currentText()
        check_boxes = [self.ui.edit_name_chl,self.ui.edit_address_chk,self.ui.edit_town_chk,self.ui.edit_country_chk,self.ui.edit_postcode_chk,self.ui.edit_email_chk,self.ui.edit_wage_chk]
        widgets = [self.ui.full_name_txt_edit,self.ui.address_txt_edit,self.ui.town_txt_edit,self.ui.country_txt_edit,self.ui.postcode_txt_edit,self.ui.email_txt_edit,self.ui.hourlywage_txt_edit]
        if self.sender().objectName() == "edit_client_dropdown":
            with open("Clients/"+client_edit+"/Base_"+client_edit,"r") as client_file:
                client_data = client_file.readlines()
                for index in range(0,len(client_data)):
                    widgets[index].setHtml(client_data[index])
        for i in check_boxes:
            widget_index = check_boxes.index(i)
            widgets[widget_index].setEnabled(i.isChecked())
        
    def update_client_information(self):
        client_edit = self.ui.edit_client_dropdown.currentText()
        new_client_information = []
        widgets = [self.ui.full_name_txt_edit,self.ui.address_txt_edit,self.ui.town_txt_edit,self.ui.country_txt_edit,self.ui.postcode_txt_edit,self.ui.email_txt_edit,self.ui.hourlywage_txt_edit]
        for i in widgets:
            new_client_information.append(i.toPlainText()+"\n")
        print(new_client_information)
        with open("Clients/"+client_edit+"/Base_"+client_edit,"w") as new_client_file:
            for i in new_client_information:
                new_client_file.write(i)
                


