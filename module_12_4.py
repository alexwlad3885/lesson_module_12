"""Домашнее задание по теме 'Систематизация и пропуск тестов'"""
import unittest
import module_12_1
import module_12_2


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = module_12_1.Runner('Вася')
        for i in range(1, 11):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = module_12_1.Runner('Дима')
        for i in range(1, 11):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_3 = module_12_1.Runner('Игорь')
        for i in range(1, 11):
            runner_3.run()
        runner_4 = module_12_1.Runner('Алекс')
        for i in range(1, 11):
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = module_12_2.Runner('Усэйн', 10)
        self.runner_2 = module_12_2.Runner('Андрей', 9)
        self.runner_3 = module_12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results.keys():
            print(cls.all_results[key])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first(self):
        result_test = {}
        tournament_1 = module_12_2.Tournament(90, self.runner_1, self.runner_3)
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second(self):
        result_test = {}
        tournament_2 = module_12_2.Tournament(90, self.runner_2, self.runner_3)
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third(self):
        result_test = {}
        tournament_3 = module_12_2.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
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


