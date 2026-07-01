import turtle

screen= turtle.Screen()
screen.title("Regioni d'italia")
image="Immagine 2026-06-21 211844.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()