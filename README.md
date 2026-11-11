# CarNav IT Assignment Semester 2 Year 12
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

#### Stage 1: Raspberry Pi and GPS
###### Description of Development

The first stage involved setting up the Raspberry Pi and connecting the GPS receiver through its GPIO pins. This required configuring the Raspberry Pi's serial port, and developing a GPS manager using Python's `serial` and `pynmea2` libraries to read and interpret NMEA messages. The GPS manager was also designed to run in a separate thread, allowing it to continuously update the user's location and speed without interrupting the main application.

###### Challenges and Changes

The first stage involved setting up the Raspberry Pi and connecting the GPS receiver through its GPIO pins. This required configuring the Raspberry Pi's serial port, and developing a GPS manager using Python's `serial` and `pynmea2` libraries to read and interpret NMEA messages. The GPS manager was also designed to run in a separate thread, allowing it to continuously update the user's location and speed without interrupting the main application.

###### Image of soldered GPS
![[IMG20260808211141.jpg|423]]


###### Example of GPS data

Indoors  - Containing almost no information and not telling the GPS where it is.
```
$GNGGA,,,,,,0,00,25.5,,,,,,*64
$GNRMC,,V,,,,,,,,,,M*4E
$GNVTG,,,,,,,,,M*2D
```
Outdoors and near windows - Now containing the correct information and usable for its purpose
```
$GNGGA,224632.000,3519.60311,S,14903.48190,E,1,10,1.3,592.1,M,0.0,M,,*60
$GNRMC,224632.000,A,3519.60311,S,14903.48190,E,0.04,0.00,130826,,,A*64
$GNVTG,0.00,T,,M,0.04,N,0.07,K,A*20
```
###### Next steps

The next stage was to begin processing the OpenStreetMap data, so that the GPS coordinates could eventually be used to display the user's location on a map.

#### Stage 2: Map data processing

###### Description of Development

This stage involved processing the OpenStreetMap data into a format that could be used by the navigation system. Initially, I attempted to load the entirety of Australia's map data, which required approximately 34 GB of RAM and took ten minutes on my computer, compared to Canberra which only required 0.14 GB and took around a minute. Due to the Raspberry Pi's limited RAM, I decided to divide the ACT into its 19 districts, using GeoJSON boundaries and Osmium to create individual OSM PBF files.

###### Ram usage when loading osm data
Loading All of Australia osm data ram usage, on PC, with base line of 6Gb ram usage prior to loading.

![[Australia_ramusage_osmloading_screenshot.png|342]]

Loading just Canberra osm data ram usage, on Laptop, with base line of  3.12Gb ram usage prior to loading.

![[canberra_ramusage_osmloading_screenshot.png]]
###### Challenges and Changes

Dividing the data required researching several unfamiliar tools and commands before I was able to successfully extract the individual districts. I also began developing an area loading system, which would use the user's coordinates to determine their current district and identify adjacent districts to load. This was intended to reduce memory usage while still allowing navigation between regions. Although I successfully divided the data, the automatic loading system remained incomplete and was never integrated into the final application. In hindsight, I spent too much time developing this system before confirming how it would connect to the navigation backend.

###### Extract from the extraction config

This part of the JSON I made to extract, the wider Canberra region's OSM, into smaller more manageable areas.
```
"extracts": [

{

"output": "belc.osm.pbf",

"polygon": {

"file_name": "Data/districts/geojson/BELC.geojson",

"file_type": "geojson"

}

},

{

"output": "boot.osm.pbf",

"polygon": {

"file_name": "Data/districts/geojson/BOOT.geojson",

"file_type": "geojson"

}

},
```
###### Next steps

The next stage was to develop the navigation backend, converting the processed road data into a graph that could be used to calculate routes between locations.

#### Stage 3: Navigation backend

###### Description of Development

This stage involved developing the navigation backend, allowing the system to calculate routes between two locations. I used Pyrosm to extract the road network from the OpenStreetMap data and convert it into a NetworkX graph. I then developed a routing class which finds the closest road nodes to the starting and destination coordinates, before using NetworkX's implementation of the A* algorithm to calculate the shortest route. I also added functions to retrieve the route's coordinates, road lengths and speed limits, which could then be used to display the route and estimate travel times.

###### Challenges and changes

Originally, I intended to develop my own routing system, before considering implementing an existing routing algorithm myself. However, after experimenting with different libraries, I decided to use NetworkX, as it already provided the functionality I required. Testing was relatively successful, with the system calculating routes between locations within the loaded map data. I also created separate testing programs to check the road graph, calculated routes and returned coordinates before connecting them to the rest of the application. Although using an existing library meant I had less control over the routing algorithm itself, it allowed me to focus on integrating navigation into the application.

###### Next steps

The next stage was to develop the user interface and map display, allowing the calculated routes to be displayed visually rather than only as coordinates in the console.

#### Stage 4: User interface and map display

###### Description of Development

This stage involved designing and developing the user interface using PyQt5. As I had not clearly defined the interface in my original proposal, I asked my classmates to draw their preferred designs for a car navigation system. I then used elements from each of their designs to create my own, before implementing it using PyQt5. The interface was divided into three main sections, displaying information such as speed, location, the map, destination selection and estimated travel time.

###### Peer UI Design

Designs from each of my IT peers,showing what they want in their vision of a car navigation systems UI, which provided the foundation for my own design.

![[IMG20261016124519.jpg|208]]![[IMG20261016124512.jpg|207]]![[IMG20261016124522.jpg|208]]
###### My own design

This is the design i made following the examples from my peers. 

![[IMG20261016124538.jpg|530]]
###### Challenges and changes

One of the main challenges was displaying the map, as I initially experimented with QGIS before deciding to use Folium, which could be displayed within PyQt5 using QWebEngineView. Although this allowed me to display the map and calculated routes, it also introduced limitations, particularly requiring an internet connection to load map tiles. I also attempted to add interactive overlays, such as a recentering button, but had difficulties getting the buttons to work over the map. While the final interface included most of the elements from my design, it was not as aesthetically polished as I had originally envisioned.

###### Next steps

The next stage was to connect the interface to the GPS and navigation systems, allowing it to display the user's current location and calculated routes, before completing the final testing.

#### Stage 5: Integration and final testing

###### Description of Development

The final stage involved connecting the previously developed systems into a single application using the `CarNavApp` class. This managed the GPS, road graph, navigation controller and user interface, allowing them to communicate with one another. I also implemented a simulated GPS, allowing me to test the application on my computer without needing the physical receiver. This allowed the system to calculate and display routes, update the user's simulated location and speed, and display their progress through the route.

###### Challenges and changes

One of the main challenges was integrating the different systems, as they had largely been developed and tested independently. This resulted in problems that were not apparent during their individual testing. For example, the map originally reset its zoom level whenever the user's location updated, as I was recreating the entire map each time. I resolved this by using JavaScript to update the existing map, allowing the user's position and route to change without resetting the zoom. However, I was unable to integrate the geographic region loading system, meaning the final application could only navigate within the map data that was initially loaded, for the submitted version this defaulted to Weston.. 

###### Next steps

Although the application was functioning on my computer, I was unable to complete testing on the Raspberry Pi before submission. Further development would involve testing the application on the intended hardware, resolving any performance problems and implementing the remaining features, particularly offline map tiles and the geographic region loading system.

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

I originally started this project to develop a car navigation system that I could use in my car, as it does not have an existing navigation system. The main requirements were that it needed to operate offline, be usable within my car, and only needed to provide mapping and navigation for Canberra. I generally managed to complete the minimum viable product, although several features required compromises, particularly the ability to operate entirely offline. The system can determine and display the user's current location when the GPS receiver has a good connection, although this requires the antenna to be positioned under the windscreen. It can also calculate and display a route to a destination, but the destination must be entered using latitude and longitude coordinates, rather than searching for an address, like I intended.

I believe the user interface communicates the navigation information relatively well, displaying the map, calculated route, estimated travel time and progress through the route. The interface was also designed to fit the resolution of the seven-inch touchscreen, with PyQt5 supporting touchscreen interaction natively. However, I have only tested the completed application on my computer, rather than the Raspberry Pi itself, so I cannot confirm how well it would perform on the intended hardware. The navigation system appears relatively reliable within the region loaded, such as the ACT or Weston, although the map tiles sometimes fail to stream correctly, leaving sections of the map unloaded. While the navigation calculations themselves can operate offline, the map display still requires an internet connection, making the system impractical for my original intended use.

Another major limitation is that I was unable to 3D print a chassis or mount the system inside my car, making unusable for my original intention. If I had more time, I could potentially resolve the internet requirement by setting up a local map tile server on the Raspberry Pi, allowing the map to be displayed without an external connection. Along with also been able to model, and print the chassis to mount in my car. Overall, I would consider the project generally successful from a technical perspective, as I managed to develop most of the core functionality. However, it did not fully achieve my original objectives, with several compromises being required and the final product only just reaching the intended MVP. 

If I were given another month to continue development especially if it was free from other assignments, I would focus primarily on refining and completing the existing systems, rather than immediately adding new functionality. One of my first priorities would be integrating the geographic region loading system I had previously developed, and resolving any problems that occurred when connecting it to the main application. I would then work on setting up a local map tile server on the Raspberry Pi, allowing the navigation system to operate entirely offline as originally intended.

I would also spend more time improving the user interface, as although it contains most of the elements from my original design, it is not as aesthetically polished as I had envisioned. Another feature I would like to implement is automatic rerouting when the driver leaves the calculated route. I would not prioritise changing the existing route calculation system, as the library I used already provides relatively efficient and accurate routes, and replacing it would require a significant amount of additional work.

Finally, I would revisit some of the original stretch goals, particularly the 3D-printed chassis and mounting system, as these would allow the device to actually be installed and used within my car. Voice navigation would also be a useful addition, although I would prioritise getting the existing systems fully functional first. Of the possible improvements, I think refining the user interface would provide the greatest immediate benefit to the user, as it would improve the overall experience of interacting with the system, regardless of which navigation features were being used.
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