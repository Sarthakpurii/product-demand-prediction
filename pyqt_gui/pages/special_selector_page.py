# pages/special_selector_page.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ..ui_pys.special_selector import Ui_Dialog

class SpecialSelectorPage(QWidget):
    next_clicked = pyqtSignal(list)  
    back_clicked = pyqtSignal()     
    
    def __init__(self):
        super().__init__()
        
        self.dialog_widget = QWidget()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog_widget)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.dialog_widget)
        
        self.ui.pushButton.clicked.connect(self.on_next_clicked)
        self.ui.pushButton_2.clicked.connect(self.on_back_clicked)
        
    def on_next_clicked(self):
        selected_stores = []
        
        if self.ui.checkBox_3.isChecked():
            selected_stores.append("S001")
        if self.ui.checkBox_2.isChecked():
            selected_stores.append("S002")
        if self.ui.checkBox.isChecked():
            selected_stores.append("S003")
        
        self.next_clicked.emit(selected_stores)
    
    def on_back_clicked(self):
        self.back_clicked.emit()
    
    def reset_selection(self):
        """Reset all checkboxes to unchecked"""
        self.ui.checkBox_3.setChecked(False)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox.setChecked(False)