from hammer_difference import hammer_difference, get_dictionary_to_compare
from robots import FactoryRobots



class TestHammer:
    """
    Collections of three test.
    - 'asd' comparation to 'as'
    - 'abcd' comparation to 'aecd', please see the code of hammer_difference.py
    - 'abcd' comparation to 'bedaffa', please see the code of hammer_difference.py
    """
    def test_one(self):
        string1 = 'as'
        string2 = 'asd'
        assert hammer_difference(string1, string2) == get_dictionary_to_compare(string1, string2, 0, 1)
    
    def test_two(self):
        string1 = 'abcd'
        string2 = 'aecd'
        assert hammer_difference(string1, string2) == get_dictionary_to_compare(string1, string2, 1)
    
    def test_three(self):
        string1 = 'abcd'
        string2 = 'bedaffa'
        assert hammer_difference(string1, string2) == get_dictionary_to_compare(string1, string2, 4, 7)


class TestRobots:
    """
    Collections of three test.
    - Factory is a Singleton
    - New name is not the same that last
    - Comparing numbers of robots
    """

    def test_one(self):
        factory1 = FactoryRobots()
        factory2 = FactoryRobots()
        factory1.delete_all_robots("'123'")
        assert factory1 == factory2
    
    def test_two(self):
        factory1 = FactoryRobots()
        robot = factory1.generate_robot()
        name_robot = robot.get_name()
        new_name_robot = factory1.restart_robot(robot)
        assert new_name_robot != name_robot
    
    def test_three(self):
        factory2 = FactoryRobots()
        factory2.delete_all_robots("'123'")
        for i in range(10):
            print('.')
            factory2.generate_robot()
        length_of_robots_list = len(factory2.get_robots_names())
        assert 10 == length_of_robots_list
