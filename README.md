# Summer Heat Waves Mobile Alert System

This project provides a tool for detecting heatwaves using historical temperature data and sends SMS alerts to notify users. Built using `Streamlit` for the front-end interface and `Twilio` for SMS notifications, it enables users to monitor temperature trends and issue warnings during heatwave conditions.

## Features

- **Heatwave Detection**: Detects heatwaves based on user-defined temperature thresholds and consecutive days of high temperatures.
- **SMS Alerts**: Sends SMS notifications to users when heatwaves are detected using the Twilio API.
- **User-Friendly Interface**: Provides a simple interface to upload temperature data and configure heatwave detection criteria.
- **Customizable Parameters**: Allows users to define the heatwave criteria (threshold temperature and consecutive days).

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- Streamlit (`pip install streamlit`)
- Pandas (`pip install pandas`)
- Twilio (`pip install twilio`)

Additionally, you will need a Twilio account to send SMS messages.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/heatwave-alert-system.git
   cd heatwave-alert-system
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Twilio account and update the `send_sms` function with your account credentials:
   ```python
   account_sid = 'your_account_sid'
   auth_token = 'your_auth_token'
   ```

## How to Run the Project

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Upload a CSV file containing temperature data. The CSV should have the following structure:
   - `Date.Full`: The full date (e.g., 2024-09-01)
   - `Data.Temperature.Avg Temp`: Average daily temperature (in °C)

3. Customize the heatwave detection settings (temperature threshold and consecutive days).

4. Enter a phone number and country code to receive SMS notifications.

5. Click the "Send SMS Notifications" button to send alerts for detected heatwaves.

## CSV File Example

Here's an example structure of the CSV file expected by the system:

```
Date.Full,Data.Temperature.Avg Temp
2024-09-01,31
2024-09-02,32
2024-09-03,33
```

## Notebook

An additional Jupyter Notebook (`heat_waves.ipynb`) is provided for detailed data analysis and testing of the heatwave detection algorithm.

