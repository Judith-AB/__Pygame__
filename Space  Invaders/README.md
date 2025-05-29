# 🛸 Space Invaders🚀
A simple Space Invaders-style arcade game built using Python and Pygame. Control a spaceship, shoot bullets, and destroy enemy invaders before they reach you. 

---
## 📸 Screenshots

<img src="img1.png" alt="Image 1" width="300" />
<img src="img2.png" alt="Image 2" width="300" />
<img src="img3.png" alt="Image 3" width="300" />

---

## 🎮 Features

- 👾 Multiple enemy invaders with rando movement
- 🚀 Player-controlled spaceship (left/right movement)
- 💣 Bullet firing with collision detection
- 🔥 Score tracking
- 🌌 Background and sound ready (add your own)

---

## 🧰 Requirements
- Python 3.x
- Pygame

### Install dependencies:

```bash
pip install pygame
```

## 🛠️ How It Works
Uses a game loop to update game state and render graphics.
Enemy and player positions are updated every frame.
Bullet collisions are detected using distance-based collision detection.
When a bullet hits an enemy, the enemy resets to a new position and the score increases.
