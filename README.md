# The Hunger Gains
*May the fasts be ever in your favor.*

---

## What is this?
**The Hunger Gains** is a minimalist intermittent fasting tracker.  
Log your fasts, keep your history, and display your progress with live stats and charts.  
Your arena isn’t a battlefield — it’s the kitchen. Your victory isn’t survival — it’s discipline.  

---

## Features
- Log fasts easily with a simple form  
- Track progress: streaks, averages, longest fast  
- Visualize history with auto-updating charts and badges  
- Own your data: everything is saved in plain CSV  
- Customize rules: define your streak threshold or chart style  

---

## Setup
1. Clone or fork this repository and name it `TheHungerGains`.  
2. Enable Issues if you want one-click fast logging.  
3. Log your first fast — it will be recorded in `data/fasts.csv`.  
4. Stats and charts are rebuilt automatically.  
5. Use the badges and charts wherever you want — README, docs, or a personal site.  

---

## Project Map
data/fasts.csv          → fasting history
scripts/build_stats.py  → stat and badge generator
badges/                 → stat badges
charts/                 → sparkline charts
README.md               → live scoreboard

---

## Customize
- Edit `MIN_HOURS_FOR_STREAK` in `scripts/build_stats.py` to change streak rules  
- Change the sparkline length (default: 30 fasts)  
- Add optional tracking fields such as weight or notes  

---

## Roadmap
- Weekly “Capitol Report” digest (PDF or HTML page)  
- Trend overlays (weight, sleep, mood)  
- District-inspired badge themes (flames, symbols, etc.)  

---

## License
MIT — because gains are best when shared.  


