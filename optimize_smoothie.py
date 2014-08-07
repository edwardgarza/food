import csv
import os
import numpy as np

def read_daily_values():
	daily_values = {}

	f = open('dv.txt', 'rb')

	count = 0
	val = ''
	for obj in f:
		if count%2 == 0:
			val = obj.replace('\n', '').strip()
		else:
			(num, unit) = obj.split(' ')
			unit = unit.replace('\n', '')
			daily_values[val] = [float(num), unit]
		count += 1

	return daily_values

#def optimize(header, daily_values):


reader = csv.reader(open('ABBREV.csv', 'rb'), delimiter=',')
reader.next()

# 'NDB_No', 'Shrt_Desc', 

header = ['Water_g', 'Energ_Kcal', 'Protein_g',\
'Lipid_Tot_g', 'Ash_g', 'Carbohydrt_g', 'Fiber_TD_g', 'Sugar_Tot_g',\
#10
'Calcium_mg', 'Iron_mg', 'Magnesium_mg', 'Phosphorus_mg', 'Potassium_mg',\
'Sodium_mg', 'Zinc_mg', 'Copper_mg', 'Manganese_mg', 'Selenium_ug',\
#20
'Vit_C_mg', 'Thiamin_mg', 'Riboflavin_mg', 'Niacin_mg', 'Panto_Acid_mg',\
'Vit_B6_mg', 'Folate_Tot_ug', 'Folic_Acid_ug', 'Food_Folate_ug', 'Folate_DFE_ug',\
#30
'Choline_Tot_mg', 'Vit_B12_ug', 'Vit_A_IU', 'Vit_A_RAE_ug_', 'Retinol_ug',\
'Alpha_Carot_ug', 'Beta_Carot_ug', 'Beta_Crypt_ug', 'Lycopene_ug', 'Lut+Zea_ug',\
#40
'Vit_E_mg', 'Vit_D_ug', 'Vit_D_IU', 'Vit_K_ug', 'FA_Sat_g', \
'FA_Mono_g', 'FA_Poly_g', 'Cholestrl_mg']

ingredients = []
portions_and_refuse = []
values = []

for row in reader:
	ingredients.append(row[1])
	portions_and_refuse = row[-5:]

	vals = []
	for val in row[2:-4]:
		if len(val) == 0:
			vals.append(0.0)
		else:
			vals.append(float(val))

	values.append(vals)

values = np.array(values, dtype=float)
print ingredients, values


daily_values = read_daily_values()