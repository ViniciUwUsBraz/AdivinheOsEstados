import pandas
import turtle
import time

screen = turtle.Screen()
screen.setup(725,491)

background = "blank_states_img.gif"
screen.addshape(background)
turtle.shape(background)


data = pandas.read_csv("50_states.csv")
estados = data["state"].tolist()
x = data["x"].tolist()
y = data["y"].tolist()

escrever = turtle.Turtle()
escrever.penup()
escrever.hideturtle()

escrever2 = turtle.Turtle()
escrever2.penup()
escrever2.hideturtle()


run = 1
while run==1:
    life = 3
    certos = 0
    respostasCertas = []
    while life>0:
        resposta = screen.textinput(title="Adivinhe os estados", prompt="Qual o nome de algum estado?").lower()
        if resposta in estados:
            if resposta not in respostasCertas:
                respostasCertas.append(resposta)
                certos+=1
                index = estados.index(resposta)
                escrever.setpos(x[index],y[index])
                escrever.write(f"{resposta.title()}", font=("Verdana", 8,"normal"), align="center")
            else:
                escrever2.setpos(0,210)
                escrever2.write("Estado repetido", font=("Verdana", 24,"normal"), align="center")
                time.sleep(1)
                escrever2.clear()
        else:
            life-=1

        if certos==50:
            escrever.clear()
            escrever2.setpos(0,0)
            escrever2.write(f"Parabens voce acertou todos os estados", font=("Verdana", 24,"normal"), align="center")
            break
    run = int(screen.textinput(title="Jogar novamente?", prompt="1-Sim 0-Não"))



screen.exitonclick()


