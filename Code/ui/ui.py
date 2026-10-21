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

        self.top_hlayout = QHBoxLayout()
        self.middle_hlayout = QHBoxLayout()
        self.bottom_hlayout = QHBoxLayout()

        self.central_vlayout.addLayout(self.top_hlayout)
        self.central_vlayout.addLayout(self.middle_hlayout)
        self.central_vlayout.addLayout(self.bottom_hlayout)

        # Top layout widgets
        self.speed_widget = QWidget()
        self.name_widget = QWidget()
        self.time_widget = QWidget()
        self.location_widget = QWidget()

        # Nested layout for name and time
        self.time_name_vlayout = QVBoxLayout()

        self.time_name_vlayout.addWidget(self.name_widget)
        self.time_name_vlayout.addWidget(self.time_widget)

        self.top_hlayout.addWidget(self.speed_widget)
        self.top_hlayout.addLayout(self.time_name_vlayout)
        self.top_hlayout.addWidget(self.location_widget)

        # Middle layout widgets
        self.map_widget = QWidget()

        self.middle_hlayout.addWidget(self.map_widget)

        # Bottom layout widgets
        self.stop_route_widget = QWidget()
        self.animation_widget = QWidget()
        self.eta_widget = QWidget()
        self.dest_select_widget = QWidget()

        self.stop_route_widget.setMaximumHeight(100)
        self.animation_widget.setMaximumHeight(100)
        self.eta_widget.setMaximumHeight(100)
        self.dest_select_widget.setMaximumHeight(100)

        self.bottom_hlayout.addWidget(self.stop_route_widget)
        self.bottom_hlayout.addWidget(self.animation_widget)
        self.bottom_hlayout.addWidget(self.eta_widget)
        self.bottom_hlayout.addWidget(self.dest_select_widget)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MainWindow()

    sys.exit(app.exec())