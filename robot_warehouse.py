class Robot:
    def __init__(self, current_position) -> None:
        self.current_position = current_position
        self.crate_carried_id = 0

    def move_robot(self, commands):
        commands_list = commands.split(" ")
        print("commands_list: ", commands_list)
        print("Starting postion: ", self.current_position)
        for command in commands_list:
            if command in ["E", "W"]:
                self.move_horizontally(command)
            elif command in ["N", "S"]:
                self.move_vertically(command)
            else:
                print("direction not found")

    def move_horizontally(self, direction):
        y = self.current_position[1]

        if direction == "E":
            if self.boundary_status([self.current_position[0], y + 1]):
                self.current_position[1] += 1
            else:
                print("Robot of grid")

        elif self.boundary_status([self.current_position[0], y - 1]):
            self.current_position[1] -= 1
        else:
            print("Robot of grid")

    def move_vertically(self, direction):
        x = self.current_position[0]
        if direction == "S":
            if self.boundary_status([x + 1, self.current_position[1]]):
                self.current_position[0] += 1
            else:
                print("Robot of grid")
        elif self.boundary_status([x - 1, self.current_position[1]]):
            self.current_position[0] -= 1
        else:
            print("Robot of grid")

    def boundary_status(self, position):
        print(0 <= position[0] <= 9 and 0 <= position[1] <= 9)

    def claw_commands(self, command):
        if command == "D":
            if self.current_position == [0, 0]:
                print("Robot is at the start position")
            elif self.current_position not in Crate.crates.values():
                Crate.update_position(id=self.crate_carried_id, position=self.current_position)
                self.crate_carried_id = 0
                print("Crate dropped")
        elif command == "G":
            if self.crate_carried_id == 0:
                for k, v in Crate.crates.items():
                    if self.current_position == v:
                        self.crate_carried_id = k
                        print("Crate grabbed")

class Crate:
    crates = {}


    def __init__(self, id, position) -> None:
        self.id = id
        self.position = position
        self.crates[self.id] = self.position

    @staticmethod
    def update_position(id, position):
        print('crates postions: ', Crate.crates)
        Crate.crates[id] = position


if __name__ == "__main__":
    crate = Crate(1, [5, 5])
    crate = Crate(2, [5, 6])
    robot = Robot([9,0])

    # commands ='N N N N E E E E E'
    # robot.move_robot(commands)
    
    robot.claw_commands('G')
    robot.move_robot('N E w')
    robot.claw_commands('D')
    print("Final Robot position: ", robot.current_position)



# South-East: [9, 0]
# South-West: [9, 9]
# North-East: [0, 0]
# North-West: [0, 9]
