import flet as ft


def main(page: ft.Page):
    page.title = "RGB Mixer"

    def update_color(e):
        r, g, b = int(slider_r.value), int(slider_g.value), int(slider_b.value)
        color = f"#{r:02x}{g:02x}{b:02x}"
        page.bgcolor = color
        page.update()

    slider_r = ft.Slider(min=0, max=255, value=0, divisions=255, label="Red: {value}", on_change=update_color)
    slider_g = ft.Slider(min=0, max=255, value=0, divisions=255, label="Green: {value}", on_change=update_color)
    slider_b = ft.Slider(min=0, max=255, value=0, divisions=255, label="Blue: {value}", on_change=update_color)



    page.add(slider_r, slider_g, slider_b)


ft.app(target=main)
