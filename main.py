
import os
from datetime import datetime, timezone

def main():
    print("ExpertOption Signal Bot")
    print("Status: DEMO MODE")
    print("Time:", datetime.now(timezone.utc).isoformat())

    token = os.getenv("EXPERTOPTION_TOKEN")

    if token:
        print("ExpertOption token: configured")
    else:
        print("ExpertOption token: not configured")

    print("Waiting for authorized market data...")
    print("No live signals or trades are enabled.")

if __name__ == "__main__":
    main()
