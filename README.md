# Dino Bot

Welcome to the Dino Bot project! This Python script uses the `pyautogui` and `keyboard` libraries to play the Chrome Dino game automatically.

## How It Works

The bot takes screenshots of the game and scans them for obstacles (cacti and birds). When it detects an obstacle, it simulates a key press to make the dino jump or duck.

The bot uses the color of the pixels in the screenshot to detect obstacles. It assumes that any pixel that is not the same color as the background is an obstacle.

## Requirements

- Python 3
- `pyautogui` library
- `keyboard` library

## How to Run

1. Install the required Python libraries with pip:

```bash
pip install pyautogui keyboard
```

2. Run the script with Python:

```bash
python dino-bot.py
```

The bot will start playing the game automatically. Press `'q'` to stop the bot.

## Note

The bot is designed to work with the default colors of the Chrome Dino game. If the colors of the game change (for example, if the game is in **_dark mode_**), the bot might not work correctly.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the MIT license.
