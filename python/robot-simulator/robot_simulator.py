# Globals for the bearings
# Change the values as you see fit
EAST = 'east'
NORTH = 'north'
WEST = 'west'
SOUTH = 'south'


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = bearing

    def turn_right(self):
        if self.bearing == EAST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = NORTH
        else:
            self.bearing = EAST

    def turn_left(self):
        if self.bearing == EAST:
            self.bearing = NORTH
        elif self.bearing == SOUTH:
            self.bearing = EAST
        elif self.bearing == WEST:
            self.bearing = SOUTH
        else:
            self.bearing = WEST

    def advance(self):
        if self.bearing == NORTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        elif self.bearing == SOUTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
        elif self.bearing == WEST:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])
        else:
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])

    def simulate(self, directions):
        for dir in directions:
            if dir == 'R':
                self.turn_right()
            elif dir == 'L':
                self.turn_left()
            else:
                self.advance()