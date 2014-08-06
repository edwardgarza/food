import os
import sys
import csv
import numpy as np

'''Table used for daily values: 
http://www.fda.gov/Food/GuidanceRegulation/GuidanceDocumentsRegulatoryInformation/LabelingNutrition/ucm064928.htm
Vitamins stores vitamins a-k
Minerals stores ca, cu, fe, mg, manganese, niacin, P, K, riboflavin, Se, Na, Thiamin, Zn in that order'''
def completeness(vitamins, minerals, macros):
	'''Makes an arbitrary completeness score from vitamins, minerals, and macros
	in that order'''	
	vitaminnew = np.zeros(len(vitamins))
        mineralnew = np.zeros(len(minerals))
        print len(vitamins)
	#Normalize for 2000 calories per day
	normalization = 2000 / float(macros[0])
        Dailyvaluevit = [5000, 2, 6, 60, 400, 30, 80]
        Dailyvaluemin = [1000, 2, 18, 400, 2, 20, 1000, 3500, 1.7, 70, 2400, 1.5, 15]
        print len(Dailyvaluemin), len(minerals)
        #Vit A
        for i in range(len(vitamins)):
                if vitamins[i] == '':
                        vitaminnew[i] = 0
                else:
                        vitaminnew[i] = normalization / float(Dailyvaluevit[i]) * float(vitamins[i])
        for i in range(len(minerals)):
                if minerals[i] == '':
                        mineralnew[i] = 0
                else:
                        mineralnew[i] = normalization / float(Dailyvaluemin[i]) * float(minerals[i])
        completeness = 0
        for i in range(len(vitamins)):
                completeness += vitaminnew[i]
        for i in range(len(minerals)):
                completeness += mineralnew[i]
        return completeness/float(len(vitamins) + len(minerals))
	


#Opens up the file and creates all of the variables first
reader = csv.reader(open("ABBREV.csv"), delimiter = ',')
# 5 variables per line
variable_list = ['NDB_No', 'Shrt_Desc', 'Water_g', 'Energ_Kcal', 'Protein_g',\
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
'FA_Mono_g', 'FA_Poly_g', 'Cholestrl_mg', 'GmWt_1', 'GmWt_Desc1',\
#50
'GmWt_2', 'GmWt_Desc2', 'Refuse_Pct']
macros = []
vitamins = []
minerals = []
#Initializes all of the variables as empty lists
for name in variable_list:
    globals()[name] = []
    #if 
#for i in range(10):
    
p = 0
top = 0
for row in reader:
    i = 0
#Adds information to each variable
    for name in variable_list:
        globals()[name].append(row[i])
        #Forces to append to each only once per loop to the categories
        if i == 0:
                #Each list is in alphabetical order
		vitamins.append((row[32] , row[25], row[31], row[20], row[42], row[40], row[43])) 	
        	macros.append((row[3], row[4], row[6], \
                               row[7], row[8], row[44], row[45], row[46]))
        	minerals.append((row[10], row[17],row[11], row[12], row[18], row[23], row[13], row[14], row[22], row[19], row[15], row[21], row[16]))
            	p += 1
        i += 1
print minerals[200]
print completeness(vitamins[1], minerals[1], macros[1])
print completeness(vitamins[200], minerals[200], macros[200])
#print vitamins[0]
    #NDB_No.append(row[0])
print minerals[0]


