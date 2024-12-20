# MQTT Sensor Monitoring System

This project demonstrates a basic IoT setup that uses MQTT to monitor real-time temperature sensor data and displays it on a web dashboard. If the temperature exceeds a predefined threshold, the system triggers an alarm to alert users.

---

## Features

- **Real-Time Monitoring:** Displays live temperature data on a user-friendly web dashboard.
- **Alarm Trigger:** Alerts the user with a warning when the temperature exceeds a threshold value (default: 75°C).
- **Lightweight Communication:** Utilizes MQTT for efficient and fast data transfer between the sensor and the dashboard.

---

## Project Structure

- **`MQTT_DATA.py`:** Python script that simulates a temperature sensor. It publishes random temperature values to an MQTT broker using WebSockets.
- **`index.html`:** A web dashboard that connects to the MQTT broker, subscribes to the temperature topic, and displays live sensor data with alarm functionality.

---

## How It Works

1. **Data Publishing:**
   - The Python script (`MQTT_DATA.py`) acts as a temperature sensor, publishing random values (50–100°C) to the topic `sensor/temperature` on the MQTT broker.
2. **Data Visualization:**
   - The web dashboard (`index.html`) connects to the MQTT broker using MQTT.js and subscribes to the `sensor/temperature` topic.
   - The temperature values are displayed in real time on the dashboard.
   - If the temperature exceeds the threshold (default: 75°C), an alarm is triggered, and the status changes to red with an alert message.

---

## Requirements

### Python Script
- Python 3.x
- [Paho MQTT library](https://pypi.org/project/paho-mqtt/)
  
  Install via pip:
  ```bash
  pip install paho-mqtt
  ```

### Web Dashboard
- A web browser with JavaScript enabled
- Internet connection to load the MQTT.js library from the CDN

---

## Setup and Usage

### Step 1: Run the MQTT Publisher
1. Open the `MQTT_DATA.py` file.
2. Update the MQTT broker details if needed:
   - **Broker:** `broker.emqx.io`
   - **Port:** `8083` (WebSocket)
3. Run the script:
   ```bash
   python MQTT_DATA.py
   ```

### Step 2: Open the Web Dashboard
1. Open the `index.html` file in any modern web browser.
2. The dashboard will connect to the MQTT broker, subscribe to the topic, and display the live temperature data.

---

## Customization

- **Threshold Value:**  
  You can change the threshold value (default: 75°C) in both:
  - `MQTT_DATA.py` (line defining `THRESHOLD`)
  - `index.html` script section (`const THRESHOLD`).

- **MQTT Broker Details:**  
  Update the broker URL, port, or topic in both files to connect to a different MQTT broker.

---

## Applications

This system can be adapted for various real-world use cases, such as:
- Monitoring greenhouse temperatures in agriculture.
- Keeping track of medicine storage conditions in healthcare.
- Industrial equipment monitoring to prevent overheating.

---

## Future Improvements

- Add support for additional sensors (e.g., humidity, motion).
- Implement data logging and analytics for historical trends.
- Enhance the UI with more visualizations (e.g., charts).

---

Feel free to use and modify this project as needed. Contributions and suggestions are welcome!

--- 
