# MMX-Spider
## Information dissemination model
&nbsp;&nbsp;With the arrival of big data, blockchain and 5G, we have entered the information age.Massive data and information spread on the Internet,so who has mastered the information and who has grasped the development direction of this era,therefore, it is necessary to master the law of information dissemination.
## Idea of the project
Part 1  Data capture  
Part 2  Data cleaning and data analysis  
Part 3  Drawing analysis chart of propagation law  
Part 4  Establishing information dissemination model based on SIR  
## Specific operation steps
### <span stype="color:blue;">Part 1 Three methods of data capture</span>
(1) Grab the tiktok and Kwai data, find the interface rules through the filler, and then use the automation framework to simulate human operation, including input click and browse. The return interface is intercepted by mitproxy to parse JSON data.
&nbsp;&nbsp;The disadvantage of this method is that it requires higher graphics card and larger memory to drive, and it may cause tiktok and search limit. The most prominent disadvantage is slow speed.  
(2)	Search the browser to access the user sharing link and find a new link interface that returns response data. On pycharm, write a way to access its video interface by logging in with an analog browser, so as to save video related information.  
(3)	There are many video data analysis platforms on the network, such as xiaohulu. We can capture the data of these online platforms. Through research and observation, it is found that the interface link can obtain a large amount of information through parameter replacement, so as to achieve massive grabbing.  
### <span stype="color:blue;">Part 2  Data cleaning and data analysis</span>
&nbsp;&nbsp;Delete the duplicate video ID data, add, delete, modify and search a series of operations in the database to extract the information you need. Remove noise information, such as foreign language, facial expression and other data.
### <span stype="color:blue;">Part 3  Drawing analysis chart of propagation law</span>
&nbsp;&nbsp;Need to master the drawing of curves, broken lines, bars, pie charts and other graphics in Python.
### <span stype="color:blue;">Part 4  Establishing information dissemination model based on SIR</span>
&nbsp;&nbsp;The basic mathematical model of infectious diseases is to study the transmission speed, spatial scope, transmission path, dynamic mechanism of infectious diseases, so as to guide the effective prevention and control of infectious diseases. According to the types of infectious diseases, common infectious disease models are divided into Si, sir, Sirs, Seir models, etc. according to the transmission mechanism, they are divided into different types based on ordinary differential equation, partial differential equation and network dynamics.


