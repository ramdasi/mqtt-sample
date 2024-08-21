from api_handler import start_server, stop_server
from pika_consumer import start_consumer, stop_consumer
import sys
import signal
import threading


def signal_handler(sig, frame):
    print("Stopping the server and consumer...")
    if server_thread.is_alive():
        stop_server()
        stop_consumer()
        exit()
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    start_consumer()
