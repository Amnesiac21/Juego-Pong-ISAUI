# Se utilizara Turtle (es una libreria para inicializar a los niños a la programacion, esta orientada al dibujo) para desarrollar este Pong.
import turtle
import os
import winsound


# primero crearemos la ventana (Window), pondremos su titulo, background color y dimensiones.
window = turtle.Screen()
window.title('Pong')
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # deja las actualizaciones de pantalla en off.

# ----Score----
score_a = 0
score_b = 0


# ----Las barras (paddles)----

# paddle A

paddle_a = turtle.Turtle()
# le creamos la velocidad de la animacion y se la ingresamos en 0 porque nosotros le ingresaremos el speed.
paddle_a.speed(0)
paddle_a.shape('square')  # le damos forma cuadrada al paddle.
# aqui le damos en tamaño al paddle
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.color('white')  # le damos color
paddle_a.penup()  # para que no dibuje mientras se mueve el paddle.
# es para darle la direccion al paddle, con coordenadas X e Y. este metodo tiene distintos alias.
paddle_a.goto(-350, 0)

# paddle B
# hacemos lo mismo para el paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)

# ----Balon----
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
# Movilidad al Balon ---> esta parte se dividira en 2 (X movement & Y movement).
ball.dx = 0.2  # el balon se movera a px.
ball.dy = -0.2

# ----Tablero----

scr = turtle.Turtle()
scr.speed(0)
scr.color("white")
scr.penup()
scr.hideturtle()  # oculta el procedimiento de dibujo
scr.goto(0, 260)  # posicionamos el marcador en pantalla.
scr.write(f"Player A: {score_a} | Player B: {score_b}", align="center",
          font=("Courier", 24, "normal"))


# ----Funciones----:
# 1)Mover los padding con los Keyboard.


def paddle_a_up():
    # el funcion ycor() y xcor() devuelven la coordenada de la X e Y respectivamente.
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# ----Pausado----


en_pausa = False  # var Bandera


def pausado():
    global en_pausa
    if en_pausa == True:  # si esta pausado
        en_pausa = False  # despauso
    else:  # si no esta pausado
        en_pausa = True  # lo hago


# ----Binding ---> Paddles y Pausado.
window.listen()  # la ventana ahora lee los keyboard input.
# le asignamos la tecla W a la funcion paddle_a_up() para que funcione, luego tambien con las otras teclas...
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")
window.onkeypress(pausado, "p")  # tecla 'P' para pausar
# creamos el main loop game para durante su ejecucion.
while True:
    if not en_pausa:  # mientras no este pausado fluira el juego.
        window.update()

        # Mover el balon

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Check y limite a los bordes de la ventana y rebote.
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            # agregamos sonido al juego
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            scr.clear()
            scr.write(f"Player A: {score_a} | Player B: {score_b}", align="center",
                      font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            scr.clear()
            scr.write(f"Player A: {score_a} | Player B: {score_b}", align="center",
                      font=("Courier", 24, "normal"))

        # Colisiones de los Paddles y Balon.
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    else:
        window.update()
