# importanto bibliotecas
import random
import string
import pyperclip
import PySimpleGUI as sg

# layout tela
sg.theme("DarkGrey14")
layout = [
    [sg.Image("logo.png")],
    [sg.Text("Tamanho:", font="Poppins"),
        sg.Input(size=4, font="Poppins", key="tamanho", justification="center", pad=(20, 20)),
        sg.Text("caracteres", font="Poppins")],
    [sg.Button("Gerar Senha", size=25, font="Poppins", button_color="#3eb72a", pad=(20, 20))],
    [sg.Text("A senha gerada foi:", font="Poppins")],
    [sg.InputText(size=23, font="Poppins", key="saida", justification="center"),
        sg.Button("Copiar", font="Poppins 11", button_color="#24292E")],
]
tela = sg.Window("Gerador de Senha", element_justification="center", layout=layout, size=(700, 350), finalize=True)

while True:
    event, values = tela.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == "Gerar Senha" and values["tamanho"] == "":
        sg.popup("Informe o tamanho da senha!")

    elif event == "Gerar Senha":
        codificacao = string.ascii_letters + string.digits + "!@#$%&*+?/<>=().;:"
        rand = random.SystemRandom()
        tela["saida"].update(
            "".join(rand.choice(codificacao) for i in range(int(values["tamanho"])))
        )

    elif event == "Copiar":
        texto_copiar = values["saida"]
        pyperclip.copy(texto_copiar)
        sg.popup("Senha copiada para a área de transferência")

    elif event == "Sair":
        break
