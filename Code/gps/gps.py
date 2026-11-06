import serial
import pynmea2
import _thread

# location of gps port
GPS_PORT = "/dev/ttyAMA0"


# GPS manager class
class GPSManager:
    def __init__(self):
        self.port = GPS_PORT
        self.lat = None
        self.lng = None

        # km/h
        self.speed = None

        # Set a refrence to the gps's serial data
        self.ser = serial.Serial(self.port, baudrate=9600, timeout=0.5)

        # Create thread for gps location update
        self.running = True
        self.update_thread = _thread.start_new_thread(self._update)
        

    def _update(self):
        while self.running:
            try:
                rawdata = self.ser.readline().decode(
                    "ascii", errors="ignore"
                ).strip()

                # Only process valid RMC messages
                if not rawdata.startswith(("$GNRMC", "$GPRMC")):
                    continue

                data = pynmea2.parse(rawdata)

                # Ignore messages without a valid GPS fix
                if data.status != "A":
                    continue

                lat = data.latitude
                lng = data.longitude

                # Convert speed from knots to km/h
                speed_knots = float(data.spd_over_grnd or 0)
                speed = speed_knots * 1.852

                self._set_location_speed(lat, lng, speed)

            except (pynmea2.ParseError, ValueError):
                continue

            except (serial.SerialException, OSError):
                if self.running:
                    print("GPS connection lost")
                break

    def get_location_speed(self):  # Called by other files when needed to get location
        return [self.lat, self.lng, self.speed]

    # Set location in class
    def _set_location_speed(self, lat, lng, speed):
        self.lat = lat
        self.lng = lng
        self.speed = speed

    def stop(self):
        self.running = False
        self.ser.close()
