import flet as ft
import os
import ssl

# --- حل مشكلة الأمان (SSL) للجهاز ---
# هذه الأسطر تجبر البرنامج على تجاهل فحص الشهادات المعطلة عند تحميل الأدوات
os.environ['PYTHONHTTPSVERIFY'] = '0'
ssl._create_default_https_context = ssl._create_unverified_context
# ----------------------------------

def main(page: ft.Page):
    page.title = "حاسبة احترافية"
    page.window_width = 350
    page.window_height = 500
    page.bgcolor = "#1e1e1e" # لون خلفية داكن
    
    display = ft.TextField(
        value="0", 
        text_align=ft.TextAlign.RIGHT, 
        width=300, 
        read_only=True,
        text_size=30,
        color="white"
    )

    def button_click(e):
        data = e.control.text
        if data == "C":
            display.value = "0"
        elif data == "=":
            try:
                display.value = str(eval(display.value.replace("×", "*").replace("÷", "/")))
            except:
                display.value = "Error"
        else:
            if display.value == "0":
                display.value = data
            else:
                display.value += data
        page.update()

    def b(text, color="#333333"):
        return ft.ElevatedButton(
            text=text, 
            on_click=button_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                bgcolor=color,
                color="white"
            ),
            width=70,
            height=70
        )

    page.add(
        ft.Column([
            ft.Row([display], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([b("7"), b("8"), b("9"), b("÷", "#f39c12")]),
            ft.Row([b("4"), b("5"), b("6"), b("×", "#f39c12")]),
            ft.Row([b("1"), b("2"), b("3"), b("-", "#f39c12")]),
            ft.Row([b("C", "#e74c3c"), b("0"), b("="), b("+", "#f39c12")]),
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)