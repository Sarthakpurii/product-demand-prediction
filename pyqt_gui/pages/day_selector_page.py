# pages/day_selector_page.py

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from ..ui_pys.day_selector import Ui_Dialog

class DaySelectorPage(QWidget):
    next_clicked = pyqtSignal(str)  # Signal to emit selected day
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Connect signals
        self.ui.pushButton.clicked.connect(self.on_next_clicked)
        
    def on_next_clicked(self):
        selected_day = self.ui.comboBox.currentText()
        if selected_day == "-Select-":
            print("Please select a day first!")
            return
        self.next_clicked.emit(selected_day)