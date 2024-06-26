from PyQt5.QtWidgets import QApplication

from welcome_window import MainWindow


def main():
    app = QApplication([])

    window = MainWindow()
    # window.show()

    # This is where the program actually starts
    app.exec_()


if __name__ == "__main__":
    main()
