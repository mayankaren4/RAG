import logging

import uvicorn

from app import app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)-15s - %(level-name)-8s - %(message)s')

    # set reload = True only for the development mode.
    uvicorn.run("main:app", host="127.0.0.1", port=1025, reload=True)
