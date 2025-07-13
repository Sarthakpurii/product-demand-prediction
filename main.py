# from PyQt5.QtWidgets import QApplication, QMainWindow
# # import qdarktheme
# import sys

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Set the window to maximized
#         self.showMaximized()

#         # Optional title
#         self.setWindowTitle("My PyQt App")

# dark_stylesheet = """
# QMainWindow {
#     background-color: #2b2b2b;
# }

# QWidget {
#     background-color: #2b2b2b;
#     color: #ffffff;
#     font-family: 'Segoe UI', Arial, sans-serif;
#     font-size: 14px;
# }

# QPushButton {
#     background-color: #3c3c3c;
#     border: 1px solid #555555;
#     padding: 8px;
#     border-radius: 4px;
#     min-width: 80px;
# }

# QPushButton:hover {
#     background-color: #4a4a4a;
#     border-color: #777777;
# }

# QPushButton:pressed {
#     background-color: #2a2a2a;
#     border-color: #333333;
# }

# QLineEdit {
#     background-color: #3c3c3c;
#     border: 1px solid #555555;
#     padding: 8px;
#     border-radius: 4px;
# }

# QLineEdit:focus {
#     border-color: #007acc;
# }

# QLabel {
#     color: #ffffff;
#     padding: 5px;
# }
# """

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyleSheet(dark_stylesheet)

#     # Apply dark theme
#     # qdarktheme.setup_theme("dark")  # options: "dark", "light", or dict for custom

#     window = MainWindow()
#     window.show()  # optional since we used showMaximized, but safe to keep

#     sys.exit(app.exec_())
# main.py


import sys
from PyQt5.QtWidgets import QApplication
from pyqt_gui.pages.main_window import MainWindow

def start_gui():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.showMaximized()  # or window.show() for normal size
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    start_gui()