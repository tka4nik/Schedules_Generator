import constants
from generators import WeeklyScheduleGenerator
from fitness_calculator import WeeklyScheduleFitnessCalculator
from crossover import WeeklyScheduleCrossover
from optimizer import GenericOptimizer
from serializer import Serializer

def main():
    classesQty = constants.classesQty
    lessons = constants.lessons
    population = []
    generator = WeeklyScheduleGenerator(lessons)

    for i in range(constants.totalPopulation):
        population[i] = generator.generate()

    optimizer = GenericOptimizer(
        WeeklyScheduleFitnessCalculator(),
        WeeklyScheduleCrossover(),
        100,
        1
    )
    bestSchedule = optimizer.getBestSchedule(population)
    serializer = Serializer()
    serializer.serialize(bestSchedule)

def testSet():
    m = [1, 2, 3, 3, 3, 3, 4, 5]
    r = set()
    for item in m:
        r.add(item)
    print(r)

if __name__ == '__main__':
    main()