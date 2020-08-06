# Smart-Drones-For-Pest-Detection

[![Watch the video](https://img.youtube.com/vi/YfdVrz5O6WU/maxresdefault.jpg)](https://www.youtube.com/watch?v=YfdVrz5O6WU)

Use the following steps to run the world on Gazebo:

```
sudo systemctl start firmwared.service
fdc ping
```

If the above commands work, ***PONG*** should appear on screen.

To start the Gazebo world, type:

```
cd Gazebo
sphinx drone.world /opt/parrot-sphinx/usr/share/sphinx/drones/bebop2.drone 
```

With the Olympe environment activated, do:

```
python main.py
```
