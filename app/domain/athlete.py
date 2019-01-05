
import os


class Athlete:
    counter = -1  # is used to generate a unique id for athlete

    def __init__(self, id_num, first_name, last_name):
        self.id = id_num
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def default_constructor(cls, first_name, last_name):
        """Constructor for building athlete object without explicitly defining id"""
        Athlete.counter = Athlete.get_counter()
        Athlete.counter += 1
        Athlete.set_counter()
        return cls(Athlete.counter, first_name, last_name)

    @classmethod
    def get_counter(cls):
        """Function to get the last used counter value from the file"""
        cwd = os.getcwd()
        file_dir = os.path.join(cwd, "data", "counter.dat")
        exists = os.path.isfile(file_dir)
        if exists:
            with open(file_dir, "r") as f:
                return int(f.read())
        else:
            with open(file_dir, "w") as f:
                f.write(str(cls.counter))
            return 0

    @classmethod
    def set_counter(cls):
        """Function to write the last value of the counter to the file"""
        cwd = os.getcwd()
        file_dir = os.path.join(cwd, "data", "counter.dat")
        with open(file_dir, "w") as f:
            f.write(str(cls.counter))
