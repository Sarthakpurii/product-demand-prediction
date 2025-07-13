import sys
from PyQt5.QtWidgets import QApplication,QStyleFactory
from pyqt_gui.pages.main_window import MainWindow
import qdarktheme

def start_gui():
    app = QApplication(sys.argv)
    print("Available styles:", QStyleFactory.keys())
    app.setStyleSheet(qdarktheme.load_stylesheet())
    # app.setStyleSheet(qdarktheme.load_stylesheet("light"))

    
    window = MainWindow()
    window.showMaximized()  
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    start_gui()