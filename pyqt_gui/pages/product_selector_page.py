from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from ..ui_pys.product_selector import Ui_Dialog

class ProductSelectorPage(QWidget):
    next_clicked = pyqtSignal(str)  # Signal to emit selected product
    back_clicked = pyqtSignal()     # Signal to go back
    
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
        
        # Connect signals
        self.ui.pushButton.clicked.connect(self.on_next_clicked)
        self.ui.pushButton_2.clicked.connect(self.on_back_clicked)  # Connect the back button
        
    def on_next_clicked(self):
        selected_product = self.ui.comboBox.currentText()
        if selected_product == "-Select-":
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.warning(self, "No Selection", "Please select a product before proceeding.")
            return
        self.next_clicked.emit(selected_product)
    
    def on_back_clicked(self):
        self.back_clicked.emit()
        
    def reset_input(self):
        self.ui.comboBox.setCurrentIndex(0)