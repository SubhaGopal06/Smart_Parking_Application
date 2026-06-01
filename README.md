# Smart Parking Application


## Overview


Urban parking congestion is a common problem that leads to increased traffic, fuel consumption, and driver frustration. This project presents a Smart Parking Application that combines Machine Learning, IoT integration, Cloud Databases, and Web Technologies to recommend suitable parking spaces and manage parking reservations in real time.



The system predicts the most appropriate parking slot for a user by considering factors such as distance and parking cost while simultaneously monitoring occupancy through IoT sensor data.



## Key Features



* Machine Learning-based parking slot recommendation using Naive Bayes Classification

* Real-time parking occupancy monitoring through IoT integration

* User authentication and reservation management using Firebase

* Interactive web dashboard built with Flask

* Dynamic slot allocation based on distance and pricing factors

* Reservation tracking and parking availability updates



## Motivation



Traditional parking systems often require drivers to manually search for available spaces. The objective of this project was to explore how Machine Learning and IoT technologies can be integrated to support intelligent parking allocation and improve the parking experience.



## System Architecture



User → Flask Web Application → Machine Learning Engine → Firebase Database → IoT Data Sources (ThingSpeak)



### Components



#### Frontend



* HTML

* CSS

* Bootstrap

* JavaScript



#### Backend



* Python

* Flask



#### Database



* Firebase Realtime Database



#### Machine Learning



* Naive Bayes Classifier

* Scikit-Learn

* Pandas

* NumPy



#### IoT Integration



* ThingSpeak Channels

* Sensor Occupancy Data



## Machine Learning Workflow



1. User logs into the system.

2. User location coordinates are processed.

3. Distances to available parking slots are calculated.

4. Parking prices are combined with distance values.

5. A feature vector is generated.

6. The trained Naive Bayes model predicts the most suitable parking slot.

7. The recommendation is displayed on the dashboard.



## Technologies Used



* Python

* Flask

* Scikit-Learn

* Firebase

* ThingSpeak

* Pandas

* NumPy

* HTML/CSS

* JavaScript

* Bootstrap



## Project Structure



```text

Smart_Parking_Application/

│

├── main.py

├── config.py

├── naive_bayes.py

├── data.csv

├── finalized_model.sav

├── templates/

├── static/

├── requirements.txt

└── ARCHITECTURE.md

```



## Learning Outcomes



Through this project, I gained practical experience in:



* Designing end-to-end software systems

* Integrating machine learning models into web applications

* Working with cloud-based databases

* Consuming and processing IoT data streams

* Managing user authentication and sessions

* Building maintainable Python applications

* Writing technical documentation



## Future Improvements



* Real-time occupancy updates using WebSockets

* Deep learning-based parking prediction

* Mobile application development

* Payment gateway integration

* License plate recognition

* Deployment on cloud infrastructure



## Academic Relevance



This project demonstrates the integration of concepts from:



* Machine Learning

* Data Analytics

* Internet of Things (IoT)

* Cloud Computing

* Database Systems

* Software Engineering

* Web Development



## Author



Subha Gopal



Bachelor's Project – Smart Parking Application
