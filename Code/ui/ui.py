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
import os

os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = (
    "--disable-gpu --disable-gpu-compositing"
)
from PyQt5.QtWebEngineWidgets import QWebEngineView

#from offline_folium import offline
import folium
from folium import plugins

from PyQt5.QtCore import Qt, QTimer

import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

# from main import CarNavApp

debug = False

# Color Palette
mono_dark_mode = {
    "background": "#121212",
    "primary text": "#E0E0E0",
    "Secondary Text": "#B0B0B0",
    "border/dividers": "#444444",
    "accent": "#888888",
}
'''
Background: #121212 (charcoal black)
Primary Text: #E0E0E0 (light gray)
Secondary Text: #B0B0B0 (medium gray)
Borders/Dividers: #444444 (dark gray)
Accent: #888888 (soft gray)
'''

deep_dark_mode = {
    "background": "#1A1A1A",
    "primary text": "#F0F0F0",
    "Secondary Text": "#004D61",
    "border/dividers": "#822659",
    "accent": "#3E5641",
}
'''
    Background: #1A1A1A (rich black)
    Primary Text: #F0F0F0 (off-white)
    Accent 1: #004D61 (dark teal)
    Accent 2: #822659 (deep ruby)
    Button/CTA: #3E5641 (forest green)
'''

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
        self.speed_widget = QLabel("0 km/h")
        self.name_widget = QLabel("CarNav")
        self.time_widget = QLabel("00:00")
        self.location_widget = QLabel("GPS: No Location")

        self.speed_widget.setAlignment(Qt.AlignCenter)
        self.name_widget.setAlignment(Qt.AlignCenter)
        self.time_widget.setAlignment(Qt.AlignCenter)
        self.location_widget.setAlignment(Qt.AlignCenter)

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
        self.middle_glayout_widget.setAttribute(
            Qt.WA_TransparentForMouseEvents,
            True
        )
        self.middle_glayout_widget.hide()

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
        self.stop_route_widget = QPushButton("Stop")
        self.animation_widget = QProgressBar()
        self.eta_widget = QLabel("ETA: -- min")
        self.dest_select_widget = QLineEdit()

        self.animation_widget.setRange(0, 100)
        self.animation_widget.setValue(0)

        self.eta_widget.setAlignment(Qt.AlignCenter)

        self.dest_select_widget.setPlaceholderText("Lat, Lng")

        self.stop_route_widget.clicked.connect(self.on_stop_route_pressed)

        self.stop_route_widget.setFixedSize(65, 65)
        self.animation_widget.setFixedHeight(65)
        self.eta_widget.setFixedSize(100, 65)
        self.dest_select_widget.setFixedHeight(65)

        self.bottom_hlayout.addWidget(self.stop_route_widget, 1)
        self.bottom_hlayout.addWidget(self.animation_widget, 1)
        self.bottom_hlayout.addWidget(self.eta_widget, 1)
        self.bottom_hlayout.addWidget(self.dest_select_widget, 1)

        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_time)
        self.clock_timer.start(1000)

        self.gps_timer = QTimer(self)
        self.gps_timer.timeout.connect(self.update_from_app)
        self.gps_timer.start(200)

        self.update_time()

        self.dest_select_widget.returnPressed.connect(
            self.find_destination
        )

        if debug:
            self.apply_debug_styling()
        else:
            self.apply_styling()

        self.destination = None

        self.show()

    def update_from_app(self):
        lat, lng, speed = (
            self.car_nav_controller.get_location_speed()
        )

        if speed is not None:
            self.update_speed(speed)

        self.update_location(lat, lng)

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
                "border:3px solid #333333;"
                "border-radius: 5px;"
            )

            label = QLabel(name)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("background: transparent; border: none;")

            layout = QVBoxLayout(widget)
            layout.setContentsMargins(2, 2, 2, 2)
            layout.addWidget(label)

    def apply_styling(self):
        self.central_widget.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #E0E0E0;
                font-family: Arial;
            }

            QLabel {
                border: none;
                background: transparent;
            }

            QPushButton {
                background-color: #303030;
                border: 1px solid #444444;
                border-radius: 8px;
                padding: 8px;
                color: #E0E0E0;
            }

            QPushButton:pressed {
                background-color: #505050;
            }

            QLineEdit {
                background-color: #303030;
                border: 1px solid #444444;
                border-radius: 8px;
                padding: 8px;
                color: #E0E0E0;
            }

            QProgressBar {
                background-color: #303030;
                border: 1px solid #444444;
                border-radius: 8px;
                text-align: center;
            }

            QProgressBar::chunk {
                background-color: #888888;
                border-radius: 7px;
            }
        """)

        self.speed_widget.setStyleSheet(
            "font-size: 22px; font-weight: bold;"
        )

        self.name_widget.setStyleSheet(
            "font-size: 20px; font-weight: bold;"
        )

        self.time_widget.setStyleSheet(
            "font-size: 16px;"
        )

        self.location_widget.setStyleSheet(
            "font-size: 13px;"
        )

        self.eta_widget.setStyleSheet(
            "font-size: 15px; font-weight: bold;"
        )

    def on_list_turns_presses(self):
        print("list turns")

    def on_stop_route_pressed(self):
        self.car_nav_controller.NavigationController.clear_route()

        self.car_nav_controller.GPSManager.stop()

        self.destination = None

        self.update_eta()
        self.update_progress(0)

        lat, lng = self.car_nav_controller.get_location()
        self.update_map(lat, lng)

    def create_map(self, latitude, longitude, zoom_start, route=None):
        map = folium.Map(
            location=[latitude, longitude],
            zoom_start=zoom_start,
            tiles="OpenStreetMap"
        )

        folium.Marker(
            [latitude, longitude],
            tooltip="Current Location",
            icon=folium.Icon(color="red")
        ).add_to(map)

        if route:
            folium.PolyLine(
                route,
                color="blue",
                weight=5
            ).add_to(map)

        return map

    def update_speed(self, speed=0):
        self.speed_widget.setText(f"{speed:.0f} km/h")


    def update_time(self):
        from datetime import datetime

        current_time = datetime.now().strftime("%H:%M")
        self.time_widget.setText(current_time)


    def update_location(self, latitude=None, longitude=None):
        if latitude is None or longitude is None:
            self.location_widget.setText("GPS: No Location")
        else:
            self.location_widget.setText(
                f"{latitude:.5f}, {longitude:.5f}"
            )


    def update_eta(self, minutes=None):
        if minutes is None:
            self.eta_widget.setText("ETA: -- min")
        else:
            self.eta_widget.setText(
                f"ETA: {minutes:.0f} min"
            )


    def update_progress(self, progress=0):
        self.animation_widget.setValue(
            max(0, min(100, int(progress)))
        )

    def update_map(self, latitude, longitude,zoom_start, route=None):
        self.map = self.create_map(
            latitude,
            longitude,
            zoom_start=zoom_start,
            route=route
        )

        self.map_widget.setHtml(
            self.map.get_root().render()
        )

    def find_destination(self):
        try:
            # Read the coordinates entered by the user
            text = self.dest_select_widget.text()

            latitude, longitude = map(
                float, text.split(",")
            )

            # Check that coordinates are valid
            if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
                raise ValueError("Coordinates out of range")

        except ValueError:
            print("Invalid destination coordinates")
            return

        # Ask the main application to calculate a route
        route = self.car_nav_controller.set_destination(
            latitude, longitude
        )

        if route is None:
            print("Unable to calculate route")
            return

        # Get current GPS location
        current_lat, current_lng = (
            self.car_nav_controller.get_location()
        )

        # Display the calculated route
        self.update_map(
            current_lat,
            current_lng,
            route=route
        )

        # Display estimated travel time
        minutes = (
            self.car_nav_controller
            .NavigationController
            .calculate_estimated_time()
        )

        self.update_eta(minutes)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setApplicationName("CarNav")

    w = MainWindow("temp")
    w.update_speed(60)
    w.update_location(-35.325833, 149.057750)
    w.update_eta(8)
    w.update_progress(35)

    sys.exit(app.exec_())
