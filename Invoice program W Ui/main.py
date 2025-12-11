import sys
from Code.Invoice import Invoice
from Code.Client import Client
from Code.Admin import Admin
from Code.Class import User_interface
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

if __name__ == '__main__':
    app = QApplication(sys.argv)
    y = User_interface()
    client_logic = Client(y.ui)
    invoice_logic = Invoice(y.ui)
    Admin_logic = Admin(y.ui)
    y.setWindowFlags(Qt.WindowStaysOnTopHint)
    y.show()
    sys.exit(app.exec_()) 

    #to do
# - settings panel - edit own info, add more descriptions
# - on invoice tab: if no personal data text file exists make a popup saying please fill in the text boxes on the admin tab
# - edit all autofilling data with personal data by doing self.personal data and reading file at the start somewhere (invoices probably again)
# - finish the search page & also put grey box behind it
# - automatically select smtp port for each email
# - finally delete all clients and clinets in client lists and personal data text file and zip it and send it to parents to test on laptop