from PyQt5.QtWidgets import *

import sys

from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CarNav")
        self.resize(720, 480)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.central_vlayout = QVBoxLayout(self.central_widget)
        
        self.bottom_hlayout = QHBoxLayout()
        self.middle_hlayout = QHBoxLayout()
        self.top_hlayout = QHBoxLayout()

        self.central_vlayout.addLayout(self.bottom_hlayout)
        self.central_vlayout.addLayout(self.middle_hlayout)
        self.central_vlayout.addLayout(self.top_hlayout)

        self.dest_select_widget = QWidget()
        self.eta_widget = QWidget()
        self.stop_route_widget = QWidget()
        self.animation_widget = QWidget()

        self.map_widget = QWidget()

        self.location_widget = QWidget()
        self.speed_widget = QWidget()
        self.time_



        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Create and show the main window.
    w = MainWindow()
    # Enter the event loop and keep the app running until the window is closed.
    sys.exit(app.exec())