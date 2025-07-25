import flet as ft
from datetime import datetime
import random
import re

def main(page: ft.Page):
    page.title = 'Мое первое приложение на Flet'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Привет, мир!")
    quote_text = ft.Text("", italic=True, color=ft.Colors.GREY)
    history_text = ft.Text("История приветствий:")

    greeting_history = []
    history_visible = True  # Флаг видимости истории

    quotes = [
        "Улыбайся чаще!",
        "Сегодня будет отличный день!",
        "Ты молодец!",
        "Продолжай в том же духе!",
        "Не забывай мечтать!",
        "Каждый день — новый шанс!",
    ]

    def get_greeting_color():
        hour = datetime.now().hour
        if 6 <= hour < 12:
            return ft.Colors.YELLOW
        elif 12 <= hour < 18:
            return ft.Colors.ORANGE
        elif 18 <= hour < 24:
            return ft.Colors.RED
        else:
            return ft.Colors.BLUE

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"Привет, {name}!"
            greeting_text.color = get_greeting_color()
            greet_button.text = "Отправить еще раз"
            name_input.value = ""

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f'{timestamp} - {name}')
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
            quote_text.value = random.choice(quotes)
        else:
            greeting_text.value = "Пожалуйста, введите имя!"
            greeting_text.color = ft.Colors.BLACK
            quote_text.value = ""

        page.update()

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()

    def toggle_theme(_):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.update()

    def toggle_history_visibility(_):
        nonlocal history_visible
        history_visible = not history_visible
        history_text.visible = history_visible
        toggle_history_button.text = "Показать историю" if not history_visible else "Скрыть историю"
        page.update()

    def validate_input(e):
        # Разрешаем только буквы и пробелы
        new_value = re.sub(r"[^а-яА-Яa-zA-Z ]", "", e.control.value)
        if new_value != e.control.value:
            e.control.value = new_value
            page.update()

    name_input = ft.TextField(
        label="Введите имя: ",
        on_submit=on_button_click,
        on_change=validate_input,
    )

    greet_button = ft.ElevatedButton("Отправить", on_click=on_button_click, icon=ft.Icons.SEND)
    clear_button = ft.IconButton(
        icon_color=ft.Colors.RED,
        icon=ft.Icons.DELETE,
        tooltip="Очистить историю",
        on_click=clear_history,
    )

    theme_switch = ft.Switch(label="Темная тема", on_change=toggle_theme)
    toggle_history_button = ft.ElevatedButton("Скрыть историю", on_click=toggle_history_visibility)

    page.add(
        ft.Row([theme_switch, clear_button, toggle_history_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
        ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([quote_text], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([name_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([greet_button], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([history_text], alignment=ft.MainAxisAlignment.CENTER),
    )

ft.app(target=main, view=ft.WEB_BROWSER)
