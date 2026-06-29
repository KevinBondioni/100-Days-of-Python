from turtle import Turtle,Screen

#timmy=Turtle()
#print (timmy)
#timmy.shape("turtle")
#timmy.color("green2")
#timmy.forward(100)
#my_screen=Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable
pokemon=["Charmender","Squirtle","Bulbasaur","Pikachu"]
type=["Fire","Water","Grass","Electric"]
table=PrettyTable()

table.add_column("Pokemon name",pokemon)
table.add_column("Type",type)
table.align="l"
print(table)