# MQTT Signal Receiver and Dashboard

This project is designed to receive MQTT signals, store them in MongoDB, and provide a dashboard to view the stored signals. The project includes a simple server and client setup to simulate and process MQTT signals.

## Project Structure

- **requirements.txt**: Contains the Python dependencies required for the project.
- **start-server.bat**: A batch script to start the server that listens for MQTT signals and stores them in MongoDB.
- **start-client.bat**: A batch script to start the client that emits MQTT signals.

## Installation

To get started with the project, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone httpsgithub.com/ramdasi/mqtt-sample.git
   cd your-repo
2. **Install the required Python dependencies:**

   Ensure you have Python 3.10 installed on your system. Then, install the dependencies using pip:

   ```bash
   pip install -r requirements.txt

## Usage
1. Starting the Server
   To start the server that will receive and store MQTT signals:
   
   Run the start-server.bat by clicking it.
   The server will start and begin listening for MQTT signals. It also provides an API to view all stored signals at:

   ```bash
   http://localhost:8000/dashboard
   
2. Starting the Client
To start the client that will emit MQTT signals:

Run the start-client.bat by clicking it.
The client will start emitting MQTT signals to the server.

## Stopping the Programs
To stop either the server or the client, press Ctrl+C in the terminal where the script is running.
The shutdown process may take 2-5 seconds.
