# Team205 Software Proposal
<img width="371" alt="image" src="https://github.com/WhoWaWay/WhoWaWay.github.io/assets/157083035/73be1216-4635-437f-bbf9-0657a8c99fb4">

Due to the design of our software, all of the sensor data will be handled internally and only the refined data will be handled by the users. This will reduce the amount of confusion users face. The way our device will work is that it will initialize the system, go into a loop that reads all the sensors, and output the data to the OLED screen every certain amount of time. While the loop is running, if the user inputs a signal to the RC car, the signal will interrupt the main loop and gain control of the car.
