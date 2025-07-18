import flet as ft 
from datetime import datetime
import random

def main(page: ft.Page):
    page.title = 'Мое первое приложение на Flet'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Привет, мир!")
    quote_text = ft.Text("", italic=True, color=ft.Colors.GREY)

    greeting_history = []
    history_text = ft.Text("История приветствий:")

    quotes = [
        "Улыбайся чаще!",
        "Сегодня будет отличный день!",
        "Ты молодец!",
        "Продолжай в том же духе!",
        "Не забывай мечтать!",
        "Каждый день — новый шанс!",
    ]

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"Привет, {name}!"
            greet_button.text = "Отправить еще раз"
            name_input.value = ""

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f'{timestamp} - {name}')
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)

            quote_text.value = random.choice(quotes)
        else:
            greeting_text.value = "Пожалуйте, введите имя!" 
            quote_text.value = ""
        
        page.update()
    
    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        quote_text.value = ""
        page.update()

    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.update()

    name_input = ft.TextField(label="Введите имя: ", on_submit=on_button_click)
    greet_button = ft.ElevatedButton("Отправить", on_click=on_button_click, icon=ft.Icons.SEND)
    clear_button = ft.IconButton(icon_color=ft.Colors.RED, icon=ft.Icons.DELETE, tooltip="Очистить историю", on_click=clear_history)
    theme_switch = ft.Switch(label="Темная тема", on_change=toggle_theme)

    page.add(
        theme_switch,
        greeting_text,
        quote_text,
        name_input,
        greet_button,
        clear_button,
        history_text
    )

ft.app(target=main, view=ft.WEB_BROWSER)
