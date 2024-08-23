"""Домашнее задание по теме 'Методы Юнит-тестирования'"""
import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results.keys():
            print(cls.all_results[key])

    def test_first(self):
        result_test = {}
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        tn = list(tournament_1.start().items())
        tn_max = max(tn)[0]
        tn_str_name_1 = self.runner_1.__dict__['name']
        tn_str_name_2 = self.runner_3.__dict__['name']
        for i in tn:
            kei = i[0]
            vol = i[1]
            if tn_str_name_1 == vol:
                result_test[kei] = tn_str_name_1
            else:
                result_test[kei] = tn_str_name_2
        self.all_results[1] = result_test
        self.assertTrue(result_test[tn_max] == 'Ник')

    def test_second(self):
        result_test = {}
        tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        tn = list(tournament_2.start().items())
        tn_max = max(tn)[0]
        tn_str_name_1 = self.runner_2.__dict__['name']
        tn_str_name_2 = self.runner_3.__dict__['name']
        for i in tn:
            kei = i[0]
            vol = i[1]
            if tn_str_name_1 == vol:
                result_test[kei] = tn_str_name_1
            else:
                result_test[kei] = tn_str_name_2
        self.all_results[2] = result_test
        self.assertTrue(result_test[tn_max] == 'Ник')

    def test_third(self):
        result_test = {}
        tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        tn = list(tournament_3.start().items())
        tn_max = max(tn)[0]
        tn_str_name_1 = self.runner_1.__dict__['name']
        tn_str_name_2 = self.runner_2.__dict__['name']
        tn_str_name_3 = self.runner_3.__dict__['name']
        for i in tn:
            kei = i[0]
            vol = i[1]
            if tn_str_name_1 == vol:
                result_test[kei] = tn_str_name_1
            elif tn_str_name_2 == vol:
                result_test[kei] = tn_str_name_2
            else:
                result_test[kei] = tn_str_name_3
        self.all_results[3] = result_test
        self.assertTrue(result_test[tn_max] == 'Ник')


if __name__ == "__main__":
    unittest.main()
