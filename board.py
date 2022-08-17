SIZE = 7


class Board:
    """
    This class represents the board of the game
    """

    def __init__(self):
        self.__lst = [["_"] * SIZE + ["#"] for _ in range(SIZE)]
        self.__lst[len(self.__lst)//2][SIZE] = "E"
        self.cars = {}
        self.exit = (3, 7)

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        print_str = ''
        for i in range(len(self.__lst)):
            for j in range(len(self.__lst[i])):
                print_str += ' ' + self.__lst[i][j]
            print_str += '\n'
        return print_str

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cell_list = []
        for i in range(len(self.__lst)):
            for j in range(len(self.__lst[i]) - 1):
                cell_list.append((i, j))
        cell_list.append(self.exit)
        return cell_list

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        moves_lst = []
        for car in self.cars.values():
            moves_dict = car.possible_moves()
            for move in moves_dict:
                requested_coordinates = car.movement_requirements(move)[0]
                if requested_coordinates in self.cell_list():
                    if self.cell_content(requested_coordinates) is None:
                        moves_lst.append((car.get_name(), move,
                                          moves_dict[move]))
        return moves_lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        return self.exit

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if (self.__lst[coordinate[0]][coordinate[1]] == '_' or
                self.__lst[coordinate[0]][coordinate[1]] == 'E'):
            return None
        else:
            return self.__lst[coordinate[0]][coordinate[1]]

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        if car.get_name() not in self.cars:
            for coordinate in car.car_coordinates():
                if coordinate in self.cell_list():
                    if self.cell_content(coordinate) is not None:
                        return False
                else:
                    return False
        else:
            return False
        self.cars.update({car.get_name(): car})
        for coordinate in car.car_coordinates():
            self.__lst[coordinate[0]][coordinate[1]] = car.get_name()
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        if name in self.cars:
            car = self.cars[name]
            if movekey in car.possible_moves():
                coordinate = \
                    car.movement_requirements(movekey)[0]
                if coordinate in self.cell_list():
                    if self.cell_content(coordinate) is None:
                        past_coordinates = set(car.car_coordinates())
                        if car.move(movekey):
                            self.__lst[coordinate[0]][coordinate[1]] = \
                                car.get_name()
                            current_coordinates = (set(car.car_coordinates()) -
                                                   {coordinate})
                            temp = \
                                list(past_coordinates - current_coordinates)[0]
                            self.__lst[temp[0]][temp[1]] = '_'
                            return True
        else:
            return False
        return False
