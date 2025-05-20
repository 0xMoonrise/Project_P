# Project\_P – Baby Cry Detector with ESP32

Project\_P is an ESP32-based baby cry detector that monitors ambient sound and sends push notifications to your mobile device when a baby's cry is detected. This project is ideal for parents who want to be promptly alerted when their baby needs attention.

## Features

* Real-time baby cry detection using a microphone connected to ESP32
* Push notifications sent to your mobile device upon detection
* Configurable sensitivity and notification settings
* Lightweight implementation suitable for continuous operation

## Hardware Requirements

* ESP32 development board
* Microphone module (e.g., Ky-037 or similar)
* Optional: Additional sensors (e.g., temperature, humidity)

## Software Requirements

* MicroPython firmware installed on ESP32
* Python 3.x environment for development
* Required Python packages listed in `requirements.txt`

## Installation

1. Flash MicroPython firmware onto your ESP32 board.

2. Clone this repository:

   ```bash
   git clone https://github.com/0xMoonrise/Project_P.git
   ```

3. Navigate to the project directory:

   ```bash
   cd Project_P
   ```

4. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure your notification service credentials in the appropriate configuration file.

6. Upload the necessary scripts to your ESP32 board.

## Usage

Once set up, the ESP32 will continuously monitor ambient sound. When a baby's cry is detected, it will send a push notification to your configured mobile device.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

