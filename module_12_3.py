"""Домашнее задание по теме 'Систематизация и пропуск тестов'"""
import unittest
import module_12_1
import module_12_2
import module_12_4


module_test_suite = unittest.TestSuite()
# Для проверки Часть 1. TestSuit закоментировать строки 13, 14
module_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
module_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))
# Для проверки Часть 2. Пропуск тестов закоментировать строки 10, 11
module_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_4.RunnerTest))
module_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_4.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(module_test_suite)
