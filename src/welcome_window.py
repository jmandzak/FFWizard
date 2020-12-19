from PyQt5.QtWidgets import QMainWindow
from welcome_widget import WelcomeWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(0, 0, 1600, 1200)
        self.setWindowTitle("FFWizard")

        self.central_widget = WelcomeWidget()
        self.setCentralWidget(self.central_widget)

        self.setStyleSheet("background-color: lightGray")
        
        self.show()
