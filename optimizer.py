"""
Файл по нахождению оптимального расписания
"""

from math import floor
from random import randint

import constants


class GenericOptimizerConfigurationClass:
    def __init__(self, fitness_calculator, crossover, populations_qty=constants.populations_qty,
                 lessonsPerDay=constants.lessonsPerDay):
        self.fitness_calculator = fitness_calculator  # Объект калькулятора пригодности расписания
        self.crossover = crossover  # Объект скрещивателя расписаний
        self.populations_qty = populations_qty  # Количество популяций
        self.lessonsPerDay = lessonsPerDay  # Количество уроков в дне


class GenericOptimizer:
    def __init__(self, config_class):
        self.fitness_calculator = config_class.fitness_calculator
        self.crossover = config_class.crossover
        self.populations_qty = config_class.populations_qty
        self.lessonsPerDay = config_class.lessonsPerDay

    def getBestSchedule(self, population):
        # Ищет наиболее подходящие под условия расписание
        for i in range(self.populations_qty):
            population = self.cross(population, self.createMatingPool(population)[:])
            concat_array = self.concatWeeklySchedules(population)
            concat_map = []
            for item in range(len(concat_array)):
                count = item
                if count:
                    concat_map.append(count + 1)
                else:
                    concat_map.append(1)
            fit = self.fitness_calculator.calculate(population[0])

        max_fitness = -1
        max_fitness_schedule_index = -1
        for i in range(len(population)):
            fit = self.fitness_calculator.calculate(population[i])
            if fit > max_fitness:
                max_fitness = fit
                max_fitness_schedule_index = i
        return population[max_fitness_schedule_index]

    def createMatingPool(self, population):
        matpool = []
        for i in range(len(population)):
            fit = self.fitness_calculator.calculate(population[i]) + 1
            for j in range(fit):
                matpool.append(i)
        return matpool

    def cross(self, population, matpool):
        # Скрещивание
        population2 = []
        for i in range(len(population)):
            a = self.getRandomInt(0, len(matpool) - 1)
            b = self.getRandomInt(0, len(matpool) - 1)
            parentA = population[matpool[a]]
            parentB = population[matpool[b]]
            child = self.crossover.crossover(parentA, parentB)
            population2.append(child)
        return population2

    def getRandomInt(self, min, max):
        return randint(min, max)

    def concatWeeklySchedules(self, population):
        concatMass = []
        for i in range(len(population)):
            dcs = population[i].getDailyClassSchedule(0, 0)
            concatString = ''
            for j in range(self.lessonsPerDay):
                concatString += dcs.scheduledLessons[j].lesson + " "
            concatMass.append(concatString)
        return concatMass


class OptimizerFactory:
    @staticmethod
    def default_optimizer(config_class):
        return GenericOptimizer(config_class)
