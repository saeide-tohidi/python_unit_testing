class Profile:
    def __init__(self, name, age, job):
        self._name = name
        self._age = age
        self._job = job

    def print_name(self):
        print(self._name)

    def print_job(self):
        print(self._job)

    def print_age(self):
        print(self._age)
