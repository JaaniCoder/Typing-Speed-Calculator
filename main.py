import flet as ft
from auth import sign_up, login
from typing_test import calculate_wpm, calculate_accuracy
import time


def main(page: ft.Page):
    page.title = "Typing Speed Calculator"
    page.bgcolor = ft.colors.GREY

    user = {"is_authenticated": False, "username": None}
    start_time = None

    test_text = "The quick brown fox jumps over the lazy dog."

    username_field = ft.TextField(label="Username", width=300)
    password_field = ft.TextField(label="Password", width=300, password=True)
    feedback = ft.Text(color=ft.colors.RED_600)

    result_text = ft.Text("", size=16, weight=ft.FontWeight.BOLD)

    typing_field = ft.TextField(
        label="Start Typing Here...",
        multiline=True,
        width=600,
        height=150,
        on_focus=lambda e: start_typing(),
        on_blur=lambda e: e,
    )

    def show_main_screen():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text(f"Welcome, {user['username']}!\n", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text("Type the following text as fast and accurately as you can: \n\n", size=14),
                    ft.Text(test_text, size=14, italic=True, color=ft.colors.BLUE_800),
                    typing_field,
                    ft.ElevatedButton("Submit", color=ft.colors.GREEN_100, on_click=submit_typing_result),
                    result_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0
            )
        )
        page.update()

    def start_typing():
        nonlocal start_time
        start_time = time.time()

    def submit_typing_result(e):
        end_time = time.time()
        typed_text = typing_field.value
        wpm = calculate_wpm(typed_text, start_time, end_time)
        accuracy = calculate_accuracy(test_text, typed_text)
        result_text.value = f"Typing Speed: {wpm} WPM | Accuracy: {accuracy}%"
        page.update()

    def show_login_screen():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Login", color=ft.colors.BLACK26, size=20, weight=ft.FontWeight.BOLD),
                    username_field,
                    password_field,
                    ft.ElevatedButton("Login", on_click=handle_login),
                    ft.TextButton("Don't have an account? Sign Up", on_click=lambda _: show_sign_up_screen()),
                    feedback,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
        )
        page.update()

    def show_sign_up_screen():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Sign Up", color=ft.colors.BLACK26, size=20, weight=ft.FontWeight.BOLD),
                    username_field,
                    password_field,
                    ft.ElevatedButton("Sign Up", on_click=handle_sign_up),
                    ft.TextButton("Already Have an account? Login", on_click=lambda _: show_login_screen()),
                    feedback,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
        )
        page.update()

    def handle_login(e):
        success, message = login(username_field.value, password_field.value)
        feedback.value = message
        if success:
            user["is_authenticated"] = True
            user["username"] = username_field.value
            show_main_screen()
        else:
            page.update()

    def handle_sign_up(e):
        success, message = sign_up(username_field.value, password_field.value)
        feedback.value = message
        page.update()

    show_login_screen()


ft.app(target=main)
