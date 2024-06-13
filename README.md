# GESTURE-DETECTION-CAR

Introduction

Welcome to the Gesture Detection Car project, a groundbreaking initiative that combines the versatility of Arduino Uno with the intelligence of Teachable Machines. This innovative project merges machine learning and robotics to create a hands-free, futuristic interface that allows users to control the car through subtle hand gestures. The Arduino Uno serves as the project's core, while the machine-learning capabilities of Teachable Machines enable the car to recognize and respond to various gestures.


Software Used

1) Visual Studio Code
  Visual Studio Code is a free, lightweight code editor with powerful writing and debugging features. It supports various programming languages and extensions, making it a popular choice among developers.

2) Teachable Machines
  Teachable Machines is an easy-to-use online tool by Google that helps you train your computer to recognize and respond to different sounds, images, or poses without coding.

3) Arduino IDE
  Arduino IDE is a software platform that allows you to write, upload, and run code on Arduino microcontrollers, enabling you to create interactive electronic projects without advanced programming knowledge.


(I) Creating Models with Teachable Machines

Follow these steps to build a model using Teachable Machines:

i)   Visit the Teachable Machines website: Teachable Machines.

ii)  Select the type of project you want to create: Image.

iii) Collect images for each class you want to recognize and upload them.

iv)  Label each class or category in your dataset.

v)   Click on the "Train Model" button to let Teachable Machines train a model based on your data.

vi)  After training, test your model using the built-in testing interface to see how well it recognizes new examples.

vii) Once satisfied with the performance, export your model. Teachable Machines provides options to export models for TensorFlow.js, TensorFlow Lite, or as a link to use in your projects.


(II) Making Arduino Sketch

After creating the model, the next step is writing an Arduino script for the Arduino Uno to take serial commands and move the motors accordingly. The script for this project is included in the repository.

(III) Python Script

The next step involves creating a Python script that interfaces with the Arduino and processes gesture data. The script for this project is included in the repository.


(IV) Hardware Requirements & Assembling

*Hardware Required:

(i)    Arduino Uno

(ii)   2 Wheels

(iii)  2 DC motors

(iv)   1 Castor wheel

(v)    1 Battery

(vi)   1 Motor Driver (L298N)

(vii)  Double-sided Tape

(viii) Screws

(ix)   Wires

(x)    Chassis


*Assembling:

(i)    Arrange the chassis or make it.

(ii)   Attach the castor wheel to the chassis using screws.

(iii)  Attach wheels to the motors using screws.

(iv)   Mount the motors on the chassis.

(v)    Use double-sided tape to affix the Arduino, motor driver, and battery to the chassis.

![Screenshot 2024-06-13 125258](https://github.com/Rhythmbellic/GESTURE-DETECTION-CAR/assets/92723976/d82c6074-21cd-44a7-8fa1-9243f97f54e9)

(vi)   Connections:

-Power Supply: Connect an external power supply (battery) to the L298N motor driver. The power supply voltage should match the motor specifications. Connect the positive (+) and negative (-) terminals of the power supply to the corresponding terminals 
 on the motor driver.
 
-Motor Connections: Connect the two motors to the output terminals of the L298N motor driver.

-Motor 1: "Out 1" and "Out 2" terminals.

-Motor 2: "Out 3" and "Out 4" terminals.

-Arduino to Motor Driver Connections: Connect the control pins from the Arduino to the input pins (IN1, IN2, IN3, IN4) of the L298N motor driver. These connections are specified in the Arduino sketch.

-motor1Pin1 is connected to IN1.

-motor1Pin2 is connected to IN2.

-motor2Pin1 is connected to IN3.

-motor2Pin2 is connected to IN4.

-Ground Connections: Connect the ground (GND) of the Arduino to the ground (GND) of the L298N motor driver to ensure a common ground reference.


-Power Enable: Some L298N modules have an additional pin labeled "ENA" (Enable A) and "ENB" (Enable B). Connect these pins to digital pins on the Arduino if you want to control the speed of the motors using PWM. If you don't need speed control, you can 

-connect these pins directly to the positive voltage.

(V) Loading the Code to Arduino & Testing

*Connect the Arduino to your computer using a USB cable.

*Load the Arduino sketch from the repository onto the Arduino Uno.

*Start the Python script and test the setup.


Conclusion

Congratulations! You have successfully built a Gesture Detection Car. Feel free to enhance and modify the project, exploring new ways to use this innovative interface.

![WhatsApp Image 2024-05-26 at 15 07 08_7d07fb44(1)(1)](https://github.com/Rhythmbellic/GESTURE-DETECTION-CAR/assets/92723976/925dfdc0-6e8b-415f-b900-72efbf315cd3)

Repository Files

*label: Contains the labels for the gestures.

*gesture.py: The Python script to process gesture data and communicate with the Arduino.

*gesture_arduino.ino: The Arduino script to control the car's motors based on serial commands.

*model: The trained model exported from Teachable Machines.
