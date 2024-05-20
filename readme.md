**README**

**Francheck: A Tool for Checking Frantech (BuyVM) Products**

**Description:**

Francheck is a command-line tool designed to check the availability of Frantech (BuyVM) products and send notifications to a designated Discord webhook. It utilizes BuyVM's API to fetch real-time product availability data and provides users with an efficient way to monitor product availability.

**Usage:**

1. Clone the repository or download the script `main.py` to your local machine.

2. Ensure you have Python installed on your system.

3. Install the required dependencies using pip:

   ```
   pip install requests argparse
   ```

4. Navigate to the directory containing the `main.py` script in your terminal or command prompt.

5. Run the script with the desired arguments:

   ```
   python main.py
   ```

   - `--code`: The product code found in the BuyVM link (e.g., `1411` from `https://my.frantech.ca/cart.php?a=add&pid=1411`).
   - `--delay`: Optional. The interval in seconds between each availability check. Default value is 3 seconds. It's recommended to set a longer delay (e.g., 300 seconds) to avoid excessive requests.
   - `--mode`: Optional. Mode 0: sends data only if it's avalable , Mode 1: sneds data no matter what , Mode 2: sends data only if it's not avalable.

**Features:**

- **Real-time Availability Checks:** Francheck uses BuyVM's API to fetch real-time availability data for specified products.
- **Discord Notifications:** Upon checking availability, Francheck sends notifications to a designated Discord webhook, providing details such as product name, ID, quantity, availability status, and a direct link to the product.
- **Flexible Usage:** Users can either specify the product code and delay via command-line arguments or interactively select products and locations.

**Example:**

```
python main.py --code 1411 --delay 300 --mode 0
```


**Contributing:**

Contributions to Francheck are welcome! Feel free to submit issues, feature requests, or pull requests via the GitHub repository.

**License:**

This project is licensed under the MIT License. See the LICENSE file for details.

**Author:**

Francheck was created by Hiradpi.

**Disclaimer:**

This tool is provided as-is, without any warranty. Use it responsibly and at your own risk.
