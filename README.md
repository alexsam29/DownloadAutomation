# Download Automation
This is a Python automation script that sorts downloaded files into different folders based on their extensions. This script is designed to run in the background and monitor system file events using the [Watchdog](https://pypi.org/project/watchdog/) library.

## Prerequisites
This script requires Python 3.8 or later. You can download Python from [here](https://www.python.org/downloads/).

## Installation
1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the following command to install the required libraries:
```bash
pip install -r requirements.txt
```
4. Run the following command to start the script:
```bash
python fileSorter.py
```

## Usage
The script will monitor the Downloads folder and sort files into different folders based on their extensions. The default folder structure is as follows:
```
.../Downloads/
├── Documents/
├── Images/
├── Audio/
├── Videos/
```