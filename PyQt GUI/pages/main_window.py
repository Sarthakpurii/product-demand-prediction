# pages/main_window.py

from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QMessageBox
from PyQt5.QtCore import Qt
from pages.day_selector_page import DaySelectorPage
from pages.product_selector_page import ProductSelectorPage
from pages.special_selector_page import SpecialSelectorPage
from pages.inflation_inputter_page import InflationInputterPage
from pages.unemployment_inputter_page import UnemploymentInputterPage
from pages.prediction_page import PredictionPage

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
        self.inflation_inputter = InflationInputterPage()
        self.unemployment_inputter = UnemploymentInputterPage()
        self.prediction_page = PredictionPage()
        
        self.stacked_widget.addWidget(self.day_selector)
        self.stacked_widget.addWidget(self.product_selector)
        self.stacked_widget.addWidget(self.special_selector)
        self.stacked_widget.addWidget(self.inflation_inputter)
        self.stacked_widget.addWidget(self.unemployment_inputter)
        self.stacked_widget.addWidget(self.prediction_page)
        
        
        self.day_selector.next_clicked.connect(self.go_to_product_selector)
        
        self.product_selector.back_clicked.connect(self.go_to_day_selector)
        self.product_selector.next_clicked.connect(self.go_to_special_selector)
        
        self.special_selector.back_clicked.connect(self.go_to_product_selector_from_special)
        self.special_selector.next_clicked.connect(self.go_to_inflation_inputter)
        
        self.inflation_inputter.back_clicked.connect(self.go_to_special_selector_from_inflation)
        self.inflation_inputter.next_clicked.connect(self.go_to_unemployment_inputter)
        
        self.unemployment_inputter.back_clicked.connect(self.go_to_inflation_inputter_from_unemployment)
        self.unemployment_inputter.next_clicked.connect(self.confirm_details)
        
        self.prediction_page.start_over_clicked.connect(self.reset_to_beginning)
        
        
        
        self.stacked_widget.setCurrentWidget(self.day_selector)
        
        self.selected_day = None
        self.selected_product = None
        self.selected_stores = []
        self.inputted_inflation = None
        self.inputted_unemployment = None
        
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
        
    def go_to_inflation_inputter(self, selected_stores):
        self.selected_stores = selected_stores
        print(f"Selected stores: {selected_stores}")
        self.stacked_widget.setCurrentWidget(self.inflation_inputter)
        
    def go_to_special_selector_from_inflation(self):
        self.stacked_widget.setCurrentWidget(self.special_selector)
        
    def go_to_unemployment_inputter(self, inflation_percentage):
        self.inputted_inflation = inflation_percentage
        print(f"Inputted inflation: {inflation_percentage}")
        self.stacked_widget.setCurrentWidget(self.unemployment_inputter)
    
    def go_to_inflation_inputter_from_unemployment(self):
        self.stacked_widget.setCurrentWidget(self.inflation_inputter)
    
        
    def confirm_details(self, unemployment_percentage):
        self.inputted_unemployment = unemployment_percentage
        print(f"Inputted unemployment: {unemployment_percentage}")
             
        reply = QMessageBox.question(
            self, 
            'Confirmation', 
            f'Confirmed the details?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        
        if reply == QMessageBox.Yes:
            self.prediction_page.set_sales_result(0, "$")
            self.stacked_widget.setCurrentWidget(self.prediction_page)
            
        
    def reset_to_beginning(self):
        """Reset the application to the first page"""
        self.selected_day = None
        self.selected_product = None
        self.selected_stores = []
        self.inputted_inflation = None
        self.inputted_unemployment = None

        
        self.stacked_widget.setCurrentWidget(self.day_selector)