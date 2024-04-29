# Team205 Software Proposal
<img width="376" alt="image" src="https://github.com/WhoWaWay/WhoWaWay.github.io/assets/157083035/17de79a4-142d-436d-838f-3815c15d8361">

Due to the design of our software, all of the sensor data will be handled internally and only the refined data will be handled by the users. This will reduce the amount of confusion users face. The way our device will work is that it will initialize the system, go into a loop that reads all the sensors, and output the data to the OLED screen. While the loop is running, if the user inputs a signal to the RC car, the signal will interrupt the main loop and gain control of the car.

# 5 Main Changes
1.1 Change 1: The biggest change we have is the components we selected in the beginning. We didn't know much about the surface mount component so they were replaced a few times.

1.1 Change 2: We removed our plan to make an OLED function that interrupts the system every 30 seconds.

1.1 Change 3: Before we decided to make an RC car, we had different designs that were completely different multiple times.

1.1 Change 4: We switched from I2C to SPI for the motor driver.

1.1 Change 5: We did not use a remote controller to control the car.
