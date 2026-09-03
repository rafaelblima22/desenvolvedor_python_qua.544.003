import pyautogui as auto
from datetime import date

#   
#   pip install pyinstaller
#   pyinstaller --onefile --name "Gitpush poltergeist v1.0" --icon "icon/ghost.ico" main.py

def hoje():
    return date.today().strftime("%d/%m/%Y")

def main():
    auto.PAUSE = 0.7
    auto.press("win")
    auto.write("cmd")
    auto.press("enter")
    auto.write("cd Rafael/desenvolvedor_python_qua.544.003")
    auto.press("enter")
    auto.write("git add .")
    auto.press("enter")
    auto.write(f'git commit -m "{hoje()}"')
    auto.press("enter")
    auto.write("git push")
    auto.press("enter")
    auto.alert(text="Finalizado com Sucesso!", button="Finalizado")

if __name__ == "__main__":
    main()