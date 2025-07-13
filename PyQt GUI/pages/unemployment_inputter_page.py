# pages/inflation_inputter_page.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QDoubleValidator
from UI_pys.unemployment_inputter import Ui_Dialog

class UnemploymentInputterPage(QWidget):
    next_clicked = pyqtSignal(float)  # Signal to emit inflation percentage
    back_clicked = pyqtSignal()       # Signal to go back
    
    def __init__(self):
        super().__init__()
        
        # Create a dialog UI but apply it to a widget
        self.dialog_widget = QWidget()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog_widget)
        
        # Create layout and add the dialog widget
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.dialog_widget)
        
        # Set up validator for percentage input (0.0 to 100.0)
        validator = QDoubleValidator(0.0, 100.0, 2)
        validator.setNotation(QDoubleValidator.StandardNotation)
        self.ui.lineEdit.setValidator(validator)
        
        # Connect signals
        self.ui.pushButton.clicked.connect(self.on_next_clicked)
        self.ui.pushButton_2.clicked.connect(self.on_back_clicked)
        
    def on_next_clicked(self):
        unemployment_text = self.ui.lineEdit.text().strip()
        
        if not unemployment_text:
            QMessageBox.warning(self, "No Input", "Please enter an unemployment percentage.")
            return
        
        try:
            unemployment_text = float(unemployment_text)
            if 0 <= unemployment_text <= 100:
                self.next_clicked.emit(unemployment_text)
            else:
                QMessageBox.warning(self, "Invalid Input", "Please enter a percentage between 0 and 100.")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
    
    def on_back_clicked(self):
        self.back_clicked.emit()
    
    def reset_input(self):
        """Clear the input field"""
        self.ui.lineEdit.clear()
    
    def set_unemployment(self, value):
        """Set the inflation value programmatically"""
        self.ui.lineEdit.setText(str(value))