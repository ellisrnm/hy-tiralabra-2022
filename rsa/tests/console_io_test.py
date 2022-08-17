# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access

import unittest
from unittest.mock import patch
from console_io import ConsoleIO


class TestConsoleIo(unittest.TestCase):
    def setUp(self):
        self._io = ConsoleIO()

    @patch('builtins.print')
    def test_write(self, mock_print):
        self._io.write('Hei!')
        mock_print.assert_called_with('Hei!')

    @patch('builtins.input', lambda *args: '1')
    def test_read(self):
        received_input = self._io.read('Valitse: ')
        self.assertEqual(received_input, '1')
