import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

soil = ctrl.Antecedent(np.arange(0, 100, 1), 'soil')
mass = ctrl.Antecedent(np.arange(0, 20, 1), 'mass')
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

rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v1'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v1'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v1'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v1'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v1'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v1'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v1'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v1'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v1'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['limpo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v1'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v2'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v3'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v1'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v1'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v3'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v4'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v5'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v1'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v2'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v3'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v4'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v1'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v3'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v4'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v5'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v2'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v3'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v4'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v1'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['pouco sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v3'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v4'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v5'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v3'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v4'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v5'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v1'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v2'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v3'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v3'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v4'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v5'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v2'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v3'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v4'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v5'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v1'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v2'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v3'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v3'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v4'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v5'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v3'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v4'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v5'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v3'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v4'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['medio sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v3'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v4'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['rapido'] & frequencia['v5'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v3'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v4'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['normal'] & frequencia['v5'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v1'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v2'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v3'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v4'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['leve'] & tempoLavagem['devagar'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v3'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v4'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['rapido'] & frequencia['v5'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v3'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v4'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['normal'] & frequencia['v5'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v2'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v3'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v4'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['medio'] & tempoLavagem['devagar'] & frequencia['v5'], qualidadeLavagem['otima']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v3'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v4'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['rapido'] & frequencia['v5'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v3'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v4'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['normal'] & frequencia['v5'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v1'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v2'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v3'], qualidadeLavagem['ruim']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v4'], qualidadeLavagem['medio']))
rules.append(ctrl.Rule(soil['muito sujo'] & mass['pesado'] & tempoLavagem['devagar'] & frequencia['v5'], qualidadeLavagem['medio']))



navigation_ctrl = ctrl.ControlSystem(rules)
fis = ctrl.ControlSystemSimulation(navigation_ctrl)

testeSoil = 43
testeMass = 14
testeTempoLavagem = 67
testeFrequencia = 800

fis.input['soil'] = testeSoil
fis.input['mass'] = testeMass
fis.input['tempo lavagem(min)'] = testeTempoLavagem
fis.input['frequencia(rpm)'] = testeFrequencia
fis.compute()

print(fis.output['qualidade lavagem'])