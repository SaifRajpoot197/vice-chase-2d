# Vice Heart

A 2D top-down action prototype built with Python and Pygame. Play as Lucia, hijack a nearby car to double your speed, and outrun the pursuing police!

## Features
* **On-Foot & Driving Mechanics:** Seamless switching between walking and driving.
* **Dynamic Speed:** Driving increases movement speed to help escape pursuit.
* **Police AI:** Basic tracking behavior where police continuously chase the player's position.

## Controls

| Key | Action |
| :--- | :--- |
| **W** | Move Up |
| **A** | Move Left |
| **S** | Move Down |
| **D** | Move Right |
| **F** | Enter / Exit Car *(must be close to the blue square)* |

## Prerequisites
* Python 3.x
* Pygame

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd vice-heart
   ```

2. **Install Pygame:**
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   ```bash
   python main.py
   ```
   *(Note: Replace `main.py` with whatever you named your Python file.)*

## Color Guide (Current Shapes)
* **Red Square:** Lucia (Player)
* **Blue Square:** Vehicle
* **Black Square:** Police

## Future Ideas
* Add collision detection (bust/game over screen when caught by police)
* Replace colored rectangles with custom 2D sprites
* Add a city map, roads, and obstacles
* Implement a wanted-level system and score timer
