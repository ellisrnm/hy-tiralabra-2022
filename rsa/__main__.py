from app import RsaApp
from console_io import ConsoleIO
from key import Key
from message import Message


def main():
    io = ConsoleIO()
    keyprocessing = Key()
    messageprocessing = Message()
    app = RsaApp(io, keyprocessing, messageprocessing)
    app.run()

if __name__ == '__main__':
    main()