import logging
import asyncio

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s : %(levelname)s\t : %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    handlers=[logging.FileHandler('filename.log'), logging.StreamHandler()])

async def main_event_loop():
    while True:
        logging.info('Tick')
        await asyncio.sleep(1.0)

loop = asyncio.get_event_loop()
task = loop.create_task(main_event_loop())

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass