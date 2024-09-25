import pandas as pd
from twilio.rest import Client
import streamlit as st

def detect_heatwaves(data, threshold=30, consecutive_days=3):
    data['heatwave'] = False
    count = 0

    for i in range(len(data)):
        if data['Data.Temperature.Avg Temp'].iloc[i] > threshold:
            count += 1
        else:
            count = 0

        if count >= consecutive_days:
            data.loc[i, 'heatwave'] = True

    return data

def send_sms(to, message):
    account_sid = 'Your SID'
    auth_token = 'Your authrizatin code here'
    client = Client(account_sid, auth_token)

    try:
        message_response = client.messages.create(
            body=message,
            from_='+120xxxxxx',
            to=to
        )
        st.success(f"Message sent to {to}: {message_response.sid}")
    except Exception as e:
        st.error(f"Failed to send message: {e}")

# Streamlit app
st.title('Summer Heat Waves Mobile Alert System')

st.markdown("""
This application helps you detect heatwaves based on historical temperature data and send SMS notifications to alert users.

**Instructions:**
1. Upload a CSV file with temperature data.
2. Set the temperature threshold and number of consecutive days to define a heatwave.
3. Select your country code and enter the phone number to receive SMS notifications.
4. Click the button to process the data and send notifications.
""")

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader("Upload CSV with temperature data", type="csv")

with col2:
    country_code = st.selectbox('Select Country Code', options=[
        '+1',    # USA
        '+44',   # UK
        '+91',   # India
        '+61',   # Australia
        '+81',   # Japan
        '+33',   # France
        '+49'    # Germany
    ], index=2)  # Default to +91 (India)
    
    phone_number = st.text_input('Enter phone number', placeholder='1234567890')

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    with st.sidebar:
        st.header('Settings')
        threshold = st.number_input('Temperature Threshold (°C)', value=30)
        consecutive_days = st.number_input('Consecutive Days for Heatwave', value=3)

    # Apply heatwave detection
    data = detect_heatwaves(data, threshold, consecutive_days)

    st.subheader('Detected Heatwaves')
    st.write(data)

    if st.button("Send SMS Notifications"):
        if phone_number:
            full_phone_number = f"{country_code}{phone_number}"
            for index, row in data.iterrows():
                if row['heatwave']:
                    send_sms(full_phone_number, f"Heatwave detected on {row['Date.Full']} with average temperature {row['Data.Temperature.Avg Temp']}°C.")
        else:
            st.error("Please enter a valid phone number.")
