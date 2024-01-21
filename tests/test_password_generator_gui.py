import unittest
import tkinter as tk;
from tkinter import Tk, N, E, S, W
from unittest.mock import patch
import password_generator.gui as PasswordGeneratorGUI
from password_generator.constants import (
    WINDOW_TITLE,
    BUTTON_GENERATE_PASSWORD,
    COPY_SYMBOL,
    LABEL_GENERATED_PASSWORD,
    DEFAULT_PASSWORD_LENGTH,
    EMPTY_STRING,
)

class TestPasswordGeneratorGUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Tk()
        cls.app = PasswordGeneratorGUI(cls.root)
        cls.app.master.geometry("600x400")  # Set a fixed windo size for testing

    def test_title(self):
        self.assertEqual(self.root.title(), WINDOW_TITLE)

    def test_left_panel(self):
        left_panel = self.app.paned_window.panes()[0]
        self.assertIsNotNone(left_panel)

        labels = left_panel.winfo_children()
        self.assertEqual(labels[0].cget("text"), "Password Length:")
        self.assertIsInstance(labels[1], tk.Spinbox)
        self.assertEqual(labels[2].cget("text"), "Include Uppercase")
        self.assertEqual(labels[3].cget("text"), "Include Digits")
        self.assertEqual(labels[4].cget("text"), "Include Special Characters")

        separator_line = labels[5]
        self.assertIsInstance(separator_line, tk.Canvas)
        self.assertEqual(separator_line.winfo_width(), 1)

    def test_right_panel(self):
        right_panel = self.app.paned_window.panes()[1]
        self.assertIsNotNone(right_panel)

        labels = right_panel.winfo_children()
        self.assertEqual(labels[0].cget("text"), LABEL_GENERATED_PASSWORD)
        self.assertIsInstance(labels[1], tk.Entry)
        self.assertEqual(labels[2].cget("text"), COPY_SYMBOL)
        self.assertIsInstance(labels[3], tk.Button)
        self.assertEqual(labels[4].cget("text"), BUTTON_GENERATE_PASSWORD)
        self.assertIsInstance(labels[5], tk.Button)

    def test_menu(self):
        menu_bar = self.root.nametowidget(self.root.winfo_pathname(self.root.winfo_id()))
        file_menu = menu_bar.nametowidget(menu_bar.winfo_children()[0])

        file_menu.invoke(0)  # Trigger Exit command
        self.assertEqual(self.root.winfo_exists(), 0)  # The application should be destroyed

    def test_about_dialog(self):
        with patch.object(self.app, 'show_about_dialog') as mock_method:
            menu_bar = self.root.nametowidget(self.root.winfo_pathname(self.root.winfo_id()))
            help_menu = menu_bar.nametowidget(menu_bar.winfo_children()[1])
            help_menu.invoke(0)  # Trigger About command
            mock_method.assert_called_once()

    def test_generate_password(self):
        with patch.object(self.app, 'generate_password') as mock_method:
            self.app.animate_generation()
            mock_method.assert_called_once()

    def test_copy_to_clipboard(self):
        with patch('builtins.print') as mock_print:
            self.app.copy_to_clipboard()
            mock_print.assert_called_with("Password copied to clipboard!")

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

if __name__ == '__main__':
    unittest.main()
