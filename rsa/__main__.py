# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from app import RsaApp
from console_io import ConsoleIO
from key import Key
from message import Message


def main():
    consoleio = ConsoleIO()
    keyprocessing = Key()
    messageprocessing = Message()
    app = RsaApp(consoleio, keyprocessing, messageprocessing)
    app.run()

if __name__ == '__main__':
    main()
