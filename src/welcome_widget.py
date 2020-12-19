from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, qApp
from mock_window import MockWindow

class WelcomeWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.central_layout = QVBoxLayout()

        # main text
        self.main_welcome_label = QLabel("Welcome to FFWizard!")
        self.main_welcome_label.setFont(QFont("Times", 24))

        self.welcome_description_label = QLabel("You're on your way to acing your fantasy football\n draft and crushing the competition. Let's get started!")
        self.welcome_description_label.setFont(QFont("Times", 12))

        # buttons for mock and live draft
        self.mock_button = QPushButton("Mock Draft")
        self.mock_button.setToolTip("Mock Draft")
        self.mock_button.setMaximumWidth(400)
        self.mock_button.setStyleSheet("background-color: darkGray")
        self.mock_button.clicked.connect(self.mock_draft)

        self.live_button = QPushButton("Live Draft")
        self.live_button.setToolTip("Live Draft")
        self.live_button.setMaximumWidth(400)
        self.live_button.setStyleSheet("background-color: darkGray")
        #self.live_button.clicked.connect(self.open_note)

        self.central_layout.addWidget(self.main_welcome_label)
        self.central_layout.addWidget(self.welcome_description_label)
        self.central_layout.addSpacing(100)
        self.central_layout.addWidget(self.mock_button)
        self.central_layout.addWidget(self.live_button)
        self.central_layout.addStretch(1)

        self.setLayout(self.central_layout)

    def mock_draft(self):
        pass
        # self.mock = MockWindow()
        # self.mock.show()
        # QWidget.qApp.quit()