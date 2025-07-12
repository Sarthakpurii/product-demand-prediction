# pages/main_window.py

from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.QtCore import Qt
from pages.day_selector_page import DaySelectorPage
from pages.product_selector_page import ProductSelectorPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Order System")
        self.resize(1000, 800)
        
        # Create the stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Create pages
        self.day_selector = DaySelectorPage()
        self.product_selector = ProductSelectorPage()
        
        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.day_selector)
        self.stacked_widget.addWidget(self.product_selector)
        
        # Connect signals
        self.day_selector.next_clicked.connect(self.go_to_product_selector)
        self.product_selector.back_clicked.connect(self.go_to_day_selector)
        self.product_selector.next_clicked.connect(self.go_to_next_page)
        
        # Show first page
        self.stacked_widget.setCurrentWidget(self.day_selector)
        
    def go_to_product_selector(self, selected_day):
        print(f"Selected day: {selected_day}")
        self.stacked_widget.setCurrentWidget(self.product_selector)
        
    def go_to_day_selector(self):
        self.stacked_widget.setCurrentWidget(self.day_selector)
        
    def go_to_next_page(self, selected_product):
        print(f"Selected product: {selected_product}")
        # Add next page navigation here