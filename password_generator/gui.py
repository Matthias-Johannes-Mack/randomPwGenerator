import tkinter as tk
from tkinter import ttk, messagebox
from generator import PasswordGenerator
import constants
from constants import (
    ABOUT_MESSAGE,
    ANIMATION_SIZE,
    CLIPBOARD_MESSAGE,
    COPY_SYMBOL,
    DASH,
    EMPTY_STRING,
    GENERATION_DELAY,
    WINDOW_TITLE,
    LABEL_ABOUT,
    LABEL_GENERATED_PASSWORD,
    LABEL_INCLUDE_SPECIAL_CHARS,
    LABEL_INCLUDE_DIGITS,
    LABEL_INCLUDE_UPPERCASE,
    LABEL_MSSQL,
    LABEL_PASSWORD_LENGTH,
    LABEL_HELP,
    LABEL_SETTINGS,
    LABEL_EXIT,
    LABEL_FILE,
    BUTTON_GENERATE_PASSWORD,
    DEFAULT_PASSWORD_LENGTH,
    FONT_SIZE,
    FONT_NAME,
    LANGUAGE_ARRAY,
    COUNTRY_CODE_ARRAY,
    DEFAULT_WINDOW_SIZE,
    WINDOW_SIZES_ARRAY
)


class PasswordGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title(WINDOW_TITLE)

        self.languages = LANGUAGE_ARRAY
        self.country_codes = COUNTRY_CODE_ARRAY
        self.settings = constants.load_settings()

        self.selected_language = tk.StringVar(value=self.settings["locale"])

        self.create_variables()
        self.create_styles()
        self.create_paned_window()
        self.create_left_panel()
        self.create_right_panel()
        self.create_menu()

    def create_variables(self):
        self.length_var = tk.IntVar(value=DEFAULT_PASSWORD_LENGTH)
        self.include_uppercase_var = tk.BooleanVar(value=True)
        self.include_digits_var = tk.BooleanVar(value=True)
        self.include_special_chars_var = tk.BooleanVar(value=False)
        self.generated_password_var = tk.StringVar(value=EMPTY_STRING)
        self.mssql_policy_var = tk.BooleanVar(value=False)

    def create_styles(self):
        self.style = ttk.Style()
        self.style.configure(
            "TButton",
            padding=5,
            relief="flat",
            foreground="black",
            font=(FONT_NAME, FONT_SIZE),
        )
        self.style.configure(
            "TCheckbutton",
            padding=(5, 0, 5, 0),
            relief="flat",
            font=(FONT_NAME, FONT_SIZE),
        )
        self.style.configure(
            "Horizontal.TProgressbar",
            thickness=10,
            troughcolor="#B0B0B0",
            background="grey",
            font=(FONT_NAME, FONT_SIZE),
        )
        self.style.configure("TLabel", font=(FONT_NAME, FONT_SIZE))
        self.style.configure(
            "TEntry",
            padding=(5, 5),
            relief="flat",
            font=(FONT_NAME, FONT_SIZE),
            borderwidth=5,
            borderColor="grey",
        )

    def create_paned_window(self):
        self.paned_window = tk.PanedWindow(
            self.master, orient=tk.HORIZONTAL, sashwidth=5
        )
        self.paned_window.pack(expand=True, fill=tk.BOTH)

    def update_slider_label(self, value):
        self.length_var.set(round(float(value)))

    def adjust_window_size(self):
        selected_language = self.selected_language.get()
        self.master.geometry(WINDOW_SIZES_ARRAY.get(selected_language, "545x300"))

    def create_left_panel(self):
        left_panel = ttk.Frame(self.paned_window, style="TFrame")
        left_panel.grid(row=0, column=0, padx=10, pady=5, sticky="ns")
        self.paned_window.add(left_panel)

        ttk.Label(left_panel, text=LABEL_PASSWORD_LENGTH, style="TLabel").grid(
            row=0, column=0, pady=5
        )

        length_slider = ttk.Scale(
            left_panel,
            from_=1,
            to=100,
            variable=self.length_var,
            command=self.update_slider_label,
            orient=tk.HORIZONTAL,
            length=100,
        )
        length_slider.grid(row=0, column=1, pady=3)

        length_entry = ttk.Entry(
            left_panel,
            textvariable=self.length_var,
            width=5,
            validate="key",
            validatecommand=(self.master.register(self.validate_entry), "%P"),
        )
        length_entry.grid(row=0, column=2, pady=3)

        checkbox_labels = [
            LABEL_INCLUDE_UPPERCASE,
            LABEL_INCLUDE_DIGITS,
            LABEL_INCLUDE_SPECIAL_CHARS,
            LABEL_MSSQL,
        ]
        checkbox_variables = [
            self.include_uppercase_var,
            self.include_digits_var,
            self.include_special_chars_var,
            self.mssql_policy_var,
        ]

        for row, (label, var) in enumerate(
            zip(checkbox_labels, checkbox_variables), start=1
        ):
            ttk.Checkbutton(
                left_panel, text=label, variable=var, style="TCheckbutton"
            ).grid(row=row, column=0, columnspan=3, pady=0, sticky="nw")

        separator_line = tk.Canvas(left_panel, width=1, bg="#E0E0E0")
        separator_line.grid(row=0, column=3, rowspan=row, sticky="ns", padx=5)
        separator_line.create_line(1, 0, 1, row, width=1)

        self.adjust_window_size()

    def create_right_panel(self):
        right_panel = ttk.Frame(self.paned_window, style="TFrame")
        right_panel.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.paned_window.add(right_panel)

        ttk.Label(right_panel, text=LABEL_GENERATED_PASSWORD, style="TLabel").grid(
            row=0, column=0, pady=0, padx=0
        )

        password_entry = ttk.Entry(
            right_panel,
            textvariable=self.generated_password_var,
            state="readonly",
            width=30,
        )
        password_entry.grid(row=1, column=0, columnspan=2, pady=5)

        copy_button = ttk.Button(
            right_panel,
            text=COPY_SYMBOL,
            command=lambda: self.copy_to_clipboard(),
            width=3,
            style="TButton",
        )
        copy_button.grid(row=1, column=3, pady=6, padx=5, sticky="w")

        ttk.Button(
            right_panel,
            text=BUTTON_GENERATE_PASSWORD,
            command=self.animate_generation,
            style="TButton",
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=LABEL_FILE, menu=file_menu)
        file_menu.add_command(label=LABEL_SETTINGS, command=self.open_settings)
        file_menu.add_command(label=LABEL_EXIT, command=self.exit_application)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=LABEL_HELP, menu=help_menu)
        help_menu.add_command(label=LABEL_ABOUT, command=self.show_about_dialog)

    def validate_entry(self, value):
        return value.isdigit()

    def generate_password(self):
        password_gen = PasswordGenerator()
        password_gen.set_length(int(self.length_var.get()))
        password_gen.set_include_uppercase(self.include_uppercase_var.get())
        password_gen.set_include_digits(self.include_digits_var.get())
        password_gen.set_include_special_chars(self.include_special_chars_var.get())
        password_gen.set_mssql_policy(self.mssql_policy_var.get())

        self.generated_password_var.set(password_gen.generate_password())

    def animate_generation(self):
        animation_pattern = DASH
        for _ in range(ANIMATION_SIZE):
            self.generated_password_var.set(animation_pattern)
            self.master.update_idletasks()
            self.master.after(GENERATION_DELAY)
            animation_pattern += DASH
        self.generate_password()

    def copy_to_clipboard(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.generated_password_var.get())
        self.master.update()
        messagebox.showinfo(EMPTY_STRING, CLIPBOARD_MESSAGE)

    def show_about_dialog(self):
        messagebox.showinfo(LABEL_ABOUT, ABOUT_MESSAGE)

    def exit_application(self):
        self.master.destroy()

    def open_settings(self):
        settings_window = tk.Toplevel(self.master)
        settings_window.title(LABEL_SETTINGS)

        frame = ttk.Frame(settings_window)
        frame.pack(padx=20, pady=10)

        for language, country_code in zip(self.languages, self.country_codes):
            button = ttk.Radiobutton(
                frame,
                text=f"{language} ({country_code})",
                variable=self.selected_language,
                value=country_code,
                command=self.print_selected_language,
            )
            button.pack(side=tk.LEFT, padx=5)

    def print_selected_language(self):
        selected_language = self.selected_language.get()
        messagebox.showinfo(
            "Language Selected", f"Selected Language: {selected_language}"
        )
        constants.update_gettext_locale(selected_language)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(DEFAULT_WINDOW_SIZE)
    app = PasswordGeneratorGUI(root)
    root.mainloop()
