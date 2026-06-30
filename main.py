import flet as ft
import uuid

def generate_password(machine_id_hex):
    digits = ''.join(filter(str.isdigit, machine_id_hex))
    if not digits: 
        digits = str(int(machine_id_hex, 16))
    num = int(digits)
    result = round(abs(num / 2 * 3.14))
    return str(result)[:6]

def main(page: ft.Page):
    page.title = "Password Generator Tool"
    page.window_width = 400
    page.window_height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    machine_id_input = ft.TextField(label="Paste the Machine ID here", width=350)
    result_text = ft.Text(size=20, weight="bold", color=ft.Colors.GREEN)

    def on_click(e):
        machine_id = machine_id_input.value.strip()
        if machine_id:
            password = generate_password(machine_id)
            result_text.value = f"The Activation Password is: {password}"
        else:
            result_text.value = "Please enter a Machine ID"
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("--- Password Generator Tool ---", size=20, weight="bold"),
                machine_id_input,
                ft.ElevatedButton("Generate", on_click=on_click),
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)