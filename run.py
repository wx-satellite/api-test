from util.config import Config

if __name__ == "__main__":
    c = Config()
    print(c.get_value("host"))
