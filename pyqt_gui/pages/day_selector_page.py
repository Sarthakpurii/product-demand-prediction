
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from ..ui_pys.day_selector import Ui_Dialog

class DaySelectorPage(QWidget):
    next_clicked = pyqtSignal(str)  
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.on_next_clicked)
        
    def on_next_clicked(self):
        selected_day = self.ui.comboBox.currentText()
        if selected_day == "-Select-":
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.warning(self, "No Selection", "Please select a day before proceeding.")
            return
        self.next_clicked.emit(selected_day)
    
    def reset_input(self):
        self.ui.comboBox.setCurrentIndex(0)