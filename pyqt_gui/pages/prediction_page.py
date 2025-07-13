
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from ..ui_pys.prediction import Ui_Dialog

class PredictionPage(QWidget):
    start_over_clicked = pyqtSignal()  # Signal to restart the application
    
    def __init__(self):
        super().__init__()
        
        self.dialog_widget = QWidget()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog_widget)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.dialog_widget)
        
        self.ui.startOverButton.clicked.connect(self.on_start_over_clicked)
        
    def on_start_over_clicked(self):
        self.start_over_clicked.emit()
    
    def set_sales_result(self, amount, currency="$"):
        """Set the sales prediction result
        
        Args:
            amount: The predicted sales amount
            currency: Currency symbol (default: $)
        """
        formatted_amount = f"{currency}{amount:,.2f}"
        self.ui.result_label.setText(f"The predicted sales are: {formatted_amount}")
    
    def set_additional_info(self, info_text):
        """Set additional information text below the result"""
        self.ui.info_label.setText(info_text)
    