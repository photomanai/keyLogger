# Keylogger Project

## Description

This project is a simple keylogger application developed in Python for **cybersecurity research and educational purposes only**. It captures keyboard inputs and periodically sends the collected data via email. This code should only be used on authorized systems, with proper consent, and in compliance with ethical and legal standards.

## Features

* Captures keyboard inputs in real time.
* Detects spaces and special keys (e.g., Enter, Space).
* Sends captured logs via email every 30 seconds.
* Securely retrieves email credentials from environment variables using `dotenv`.

## Requirements

* Python 3.x
* Required Python libraries:

  * `pynput`
  * `smtplib`
  * `python-dotenv`

## Installation

1. Install the required libraries:

   ```bash
   pip install pynput python-dotenv
   ```

2. Configure environment variables:

   * Create a `.env` file in the project directory.
   * Add the following credentials:

     ```ini
     MAIL=example@gmail.com
     PASS=your_app_password
     ```

     **Note:** For Gmail, you may need to generate an **App Password**. Enable Two-Factor Authentication (2FA) in your Google account and create an app-specific password.

3. Place the code file in the project directory:

   * Save the script (e.g., `keylogger.py`) inside the project folder.

## Usage

1. Navigate to the project directory in your terminal.
2. Run the script:

   ```bash
   python keylogger.py
   ```
3. The keylogger will start capturing keystrokes and send logs via email every 30 seconds.
4. To stop the program, terminate it manually (Ctrl+C).

## Code Structure

* **`callback_function`**: Captures keystrokes and stores them in a log list.
* **`send_mail`**: Sends the collected logs via email.
* **`thread_function`**: Handles periodic sending of logs using a timer.
* **Main program**: Starts the keylogger listener and the log-sending thread.

## Important Notes

* **Ethical Use**: This project is for **educational and cybersecurity testing purposes only**. Unauthorized use of keyloggers is illegal and may lead to serious legal consequences.
* **Security**: Keep the `.env` file secure. Never share your credentials.
* **Gmail Settings**: Do not enable "Less secure apps". Always use App Passwords for email authentication.

## Disclaimer

This project is intended strictly for **educational purposes**. The developer assumes no responsibility for misuse of the code. Users are fully responsible for ensuring compliance with local laws and ethical guidelines.

## Contributing

* To report bugs or suggest improvements, please open an issue.
* Pull requests for new features are welcome.
