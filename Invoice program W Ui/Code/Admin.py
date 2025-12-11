from PyQt5.QtWidgets import *
from Code.Buttons import connect_buttons_admin
from PyQt5.QtGui import QPixmap
from email_validator import validate_email, EmailNotValidError
import os

class Admin(QDialog):
    def __init__(self,ui):
        super().__init__()
        self.valid = []
        self.ui = ui
        self.green = QPixmap("Ui\Images\Tick_indicator.png")
        self.red = QPixmap("Ui\Images\Cross_indicator.png")
        connect_buttons_admin(self)
        self.text_boxes = [self.ui.user_full_name_txt_edit,self.ui.user_address_txt_edit,self.ui.user_town__txt_edit,self.ui.user_country_txt_edit,self.ui.user_postcode_txt_edit,
                           self.ui.user_email_txt_edit,self.ui.user_phone_txt_edit,self.ui.user_bankname_txt_edit,self.ui.user_sort_txt_edit,self.ui.user_accountnum_txt_edit,
                           self.ui.user_accountname_txt_edit,self.ui.user_emailsubject_txt_edit,self.ui.user_emailmessage_txt_edit]
        if os.path.exists("Personal\Personal_data.txt") == True:
            with open("Personal\Personal_data.txt","r") as personal_data:
                for i in enumerate(personal_data):
                    self.text_boxes[i[0]].setHtml(i[1].replace("\n","").replace(" ",""))

    def enable_text_boxes(self):
        for i in self.text_boxes:
            i.setEnabled(self.sender().isChecked())
            
    def Validate_Text_Boxes(self):
        self.valid = {}
        presence_fields = [
            ("full_name", self.ui.user_full_name_txt_edit, self.ui.user_name_edit_ind),
            ("address", self.ui.user_address_txt_edit, self.ui.user_address_edit_ind),
            ("town", self.ui.user_town__txt_edit, self.ui.user_town_edit_ind),
            ("country", self.ui.user_country_txt_edit, self.ui.user_country_edit_ind),
            ("postcode", self.ui.user_postcode_txt_edit, self.ui.user_edit_postcode_ind),
            ("bank_name", self.ui.user_bankname_txt_edit, self.ui.user_bankname_edit_ind),
            ("account_name", self.ui.user_accountname_txt_edit, self.ui.user_accountname_edit_ind),
            ("email_subject", self.ui.user_emailsubject_txt_edit, self.ui.user_emailsubject_edit_ind),
            ("email_message", self.ui.user_emailmessage_txt_edit, self.ui.user_emailmessage_edit_ind)
        ]
        
        # Presence check
        for field_name, textbox, indicator in presence_fields:
            is_valid = bool(textbox.toPlainText().strip())
            self.valid[field_name] = is_valid
            indicator.setPixmap(self.green if is_valid else self.red)

        # Email check
        try:
            email = validate_email(self.ui.user_email_txt_edit.toPlainText(), check_deliverability=True).normalized
            self.valid["email"] = True
            self.ui.user_email_edit_ind.setPixmap(self.green)
        except EmailNotValidError:
            self.valid["email"] = False
            self.ui.user_email_edit_ind.setPixmap(self.red)

        # Phone check
        phone = self.ui.user_phone_txt_edit.toPlainText().replace(" ", "")
        self.valid["phone"] = (phone.isnumeric() and len(phone) == 11)
        self.ui.user_phonenum_edit_ind.setPixmap(self.green if self.valid["phone"] else self.red)

        # Sort code check
        sort_code = self.ui.user_sort_txt_edit.toPlainText().replace("-", "").replace(" ", "")
        self.valid["sort_code"] = sort_code.isnumeric() and len(sort_code) == 6
        self.ui.user_sortcode_edit_ind.setPixmap(self.green if self.valid["sort_code"] else self.red)

        # Account number check
        account_number = self.ui.user_accountnum_txt_edit.toPlainText().replace(" ", "")
        self.valid["account_number"] = account_number.isnumeric() and len(account_number) in range(5,18)
        self.ui.user_accountnum_edit_ind.setPixmap(self.green if self.valid["account_number"] else self.red)

        self.ui.update_user_btn.setEnabled(all(self.valid.values()))

    def create_personal_data_file(self):
        with open("Personal/Personal_data.txt","w") as personal_data_txt:
            for i in self.text_boxes:
                personal_data_txt.write(i.toPlainText()+"\n")