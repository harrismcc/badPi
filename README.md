# badPi
A really dumb way of calculating pi

## Overview
Simply speaking, badPi is a very interesting, but very ineffective way of calculating digits of pi. It works by simulating two masses in a 2D space in which there is no friction and each object has perfect elasticity (aka no energy is lost). Additionally it has a wall at x=0 where the objects can collide. By sending the objects at each other and counting the total number of collisions we can find digits of pi! Exciting!

![alt text](https://raw.githubusercontent.com/harrismcc/badPi/master/example.png)

## Usage
In order to use it, you simply need to run the command as follows:
```
    python pi.py <number of digits>
 ```
Additionally, you can run it with no arguments or with the -h flag to get the help screen. The program attempts to calculate the fewest frames as possible by default, but if you want to specify this manually you can do so like this:
```
    python py.py <number of digits> -m <number of frames>
```

![alt text](https://raw.githubusercontent.com/harrismcc/badPi/master/exampleRun.gif)
