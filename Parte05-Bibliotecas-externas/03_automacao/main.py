import pyautogui as auto

def ir_pesquisa():
    auto.press("tab")
    auto.press("tab")
    auto.press("tab")
    auto.press("tab")

def main():
    auto.PAUSE = 0.7
    auto.press("win")
    auto.write("firefox")
    auto.press("enter")
    auto.write("youtube.com.br")
    auto.press("enter")
    auto.sleep(3)
    ir_pesquisa()
    auto.write("Python")
    auto.press("enter")
    auto.sleep(3)
    auto.hotkey("ctrl","t")
    auto.write("Python.org")
    auto.press("enter")


if __name__ == "__main__":
    main()