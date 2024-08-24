"""Домашнее задание по теме 'Логирование'"""
import unittest
import logging

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode="w+",
                    encoding='utf8', format="%(asctime)s | %(levelname)s | %(message)s")


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner_1 = Runner('Вася', -8)
            for i in range(1, 11):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 100)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            runner_2 = Runner({5})
            for i in range(1, 11):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        runner_3 = Runner('Игорь')
        for i in range(1, 11):
            runner_3.run()
        runner_4 = Runner('Алекс')
        for i in range(1, 11):
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)
