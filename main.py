import optimizer
import serializer
import generators
import crossover
import fitness_calculator


def main():
    totalPopulation = 100
    lessons = {"Алгебра": 4, "Геометрия": 3, "Физика": 4, "Английский язык": 1,
               "Информатика": 3}  # Список всех уроков и их количество
    population = []  # Массив популяций

    GeneratorsFactory = generators.GeneratorsFactory  # Фабрика по созданию Генераторов
    OptimizerFactory = optimizer.OptimizerFactory  # Фабрика по созданию Оптимизаторов расписания
    CrossoverFactory = crossover.CrossoverFactory  # Фабрика по созданию Скрещивателей
    FitnessFactory = fitness_calculator.FitnessFactory  # Фабрика по созданию Калькуляторов пригодности
    SerializerFactory = serializer.SerializerFactory  # Фабрика по созданию Сериализаторов

    generator_config = generators.WeeklyScheduleGeneratorConfigurationClass(lessons)
    crossover_config = crossover.WeeklyScheduleCrossoverConfigurationClass()
    serializer_config = serializer.SerializerConfigurationClass()
    optimizer_config = optimizer.GenericOptimizerConfigurationClass(
        FitnessFactory.CreateFitnessCalculator(),
        CrossoverFactory.CreateDefaultCrossover(crossover_config)
    )

    generator = GeneratorsFactory.defaultGenerator(generator_config)
    optimizer = OptimizerFactory.default_optimizer(optimizer_config)

    for i in range(totalPopulation):
        population.append(generator.generate())

    bestSchedule = optimizer.getBestSchedule(population)
    serializer = SerializerFactory.CreateSerializer(serializer_config)
    serializer.serialize(bestSchedule)


def testSet():
    m = [1, 2, 3, 3, 3, 3, 4, 5]
    r = set()
    for item in m:
        r.add(item)
    print(r)


if __name__ == '__main__':
    main()
