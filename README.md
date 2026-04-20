#  AI-Powered Network Traffic Anomaly Detector

##  Project Overview

This project is a simple AI-based network security tool that captures live network traffic and detects unusual or suspicious activity in real time.

It uses packet capture, feature extraction, and machine learning to classify network traffic as either normal or suspicious.

The goal of this project is to demonstrate how AI can be applied in cybersecurity for basic anomaly detection such as unusual traffic patterns, large packets, or suspicious behavior.

---

##  Requirements

Before running the project, make sure Python is installed on your computer.

Install the required libraries:

pip install scapy scikit-learn numpy pandas

---

##  Project Structure

ai-network-detector/
 sniffer.py
 model.py
 README.md

---

##  Setup Instructions

### 1. Open the project folder

Go to the folder:

ai-network-detector

### 2. Install dependencies

Run:

pip install scapy scikit-learn numpy pandas

### 3. Run the project

Execute:

python sniffer.py

---

##  How It Works

1. The system captures live network packets using Scapy.

2. Each packet is converted into useful features such as:
- Packet size
- Protocol type
- Port number

3. The features are sent to a machine learning model.

4. The model classifies traffic as:
- Normal traffic
- Suspicious traffic

5. The result is displayed in real time in the terminal.

---

##  Example Output

✅ Normal traffic
🚨 ALERT detected
✅ Normal traffic

---

##  Technologies Used

- Python
- Scapy
- Scikit-learn
- RandomForestClassifier
- Terminal / Command Line

---

## Demo Video
https://youtu.be/5alJVP70PT4

