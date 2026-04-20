from sklearn.ensemble import RandomForestClassifier

# Sample training data
# [packet_size, protocol, port]
X = [
    [60, 6, 80], # normal web
    [70, 6, 443], # normal https
    [100, 17, 53], # DNS
    [1200, 17, 443], # video traffic

    [5000, 6, 80], # suspicious (too large)
    [4000, 17, 443], # suspicious
    [50, 6, 1], # unusual port
    [60, 6, 2] # suspicious scanning
]

# Labels: 0 = normal, 1 = attack
y = [0, 0, 0, 0, 1, 1, 1, 1]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

print("Model trained successfully!")