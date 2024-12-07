import socket
import threading
from queue import Queue
import time

def banner_grab(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target, port))
        sock.send(b'Hello\r\n')
        banner = sock.recv(1024).decode().strip()
        return banner
    except:
        return "No Banner"
    finally:
        sock.close()

import socket
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))  # 0 = open, other = closed/filtered
        if result == 0:
            try:
                service_name = socket.getservbyport(port, 'tcp')
            except:
                service_name = "Unknown"
            banner = banner_grab(target, port)
            print(f"[OPEN] Port {port} - Service: {service_name} - Banner: {banner}")
            with open("scan_report.txt", "a") as report_file:
                report_file.write(f"Port {port} - OPEN - Service: {service_name} - Banner: {banner}\n")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Worker thread function
def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(target, port)
        queue.task_done()

# Main function
def port_scanner(target, start_port, end_port, num_threads):
    global queue
    queue = Queue()
    for port in range(start_port, end_port + 1):
        queue.put(port)

    print(f"Starting scan on {target} from port {start_port} to {end_port} with {num_threads} threads...\n")
    start_time = time.time()

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"\nScan completed in {end_time - start_time:.2f} seconds.")
    print("Results saved in 'scan_report.txt'.")

# User inputs
if __name__ == "__main__":
    target = input("Enter the target IP: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    num_threads = int(input("Enter the number of threads: "))

    with open("scan_report.txt", "w") as report_file:
        report_file.write(f"Port Scan Report for {target}\n")
        report_file.write(f"Scan Range: {start_port} to {end_port}\n")
        report_file.write("============================================\n")

    port_scanner(target, start_port, end_port, num_threads)
































    
