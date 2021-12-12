# Greed

The objective of Greed is to erase as much of the screen as possible by moving around in a
grid of numbers. To move your cursor, simply use the wasdqezc keys (for vertical, horizontal,
or diagonal movement). Your location is signified by the @ symbol.

When you move in a direction, you erase N number of grid squares in that direction, N
being the first number in that direction, i.e., the number adjecent to the cursor in the
direction in which you move. Your score reflects the total number of squares eaten.

http://manpages.ubuntu.com/manpages/bionic/man6/greed.6.html

https://gitlab.com/esr/greed

Installation of default game (Debian/Ubuntu):
```
sudo apt install greed
```

## Requirements:
- numpy
- termcolor
- getch

```
pip3 install numpy termcolor getch
```

## Usage:
For help with usage:
```python3 main.py -h```

Human Agent (controlled by user input, should be run with no flags):
```
python3 main.py
```
Random Agent
```
python3 main.py --random
```
Circular Agent
```
python3 main.py --circular
```
Q-Learning Agent
```
python3 main.py --qlearn
```

Additional Flags
- -i ITERATIONS to run the agent ITERATIONS times
- --no_graphics to run the game without graphics
Example (1k episodes of q-learning):
```
python3 main.py --qlearn --no_graphics -i 1000
```
