import time
import serial

# Define the RFC2217 server address and port
rfc2217_server_port = 4000
rfc2217_server_url = f"rfc2217://localhost:{rfc2217_server_port}"
log_file = "testlog.txt"

# Expected prompts and responses
interaction_sequence = [
    ("What are the next 8 encodings?", "KJUEZEEJ"),
    ("What are the next 16 encodings?", "1271379391471391"),
    ("What are the next 8 encodings?", "cdefkopq"),
    ("What are the next 8 encodings?", "kuvclngo")
]

def connect_to_serial():
    while True:
        try:
            # Attempt to connect to the serial port
            ser = serial.serial_for_url(rfc2217_server_url, baudrate=115200, timeout=1)
            print(f"Connected to serial port on {rfc2217_server_url}")
            return ser
        except serial.SerialException:
            print("Serial port not available. Retrying in 2 seconds...")
            time.sleep(2)

def log_to_file(data):
    with open(log_file, "a") as f:
        f.write(data + "\n")

def handle_interaction(ser):
    sequence_index = 0

    try:
        while sequence_index < len(interaction_sequence):
            # Read a full line from serial
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            
            if line:
                print(f"Received: {line}")
                log_to_file(f"Received: {line}")
                
                # Check if the current line contains the expected prompt
                expected_prompt, response = interaction_sequence[sequence_index]
                if expected_prompt in line:
                    # Send the response
                    print(f"Sending: {response}")
                    ser.write((response + "\n").encode('utf-8'))
                    log_to_file(f"Sent: {response}")
                    sequence_index += 1
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()

if __name__ == "__main__":
    # Open or clear the log file
    open(log_file, "w").close()

    # Connect to the serial port and handle interaction
    serial_connection = connect_to_serial()
    handle_interaction(serial_connection)
