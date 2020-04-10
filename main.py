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
    classesQty = 4  # Количество классов
    lessonsPerDay = 3  # Кол-во уроков в день
    daysPerWeek = 5  # Кол-во учебных дней в неделе
    populations_qty = 100  # Количество популяций

    GeneratorsFactory = generators.GeneratorsFactory  # Фабрика по созданию Генераторов
    CrossoverFactory = crossover.CrossoverFactory  # Фабрика по созданию Скрещивателей
    FitnessFactory = fitness_calculator.FitnessFactory  # Фабрика по созданию Калькуляторов пригодности
    SerializerFactory = serializer.SerializerFactory  # Фабрика по созданию Сериализаторов

    generator_config = generators.WeeklyScheduleGeneratorConfigurationClass(lessons, classesQty, lessonsPerDay,
                                                                            daysPerWeek)
    crossover_config = crossover.WeeklyScheduleCrossoverConfigurationClass(lessonsPerDay)
    serializer_config = serializer.SerializerConfigurationClass(daysPerWeek, lessonsPerDay)
    optimizer_config = optimizer.GenericOptimizerConfigurationClass(
        FitnessFactory.CreateFitnessCalculator(),
        CrossoverFactory.CreateDefaultCrossover(crossover_config),
        populations_qty
    )

    generator = GeneratorsFactory.defaultGenerator(generator_config)

    for i in range(totalPopulation):
        population.append(generator.generate())

    bestSchedule = optimizer.OptimizerFactory.default_optimizer(optimizer_config).getBestSchedule(population)
    serializer.SerializerFactory.CreateSerializer(serializer_config).serialize(bestSchedule)


def testSet():
    m = [1, 2, 3, 3, 3, 3, 4, 5]
    r = set()
    for item in m:
        r.add(item)
    print(r)


if __name__ == '__main__':
    main()
