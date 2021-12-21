from src.deal import App

if __name__ == "__main__":
    try:
        App()
    except KeyboardInterrupt:
        print('Goodbye.')