import argparse
import joblib
from colorama import Fore, init
from phishguard.features import extract_features

init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description="PhishGuard - AI Phishing URL Detector")
    parser.add_argument("url", help="URL to analyze")
    args = parser.parse_args()

    print(Fore.CYAN + "🔍 Analyzing URL...\n")

    model = joblib.load("phishguard/model.pkl")
    features = extract_features(args.url)

    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0][1] * 100

    print(Fore.YELLOW + f"Risk Score: {probability:.2f}%\n")

    if prediction == 1:
        print(Fore.RED + "🚨 Result: PHISHING")
    else:
        print(Fore.GREEN + "✅ Result: SAFE")

if __name__ == "__main__":
    main()
