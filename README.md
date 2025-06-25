# 🚀 Alien Invasion – A Python Arcade Shooter Built with Pygame

**Alien Invasion** is a retro-style arcade shooter game developed using Python and the Pygame library. Inspired by the classic alien shooter genre and based on the project in *Python Crash Course* by Eric Matthes, this game serves as both a nostalgic experience and a deep dive into game development with Python.

## 🎮 Game Objective

You control a rocket ship at the bottom of the screen and must shoot down waves of descending alien ships. Survive as long as possible, score points, and progress through increasingly difficult levels. Dodge collisions, manage limited bullets, and stay alive!

---

## 🛠️ Technologies & Concepts Used

- **Python** (core programming language)
- **Pygame** (game development library)
- **Object-Oriented Programming (OOP)**  
  Classes for `Ship`, `Alien`, `Bullet`, `Button`, `Score`, and `Life`
- **Sprite Groups**  
  Efficient rendering and collision detection
- **Custom Event Handling**  
  Keyboard and mouse inputs for dynamic interaction

---

## 📁 Project Structure

alien_invasion/  
├── alien_invasion.py # Main game loop & controller  
├── ship.py # Ship class (movement, drawing)  
├── alien.py # Alien class (behavior, appearance)  
├── bullet.py # Bullet class (firing, movement)  
├── button.py # Play button implementation  
├── score.py # Scoreboard logic  
├── life.py # Life indicator with hearts  
├── settings.py # All configurable game settings  
├── images/ # BMP assets (ship, aliens, hearts, game over)  
├── README.md # This file  

---

## ✨ Features

- **User Input**: Smooth ship control (left/right), spacebar to shoot, mouse click to play.
- **Real-Time Movement**: Continuous motion using key state detection.
- **Collision Detection**: Bullets vs aliens, aliens vs ship.
- **Score & Levels**: Scoreboard with increasing difficulty per wave.
- **Life System**: Limited lives shown via heart icons.
- **Game Over Screen**: Custom full-screen image when lives are lost.
- **Responsive UI**: Adaptive layout for score, level, and buttons.

---

## 🎨 Assets

All artwork (spaceship, alien, heart icons, and game over screen) was generated using **Microsoft Copilot** and integrated in `.bmp` format for seamless rendering in Pygame.

---

## 📚 Inspiration & Credits

This project was inspired by the hands-on Alien Invasion game from the book:

> *Python Crash Course* by Eric Matthes

Special thanks to Eric Matthes for the exceptional guidance and foundational codebase.

---

## 🚧 Future Enhancements

- 👾 Alien patrol movement with edge bounce
- 🔊 Sound effects and background music
- 🔫 Power-ups and weapon variety
- 👹 Boss levels or unique alien types
- 🌐 Online leaderboard with high scores

---

## 🧠 Lessons Learned

- Implementing clean, modular OOP architecture for games
- Working with sprite-based animation and collision detection
- Designing user-friendly UI with Pygame
- Managing state transitions (menu, active game, game over)
- Optimizing frame rate and performance

---

## 🔗 Try It Out

Clone the repository and run the game locally:

```bash
git clone https://github.com/your-username/alien-invasion
cd alien-invasion
python alien_invasion.py
```

✅ Make sure you have Pygame installed:
```bash
pip install pygame
```

## 📝 Acknowledgements
Eric Matthes – For the original Alien Invasion project in Python Crash Course.

Microsoft Copilot – For assisting with game asset creation.
