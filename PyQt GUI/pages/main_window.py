# pages/main_window.py

from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QMessageBox
from PyQt5.QtCore import Qt
from pages.day_selector_page import DaySelectorPage
from pages.product_selector_page import ProductSelectorPage
from pages.special_selector_page import SpecialSelectorPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Order System")
        self.resize(1000, 800)
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.day_selector = DaySelectorPage()
        self.product_selector = ProductSelectorPage()
        self.special_selector = SpecialSelectorPage()
        
        self.stacked_widget.addWidget(self.day_selector)
        self.stacked_widget.addWidget(self.product_selector)
        self.stacked_widget.addWidget(self.special_selector)
        
        self.day_selector.next_clicked.connect(self.go_to_product_selector)
        
        self.product_selector.back_clicked.connect(self.go_to_day_selector)
        self.product_selector.next_clicked.connect(self.go_to_special_selector)
        
        self.special_selector.back_clicked.connect(self.go_to_product_selector_from_special)
        self.special_selector.next_clicked.connect(self.complete_order)
        
        self.stacked_widget.setCurrentWidget(self.day_selector)
        
        self.selected_day = None
        self.selected_product = None
        self.selected_stores = []
        
    def go_to_product_selector(self, selected_day):
        self.selected_day = selected_day
        print(f"Selected day: {selected_day}")
        self.stacked_widget.setCurrentWidget(self.product_selector)
        
    def go_to_day_selector(self):
        self.stacked_widget.setCurrentWidget(self.day_selector)
        
    def go_to_special_selector(self, selected_product):
        self.selected_product = selected_product
        print(f"Selected product: {selected_product}")
        self.stacked_widget.setCurrentWidget(self.special_selector)
    
    def go_to_product_selector_from_special(self):
        self.stacked_widget.setCurrentWidget(self.product_selector)
        
    def complete_order(self, selected_stores):
        self.selected_stores = selected_stores
        
        if selected_stores:
            stores_text = ", ".join(selected_stores)
        else:
            stores_text = "None (No special for any store)"
        
        summary = f"""Order Summary:
- Day: {self.selected_day}
- Product: {self.selected_product}
- Stores with special: {stores_text}"""
        
        print(summary)
        
        reply = QMessageBox.question(
            self, 
            'Order Confirmation', 
            f'{summary}\n\nConfirm this order?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Success", "Order placed successfully!")
            self.reset_to_beginning()
        
    def reset_to_beginning(self):
        """Reset the application to the first page"""
        self.selected_day = None
        self.selected_product = None
        self.selected_stores = []

        
        self.stacked_widget.setCurrentWidget(self.day_selector)