import os
import asyncio
from ExpertOptionApiV2.stable_api import ExpertOptionApiV2

TOKEN = os.getenv("EXPERTOPTION_TOKEN")

async def main():
    print("ExpertOption Signal Bot")

    if not TOKEN:
        print("ERROR: Token not found")
        return

    print("Token loaded securely")

    api = ExpertOptionApiV2(
        TOKEN,
        server_region="wss://fr24g1eu.expertoption.finance/ws/v40"
    )

    try:
        await api.connect()
        print("Connected to ExpertOption")

        balance = await api.GetBalance()
        print("Balance:", balance)

        candles = await api.GetSingleCandles()
        print("Candles received:", candles)

    except Exception as e:
        print("Connection error:", type(e).__name__, str(e))

if __name__ == "__main__":
    asyncio.run(main())
