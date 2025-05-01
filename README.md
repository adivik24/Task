# Task
Prerequisites are
1.ROS 2 Version: ROS 2 Jazzy
2.Python Version: Python 3.10 (which is compatible with ROS 2 Jazzy)
3.Simulation Tool: Gazebo Classic

Brief desciption about python files:
sensor_publisher.py : Its a node which publishes a random number between 0 to 1 at regular interval, on 'topic sensor_readings'.
sensor_subscriber.py : Its a node which subscribes to the topic sensor_readings and print message on wether the incoming value is greater or lower than 0.5.
The main scripts to run:

First, run the sensor_publisher.py in one terminal then  in another terminal, run the sensor_subscriber.py:
<img width="926" alt="Image" src="https://github.com/user-attachments/assets/63159bf4-e88b-4969-ac06-18b8d85619f4" />
<img width="938" alt="Image" src="https://github.com/user-attachments/assets/ffd4540f-ea75-4d51-9d19-dfbee2352cf0" />
<img width="521" alt="Image" src="https://github.com/user-attachments/assets/a1a8a21a-1635-4747-9762-c35a54760e5b" />
<img width="590" alt="Image" src="https://github.com/user-attachments/assets/426087ed-4a7a-4464-a4b7-4e7d1ab746ab" />
