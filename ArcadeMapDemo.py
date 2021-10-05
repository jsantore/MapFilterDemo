import random

import arcade

# once we understand this - lets add a couple of asteroids and try filter


class MapDemoWindow(arcade.Window):
    def __init__(self):
        super().__init__(width=1080, height=960, title="Demo Map")
        self.shipList = arcade.SpriteList()
        # now add 5 ships
        for count in range(5):
            ship = arcade.Sprite(":resources:images/space_shooter/playerShip1_blue.png")
            ship.change_y = 3
            ship.center_x = random.randint(int(ship.width/2), int(1080-ship.width/2))
            ship.center_y = random.randint(50, 700)
            self.shipList.append(ship)

    def on_update(self, delta_time: float):
        tempList = arcade.SpriteList()
        adjustedList = list(map(flip_ship, self.shipList))
        tempList.extend(adjustedList)
        self.shipList = tempList
        tempList.update()

    def on_draw(self):
        arcade.start_render()
        self.shipList.draw()


def flip_ship(ship: arcade.Sprite):
    if ship.change_y <0 and (ship.center_y-ship.height/2)<0:
        ship.change_y = -ship.change_y
    elif ship.change_y >0 and (ship.center_y+ship.height/2)>960:
        ship.change_y = -ship.change_y
    return ship


def main():
    window = MapDemoWindow()
    arcade.run()

if __name__ == '__main__':
    main()