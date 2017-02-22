Installation ROS : http://wiki.ros.org/kinetic/Installation/Ubuntu

launch roscore server first : 
```
roscore
```

then, in another terminal, launch turtlesim: 
```
rosrun turtlesim turtlesim_node
```

Finally launch the terminal that control the turtle:
```
rosrun turtlesim turtle_teleop_key
```

For listening a topic:
```
rostopic echo /turtle1/cmd_vel
```


For seing topic graph:
```
rosrun rqt_graph rqt_graph
```