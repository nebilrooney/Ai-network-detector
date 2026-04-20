from scapy.all import *
from sklearn.ensemble import RandomForestClassifier

# -------------------------
# TRAIN MODEL
# -------------------------
X = [
    [60, 6, 443],
    [70, 6, 80],
    [90, 6, 443],
    [120, 17, 53],
    [150, 6, 443],

    [2000, 6, 80],
    [3000, 6, 80],
    [4000, 17, 443],
    [5000, 6, 22],
    [6000, 6, 21],
]

y = [0,0,0,0,0,1,1,1,1,1]

model = RandomForestClassifier()
model.fit(X, y)

print("🚀 AI Detector Running...\n")

# -------------------------
# LAST MESSAGE MEMORY
# -------------------------
last_result = ""

# -------------------------
# PACKET HANDLER
# -------------------------
def packet_handler(packet):
    global last_result

    if packet.haslayer(IP):

        protocol = packet.proto
        size = len(packet)

        port = 0
        if packet.haslayer(TCP):
            port = packet[TCP].dport
        elif packet.haslayer(UDP):
            port = packet[UDP].dport

        features = [size, protocol, port]

        # RULE DETECTION
        if size > 1500:
            result = "🚨 ALERT detected"
        else:
            prediction = model.predict([features])[0]

            if prediction == 1:
                result = "🚨 ALERT detected"
            else:
                result = "✅ Normal traffic"

        # Print only if changed
        if result != last_result:
            print(result)
            last_result = result

# -------------------------
# START
# -------------------------
sniff(prn=packet_handler, count=30)
