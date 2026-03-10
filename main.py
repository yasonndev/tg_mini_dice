import asyncio
import logging

from app.bot import start

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start())