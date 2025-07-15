import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Моё первое приложение'

    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text('Привет мир')

    greet_button = ft.ElevatedButton('Отправить')

    greet_history = []
    histoy_text = ft.Text("История приветствия: ")

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f'Привет, {name}!'
            name_input.value = ''  

            greet_button.text = 'Отправить ещё раз'

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greet_history.append(f'{timestamp} - {name}')
            histoy_text.value = "История приветствия: \n" + "\n".join(greet_history)
        else:
            greeting_text.value = 'Пожалуйста, введите имя!'

        page.update()

    def clear_history(_):
        greet_history.clear()
        histoy_text.value = "История очищена: "
        page.update()

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, tooltip='Очистить историю', 
                                 on_click=clear_history, icon_color=ft.Colors.RED_ACCENT_700)

    name_input = ft.TextField(label='Введите имя:', on_submit=on_button_click)

    greet_button.on_click = on_button_click

    page.add(greeting_text, name_input, greet_button, clear_button, histoy_text)

ft.app(target=main, view=ft.WEB_BROWSER)
