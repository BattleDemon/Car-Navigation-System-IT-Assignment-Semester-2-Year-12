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

My original plan for an entirely offline navigation system is and was technically achievable, but  was not actually completed. I was unable to make the final product offline, due to  the map needing to download tiles from  a web socket. Without that limitation which I attempted to solve, but could not in time the system could of achieved my goal. 

Most of my initial research was useful throughout development, although not always directly, as it provided a general understanding of how the different systems could be implemented, but further research was required for the specifics. I also think the decision to use QT was correct as unlike some of my peers I didn't have to learn a whole new UI library, while also attempting an ambitious project.

One of the main problems with my original planning was underestimating the complexity of processing and managing the OpenStreetMap data. I spent almost two weeks experimenting with dividing the OSM and GeoJSON files into smaller regions, developing a system to load them when required, and researching different libraries for route calculation. Several of these approaches were eventually abandoned, either because they lacked the functionality I required or because I was unable to integrate them into the final system. 

The original timeline, particularly the intention to complete the minimum viable product by 17 September, was also overly optimistic. Although I believe it could have been achievable if I had dedicated more time outside of class, I failed to properly account for the dependencies between different systems. While I had allocated time for debugging, I underestimated how difficult it would be to test and integrate systems that depended on other components being completed first. This became particularly problematic towards the end of development, when several components had been developed separately but had not yet been connected.

One of the first significant changes was my decision to divide the ACT's map data into smaller geographic regions, rather than loading the entire dataset into the Raspberry Pi's RAM. The intention was to reduce memory usage by only loading the region required for navigation. However, despite spending a considerable amount of time preparing the data and developing a loading system, I was ultimately unable to integrate this into the final product.

The user interface was another area that changed significantly, although this was more of an improvement rather than a compromise. My original proposal did not clearly define how the interface would look, so I conducted a small survey among my IT classmates, asking each of them to draw their preferred design for a car navigation interface. I then used these designs as a basis for developing my own interface, incorporating elements that I liked and fit with the project.

### 2. Development

One of the first technical challenges I encountered was connecting the GPS receiver to the Raspberry Pi, particularly as this required me to learn how to solder. It took several attempts to get a working connection, and even then, the solder occasionally broke during testing, requiring me to redo it. Although I gained some experience with soldering, I don't think I learnt it particularly well, as the connections were still quite poor. The GPS receiver itself was relatively straightforward to program, with no major problems interpreting the NMEA messages.

Another major challenge was processing the OpenStreetMap data, particularly due to the large amount of memory required. Initially, I attempted to load the entirety of Australia's map data, which used approximately 34 GB of RAM and took around ten minutes to load on my computer. In comparison, loading just Canberra required approximately 0.14 GB and took around a minute. Due to the Raspberry Pi's limited RAM, I decided to divide the ACT's map data into smaller geographic regions, which could be loaded individually when required. However, this introduced additional complications, particularly when trying to divide the OSM files using GeoJSON boundaries, which required me to learn several unfamiliar commands and tools. Which was all for nothing in the end as I was unable to integrate that system into the whole before the assignment was due.

Developing the user interface presented a different set of challenges, particularly as I don't consider myself good at designing graphical interfaces from scratch. To help with this, I asked my classmates to draw their preferred designs for a car navigation interface, which I then used as a basis for my own. Displaying the map was also more complicated than expected, as I initially experimented with QGIS before deciding to use Folium. However, Folium introduced some limitations, particularly when I attempted to add my own interactive overlays, such as a recentering button, and it required the program to be online. I was unable to find a way to place these over the map while still allowing interaction with the elements beneath them.

When connecting the map display to the navigation backend, I was able to successfully display a calculated route to the user's desired coordinates. However, I was unable to implement address searching, meaning destinations had to be entered using latitude and longitude rather than a street address. Another problem occurred when updating the user's location, as my original approach recreated the entire map with each update, causing the zoom level to reset. I resolved this by changing the system to update the existing map rather than recreating it each time. I had also planned to include an animation within the interface, although I was unable to complete this before submission.

Most of the problems I encountered were identified through testing the individual systems as I developed them. When something didn't work as intended, I would examine the output or errors to determine what was causing the problem, before either modifying my approach or researching possible solutions. I also created several separate testing programs, particularly for the navigation backend and map processing, which allowed me to test the functionality of individual components before connecting them to the main application. However, while this was useful for identifying problems within individual systems, it also meant that some issues were not discovered until the final integration, luckily those were minor problems.

### 3. Project Management

My time management was relatively successful during the first two milestones, which were completed close to their originally planned dates. However, the third milestone took significantly longer than expected, particularly due to the complications involved in processing the map data and managing the Raspberry Pi's limited RAM. I spent approximately a week and a half working on the map processing alone, roughly equal to the time spent developing the user interface. This delayed the remaining milestones, with the original timeline becoming increasingly difficult to follow.

Although I worked relatively consistently throughout the semester, most of this was confined to class time, with occasional work at home and on weekends. Unlike previous IT assignments, where I would often spend considerable amounts of time working on them during the final weeks, this project was frequently interrupted by other assignments, particularly my Year 12 report towards the end. The school holidays also contributed to this, as I was working most days, resulting in no recorded commits between 23 September and 13 October. Additionally, the relatively distant due date made the assignment feel less urgent, until I had already fallen significantly behind. While I continued testing individual systems throughout development, the final integration was largely completed during the day before and the day of submission, leaving insufficient time to properly test and polish the completed product.

If I were to undertake this project again, I would divide it into more milestones, each with smaller and more specific goals, rather than necessarily allocating more time to any particular stage. I would also reconsider how the different systems were designed, particularly their dependencies on one another. While I attempted to develop several systems independently, the way they were structured made it difficult to integrate and test them together until towards the end of development. Developing the GPS, navigation and interface systems with integration in mind from the beginning, alongside more frequent testing checkpoints, would have helped identify these problems earlier.

I would also change how I prioritised the project against my other assignments. In hindsight, I could have dedicated more time to this project rather than prioritising assignments that were unlikely to contribute to my ATAR. My motivation towards schoolwork had also decreased during the final semester, particularly after receiving confirmed early entry to uni, which reduced the pressure I previously felt to spend considerable amounts of time on assignments. Combined with the relatively distant deadline, this contributed to me putting off work that could have been completed earlier, ultimately limiting how much of the original project I was able to complete and polish.

### 4. Skills

One of the more interesting aspects of this project was working with a Raspberry Pi, rather than the LEGO Mindstorms systems we had previously used in IT. This required me to consider things such as RAM, computational power, power supply and the different connectors, along with more intricate tasks such as soldering. Working with the GPS receiver was particularly interesting, as it required me to manage the physical connections, while also considering its limitations, such as only being able to receive a reliable signal outdoors or through thinner walls. I also learnt how to use Python's serial library to read the stream of NMEA data being sent by the GPS receiver.

Working with OpenStreetMap also showed me how much geographic data is freely available for anyone to use, along with the large number of open-source libraries designed to process it. However, I also learnt that each library has its own limitations, which became particularly apparent when working with OSM PBF and GeoJSON files, as I had to experiment with several libraries before finding ones that suited my needs.

Another skill I developed was gathering and incorporating feedback into my user interface design. By surveying my IT classmates, I learnt that the minimalistic approach commonly used in modern interfaces is not necessarily what everyone prefers. It was interesting seeing the different designs people came up with, and considering how to combine their suggestions into a single interface. I also learnt about the benefits and drawbacks of developing software components independently. While this allowed me to test individual systems before they were completed, it also created a significant amount of integration work towards the end of development, which required more time than I had originally anticipated.

Although I learnt some new Python features, such as `isinstance()`, along with the functionality of several new libraries, I do not think my general Python programming abilities improved significantly. A large portion of this assignment was spent researching unfamiliar libraries and their alternatives, reading documentation, and creating small tests to determine whether they would be suitable before developing the full feature.

### 5. Evaluation

#### How well does the final product meet user needs?

- What were your original needs as a provisional driver without an existing in-car navigation system?
		I started this project to make a car navigation system in to have in my car, It needed to be offline, and usable within my car. It only needed to include mapping and navigation for canberra.

- Which of the original MVP features were successfully implemented?
		I generally completed the MVP features, athough did need to change or compromise on somethings, such as offline ect.
    
- Can the system determine and display the user's current location?
		It can when connection is good, but requires the antenna to be positioned under the glass of  the windshield
    
- Can it calculate and display a route to a destination?
		yes it can calculate and display a route to a destination, although it cannot look up the destination as if it were an address, instead needing latitude and longitude
    
- Does the system function without an internet connection?
		Technically the navigation does, but you won't see anything on the map.
    
- How successfully does the UI communicate navigation information to the user?
		I believe it does well, showing the user the map and the route needed, it shows the estimated time, and how far through the route they are.
    
- Is the interface practical to operate using a seven-inch touchscreen?
		Qt naturally supports a touch screen interface, and i have designed it to fit within the resolution of the screen.
    
- Was the final system tested on the Raspberry Pi hardware, or primarily on your desktop?
		Although i have only tested on my computer and not the raspberry pi system.
    
- How reliable is the navigation system compared with existing commercial alternatives?
		It is reliable but only for the region inputed so ACT or Weston, but can sometimes have unreliable map streaming preventing some of the map from loading
    
- What limitations would prevent you from using the current version for everyday driving?
		I was unable to 3d print a chasiss, and mout it in my car so it can't be used. Also it would need an internet connection which i don't want to bother with, but if i spent some more time working on it i could setup a local server and keep the map tiles on there for canberra.
    
- Overall, would you consider the project successful when compared with your original objectives? Why?
	    It was generally successful but did need to compromise in aspects, and didn't go as far as i originally planed, barely making the MVP.

#### What would you improve if given another month?

- Would you prioritise fixing existing problems or adding new functionality?
		I would refine and fix existing systems, and actually connect my area loading system, and fix anyproblems with it, before making a map tile server (locally on the raspberry pi).

- Would you improve the interface, particularly navigation controls and information display?
		My current interface although including the parts from my design, is not as aesthetically good for the ui i was envisioning.

- Would you implement automatic rerouting when the driver leaves the calculated route?
		It would be good to implement, but might not be an instant thing, it might be a periodic check to reduce load on the raspbery pi. 

- Would you improve the efficiency or accuracy of the route calculation?
		No since i have used a library it is already quite efficient and accurate, if i were to change it i would need to build it from scratch.

- Would you revisit any of your original stretch goals, such as voice navigation or a 3D-printed chassis?
		It would be good to revisit all the stretch goals and implement them especially yhe ones which allow it to be mouted in my car.

- Which improvement would provide the greatest benefit to the user?
		Mostlikely UI improvements, as it improves every users experience instantly.

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