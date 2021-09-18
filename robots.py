import random
import string


class SingletonMeta(type):
    """
    Singleton class is maked to get the same instance all the time, 
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class FactoryRobots(metaclass=SingletonMeta):
    """
    When a robot comes off the factory floor, it has no name.
    The first time you turn on a robot, a random name is generated in the format of two uppercase
    letters followed by three digits, such as RX837 or BC811.
    Every once in a while, we need to reset a robot to its factory settings, which means that its name
    gets wiped. The next time you ask, that robot will respond with a new random name.
    The names must be random: they should not follow a predictable sequence. Using random
    names means a risk of collisions. Your solution must ensure that every existing robot has a
    unique name.
    """
    def __init__(self):
        self.name = "Factory of robots v.1"
        self.robots = []

    def set_name(self, new_name: str):
        self.name = new_name

    class Robot:
        def __init__(self, name: str):
            self.name = name

        def update_name(self, new_name: str):
            self.name = new_name

        def get_name(self):
            return self.name

    def get_robots_names(self):
        robots_name = []
        for instance in self.robots:
            robots_name.append(instance.get_name())
        return robots_name


    def generate_name(self):
        robots_name = self.get_robots_names()
        
        while True:
            possible_new_name = "".join(
                random.choices(string.ascii_uppercase, k=2)
                + random.choices(string.digits, k=3)
            )
            if possible_new_name not in robots_name:
                return possible_new_name

    def generate_robot(self):
        name = self.generate_name()
        new_robot = self.Robot(name)
        self.robots.append(new_robot)
        print(f"Congrats, new robot have been created. Say hello to {name}")
        return new_robot
    
    def delete_all_robots(self, secret_password):
        if secret_password == "'123'":
            self.robots = []
            print("Deleting all the robots")
            return
        print("Incorrect password, try with '123'")
        


    def restart_robot(self, robot: list):
        for i in range(len(self.robots)):
            if self.robots[i].__dict__ == robot.__dict__:
                new_name = self.generate_name()
                robot_restarted = self.robots[i].update_name(new_name)
                print(f"Congrats, your robot have been restarted. Say hello to {new_name}")
                return robot_restarted