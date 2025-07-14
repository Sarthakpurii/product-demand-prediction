

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QDoubleValidator
from ..ui_pys.inflation_inputter import Ui_Dialog

class InflationInputterPage(QWidget):
    next_clicked = pyqtSignal(float)  
    back_clicked = pyqtSignal()       
    
    def __init__(self):
        super().__init__()
        

        self.dialog_widget = QWidget()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog_widget)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.dialog_widget)
        
        validator = QDoubleValidator(0.0, 100.0, 2)
        validator.setNotation(QDoubleValidator.StandardNotation)
        self.ui.lineEdit.setValidator(validator)
        
        self.ui.pushButton.clicked.connect(self.on_next_clicked)
        self.ui.pushButton_2.clicked.connect(self.on_back_clicked)
        
    def on_next_clicked(self):
        inflation_text = self.ui.lineEdit.text().strip()
        
        if not inflation_text:
            QMessageBox.warning(self, "No Input", "Please enter an inflation percentage.")
            return
        
        try:
            inflation_percentage = float(inflation_text)
            if 0 <= inflation_percentage <= 100:
                self.next_clicked.emit(inflation_percentage)
            else:
                QMessageBox.warning(self, "Invalid Input", "Please enter a percentage between 0 and 100.")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
    
    def on_back_clicked(self):
        self.back_clicked.emit()
    
    def reset_input(self):
        """Clear the input field"""
        self.ui.lineEdit.clear()
    
    def set_inflation(self, value):
        """Set the inflation value programmatically"""
        self.ui.lineEdit.setText(str(value))