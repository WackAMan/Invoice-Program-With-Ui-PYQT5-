from Ui.Invoice_Ui import Ui_Dialog
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *

class User_interface(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
