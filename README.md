# Greed

The object of Greed is to erase as much of the screen as possible by moving around in a
grid of numbers. To move your cursor, simply use the wasdqezc keys. Your location is 
signified by the @ symbol.

When you move in a direction, you erase N number of grid squares in that direction, N
being the first number in that direction. Your score reflects the total number of squares
eaten.

http://manpages.ubuntu.com/manpages/bionic/man6/greed.6.html

## Requirements:
- numpy
- termcolor
- getch

```
pip3 install numpy termcolor getch
```

## Usage:
Human Agent (controlled by user input):
```
python3 main.py
```
Random Agent
```
python3 main.py --random
```
Q-Learning Agent
```
python3 main.py --qlearn
```

