# MQTT Signal Receiver and Dashboard

This project is designed to receive MQTT signals, store them in MongoDB, and provide a dashboard to view the stored signals. The project includes a simple server and client setup to simulate and process MQTT signals.

## Project Structure

- **requirements.txt**: Contains the Python dependencies required for the project.
- **start-server.bat**: A batch script to start the server that listens for MQTT signals and stores them in MongoDB.
- **start-client.bat**: A batch script to start the client that emits MQTT signals.

## Installation

To get started with the project, follow these steps:

1. **Clone the repository:**
   Use Terminal or Command prompt to run following commands
   ```bash
   git clone https://github.com/ramdasi/mqtt-sample.git
   cd mqtt-sample
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
   ```
    Note: If using Linux, following command can be used
   ```bash
   python .\server\main.py
2. Starting the Client
   To start the client that will emit MQTT signals:
   
   Run the start-client.bat by clicking it.
   The client will start emitting MQTT signals to the server.
   Note: If using Linux, following command can be used
   ```bash
   python .\server\status-emmiter.py
## Stopping the Programs
To stop either the server or the client, press Ctrl+C in the terminal where the script is running.
The shutdown process may take 2-5 seconds.

## Debugging
1. MongoDB Compass Url
   Paste the following url to debug or view database in MongoDB Compass:
   ```bash
   mongodb+srv://upswing:upswing24@cluster0.yzuqkah.mongodb.net/
2. RabbitMQ Url
   Following is rabbitMQ url which can be pasted to browser to debug rabbitMQ queues
   ```bash
   https://puffin.rmq2.cloudamqp.com/#/queues

Thanks for reading
