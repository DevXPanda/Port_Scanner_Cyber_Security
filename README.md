# Port Scanner Project

## Overview

The **Port Scanner** is a Python-based tool designed to scan and identify open, closed, and filtered ports on a given target system. This tool is aimed at cybersecurity professionals, network administrators, and anyone interested in auditing network security.

## Features

- **Multi-threaded Scanning**: Efficiently scans multiple ports concurrently to save time.
- **Service Identification**: Detects services running on open ports (e.g., HTTP, SSH).
- **Banner Grabbing**: Retrieves the banner information for services to help identify service versions.
- **Logging**: Stores scan results in a structured text file (`scan_report.txt`) for later analysis.

## Installation

### Prerequisites

- **Python 3.x** (Ensure you have Python 3 or higher installed)
- **Required Libraries**:  
  You will need some Python libraries, which can be installed using `pip`.

### Installation Steps

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/DevXPanda/Port-Scanner.git
2. Navigate to the project directory:
    cd Port-Scanner.
3. INstall the require python libraries:
    pip install -r requirements.txt
4. Run the port scanner:
    pythn3 port_scanner.py
Usage
Once installed, you can use the port scanner by running the script from your command line or terminal.

Example Usage:

bash
Copy code
python3 port_scanner.py
You will be prompted to enter:

The target IP address of the system you want to scan (e.g., 127.0.0.1 for localhost).
The start and end port range to scan (e.g., 1 to 1000).
The number of threads (e.g., 10 to speed up scanning).
The scanner will display the open ports and their associated services, and store the results in a file (scan_report.txt).

Example Output:
Scanning ports 1 to 100 on 192.168.1.1...
[OPEN] Port 22: Service - SSH
[OPEN] Port 80: Service - HTTP
[CLOSED] Port 25
[OPEN] Port 443: Service - HTTPS
Contributing
If you'd like to contribute to this project, you can follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes and commit them (git commit -m 'Add feature').
Push your changes to your forked repository.
Create a pull request on GitHub.

