import optimizer
import serializer
import generators
import crossover
import fitness_calculator


def main():
    totalPopulation = 100
    lessons = {"�������": 4, "���������": 3, "������": 4, "���������� ����": 1,
               "�����������": 3}  # ������ ���� ������ � �� ����������
    population = []  # ������ ���������
    classesQty = 4  # ���������� �������
    lessonsPerDay = 3  # ���-�� ������ � ����
    daysPerWeek = 5  # ���-�� ������� ���� � ������
    populations_qty = 100  # ���������� ���������

    GeneratorsFactory = generators.GeneratorsFactory  # ������� �� �������� �����������
    CrossoverFactory = crossover.CrossoverFactory  # ������� �� �������� �������������
    FitnessFactory = fitness_calculator.FitnessFactory  # ������� �� �������� ������������� �����������
    SerializerFactory = serializer.SerializerFactory  # ������� �� �������� ��������������

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
