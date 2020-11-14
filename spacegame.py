import play
play.set_backdrop("darkblue")

#-------------------------------------
spaceship = play.new_image(image="spaceship.png", size=15, x=0, y=-200)
asteroid1 = play.new_image(image="asteroid.png", size=3, x=-300, y=-100)
asteroid2 = play.new_image(image="asteroid.png", size=3, x=300, y=0)
asteroid3 = play.new_image(image="asteroid.png", size=3, x=-300, y=100)
finish = play.new_text(
    words="FINISH", x=0, y=250, font_size=100, color="yellow")
#-------------------------------------


@play.when_program_starts
def start():
    spaceship.start_physics(
        stable=True, obeys_gravity=False, bounciness=1, mass=10)
    asteroid1.start_physics(stable = False, x_speed = 5, y_speed = 0, obeys_gravity = False, bounciness = 1, mass = 1)
    asteroid2.start_physics(stable = False, x_speed = 5, y_speed = 0, obeys_gravity = False, bounciness = 1, mass = 1)
    asteroid3.start_physics(stable = False, x_speed = 5, y_speed = 0, obeys_gravity = False, bounciness = 1, mass = 1)



@play.repeat_forever
def do():
    spaceship.physics.y_speed = 0
    spaceship.physics.x_speed = 0

    if play.key_is_pressed('w'):
        spaceship.physics.y_speed = 15
    if play.key_is_pressed('s'):
        spaceship.physics.y_speed = -15
    if play.key_is_pressed('a'):
        spaceship.physics.x_speed = -15
    if play.key_is_pressed('d'):
        spaceship.physics.x_speed = 15
    if spaceship.is_touching(finish):
        asteroid1.hide()
        asteroid2.hide()
        asteroid3.hide()
        spaceship.hide()
        finish.hide()
        win = play.new_text(
            words="WIN", x=0, y=0, font_size=200, color="green")
    if spaceship.is_touching(asteroid1) or spaceship.is_touching(
            asteroid2) or spaceship.is_touching(asteroid3):
        asteroid1.hide()
        asteroid2.hide()
        asteroid3.hide()
        spaceship.hide()
        finish.hide()
        lose = play.new_text(
            words="LOSE", x=0, y=0, font_size=200, color="red")


play.start_program()
