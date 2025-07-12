# pages/product_selector_page.py

from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal, QRect
from PyQt5.QtGui import QFont
from UI_pys.product_selector import Ui_Dialog

class ProductSelectorPage(QWidget):
    next_clicked = pyqtSignal(str)  # Signal to emit selected product
    back_clicked = pyqtSignal()     # Signal to go back
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Add a back button
        self.back_button = QPushButton(self.ui.widget_7)
        self.back_button.setGeometry(QRect(170, 20, 121, 41))
        font = QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.back_button.setFont(font)
        self.back_button.setText("Back")
        
        # Connect signals
        self.ui.pushButton.clicked.connect(self.on_next_clicked)
        self.back_button.clicked.connect(self.back_clicked.emit)
        
    def on_next_clicked(self):
        selected_product = self.ui.comboBox.currentText()
        if selected_product == "-Select-":
            print("Please select a product first!")
            return
        self.next_clicked.emit(selected_product)