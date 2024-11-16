### Phishing Simulator Toolkit

#### Introduction
This is a web-based phishing simulator designed for organizations to train their employees on how to recognize phishing attempts. It allows admins to send phishing emails to a controlled group of employees and then track who clicked the links and what data they entered.

#### Features
- **Phishing Email Sending**: Sends custom phishing emails to specified recipients.
- **Track Clicks**: Logs when a recipient clicks on a phishing link.
- **Data Entry Capture**: Tracks any sensitive data that a user might enter.
- **Generate Reports**: Provides a detailed report on employee responses to the phishing attempt.

#### Usage Instructions
1. **Setup Dependencies**: Install necessary packages using `pip`.
    ```sh
    pip install Flask requests
    ```
2. **Configure SMTP Settings**: Update the SMTP server, email, and password in `send_phishing_email()` function.
3. **Run the Server**: Use the command below to run the server.
    ```sh
    python phishing_simulator.py
    ```
4. **Access the Interface**: Open a web browser and navigate to `http://127.0.0.1:5000/` to use the phishing simulator.

#### Endpoints
- `/send_emails`: Sends phishing emails to a list of specified recipients.
- `/click/<tracking_token>`: Handles clicks from phishing emails and logs the activity.
- `/report`: Displays a report showing which users clicked the phishing link and entered data.

#### Prerequisites
- **Python 3.6 or above**
- **SMTP Email Account**: You will need access to an SMTP email account to send phishing emails.
- **Flask and Required Libraries**: Install using `pip install Flask requests`.

#### Implementation Steps
1. **Clone Repository**: Clone this repository from GitHub.
2. **Install Dependencies**: Run the command `pip install -r requirements.txt`.
3. **Configure SMTP Settings**: Replace the SMTP settings with the appropriate values for your environment.
4. **Run the Tool**: Run the server using `python phishing_simulator.py` and use the web interface for phishing simulation.

#### Contributing
If you find bugs or have suggestions for improvements, feel free to contribute by opening an issue or making a pull request.

#### License
This project is open-source and licensed under the MIT License.

#### Disclaimer
This toolkit is intended for educational and training purposes only. Users must ensure that all simulated phishing campaigns are performed ethically and with proper authorization.
