import sys
import optimizer
import serializer
import generators
import crossover
import fitness_calculator
import yaml


def main():
    try:
        with open('config.yaml', 'r', encoding='utf-8') as config_file:
            config = yaml.safe_load(config_file)
        lessons = config["lessons"]  # Список всех уроков и их количество
        population = []  # Массив популяций
        classesQty = config["classesQty"]  # Количество классов
        lessonsPerDay = config["lessonsPerDay"]  # Кол-во уроков в день
        daysPerWeek = config.get("daysPerWeek", 5)  # Кол-во учебных дней в учебной неделе
        populations_qty = config.get("populations_qty", 100)  # Количество популяций
    except FileNotFoundError:
        print("Не найден файл 'config.yaml'.")
        sys.exit(1)
    except KeyError as key:
        print("Не указан ключевой параеметр {}.".format(key))
        sys.exit(1)

    GeneratorsFactory = generators.GeneratorsFactory  # Фабрика по созданию Генераторов
    CrossoverFactory = crossover.CrossoverFactory  # Фабрика по созданию Скрещивателей
    FitnessFactory = fitness_calculator.FitnessFactory  # Фабрика по созданию Калькуляторов пригодности

    generator_config = generators.WeeklyScheduleGeneratorConfigurationClass(lessons, classesQty, lessonsPerDay,
                                                                            daysPerWeek)
    crossover_config = crossover.WeeklyScheduleCrossoverConfigurationClass(lessonsPerDay)
    serializer_config = serializer.SerializerConfigurationClass(daysPerWeek, lessonsPerDay)

    fit_calc = FitnessFactory.CreateFitnessCalculator()
    def_crossover = CrossoverFactory.CreateDefaultCrossover(crossover_config)
    optimizer_config = optimizer.GenericOptimizerConfigurationClass(
        fit_calc,
        def_crossover,
        populations_qty
    )

    generator = GeneratorsFactory.defaultGenerator(generator_config)

    for i in range(populations_qty):
        population.append(generator.generate())

    bestSchedule = optimizer.OptimizerFactory.default_optimizer(optimizer_config).getBestSchedule(population)
    serializer.SerializerFactory.CreareCsvSerializer(serializer_config).serialize(bestSchedule)


def testSet():
    m = [1, 2, 3, 3, 3, 3, 4, 5]
    r = set()
    for item in m:
        r.add(item)
    print(r)


def testYaml():
    with open('config.yaml') as input_file:
        var = yaml.safe_load(input_file)
    print(var)

    for item in var["lessons"]:
        print(var["lessons"][item])

    lessons = var["lessons"]
    print(lessons)

    lessons2 = {"Алгебра": 4, "Геометрия": 3, "Физика": 4, "Английский язык": 1,
                "Информатика": 3}
    print(lessons2)


if __name__ == '__main__':
    main()
