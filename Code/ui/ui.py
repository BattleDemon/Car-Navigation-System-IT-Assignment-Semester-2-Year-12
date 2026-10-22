
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QApplication,
    QGridLayout,
    QStackedLayout,
    QGraphicsOpacityEffect,
)

from PyQt5.QtCore import Qt

import sys

debug = True


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CarNav")
        self.resize(720, 480)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.central_vlayout = QVBoxLayout(self.central_widget)
        self.central_vlayout.setContentsMargins(0, 0, 0, 0)
        self.central_vlayout.setSpacing(0)

        # Main layouts
        self.top_hlayout = QHBoxLayout()
        self.middle_slayout = QStackedLayout()
        self.bottom_hlayout = QHBoxLayout()

        self.middle_slayout.setStackingMode(QStackedLayout.StackAll)

        self.central_vlayout.addLayout(self.top_hlayout)
        self.central_vlayout.addLayout(self.middle_slayout, 1)
        self.central_vlayout.addLayout(self.bottom_hlayout)

        self.top_hlayout.setContentsMargins(5, 5, 5, 5)
        self.top_hlayout.setSpacing(5)

        self.bottom_hlayout.setContentsMargins(5, 5, 5, 5)
        self.bottom_hlayout.setSpacing(5)

        # Top layout widgets
        self.speed_widget = QWidget()
        self.name_widget = QWidget()
        self.time_widget = QWidget()
        self.location_widget = QWidget()

        self.speed_widget.setFixedSize(100, 65)
        self.location_widget.setFixedHeight(65)

        self.time_name_vlayout = QVBoxLayout()
        self.time_name_vlayout.setContentsMargins(0, 0, 0, 0)
        self.time_name_vlayout.setSpacing(5)

        self.time_name_vlayout.addWidget(self.name_widget)
        self.time_name_vlayout.addWidget(self.time_widget)

        self.top_hlayout.addWidget(self.speed_widget)
        self.top_hlayout.addLayout(self.time_name_vlayout, 1)
        self.top_hlayout.addWidget(self.location_widget, 1)

        # Middle layout widgets
        self.map_widget = QWidget()

        # Transparent overlay positioned over the map
        self.middle_glayout_widget = QWidget()
        self.middle_glayout_widget.setStyleSheet(
            "background: transparent; border: none;"
        )

        self.middle_glayout = QGridLayout(self.middle_glayout_widget)
        self.middle_glayout.setContentsMargins(10, 10, 10, 10)

        self.overlay_1 = QWidget()
        self.overlay_1.setFixedSize(150, 75)

        self.overlay_1_opacity = QGraphicsOpacityEffect(self.overlay_1)
        self.overlay_1_opacity.setOpacity(0.7)
        self.overlay_1.setGraphicsEffect(self.overlay_1_opacity)

        self.middle_glayout.addWidget(
            self.overlay_1,
            0,
            0,
            Qt.AlignTop | Qt.AlignLeft
        )

        self.middle_slayout.addWidget(self.map_widget)
        self.middle_slayout.addWidget(self.middle_glayout_widget)

        self.middle_slayout.setCurrentWidget(self.middle_glayout_widget)

        # Bottom layout widgets
        self.stop_route_widget = QWidget()
        self.animation_widget = QWidget()
        self.eta_widget = QWidget()
        self.dest_select_widget = QWidget()

        self.stop_route_widget.setFixedHeight(65)
        self.animation_widget.setFixedHeight(65)
        self.eta_widget.setFixedHeight(65)
        self.dest_select_widget.setFixedHeight(65)

        self.bottom_hlayout.addWidget(self.stop_route_widget, 1)
        self.bottom_hlayout.addWidget(self.animation_widget, 1)
        self.bottom_hlayout.addWidget(self.eta_widget, 1)
        self.bottom_hlayout.addWidget(self.dest_select_widget, 1)

        # Debug styling
        debug_widgets = {
            self.speed_widget: ("Speed", "#e57373"),
            self.name_widget: ("Name", "#ffb74d"),
            self.time_widget: ("Time", "#fff176"),
            self.location_widget: ("Location", "#81c784"),
            self.map_widget: ("Map", "#64b5f6"),
            self.stop_route_widget: ("Stop Route", "#ba68c8"),
            self.animation_widget: ("Travel Animation", "#4dd0e1"),
            self.eta_widget: ("ETA", "#f06292"),
            self.dest_select_widget: ("Destination Select", "#a1887f"),
            self.overlay_1: ("Overlay", "#ffb74d"),
        }

        if debug:
            for widget, (name, colour) in debug_widgets.items():
                widget.setStyleSheet(
                    f"background-color: {colour};"
                    "border: 2px solid #333333;"
                    "border-radius: 4px;"
                )

                label = QLabel(name)
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet(
                    "background: transparent; border: none;"
                )

                layout = QVBoxLayout(widget)
                layout.setContentsMargins(2, 2, 2, 2)
                layout.addWidget(label)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MainWindow()

    sys.exit(app.exec_())
