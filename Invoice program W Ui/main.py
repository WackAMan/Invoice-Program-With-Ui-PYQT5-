
try:
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
        
except Exception as e:
    print(e)
    input("Cheese")

#modules pyqt5,reportlab, fitz, email_validator
