import re
import tldextract

def extract_features(url):
    features = []

    # 1. URL Length
    features.append(len(url))

    # 2. Number of dots
    features.append(url.count("."))

    # 3. Contains @
    features.append(1 if "@" in url else 0)

    # 4. Contains -
    features.append(1 if "-" in url else 0)

    # 5. Uses HTTPS
    features.append(1 if url.startswith("https") else 0)

    # 6. Suspicious words
    suspicious_words = ["login", "verify", "update", "secure", "bank"]
    features.append(1 if any(word in url.lower() for word in suspicious_words) else 0)

    return features
