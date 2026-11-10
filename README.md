# CarNav 
<div style="text-align: right;"> Dexter Hart </div>

## Proposal 

### Project Overview

I intend to design and produce an integrated system for GPS navigation, which will be similar to commercial options such as Garmin, or Navig8r. It will use a Raspberry Pi 5, GPS receiver, and touch screen, for the physical system. While connected with a PyQT UI, and python route calculation using OpenStreetData. It is designed for my own use, as a test of my skills, and to learn new systems. As I should soon get my provisional license, and my car doesn't have a navigation system of its own, along with the restrictions to phone, I found it useful and within my ability to make my own. 

### Research

#### Commercial Systems and Other Alternatives

Existing navigation systems form in two categories of hardware and software. With dedicated GPS systems such as Garmin and Navig8r, useing inbuilt GPS receiver, processor, storage, and a touchscreen, combined into a single device. With these devices ranging in price form $100 - $1000, while my system should be around $300, and repurposable in the future. These standalone devices are often used offline, and store their maps locally, but prevents traffic or map updates.

Software such as Google Maps, Waze, and Organic Maps offer a system that utilised your phone or other hardware. With Google Maps and Waze providing features such as live traffic, automatic rerouting, and frequent updates, although these depend on an active internet connection. While Organic Maps, acts fully offline with navigation possible using open street maps similar to my proposed project.
#### Data Sources

Navigation systems require detailed geographical data, including roads, intersections, and points of interest. With commercial options such as HERE Technologies, TomTom, and Google Maps offering accurate datasets and other services like traffic information, but their licensing cost range from HERE and TomTom, which offer free initial use but with steep prices if those limits are breach, and google starting at $100 per month causing too many risks especially if my code is inefficient or making too many API calls. This combined with excellent free and open source options been available such as OpenStreetMaps. Which contains roads, intersections, and some additional data, making it susceptible for my needs. Although the quality for some regions can vary, although this shouldn't be as big of a problem since, it will be primarily used within the ACT which has been mapped. 
#### Route Calculation Algorithms

Route calculations rely on graph based search algorithms to determine the most efficient path between two locations. Dijkstra's Algorithm is one of the most well known and is generally efficient at finding the optimal routes but can become ineffective on larger road networks. With A* improving on this by less perfectionist search, reducing the number of paths checked while still been usable. More advanced option can also be used, such as a Bidirectional search either A* or Dijkstra's, allowing it to search from start to end and end to start. Along with Contraction Hierarchies, which reduces the use of smaller streets in the algorithm. Companies don't publicly showcase their algorithms, but most are adaptations of A* or Dijkstra's, with some combining historic traffic in the weighting. Due to the scale of this project and complexities in this assignment I will be using A* with possibilities for growth. 

### Core Features / Minimal Viable Product

The core features will consist of an offline navigation system integrating custom hardware and software. The system will be built around a Raspberry Pi 5 with a GPS receiver and touchscreen display. The software will interpret GPS data to determine the user's location and display this position using locally stored OpenStreetMap data through a Qt-based UI. The interface will include destination searching, triggering route calculation.

### Beyond Minimum Viable Product

#### Expanded Route Algorithm
Implement bidirectional and heirachical, and or offline traffic estimations. 
#### Additional UI Features
Be able to have multi destination routes, saved locations, along with other user settings.
#### Voice Instructions
Add "Turn Left", "Turn Right" notifications, require adding a speaker or integration into the cars speaker.
#### 3D Printed Chassis 
3D model and print a chassis designed to mount the system in my car. 

### Timeline

##### Milestone 1: Research and Initial set up 
Start/End Date: Project assigned - 7th August

Research navigation systems and algorithms
Research OpenStreetMap data, format, and download
Setup rough file structure and plan
Setup raspberry pi
Test hardware

##### Milestone 2: Extract data and GPS system
Start/End Date: 7th August - 19th August

Connect GPS to Raspberry Pi
Decode GPS NMEA data
Transform into usable location data
Import and process OpenStreetMap data
link GPS location and map
Test GPS in multiple locations and in differing conditions

##### Milestone 3: Navigation Backend
Start/End Date: 19th August - 3rd September

Create testing node route system
Implement and test A* 
Optimise route calculation 
Test routes using various data / route length

##### Milestone 4: UI and Last MVP
Start/End Date: 3rd - 17th September

Make Qt touchscreen UI
Render map
Display current location
Add destination search
Render route information
Integrate GPS, routing, and UI as one thing
Complete the minimum viable product

##### Milestone 5: Stress Testing and Documenting
Start/End Date: 17th September - 25th 

Test navigation accuracy IRL in many situations
Test different routes, accuracy, and compare to other alternatives
Complete MVP documentation

Steps following MVP might not follow same order as shown and all have same time frame

##### Milestone 6: Stretch Goal - Expanded route Algorithm
Start/End Date: 25th September - 6th November

Implement bidirectional search into testing program
Implement heirachical into testing program
Improve on algorithm and test various cases
Implement into full program

##### Milestone 7: Stretch Goal - Voice Instructions
Start/End Date: 25th September - 6th November

Research into connecting into car speaker or deticated speakers 
Implement best option
Record voice lines
Connect to full system

##### Milestone 8: Stretch Goal - UI Improvements and addional features
Start/End Date: 25th September - 6th November

Research into similar options specifically their UI
Test how other individuals find my UI
Improve on others suggestions
Implement found features 
Implement multi location search
Allow user settings

##### Milestone 9: Stretch Goal - 3D printed chassis
Start/End Date: 25th September - 6th November

Design 3D printed chassis
Print chassis
mount chassis 
Test system in car with chassis
Test system with other drivers

### Proposal Bibliography

Codecademy 2025, _A complete guide to Dijkstra’s shortest path algorithm_, _Codecademy_, viewed 6 August 2026, <https://www.codecademy.com/article/dijkstras-shortest-path-algorithm>.

Gakstatter, E 2015, _What exactly is GPS NMEA data?_, _GPS World_, 4 February, viewed 6 August 2026, <https://www.gpsworld.com/what-exactly-is-gps-nmea-data/>.

Garmin 2026, _Garmin product updates_, Garmin.com, viewed 6 August 2026, <https://aoem.garmin.com/>.

GeeksforGeeks 2012, _Dijkstra’s algorithm to find shortest paths from a source to all_, _GeeksforGeeks_, 25 November, viewed 6 August 2026, <https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/>.

GeeksforGeeks 2016, _A* search algorithm_, _GeeksforGeeks_, 16 June, viewed 6 August 2026, <https://www.geeksforgeeks.org/dsa/a-search-algorithm/>.

GeeksforGeeks 2017, _Bidirectional search_, _GeeksforGeeks_, 11 June, viewed 6 August 2026, <https://www.geeksforgeeks.org/dsa/bidirectional-search/>.

Google 2025, _Google maps platform pricing - subscriptions and pay as you go_, _Google Maps Platform_, viewed 6 August 2026, <https://mapsplatform.google.com/pricing/#pay-as-you-go>.

Here 2026, _HERE base plan | location services | pricing | HERE_, _www.here.com_, viewed 6 August 2026, <https://www.here.com/get-started/pricing>.

Lazarsfeld, J 2018, _1-Intro_, Contraction Hierarchies Guide, viewed 6 August 2026, <https://jlazarsfeld.github.io/ch.150.project/sections/1-intro/>.

LazerCo 2026, ‘Laser corporation product feed’, _Laserco.com.au_, viewed 6 August 2026, <https://www.laserco.com.au/brands/navig8r>.

Navigation Systems Authority Network America 2026, _Navigation map data providers: Comparing HERE, TomTom, Google, and others_, Navigation Systems Authority, viewed 6 August 2026, <https://navigationsystemsauthority.com/map-data-providers-comparison/>.

Navone, EC 2020, _Dijkstra’s shortest path algorithm - a detailed and visual introduction_, _freeCodeCamp.org_, 28 September, viewed 6 August 2026, <https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/>.

Open Street Map 2026, _OpenStreetMap_, OpenStreetMap, viewed 6 August 2026, <https://www.openstreetmap.org/#map=11/-35.2891/149.1466>.

Organic Maps 2025, _Organic Maps: Offline Hike, Bike, Trails and Navigation_, _organicmaps.app_, viewed 6 August 2026, <https://organicmaps.app/>.

Patel, A 1997, _Introduction to A*_, _theory.stanford.edu_, viewed 6 August 2026, <https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html>.

TomTom 2026, _Pricing_, TomTom Documentation, viewed 6 August 2026, <https://docs.tomtom.com/pricing>.

Waze 2026, _Driving directions, live traffic & road conditions updates_, _Waze_, viewed 6 August 2026, <https://www.waze.com/live-map>.



## Development and Design Thinking

### Developing Minimum Viable Project

#### Milestone 1: Initial set up of the Raspberry Pi 

This milestone was the simplest to complete as it only involved, the ordering of parts and their initial setup. 


#### Milestone 2: Gathering and Extraction of data and GPS System

This is where the actual development and coding began, along with the gathering of data that will allow for the future systems. This began with finding the 

#### Milestone 3: Navigation and Backend

This is the step where i fell behind and other assignments took the primary focus of my attention

#### Milestone 4: UI 

#### Milestone 5: Stress Testing
### Expanding on Minimum Viable Project

## Evaluation and Review

### 1. Planning
#### What aspects of your original plan were successful?

- Was the original concept of an offline navigation system achievable using the hardware and software you selected?
		The original concept was technically achievable although i was unable to, due to the map processing requiring an internet connection to stream the map tiles. But if that wasn't a factor the system could be run offline in the car, but with possible concerns around power supply from a car engine, to a raspberry pi possibly causing problems when the engine is turned off.
    
- Which parts of your initial research proved useful during development?
		Most of the initial research was useful for development, although not all directly, with it giving me the rough info on how to implement systems, but not the specifics.
    
- Was choosing Python, PyQt5 and OpenStreetMap appropriate for this project?
		PyQt5 was suficient for the ui of my app, and was useful due to it already been a library we had worked with in the past, so i didn't have to learn a whole new library, compared to if i had used tkinter or someother python ui.
    
- Was dividing the project into five main milestones helpful for organising development?
	    It was helpful, but I struggled to follow them, as other assignments got in the way, and its distance from due date, made it feel more like a task i could set aside for later. But it was the rough structure of what i developed in order, although not at the planned upon times.
    
- Which parts of the original plan did you follow most closely?
	    Milestone 1 and 2, whith it startin to fall apart around milestone 3, when other assingments drew my attention, and it required me to research how to handle the datasets, and i kept falling into pitfalls of other steps, such as spliting geojsons, and osms so they could be loaded when needed, and making an early loading system, which i was unable to integrate in the end. 

#### What aspects were unsuccessful?

- Which parts of the project were more complicated than you originally expected?
    
- Did you underestimate how long processing OpenStreetMap data would take?
		Yes this took almost two weeks of trying to spit the files, geojsons, then making a loading sytem, then also the navigation backend which i used a few libraries for before landing on the final one, after i founf the others didn't have what i needed.
    
- Was the original timeline realistic, particularly the plan to complete the MVP by 17 September?
		It probably wasn't entirely realistic but if i had done more work then i had out of class, i most likely could of finished around when i originally intended.
    
- Were there any dependencies between different systems that you failed to account for?
		As said before, also i intended to have my own map presenting system instead of using an already made library.
    
- Did your original planning include enough time for debugging and integration?
	    I did provide enough for debugging, but failed to see that this type of project requires interconnected systems to be made one by one unable to test in its truth until the end, and unable to integrate.

#### What changes did you make and why?

- Why did you decide to divide the ACT's map data into smaller geographic regions?
		So it wouldn't all be loaded into the raspberry pi's ram, so i though it would be better to load a small region,  which i spent quite a while preparing without any actual turnout, as i didn't have time to connect the system.
    
- How did your approach to route calculation change during development?
	Initially i wanted to make my own route calculation then i wanted to do my own implementation of a known route algorithm, before i ended up using a library.
    
- Did you change your intended UI design? What motivated those changes?
		The ui wasn't defined well from the begining, so i ran a suvey like thing amoung my IT peers having each of the other three draw their favoured ui for a car navigator, which i used as basis to design my own before implementing it.
    
- Were these changes improvements to the original design, or compromises made because of time constraints?
	    compromised for library things, but improvements for the ui.

### 2. Development

#### What technical challenges did you encounter?

Hardware and GPS

- Were there any difficulties connecting the GPS receiver to the Raspberry Pi?
    
- Did you encounter problems interpreting NMEA messages or obtaining accurate location data?
    
- Why did you change the GPS program into an object-oriented class?
    
- Did GPS accuracy vary between indoor, window and outdoor testing?
    

Map data

- What happened when you attempted to load the larger OpenStreetMap datasets?
    
- How did memory usage affect your approach?
    
- What difficulties did you encounter when dividing OSM data using GeoJSON boundaries?
    
- Were there problems identifying which geographic region contained the user's location?
    

Navigation

- What difficulties did you encounter converting road data into a usable graph?
    
- Were there any problems identifying the nearest road node to a GPS location?
    
- Did A* initially produce incorrect routes, errors or unexpected results?
    
- What problems occurred when calculating route distances or estimated travel times?
    

User interface

- What difficulties did you encounter developing the PyQt5 interface?
    
- Did you have to redesign any parts of the layout?
    
- What happened when you connected the map display to the navigation backend?
    
- Why did the map zoom reset during updates?
    
- Why did the calculated route sometimes remain behind the user's position?
    

#### How did you overcome them?

- How did you identify the causes of these problems?
    
- Did you use separate testing programs to isolate individual systems?
    
- Which problems required research into documentation or external resources?
    
- Did you experiment with multiple possible solutions before finding one that worked?
    
- Were there any problems you couldn't completely resolve?
    
- Which technical solution had the greatest effect on the project?
    

### 3. Project Management

#### How effectively did you manage your time?

- How closely did your actual development follow the original milestone dates?
    
- Which milestones took significantly longer than expected?
    
- How much time did you spend on map data processing compared with navigation and UI development?
    
- How did other assignments affect your available development time?
    
- What happened during the period between 23 September and 13 October when there were no recorded commits?
    
- Did you work consistently throughout the semester, or did most progress occur closer to the deadline?
    
- How did falling behind affect the quality or completeness of the final product?
    
- Did you leave enough time for testing and documentation?
    

#### What would you do differently?

- Would you allocate more time to any particular milestone?
    
- Would you develop a basic working version using a small map before attempting the entire ACT?
    
- Would you begin integrating the GPS, navigation and UI systems earlier?
    
- Would you establish more frequent testing checkpoints?
    
- How could you improve your Git commit messages and development documentation?
    
- Would you change how you prioritised this project against your other assignments?
    
- How would you organise the project differently to avoid leaving so much work until the final weeks?
    

### 4. Skills

#### What new skills did you learn?

- What did you learn about configuring and programming a Raspberry Pi?
    
- How did working with a GPS receiver improve your understanding of serial communication and NMEA data?
    
- What did you learn about OpenStreetMap, OSM PBF files and GeoJSON?
    
- How did your understanding of geographic coordinates and spatial data develop?
    
- What did implementing A* teach you about graphs and pathfinding algorithms?
    
- What did you learn about building graphical interfaces using PyQt5?
    
- What did you learn about connecting multiple independent software components into one application?
    

#### Which skills improved most?

- How did your Python programming abilities change between the beginning and end of the project?
    
- Did your understanding of classes and object-oriented programming improve?
    
- Did you become better at debugging errors and identifying their causes?
    
- Did you improve at researching unfamiliar libraries and understanding their documentation?
    
- How did your approach to testing change during development?
    
- Did you become better at breaking large technical problems into smaller tasks?
    
- Which skill do you think improved the most, and what specific part of CarNav demonstrates that improvement?
    

### 5. Evaluation

#### How well does the final product meet user needs?

- What were your original needs as a provisional driver without an existing in-car navigation system?
    
- Which of the original MVP features were successfully implemented?
    
- Can the system determine and display the user's current location?
    
- Can it calculate and display a route to a destination?
    
- Does the system function without an internet connection?
    
- How successfully does the UI communicate navigation information to the user?
    
- Is the interface practical to operate using a seven-inch touchscreen?
    
- Was the final system tested on the Raspberry Pi hardware, or primarily on your desktop?
    
- How reliable is the navigation system compared with existing commercial alternatives?
    
- What limitations would prevent you from using the current version for everyday driving?
    
- Overall, would you consider the project successful when compared with your original objectives? Why?
    

#### What would you improve if given another month?

- Would you prioritise fixing existing problems or adding new functionality?
    
- What additional testing would be necessary before using CarNav regularly in a car?
    
- Would you improve the interface, particularly navigation controls and information display?
    
- Would you implement automatic rerouting when the driver leaves the calculated route?
    
- Would you improve the efficiency or accuracy of the route calculation?
    
- Would you revisit any of your original stretch goals, such as voice navigation or a 3D-printed chassis?
    
- Which improvement would provide the greatest benefit to the user?
    
- How would you test whether those improvements were successful?

## Bibliography

Australian Government 2026, _Actgov division_, Arcgis.com, viewed 11 September 2026, <https://actmapi-actgov.opendata.arcgis.com/datasets/ACTGOV::actgov-division/explore?location=-35.520000,149.085000,9>.

brean 2026, _Brean/python-pathfinding: Implementation of common pathfinding algorithms_, GitHub, viewed 23 September 2026, <https://github.com/brean/python-pathfinding>.

Bresser, A 2026, _Pathfinding: Pathfinding algorithms (based on pathfinding.JS)_, PyPI, viewed 23 September 2026, <https://pypi.org/project/pathfinding/>.

Code Academy 2025, _A complete guide to Dijkstra’s shortest path algorithm_, Codecademy, viewed 11 September 2026, <https://www.codecademy.com/article/dijkstras-shortest-path-algorithm>.

Gakstatter, E 2015, ‘What exactly is GPS NMEA data?’, _GPS World_, viewed 11 September 2026, <https://www.gpsworld.com/what-exactly-is-gps-nmea-data/>.

Garmin 2026, _Garmin product updates_, Garmin.com, viewed 11 September 2026, <https://aoem.garmin.com/>.

Geeks For Geeks 2012, _Dijkstra’s algorithm to find shortest paths from a source to all_, GeeksforGeeks, viewed 11 September 2026, <https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/>.

― 2016, _A* search algorithm_, GeeksforGeeks, viewed 11 September 2026, <https://www.geeksforgeeks.org/dsa/a-search-algorithm/>.

― 2017, _Bidirectional search_, GeeksforGeeks, viewed 11 September 2026, <https://www.geeksforgeeks.org/dsa/bidirectional-search/>.

Geofabrik 2026, _Download OpenStreetMap for Australian capital territory | geofabrik download server_, Geofabrik Download Server, Geofabrik, viewed 11 September 2026, <https://download.geofabrik.de/australia-oceania/australia/act.html>.

Gillies, S 2025, _Shapely — Shapely 1.8.0 documentation_, shapely.readthedocs.io, viewed 18 September 2026, <https://shapely.readthedocs.io/en/stable/>.

Google 2025, _Google maps platform pricing - subscriptions and pay as you go_, Google Maps Platform, viewed 11 September 2026, <https://mapsplatform.google.com/pricing/#pay-as-you-go>.

Here n.d., _HERE base plan | location services | pricing | HERE_, www.here.com, viewed 11 September 2026, <https://www.here.com/get-started/pricing>.

LazerCo 2026, _Laser corporation product feed_, Laserco.com.au, viewed 11 September 2026, <https://www.laserco.com.au/brands/navig8r>.

Lazerfield, J 2018, _1-Intro_, Contraction Hierarchies Guide, viewed 11 September 2026, <https://jlazarsfeld.github.io//ch.150.project/sections/1-intro/>.

Navigation Systems Authority Network America 2026, _Navigation map data providers: Comparing HERE, TomTom, Google, and others_, Navigation Systems Authority, viewed 11 September 2026, <https://navigationsystemsauthority.com/map-data-providers-comparison/>.

Navone, E 2020, _Dijkstra’s shortest path algorithm - a detailed and visual introduction_, freeCodeCamp.org, viewed 11 September 2026, <https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/>.

Open Street Maps 2026, _OpenStreetMap_, OpenStreetMap, OpenStreetMap, viewed 11 September 2026, <https://www.openstreetmap.org/#map=11/-35.2891/149.1466>.

Organic Maps 2025, _Organic Maps: Offline Hike, Bike, Trails and Navigation_, organicmaps.app, viewed 11 September 2026, <https://organicmaps.app/>.

Patel, A 1997, _Introduction to A*_, theory.stanford.edu, viewed 11 September 2026, <https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html>.

pyrosm 2026, _Pyrosm/tests at master · PYROSM/pyrosm_, GitHub, viewed 11 September 2026, <https://github.com/pyrosm/pyrosm/tree/master/tests>.

Pyrosm Contributors & Tenkanen, H 2020, _Pyrosm Documentation_, Readthedocs.io, viewed 11 September 2026, <https://pyrosm.readthedocs.io/en/stable/quickstart.html>.

Python Software Foundation 2023, _JSON — JSON encoder and decoder — Python 3.8.3RC1 documentation_, docs.python.org, viewed 18 September 2026, <https://docs.python.org/3/library/json.html>.

TomTom 2026, _Pricing_, TomTom Documentation, viewed 11 September 2026, <https://docs.tomtom.com/pricing>.

Topf, J 2021, _Osmium tool manual - osmcode_, Osmcode.org, viewed 11 September 2026, <https://osmcode.org/osmium-tool/manual.html>.

Waze 2026, _Driving directions, live traffic & road conditions updates_, Waze, viewed 11 September 2026, <https://www.waze.com/live-map>.