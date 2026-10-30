from PyQt5.QtWidgets import *

"""(
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QApplication,
    QGridLayout,
    QStackedLayout,
    QGraphicsOpacityEffect,
    QPushButton
)"""

from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView

#from offline_folium import offline
import folium
from folium import plugins

import sys
import os
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

# from main import CarNavApp

debug = False

# Color Palette
color_pallet = {
    "jet-black": "#30343fff",
    "ghost-white": "#fafaffff",
    "dusty-olive": "#709176ff",
    "twilight-indigo": "#273469ff",
    "space-indigo": "#1e2749ff",
}

class MainWindow(QMainWindow):
    def __init__(self, carnavapp):
        super().__init__()

        self.setWindowTitle("CarNav")
        self.resize(720, 480)
        self.setFixedSize(
            720, 480
        )  # Needed due to my computers using Hyprland (auto tiling window manager), which overwrote the handling of size

        self.car_nav_controller = carnavapp

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

        self.name_widget.setFixedWidth(200)
        self.time_widget.setFixedWidth(200)

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
        self.map_widget = QWebEngineView()
        self.map = self.create_map(-35.3265,149.053,17)
        self.map.save('map.html')
        self.map_widget.setHtml(self.map.get_root().render())

        # Transparent overlay positioned over the map
        self.middle_glayout_widget = QWidget()
        self.middle_glayout_widget.setStyleSheet(
            "background: transparent; border: none;"
        )

        self.middle_glayout = QGridLayout(self.middle_glayout_widget)
        self.middle_glayout.setContentsMargins(10, 10, 10, 10)

        self.list_turns = QPushButton()
        self.list_turns.setFixedSize(50, 50)
        self.list_turns.clicked.connect(self.on_list_turns_presses)

        self.middle_glayout.addWidget(self.list_turns, 1, 1, Qt.AlignBottom | Qt.AlignRight)

        self.middle_slayout.addWidget(self.map_widget)
        self.middle_slayout.addWidget(self.middle_glayout_widget)

        self.middle_slayout.setCurrentWidget(self.middle_glayout_widget)

        # Bottom layout widgets
        self.stop_route_widget = QPushButton()
        self.animation_widget = QWidget()
        self.eta_widget = QWidget()
        self.dest_select_widget = QLineEdit()

        self.stop_route_widget.clicked.connect(self.on_stop_route_pressed)

        self.stop_route_widget.setFixedSize(65, 65)
        self.animation_widget.setFixedHeight(65)
        self.eta_widget.setFixedSize(100, 65)
        self.dest_select_widget.setFixedHeight(65)

        self.bottom_hlayout.addWidget(self.stop_route_widget, 1)
        self.bottom_hlayout.addWidget(self.animation_widget, 1)
        self.bottom_hlayout.addWidget(self.eta_widget, 1)
        self.bottom_hlayout.addWidget(self.dest_select_widget, 1)

        if debug:
            self.apply_debug_styling()
        else:
            self.apply_styling()

        self.show()

    def __update(self):
        pass

    def apply_debug_styling(self):
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
            self.list_turns: ("List Turns", "#ffb74d"),
        }

        for widget, (name, colour) in debug_widgets.items():
            widget.setStyleSheet(
                f"background-color: {colour};"
                "border: 2px solid #333333;"
                "border-radius: 4px;"
            )

            label = QLabel(name)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("background: transparent; border: none;")

            layout = QVBoxLayout(widget)
            layout.setContentsMargins(2, 2, 2, 2)
            layout.addWidget(label)

    def apply_styling(self):    

        '''
        "jet-black": "#30343fff",
        "ghost-white": "#fafaffff",
        "dusty-olive": "#709176ff",
        "twilight-indigo": "#273469ff",
        "space-indigo": "#1e2749ff",
        '''

        widget_styles = {
            self.speed_widget: color_pallet["jet-black"],
            self.name_widget: color_pallet["dusty-olive"],
            self.time_widget: color_pallet["ghost-white"],
            self.location_widget: color_pallet["space-indigo"],
            self.stop_route_widget: color_pallet["twilight-indigo"]
        }

        for widget, colour in widget_styles.items():
            widget.setStyleSheet(
                f"background-color: {colour};"
                "border: 2px solid #333333;"
                "border-radius: 4px;"
            )

            layout = QVBoxLayout(widget)
            layout.setContentsMargins(2, 2, 2, 2)


    def on_list_turns_presses(self):
        print("list turns")

    def on_stop_route_pressed(self):
        print("Route Stopped")

    def create_map(self, latitude, longitude, zoom_start = 12):
        map = folium.Map(
            location=[latitude, longitude],
            zoom_start=zoom_start,
            tiles='OpenStreetMap')
        
        folium.Marker(
            [latitude, longitude],
            icon=folium.Icon(color='red', icon='ion.car-sport-outline')
        ).add_to(map)

        plugins.LocateControl().add_to(map)

        return map

    def update_speed(self):
        pass

    def update_time(self):
        pass

    def find_destination(self):
        pass

    def get_estimated_time(self):
        pass

    def update_map(self):
        pass

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setApplicationName("CarNav")

    w = MainWindow("temp")

    sys.exit(app.exec_())
