# Snake Game - Python Personal Project

## Description
This project is an implementation of the classic Snake game, developed in Python using the Pygame library. The objective of the project was to deepen my understanding of Object-Oriented Programming (OOP) concepts and manage game logic within a 2D graphical environment.

## Technologies and Computer Science Concepts

* **Object-Oriented Programming (OOP):** The code is modularized into specific classes (`SNAKE`, `FRUIT`, `MAIN`), ensuring a clear separation of concerns and responsibilities.
* **Vector Math:** Utilization of the `Vector2` class from `pygame.math` for grid calculations and direction management, simplifying translation and collision operations.
* **Game Loop & Event Handling:** Implementation of an application lifecycle that manages component state updates, graphical rendering, and keyboard input processing.
* **Asset Management:** Dynamic loading of PNG textures and OGG audio files, using the `convert_alpha()` method to optimize rendering performance.
* **"Wrapped Grid" Movement Logic:** Implementation of an algorithm that allows the snake to traverse screen boundaries and reappear on the opposite side, providing a smooth gameplay experience.
* **Custom Events:** Use of `pygame.time.set_timer` to decouple the snake's logical movement speed from the screen refresh rate.

## Features
* **Scoring System:** Real-time calculation and display of the score, based on the number of fruits collected.
* **Adaptive Graphics:** The snake's body textures (head, segments, corners, and tail) adjust automatically based on movement direction and the position of neighboring segments.
* **Audio Feedback:** Integration of sound effects for interactions with fruits and for the Game Over state.
* **Randomization:** Random generation of fruits on the grid, with position validation to avoid overlapping with the snake's body.

## Project Structure
* `main.py` - Contains the core logic, object classes, and the main game loop.
* `gallery/` - Folder containing graphical resources for the snake, fruits, and decor.
* `sounds/` - Folder dedicated to audio files (bite sound, die sound).
