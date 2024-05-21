import unittest
from unittest.mock import patch
import os
from PIL import Image
import Main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.st_mock = patch('Main.st').start()

    def tearDown(self):
        patch.stopall()
        if os.path.exists("OOPBilledeTingeling.png"):
            os.remove("OOPBilledeTingeling.png")

    def test_main(self):
        self.st_mock.sidebar.multiselect.return_value = ['Cirkel', 'Rektangel', 'Trekant', 'Ottekant']
        self.st_mock.sidebar.slider.return_value = 50
        self.st_mock.sidebar.color_picker.return_value = '#FF6347'
        self.st_mock.button.return_value = True

        Main.main()

        self.st_mock.title.assert_called_once_with('Figurer med OOP')
        self.st_mock.sidebar.multiselect.assert_called_once_with("Vælg former for at tegne:", ['Cirkel', 'Rektangel', 'Trekant', 'Ottekant'], default=['Cirkel', 'Rektangel', 'Trekant', 'Ottekant'])
        self.assertEqual(self.st_mock.sidebar.slider.call_count, 14)
        self.assertEqual(self.st_mock.sidebar.color_picker.call_count, 4)
        self.st_mock.button.assert_called_once_with('Gem billede')
        self.st_mock.success.assert_called_once_with("Billedet er gemt!")
        self.assertTrue(os.path.exists("OOPBilledeTingeling.png"))

if __name__ == "__main__":
    unittest.main()