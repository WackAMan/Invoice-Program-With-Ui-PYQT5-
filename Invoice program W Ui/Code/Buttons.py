def connect_buttons_Invoice(self):
    self.ui.Add_Clean.clicked.connect(self.Add_clean)
    self.ui.Add_Clean.clicked.connect(self.update_table)
    self.ui.Day_table.cellClicked.connect(self.select_clean)
    self.ui.Delete_Day.clicked.connect(self.delete_day)
    self.ui.Preview.clicked.connect(self.invoice_make)
    self.ui.Client_Box.activated.connect(self.validate_client)
    self.ui.Send.clicked.connect(self.send_invoice)

def connect_buttons_client(self):
    widgets_add = [self.ui.full_name_txt,self.ui.address_txt,self.ui.town_txt,
                   self.ui.country_txt,self.ui.postcode_txt,self.ui.email_txt,self.ui.wage_txt]
    self.ui.add_client_page_btn.clicked.connect(self.goto_add_client)
    self.ui.edit_client_page_btn.clicked.connect(self.goto_edit_client)
    self.ui.add_delete_page_btn.clicked.connect(self.goto_add_delete_client)
    for i in widgets_add:
        i.textChanged.connect(self.add_client_valid)
    self.ui.add_client_btn.clicked.connect(self.add_client)
    self.ui.delete_client_rb.toggled.connect(self.client_remove_add_select)
    self.ui.add_client_rb.toggled.connect(self.client_remove_add_select)
    self.ui.final_add_delete_btn.clicked.connect(self.confirm_delete)
    self.ui.edit_client_dropdown.activated.connect(self.edit_client_widgets)
    check_boxes = [self.ui.edit_name_chl,self.ui.edit_address_chk,self.ui.edit_town_chk,self.ui.edit_country_chk,self.ui.edit_postcode_chk,self.ui.edit_email_chk,self.ui.edit_wage_chk]
    for i in check_boxes:
        i.stateChanged.connect(self.edit_client_widgets)
    self.ui.update_client_btn.clicked.connect(self.update_client_information)
    
def connect_buttons_admin(self):
    self.ui.edit_user_info.stateChanged.connect(self.enable_text_boxes)
    text_boxes = [self.ui.user_full_name_txt_edit,self.ui.user_address_txt_edit,self.ui.user_town__txt_edit,self.ui.user_country_txt_edit,self.ui.user_postcode_txt_edit,
                        self.ui.user_bankname_txt_edit,self.ui.user_accountname_txt_edit,self.ui.user_emailsubject_txt_edit,self.ui.user_emailmessage_txt_edit,self.ui.user_phone_txt_edit,
                        self.ui.user_sort_txt_edit,self.ui.user_accountnum_txt_edit,self.ui.user_email_txt_edit]
    for i in text_boxes:
        i.textChanged.connect(self.Validate_Text_Boxes)
    self.ui.update_user_btn.clicked.connect(self.create_personal_data_file)