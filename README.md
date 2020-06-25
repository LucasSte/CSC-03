# CSC-03

Use the following steps to run the world on Gazebo:

```
sudo systemctl start firmwared.service
fdc ping
```

If the above commands worked, ***PONG*** should appear on screen.

To start the word, type:

```
cd Gazebo
sphinx drone.world /opt/parrot-sphinx/usr/share/sphinx/drones/bebop2.drone 
```
