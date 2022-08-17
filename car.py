VERTICAL = 0
HORIZONTAL = 1
UP = 'u'
DOWN = 'd'
LEFT = 'l'
RIGHT = 'r'


class Car:
    """
    This class represents the cars of the game
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col)
        location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coordinates_list = []
        if self.orientation == VERTICAL:
            for i in range(self.length):
                coordinates_list.append((self.location[0] + i,
                                         self.location[1]))
        elif self.orientation == HORIZONTAL:
            for i in range(self.length):
                coordinates_list.append((self.location[0],
                                         self.location[1] + i))
        return coordinates_list

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
        permitted by this car.
        """
        if self.orientation == VERTICAL:
            return {UP: 'cause the car to go up',
                    DOWN: 'cause the car to go down'}
        elif self.orientation == HORIZONTAL:
            return {LEFT: 'cause the car to go left',
                    RIGHT: 'cause the car to go right'}

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this
         move to be legal.
        """
        if self.orientation == VERTICAL:
            if movekey == UP:
                return [(self.location[0]-1, self.location[1])]
            elif movekey == DOWN:
                return [(self.location[0] + self.length, self.location[1])]
        elif self.orientation == HORIZONTAL:
            if movekey == RIGHT:
                return [(self.location[0], self.location[1] + self.length)]
            elif movekey == LEFT:
                return [(self.location[0], self.location[1] - 1)]

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if self.orientation == VERTICAL:
            if movekey == UP:
                self.location = (self.location[0]-1, self.location[1])
                return True
            if movekey == DOWN:
                self.location = (self.location[0] + 1, self.location[1])
                return True
        elif self.orientation == HORIZONTAL:
            if movekey == LEFT:
                self.location = (self.location[0], self.location[1] - 1)
                return True
            if movekey == RIGHT:
                self.location = (self.location[0], self.location[1] + 1)
                return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name
