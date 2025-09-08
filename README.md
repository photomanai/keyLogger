Keylogger Project
Description
This project is a simple keylogger application developed using Python for cybersecurity research and educational purposes. It captures keyboard inputs and sends them via email at regular intervals. This code must only be used for ethical and legal purposes on systems with explicit permission.
Features

Captures keyboard inputs in real time.
Detects spaces and special keys (e.g., Enter, Space).
Sends captured logs via email every 30 seconds.
Securely retrieves email credentials from environment variables using dotenv.

Requirements

Python 3.x
Required Python libraries:
pynput
smtplib
python-dotenv



Installation

Install required libraries:
pip install pynput python-dotenv


Set up environment variables:

Create a .env file in the project directory.
Add the following information:MAIL=example@gmail.com
PASS=your_app_password

Note: For Gmail, you may need to use an App Password. Enable two-factor authentication on your Gmail account and generate an App Password.


Place the code file in the project directory:

Save the code file (e.g., keylogger.py) in the project directory.



Usage

Navigate to the project directory in your terminal or command prompt.
Run the code:python keylogger.py


The keylogger will start capturing keyboard inputs and send logs via email every 30 seconds.
To stop the program, manually terminate it (Ctrl+C).

Code Structure

callback_function: Captures keyboard inputs and appends them to the log list.
send_mail: Sends logs via email.
thread_function: Manages the periodic sending of logs using a timer.
Main program: Starts the keylogger listener and the timer.

Important Notes

Ethical Use: This code is intended solely for educational or cybersecurity testing purposes. Using a keylogger on systems without permission is illegal and may have serious legal consequences.
Security: Keep the .env file with credentials secure and never share it.
Gmail Settings: Ensure Gmail's "Less secure app access" is disabled. Use an App Password for email functionality.

Disclaimer
This project is for educational purposes only. The developer is not responsible for any misuse of the code. Users must comply with local laws and ethical guidelines.
Contributing

Report bugs or suggest improvements by opening an issue.
Submit pull requests for new features or enhancements.
