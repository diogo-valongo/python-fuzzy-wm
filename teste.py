import itertools
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

soil_options = ['limpo', 'pouco sujo', 'medio sujo', 'muito sujo']
mass_options = ['leve', 'medio', 'pesado']
tempoLavagem_options = ['rapido', 'normal', 'devagar']
frequencia_options = ['v1', 'v2', 'v3', 'v4', 'v5']

soil = ctrl.Antecedent(np.arange(0, 100, 1), 'soil')
mass = ctrl.Antecedent(np.arange(0, 20, 1), 'soil')
tempoLavagem = ctrl.Antecedent(np.arange(20, 130, 1), 'tempo lavagem(min)')
#temperatura = ctrl.Antecedent(np.arange(30, 60, 1), 'temperatura(c)')
frequencia = ctrl.Antecedent(np.arange(400, 1200, 100), 'frequencia(rpm)')

qualidadeLavagem = ctrl.Consequent(np.arange(0, 100, 1), 'qualidade lavagem')


soil['limpo'] = fuzz.trimf(soil.universe, [0, 0, 25])
soil['pouco sujo'] = fuzz.trimf(soil.universe, [10, 35, 40])
soil['medio sujo'] = fuzz.trimf(soil.universe, [30, 60, 70])
soil['muito sujo'] = fuzz.trimf(soil.universe, [50, 100, 100])

mass['leve'] = fuzz.trimf(mass.universe, [0, 0, 5])
mass['medio'] = fuzz.trimf(mass.universe, [3, 7, 12])
mass['pesado'] = fuzz.trimf(mass.universe, [10, 20, 20])

tempoLavagem['rapido'] = fuzz.trimf(tempoLavagem.universe, [20, 20, 45])
tempoLavagem['normal'] = fuzz.trimf(tempoLavagem.universe, [40, 70, 80])
tempoLavagem['devagar'] = fuzz.trimf(tempoLavagem.universe, [60, 130, 130])

frequencia['v1'] = fuzz.trimf(frequencia.universe, [400, 400, 410])
frequencia['v2'] = fuzz.trimf(frequencia.universe, [590, 600, 610])
frequencia['v3'] = fuzz.trimf(frequencia.universe, [790, 800, 810])
frequencia['v4'] = fuzz.trimf(frequencia.universe, [990, 1000, 1010])
frequencia['v5'] = fuzz.trimf(frequencia.universe, [1190, 1200, 1200])

qualidadeLavagem['ruim'] = fuzz.trimf(qualidadeLavagem.universe, [0, 0, 35])
qualidadeLavagem['medio'] = fuzz.trimf(qualidadeLavagem.universe, [30, 50, 60])
qualidadeLavagem['otima'] = fuzz.trimf(qualidadeLavagem.universe, [50, 100, 100])


rules = []
c = 0
for combination in itertools.product(soil_options, mass_options, tempoLavagem_options, frequencia_options):
    c += 1
    rule_str = f"rules.append(ctrl.Rule(soil['{combination[0]}'] & mass['{combination[1]}'] & tempoLavagem['{combination[2]}'] & frequencia['{combination[3]}'], qualidadeLavagem['ruim']))"
    print(rule_str)


soil = ctrl.Antecedent(np.arange(0, 100, 1), 'soil')
mass = ctrl.Antecedent(np.arange(0, 20, 1), 'mass')
tempoLavagem = ctrl.Antecedent(np.arange(20, 130, 1), 'tempo lavagem(min)')
#temperatura = ctrl.Antecedent(np.arange(30, 60, 1), 'temperatura(c)')
frequencia = ctrl.Antecedent(np.arange(400, 1200, 100), 'frequencia(rpm)')

qualidadeLavagem = ctrl.Consequent(np.arange(0, 100, 1), 'qualidade lavagem')