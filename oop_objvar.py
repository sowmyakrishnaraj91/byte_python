class Robot:
    """ Represents a robot with a name."""
    population = 0
    def __init__(self,name):
        self.name = name
        print('Initialising {}'.format(self.name))

        Robot.population += 1

    def die(self):
        """ Robots dying."""
        print('{} is being destroyed'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last'.format(self.name))
        else:
            print('Remaining {:d} robots'.format(Robot.population))


    def say_hi(self):
        """ Welcome.

        Just checking"""
        print('Hi, My name is {}'.format(self.name))

    @classmethod

    def how_many(cls):
        """ Current population."""
        print('we have {:d} robots'.format(cls.population))

droid1 = Robot("robot1")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("robot2")
droid2.say_hi()
Robot.how_many()

droid1.die()
droid2.die()

Robot.how_many()

#droid1.how_many()