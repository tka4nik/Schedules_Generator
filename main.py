"""
Главный файл программы. Здесь программа получает параметры из конфигурационного файла,
создает все необходимые объекты и вызывает нужные функции для работы генератора.
"""
import sys
import optimizer
import serializer
import generators
import crossover
import fitness_calculator
import yaml
import constants


def main():
    try:
        with open('config.yaml', 'r', encoding='utf-8') as config_file:
            config = yaml.safe_load(config_file)
        lessons = config["lessons"]  # Список всех уроков и их количество
        population = []  # Массив популяций
        classesQty = config["classesQty"]  # Количество классов
        lessonsPerDay = config["lessonsPerDay"]  # Кол-во уроков в день
        daysPerWeek = config.get("daysPerWeek", constants.daysPerWeek)  # Кол-во учебных дней в учебной неделе
        populations_qty = config.get("populations_qty", constants.populations_qty)  # Количество популяций
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
    crossover_config = crossover.WeeklyScheduleCrossoverConfigurationClass(lessonsPerDay, daysPerWeek)
    serializer_config = serializer.SerializerConfigurationClass(daysPerWeek, lessonsPerDay)

    fit_calc = FitnessFactory.CreateFitnessCalculator()
    def_crossover = CrossoverFactory.CreateDefaultCrossover(crossover_config)
    optimizer_config = optimizer.GenericOptimizerConfigurationClass(
        fit_calc,
        def_crossover,
        populations_qty,
        lessonsPerDay
    )

    generator = GeneratorsFactory.defaultGenerator(generator_config)

    for i in range(populations_qty):
        population.append(generator.generate())

    bestSchedule = optimizer.OptimizerFactory.default_optimizer(optimizer_config).getBestSchedule(population)
    serializer.SerializerFactory.CreateCsvSerializer(serializer_config).serialize(bestSchedule)


if __name__ == '__main__':
    main()
