# FranChecker

## Description
FranChecker is a Python script that checks BuyVM's website for VPS availability. If any VPS becomes available, it sends the information to you through your Discord webhook.

## Features
- Monitors BuyVM's website for VPS availability.
- Sends notifications to your Discord webhook when a VPS becomes available.
- Configurable interval for checking VPS availability.

## Requirements
- Python 3.8 +
- bs4 (apt install bs4)
- Requests library (Install with `pip install requirements.txt`)

## Usage
1. Clone the repository: `git clone https://github.com/Hiradpi/francheck.git`
2. Navigate to the project directory: `cd FranChecker`
3. Install required dependencies: `pip install requests`
4. Configure your Discord webhook URL in `main.py`.
5. Run the script: `python3 main.py`

## Configuration
Edit the `main.py` file to set your Discord webhook URL. You can find your Discord webhook URL by going to your Discord server settings -> Integrations -> Webhooks -> Create Webhook.

You can also adjust the checking interval in the `config.py` file by modifying the `CHECK_INTERVAL_SECONDS` variable.

## Disclaimer
This script is intended for educational purposes and personal use only. The author is not responsible for any misuse or violation of the terms of service of BuyVM or Discord. Use it at your own risk.

## Contributions
Contributions and suggestions are welcome! Feel free to open issues or submit pull requests for any improvements or bug fixes.


