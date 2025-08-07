from nicegui import ui


def main():
    ui.label("Hello from NiceGUI Scanner App!")
    ui.button("Click me!", on_click=lambda: ui.notify("Button clicked!"))
    
    ui.run(port=3001)


if __name__ in {"__main__", "__mp_main__"}:
    main()
