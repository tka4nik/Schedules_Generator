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

    GeneratorsFactory = generators.GeneratorsFactory  # ������� �� �������� �����������
    OptimizerFactory = optimizer.OptimizerFactory  # ������� �� �������� ������������� ����������
    CrossoverFactory = crossover.CrossoverFactory  # ������� �� �������� �������������
    FitnessFactory = fitness_calculator.FitnessFactory  # ������� �� �������� ������������� �����������
    SerializerFactory = serializer.SerializerFactory  # ������� �� �������� ��������������

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
