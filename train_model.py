import joblib
from sklearn.ensemble import RandomForestClassifier

# Simple training data (You can improve later)
X = [
    [20, 1, 0, 0, 1, 0],   # Safe
    [75, 3, 0, 1, 0, 1],   # Phishing
    [15, 1, 0, 0, 1, 0],   # Safe
    [90, 4, 1, 1, 0, 1],   # Phishing
]

y = [0, 1, 0, 1]  # 0 = Safe, 1 = Phishing

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "phishguard/model.pkl")

print("Model trained and saved!")
