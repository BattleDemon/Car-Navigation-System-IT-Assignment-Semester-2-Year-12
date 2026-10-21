
import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QColor, QPainter, QPen, QBrush, QFont
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QStackedLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QListWidget,
    QSizePolicy,
)

debug = False


class JourneyAnimation(QWidget):
    def __init__(self):
        super().__init__()

        self.progress = 0
        self.setMinimumWidth(130)
        self.setMinimumHeight(55)

    def set_progress(self, progress):
        # Journey progress is between 0 and 100 percent.
        self.progress = max(0, min(100, progress))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()

        start_x = 20
        end_x = width - 20
        road_y = height // 2 + 5

        # Draw the road/progress track.
        painter.setPen(QPen(QColor("#475569"), 5))
        painter.drawLine(start_x, road_y, end_x, road_y)

        # Draw the completed portion of the journey.
        current_x = start_x + (
            (end_x - start_x) * self.progress / 100
        )

        painter.setPen(QPen(QColor("#38bdf8"), 5))
        painter.drawLine(
            start_x, road_y,
            int(current_x), road_y
        )

        # Draw a small car travelling along the road.
        car_x = int(current_x)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor("#f8fafc")))

        painter.drawRoundedRect(
            car_x - 12,
            road_y - 14,
            24,
            11,
            3,
            3
        )

        # Wheels
        painter.setBrush(QBrush(QColor("#0f172a")))
        painter.drawEllipse(car_x - 9, road_y - 5, 5, 5)
        painter.drawEllipse(car_x + 5, road_y - 5, 5, 5)

        painter.end()


class MainWindow(QMainWindow):

    destinationRequested = pyqtSignal(str)
    stopRouteRequested = pyqtSignal()
    recenterRequested = pyqtSignal()
    zoomInRequested = pyqtSignal()
    zoomOutRequested = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CarNav")
        self.resize(720, 480)
        self.setMinimumSize(640, 400)

        self.current_speed = None
        self.speed_limit = None

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.central_vlayout = QVBoxLayout(
            self.central_widget
        )
        self.central_vlayout.setContentsMargins(5, 5, 5, 5)
        self.central_vlayout.setSpacing(5)

        # Main layouts
        self.top_hlayout = QHBoxLayout()
        self.middle_slayout = QStackedLayout()
        self.bottom_hlayout = QHBoxLayout()

        self.middle_slayout.setStackingMode(
            QStackedLayout.StackAll
        )

        self.central_vlayout.addLayout(
            self.top_hlayout
        )
        self.central_vlayout.addLayout(
            self.middle_slayout, 1
        )
        self.central_vlayout.addLayout(
            self.bottom_hlayout
        )

        self.top_hlayout.setSpacing(5)
        self.bottom_hlayout.setSpacing(5)

        # ---------------- Top bar ----------------

        self.speed_widget = QFrame()
        self.location_widget = QFrame()
        self.name_time_widget = QFrame()

        self.speed_widget.setObjectName("speed_widget")
        self.location_widget.setObjectName("location_widget")
        self.name_time_widget.setObjectName(
            "name_time_widget"
        )

        for widget in (
            self.speed_widget,
            self.location_widget,
            self.name_time_widget
        ):
            widget.setFixedHeight(75)

        self.speed_widget.setFixedWidth(110)
        self.name_time_widget.setFixedWidth(115)

        self.top_hlayout.addWidget(self.speed_widget)
        self.top_hlayout.addWidget(
            self.location_widget, 1
        )
        self.top_hlayout.addWidget(self.name_time_widget)

        # Speed display
        speed_layout = QVBoxLayout(self.speed_widget)
        speed_layout.setContentsMargins(4, 3, 4, 3)
        speed_layout.setSpacing(0)

        self.speed_label = QLabel("--")
        self.speed_label.setObjectName("speed_value")
        self.speed_label.setAlignment(Qt.AlignCenter)

        self.speed_limit_label = QLabel("Limit: --")
        self.speed_limit_label.setObjectName("secondary")
        self.speed_limit_label.setAlignment(Qt.AlignCenter)

        speed_layout.addWidget(self.speed_label)
        speed_layout.addWidget(self.speed_limit_label)

        # Current location
        location_layout = QVBoxLayout(
            self.location_widget
        )
        location_layout.setContentsMargins(12, 6, 12, 6)
        location_layout.setSpacing(4)

        self.location_title = QLabel("CURRENT LOCATION")
        self.location_title.setObjectName("secondary")

        self.location_label = QLabel(
            "Location unavailable"
        )
        self.location_label.setObjectName(
            "location_value"
        )

        self.gps_label = QLabel("GPS: Waiting")
        self.gps_label.setObjectName("secondary")

        location_layout.addWidget(self.location_title)
        location_layout.addWidget(self.location_label)
        location_layout.addWidget(self.gps_label)

        # Application name and time
        name_time_layout = QVBoxLayout(
            self.name_time_widget
        )
        name_time_layout.setContentsMargins(5, 5, 5, 5)

        self.name_label = QLabel("CarNav")
        self.name_label.setObjectName("app_name")
        self.name_label.setAlignment(Qt.AlignCenter)

        self.time_label = QLabel()
        self.time_label.setObjectName("secondary")
        self.time_label.setAlignment(Qt.AlignCenter)

        name_time_layout.addWidget(self.name_label)
        name_time_layout.addWidget(self.time_label)

        # ---------------- Middle map ----------------

        self.map_widget = QFrame()
        self.map_widget.setObjectName("map_widget")

        map_layout = QVBoxLayout(self.map_widget)

        self.map_placeholder = QLabel(
            "Offline Map\nNot connected"
        )
        self.map_placeholder.setObjectName(
            "map_placeholder"
        )
        self.map_placeholder.setAlignment(Qt.AlignCenter)

        map_layout.addWidget(self.map_placeholder)

        # Transparent controls layer over the map
        self.middle_glayout_widget = QWidget()
        self.middle_glayout_widget.setObjectName(
            "overlay_widget"
        )

        self.middle_glayout = QGridLayout(
            self.middle_glayout_widget
        )
        self.middle_glayout.setContentsMargins(
            10, 10, 10, 10
        )
        self.middle_glayout.setSpacing(5)

        # Map buttons
        self.recenter_button = QPushButton("◎")
        self.zoom_in_button = QPushButton("+")
        self.zoom_out_button = QPushButton("−")
        self.nodes_button = QPushButton("☷")

        self.map_buttons = [
            self.recenter_button,
            self.zoom_in_button,
            self.zoom_out_button,
            self.nodes_button
        ]

        for button in self.map_buttons:
            button.setObjectName("map_button")
            button.setFixedSize(45, 45)

        self.recenter_button.setToolTip(
            "Recentre map"
        )
        self.zoom_in_button.setToolTip("Zoom in")
        self.zoom_out_button.setToolTip("Zoom out")
        self.nodes_button.setToolTip(
            "Upcoming route nodes"
        )

        # Place the map buttons vertically on the right
        self.map_controls = QVBoxLayout()
        self.map_controls.setSpacing(5)

        for button in self.map_buttons:
            self.map_controls.addWidget(button)

        self.map_controls.addStretch()

        self.middle_glayout.addLayout(
            self.map_controls,
            0, 1,
            Qt.AlignTop | Qt.AlignRight
        )

        # Upcoming nodes panel
        self.nodes_panel = QFrame()
        self.nodes_panel.setObjectName("nodes_panel")
        self.nodes_panel.setFixedWidth(210)

        nodes_layout = QVBoxLayout(self.nodes_panel)

        self.nodes_title = QLabel("Upcoming Nodes")
        self.nodes_title.setObjectName("panel_title")

        self.nodes_list = QListWidget()

        nodes_layout.addWidget(self.nodes_title)
        nodes_layout.addWidget(self.nodes_list)

        self.nodes_panel.hide()

        self.middle_glayout.addWidget(
            self.nodes_panel,
            0, 0,
            Qt.AlignTop | Qt.AlignLeft
        )

        self.middle_glayout.setColumnStretch(0, 1)
        self.middle_glayout.setRowStretch(1, 1)

        self.middle_slayout.addWidget(self.map_widget)
        self.middle_slayout.addWidget(
            self.middle_glayout_widget
        )
        self.middle_slayout.setCurrentWidget(
            self.middle_glayout_widget
        )

        self.recenter_button.clicked.connect(
            self.recenterRequested.emit
        )
        self.zoom_in_button.clicked.connect(
            self.zoomInRequested.emit
        )
        self.zoom_out_button.clicked.connect(
            self.zoomOutRequested.emit
        )
        self.nodes_button.clicked.connect(
            self.toggle_nodes
        )

        # ---------------- Bottom bar ----------------

        self.stop_route_widget = QPushButton(
            "Stop\nRoute"
        )
        self.animation_widget = QFrame()
        self.eta_widget = QFrame()
        self.dest_select_widget = QFrame()

        self.stop_route_widget.setObjectName(
            "stop_route_widget"
        )
        self.animation_widget.setObjectName(
            "animation_widget"
        )
        self.eta_widget.setObjectName("eta_widget")
        self.dest_select_widget.setObjectName(
            "dest_select_widget"
        )

        for widget in (
            self.stop_route_widget,
            self.animation_widget,
            self.eta_widget,
            self.dest_select_widget
        ):
            widget.setFixedHeight(75)

        self.stop_route_widget.setFixedWidth(85)
        self.eta_widget.setFixedWidth(95)
        self.dest_select_widget.setMinimumWidth(160)

        self.stop_route_widget.clicked.connect(
            self.stopRouteRequested.emit
        )

        # Journey progress animation
        animation_layout = QVBoxLayout(
            self.animation_widget
        )
        animation_layout.setContentsMargins(
            6, 4, 6, 4
        )
        animation_layout.setSpacing(0)

        self.journey_animation = JourneyAnimation()

        self.progress_label = QLabel("Journey: 0%")
        self.progress_label.setObjectName("secondary")
        self.progress_label.setAlignment(Qt.AlignCenter)

        animation_layout.addWidget(
            self.journey_animation, 1
        )
        animation_layout.addWidget(self.progress_label)

        # ETA
        eta_layout = QVBoxLayout(self.eta_widget)
        eta_layout.setContentsMargins(4, 4, 4, 4)
        eta_layout.setSpacing(0)

        self.eta_label = QLabel("-- min")
        self.eta_label.setObjectName("eta_value")
        self.eta_label.setAlignment(Qt.AlignCenter)

        self.eta_title = QLabel("Travel time")
        self.eta_title.setObjectName("secondary")
        self.eta_title.setAlignment(Qt.AlignCenter)

        eta_layout.addWidget(self.eta_label)
        eta_layout.addWidget(self.eta_title)

        # Destination selection
        dest_layout = QVBoxLayout(
            self.dest_select_widget
        )
        dest_layout.setContentsMargins(6, 5, 6, 5)

        self.destination_title = QLabel(
            "DESTINATION"
        )
        self.destination_title.setObjectName("secondary")

        dest_input_layout = QHBoxLayout()
        dest_input_layout.setSpacing(4)

        self.destination_input = QLineEdit()
        self.destination_input.setPlaceholderText(
            "Enter destination"
        )

        self.destination_button = QPushButton("Go")
        self.destination_button.setObjectName(
            "primary_button"
        )
        self.destination_button.setFixedWidth(40)

        dest_input_layout.addWidget(
            self.destination_input
        )
        dest_input_layout.addWidget(
            self.destination_button
        )

        dest_layout.addWidget(self.destination_title)
        dest_layout.addLayout(dest_input_layout)

        self.destination_button.clicked.connect(
            self.request_destination
        )
        self.destination_input.returnPressed.connect(
            self.request_destination
        )

        self.bottom_hlayout.addWidget(
            self.stop_route_widget
        )
        self.bottom_hlayout.addWidget(
            self.animation_widget, 1
        )
        self.bottom_hlayout.addWidget(
            self.eta_widget
        )
        self.bottom_hlayout.addWidget(
            self.dest_select_widget, 1
        )

        # ---------------- Styling ----------------

        self.setStyleSheet(self.get_stylesheet())

        # ---------------- Clock ----------------

        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(
            self.update_clock
        )
        self.clock_timer.start(1000)

        self.update_clock()

    # ---------------- UI functions ----------------

    def update_clock(self):
        self.time_label.setText(
            datetime.now().strftime("%H:%M")
        )

    def set_speed(self, speed):
        self.current_speed = speed

        if speed is None:
            self.speed_label.setText("--")
        else:
            self.speed_label.setText(
                str(round(speed))
            )

        self.update_speed_colour()

    def set_speed_limit(self, limit):
        self.speed_limit = limit

        if limit is None:
            self.speed_limit_label.setText(
                "Limit: --"
            )
        else:
            self.speed_limit_label.setText(
                f"Limit: {round(limit)} km/h"
            )

        self.update_speed_colour()

    def update_speed_colour(self):
        # Highlight speeding when both the GPS speed
        # and estimated speed limit are available.
        speeding = (
            self.current_speed is not None
            and self.speed_limit is not None
            and self.current_speed > self.speed_limit
        )

        self.speed_widget.setProperty(
            "speeding", speeding
        )

        self.speed_widget.style().unpolish(
            self.speed_widget
        )
        self.speed_widget.style().polish(
            self.speed_widget
        )

        self.speed_widget.update()

    def set_location(self, location):
        self.location_label.setText(str(location))

    def set_gps_status(self, connected):
        if connected:
            self.gps_label.setText(
                "GPS: Connected"
            )
        else:
            self.gps_label.setText(
                "GPS: Waiting"
            )

    def set_eta(self, minutes):
        if minutes is None:
            self.eta_label.setText("-- min")
        else:
            self.eta_label.setText(
                f"{round(minutes)} min"
            )

    def set_journey_progress(self, progress):
        progress = max(0, min(100, progress))

        self.journey_animation.set_progress(
            progress
        )

        self.progress_label.setText(
            f"Journey: {round(progress)}%"
        )

    def set_upcoming_nodes(self, nodes):
        # Display node IDs or descriptions supplied
        # by the navigation system.
        self.nodes_list.clear()

        for node in nodes:
            self.nodes_list.addItem(str(node))

    def toggle_nodes(self):
        self.nodes_panel.setVisible(
            not self.nodes_panel.isVisible()
        )

    def request_destination(self):
        destination = self.destination_input.text().strip()

        if destination:
            self.destinationRequested.emit(
                destination
            )

    def clear_navigation(self):
        self.destination_input.clear()
        self.set_eta(None)
        self.set_journey_progress(0)
        self.set_speed_limit(None)
        self.set_upcoming_nodes([])
        self.nodes_panel.hide()

    # ---------------- Styling ----------------

    def get_stylesheet(self):
        style = """
            QWidget {
                background-color: #242424;
                color: #eeeeee;
                font-family: "DejaVu Sans";
                font-size: 12px;
            }

            QLabel {
                background: transparent;
            }

            QFrame {
                background-color: #303030;
            }

            QFrame#map_widget {
                background-color: #d2d2ca;
            }

            QPushButton {
                background-color: #404040;
                border: 1px solid #606060;
                border-radius: 2px;
                padding: 5px;
            }

            QPushButton:pressed {
                background-color: #606060;
            }

            QLineEdit {
                background-color: #353535;
                border: 1px solid #606060;
                padding: 5px;
            }

            QLabel#speed_value {
                font-size: 32px;
                font-weight: bold;
            }

            QFrame#speed_widget[speeding="true"] {
                background-color: #a52626;
            }

            QFrame#speed_widget[speeding="true"] QLabel {
                color: white;
            }

            QWidget#overlay_widget {
                background: transparent;
            }
        """

        if debug:
            style += """
                QFrame {
                    border: 1px dashed orange;
                }
            """

        return style


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    # Example information for UI testing
    window.set_speed(54)
    window.set_speed_limit(50)
    window.set_location("Weston Creek, ACT")
    window.set_gps_status(True)
    window.set_eta(12)
    window.set_journey_progress(35)

    window.set_upcoming_nodes([
        "Node: 1809023157",
        "Node: 24558260",
        "Node: 77137888",
    ])

    window.destinationRequested.connect(
        lambda destination: print(
            "Destination:", destination
        )
    )

    window.stopRouteRequested.connect(
        window.clear_navigation
    )

    window.recenterRequested.connect(
        lambda: print("Recentre requested")
    )

    window.zoomInRequested.connect(
        lambda: print("Zoom in requested")
    )

    window.zoomOutRequested.connect(
        lambda: print("Zoom out requested")
    )

    window.show()

    sys.exit(app.exec_())
