import folium
from folium import plugins

def create_map(latitude, longitude, zoom_start=18):
    """
    Create an interactive map with a custom marker at specified coordinates.
    
    Parameters:
    latitude (float): Latitude of the location
    longitude (float): Longitude of the location
    zoom_start (int): Initial zoom level of the map (default: 12)
    
    Returns:
    folium.Map: Interactive map object
    """
    # Create a map centered at the specified location
    m = folium.Map(location=[latitude, longitude], 
                   zoom_start=zoom_start,
                   tiles='OpenStreetMap')
    
    # Add a marker with a popup
    folium.Marker(
            [latitude, longitude],
            icon=folium.Icon(color='red', icon='ion.car-sport-outline')
        ).add_to(m)
    
    # Add fullscreen button
    plugins.Fullscreen().add_to(m)
    
    # Add location finder
    plugins.LocateControl().add_to(m)
    
    return m

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MapWindow(QMainWindow):
    def __init__(self, latitude, longitude, zoom_start=12):
        super().__init__()
        
        # Create the map
        self.map = create_map(latitude, longitude, zoom_start)
        
        # Save the map to an HTML file
        self.map.save('map.html')
        
        # Create a QWebEngineView widget
        self.browser = QWebEngineView()
        
        # Load the HTML content into the QWebEngineView
        self.browser.setHtml(self.map.get_root().render())
        
        # Set the central widget of the MainWindow to the QWebEngineView
        self.setCentralWidget(self.browser)
        
        # Set the window title
        self.setWindowTitle('Folium Map with PyQt5')
        
        # Set the window size
        self.resize(800, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Example coordinates 
    latitude = -35.3265
    longitude = 149.053


    #35°19'35.0"S 149°03'32.3"E
    
    # Create the main window
    window = MapWindow(latitude, longitude)
    window.show()
    
    # Run the application
    sys.exit(app.exec_())