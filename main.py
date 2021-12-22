from src.data import App
from dotenv import dotenv_values

if __name__ == "__main__":
    try:
        config = dotenv_values(".env")
        App(config)
    except KeyboardInterrupt:
        print('Goodbye.')