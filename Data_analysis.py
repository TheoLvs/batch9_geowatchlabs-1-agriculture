###########################################################################
# Ce que fait ce programme
# Analyse des données
###########################################################################
# Librairies

import os
os.chdir(r'C:\Users\lebce\OneDrive\Documents\DataForGood')
print(os.getcwd())

import Import_fichiers_sav as fs
import Import_fichiers_tiff as ti

import pandas as pd
import numpy as np

import seaborn as sns

from matplotlib import pyplot
import matplotlib.pyplot as plt
    
###########################################################################
# Chargement de la base
df_analyse_rend=ti.df_analyse.copy()

#df_analyse_rend=df_analyse.loc[df_analyse["HY_Rend_tot"]>0]
#df_moughataa_rend=df_moughataa.loc[df_moughataa["HY_Rend_tot"]>0]

#df_analyse_rend.to_csv('C:/0 - Data/df_analyse_rend.csv', sep = ';')
#df_moughataa_rend.to_csv('C:/0 - Data/df_moughataa_rend.csv', sep = ';')


# Creation de variables : Avec Sans rendement
df_analyse_rend['Rend_Pos']=0
df_analyse_rend.loc[df_analyse_rend.loc[:,'HY_Rend_tot']>0,'Rend_Pos']= 1 

# Creation de variables : Tranches de scores
df_analyse_rend['Cat_Score']=df_analyse_rend.loc[:,'FCS']/10
df_analyse_rend['Cat_Score']=df_analyse_rend['Cat_Score'].astype(int)

df_analyse_rend['YEAR_INT']=df_analyse_rend['YEAR'].astype(int)

sns.distplot(df_analyse_rend['Cat_Score'])
sns.displot(df_analyse_rend, x="Cat_Score", col="YEAR", facet_kws=dict(margin_titles=True),)

sns.distplot(df_analyse_rend['FCS'])
sns.displot(df_analyse_rend, x="FCS", col="YEAR", facet_kws=dict(margin_titles=True),)

plt.figure(figsize=(10,10))
sns.boxplot(y=df_analyse_rend['FCS'], x=df_analyse_rend['YEAR'])
plt.show()

temp = pd.crosstab([df_analyse_rend["YEAR"]],df_analyse_rend["FCS_BIN"], margins=True)
temp = pd.crosstab([df_analyse_rend["Q4_3"]],df_analyse_rend["FCS_BIN"], margins=True)
temp = pd.crosstab([df_analyse_rend["Q4_3"]],df_analyse_rend["POS_BOVIN"], margins=True)
temp = pd.crosstab([df_analyse_rend["Q7_5"]],df_analyse_rend["FCS_BIN"], margins=True)
temp = pd.crosstab([df_analyse_rend["Q2_1"]],df_analyse_rend["FCS_BIN"], margins=True)
temp = pd.crosstab([df_analyse_rend["Q2_2"]],df_analyse_rend["FCS_BIN"], margins=True)
temp = pd.crosstab([df_analyse_rend["Q2_3"]],df_analyse_rend["FCS_BIN"], margins=True)
temp = pd.crosstab([df_analyse_rend["Q4_5_1"]],df_analyse_rend["FCS_BIN"], margins=True)

###########################################################################
# Quantification et elimination des NA

temp = pd.DataFrame(df_analyse_rend.isnull().sum(),columns=['Nb']).sort_values('Nb', ascending = False)
temp =  100*df_analyse_rend.isnull().sum()/len(df_analyse_rend)

# Suppression des variables incompletes ou sans signifiation
df_analyse_rend=df_analyse_rend.drop(['MIGRATION','IDENT','STRATE','STRATE1','NOMVILLAGE','STRATES',
                                      'ALTITUDE','ACCURACY','DEPNALIM','FCG_RECODED','COPING_STRATEGY','LHZ',
                                      'PONDERATION','QUEST','NUMQUEST','FCG_28_42','EXTRAPOLATION','MONTH',
                                      'CODEVILLAGE','MIGRATION','IDENT','CODEVILLAGE','TAILMENOLD','STRATES',
                                      'NOMVILLAGE','MOUGHATAA_GEOMATCH','Q2_NOM_CHEF'], axis=1)

# Suppression des variables liées au score IA
df_analyse_rend=df_analyse_rend.drop(["ADBASE","LEGUMINEUSE","FRUITS","LEGUMES","VIANDE_POISSON","LAIT",
                                      "HUILE","SUCRE"], axis=1)

# Remplacement des NA par moyenne
df_analyse_rend.Q2_1[df_analyse_rend.Q2_1.isna()] = df_analyse_rend["Q2_1"].mean()

# Remplacement des NA par -1
df_analyse_rend['Q2_11'].loc[df_analyse_rend['Q2_11'].isnull()]=-1
df_analyse_rend['Q2_83'].loc[df_analyse_rend['Q2_83'].isnull()]=-1
df_analyse_rend['Q2_82'].loc[df_analyse_rend['Q2_82'].isnull()]=-1
df_analyse_rend['Q2_8$2'].loc[df_analyse_rend['Q2_8$2'].isnull()]=-1
df_analyse_rend['S_FRUIT'].loc[df_analyse_rend['S_FRUIT'].isnull()]=-1
df_analyse_rend['Q7_0B3'].loc[df_analyse_rend['Q7_0B3'].isnull()]=-1
df_analyse_rend['Q2_81'].loc[df_analyse_rend['Q2_81'].isnull()]=-1
df_analyse_rend['Q7_23'].loc[df_analyse_rend['Q7_23'].isnull()]=-1
df_analyse_rend['Q2_8$1'].loc[df_analyse_rend['Q2_8$1'].isnull()]=-1
df_analyse_rend['S_ADBASE2'].loc[df_analyse_rend['S_ADBASE2'].isnull()]=-1
df_analyse_rend['PC_VENTLAIT'].loc[df_analyse_rend['PC_VENTLAIT'].isnull()]=-1
df_analyse_rend['Q6_3_A'].loc[df_analyse_rend['Q6_3_A'].isnull()]=-1
df_analyse_rend['Q7_0C'].loc[df_analyse_rend['Q7_0C'].isnull()]=-1
df_analyse_rend['Q11_2A'].loc[df_analyse_rend['Q11_2A'].isnull()]=-1
df_analyse_rend['Q7_0B2'].loc[df_analyse_rend['Q7_0B2'].isnull()]=-1
df_analyse_rend['Q2_7A'].loc[df_analyse_rend['Q2_7A'].isnull()]=-1
df_analyse_rend['Q2_7B'].loc[df_analyse_rend['Q2_7B'].isnull()]=-1
df_analyse_rend['Q2_8'].loc[df_analyse_rend['Q2_8'].isnull()]=-1
df_analyse_rend['Q2_9'].loc[df_analyse_rend['Q2_9'].isnull()]=-1
df_analyse_rend['Q2_10'].loc[df_analyse_rend['Q2_10'].isnull()]=-1
df_analyse_rend['S_LAITIERS'].loc[df_analyse_rend['S_LAITIERS'].isnull()]=-1
df_analyse_rend['D_FRUIT'].loc[df_analyse_rend['D_FRUIT'].isnull()]=-1
df_analyse_rend['S_SMALLAI'].loc[df_analyse_rend['S_SMALLAI'].isnull()]=-1
df_analyse_rend['S_VIAND_POISS'].loc[df_analyse_rend['S_VIAND_POISS'].isnull()]=-1
df_analyse_rend['S_PROTEISMALL'].loc[df_analyse_rend['S_PROTEISMALL'].isnull()]=-1
df_analyse_rend['D_ADBASE2'].loc[df_analyse_rend['D_ADBASE2'].isnull()]=-1
df_analyse_rend['Q7_22'].loc[df_analyse_rend['Q7_22'].isnull()]=-1
df_analyse_rend['Q2_9_1564'].loc[df_analyse_rend['Q2_9_1564'].isnull()]=-1
df_analyse_rend['Q9_9_8'].loc[df_analyse_rend['Q9_9_8'].isnull()]=-1
df_analyse_rend['Q9_9_9'].loc[df_analyse_rend['Q9_9_9'].isnull()]=-1
df_analyse_rend['Q10_25'].loc[df_analyse_rend['Q10_25'].isnull()]=-1
df_analyse_rend['Q11_1_8$3'].loc[df_analyse_rend['Q11_1_8$3'].isnull()]=-1
df_analyse_rend['Q11_1_8$4'].loc[df_analyse_rend['Q11_1_8$4'].isnull()]=-1
df_analyse_rend['Q11_9_16$2'].loc[df_analyse_rend['Q11_9_16$2'].isnull()]=-1
df_analyse_rend['Q11_9_16$7'].loc[df_analyse_rend['Q11_9_16$7'].isnull()]=-1
df_analyse_rend['Q11_9_16$8'].loc[df_analyse_rend['Q11_9_16$8'].isnull()]=-1
df_analyse_rend['Q2_7_1564'].loc[df_analyse_rend['Q2_7_1564'].isnull()]=-1
df_analyse_rend['Q9_8_A'].loc[df_analyse_rend['Q9_8_A'].isnull()]=-1
df_analyse_rend['Q9_9_7'].loc[df_analyse_rend['Q9_9_7'].isnull()]=-1
df_analyse_rend['Q9_9_5'].loc[df_analyse_rend['Q9_9_5'].isnull()]=-1
df_analyse_rend['Q9_9_6'].loc[df_analyse_rend['Q9_9_6'].isnull()]=-1
df_analyse_rend['Q9_9_4'].loc[df_analyse_rend['Q9_9_4'].isnull()]=-1
df_analyse_rend['Q9_9_3'].loc[df_analyse_rend['Q9_9_3'].isnull()]=-1
df_analyse_rend['Q9_9_2'].loc[df_analyse_rend['Q9_9_2'].isnull()]=-1
df_analyse_rend['Q9_8_B'].loc[df_analyse_rend['Q9_8_B'].isnull()]=-1
df_analyse_rend['D_LAITIERS'].loc[df_analyse_rend['D_LAITIERS'].isnull()]=-1
df_analyse_rend['Q9_17'].loc[df_analyse_rend['Q9_17'].isnull()]=-1
df_analyse_rend['S_LEGUMES'].loc[df_analyse_rend['S_LEGUMES'].isnull()]=-1
df_analyse_rend['Q5_0B'].loc[df_analyse_rend['Q5_0B'].isnull()]=-1
df_analyse_rend['D_PROTEISMALL'].loc[df_analyse_rend['D_PROTEISMALL'].isnull()]=-1
df_analyse_rend['D_VIAND_POISS'].loc[df_analyse_rend['D_VIAND_POISS'].isnull()]=-1
df_analyse_rend['D_SMALLAI'].loc[df_analyse_rend['D_SMALLAI'].isnull()]=-1
df_analyse_rend['Q7_21'].loc[df_analyse_rend['Q7_21'].isnull()]=-1
df_analyse_rend['Q7_0B1'].loc[df_analyse_rend['Q7_0B1'].isnull()]=-1
df_analyse_rend['D_LEGUMES'].loc[df_analyse_rend['D_LEGUMES'].isnull()]=-1
df_analyse_rend['S_PULSES'].loc[df_analyse_rend['S_PULSES'].isnull()]=-1
df_analyse_rend['Q7_92'].loc[df_analyse_rend['Q7_92'].isnull()]=-1
df_analyse_rend['Q7_99'].loc[df_analyse_rend['Q7_99'].isnull()]=-1
df_analyse_rend['Q7_98'].loc[df_analyse_rend['Q7_98'].isnull()]=-1
df_analyse_rend['Q7_97'].loc[df_analyse_rend['Q7_97'].isnull()]=-1
df_analyse_rend['Q7_95'].loc[df_analyse_rend['Q7_95'].isnull()]=-1
df_analyse_rend['Q7_94'].loc[df_analyse_rend['Q7_94'].isnull()]=-1
df_analyse_rend['Q7_93'].loc[df_analyse_rend['Q7_93'].isnull()]=-1
df_analyse_rend['Q7_80'].loc[df_analyse_rend['Q7_80'].isnull()]=-1
df_analyse_rend['Q7_81'].loc[df_analyse_rend['Q7_81'].isnull()]=-1
df_analyse_rend['Q7_90'].loc[df_analyse_rend['Q7_90'].isnull()]=-1
df_analyse_rend['Q7_89'].loc[df_analyse_rend['Q7_89'].isnull()]=-1
df_analyse_rend['Q7_88'].loc[df_analyse_rend['Q7_88'].isnull()]=-1
df_analyse_rend['Q7_87'].loc[df_analyse_rend['Q7_87'].isnull()]=-1
df_analyse_rend['Q7_86'].loc[df_analyse_rend['Q7_86'].isnull()]=-1
df_analyse_rend['Q7_85'].loc[df_analyse_rend['Q7_85'].isnull()]=-1
df_analyse_rend['Q7_84'].loc[df_analyse_rend['Q7_84'].isnull()]=-1
df_analyse_rend['Q7_83'].loc[df_analyse_rend['Q7_83'].isnull()]=-1
df_analyse_rend['Q7_82'].loc[df_analyse_rend['Q7_82'].isnull()]=-1
df_analyse_rend['Q7_91'].loc[df_analyse_rend['Q7_91'].isnull()]=-1
df_analyse_rend['Q7_96'].loc[df_analyse_rend['Q7_96'].isnull()]=-1
df_analyse_rend['Q2_NBPERS_M_18A'].loc[df_analyse_rend['Q2_NBPERS_M_18A'].isnull()]=-1
df_analyse_rend['Q2_NBPERS_F_64A'].loc[df_analyse_rend['Q2_NBPERS_F_64A'].isnull()]=-1
df_analyse_rend['Q2_NBPERS_M_64A'].loc[df_analyse_rend['Q2_NBPERS_M_64A'].isnull()]=-1
df_analyse_rend['Q2_NBPERS_F_18A'].loc[df_analyse_rend['Q2_NBPERS_F_18A'].isnull()]=-1
df_analyse_rend['D_PULSES'].loc[df_analyse_rend['D_PULSES'].isnull()]=-1
df_analyse_rend['S_SUCRE'].loc[df_analyse_rend['S_SUCRE'].isnull()]=-1
df_analyse_rend['D_OTHER'].loc[df_analyse_rend['D_OTHER'].isnull()]=-1
df_analyse_rend['S_HUILE'].loc[df_analyse_rend['S_HUILE'].isnull()]=-1
df_analyse_rend['S_OTHER'].loc[df_analyse_rend['S_OTHER'].isnull()]=-1
df_analyse_rend['D_ADBASE1'].loc[df_analyse_rend['D_ADBASE1'].isnull()]=-1
df_analyse_rend['D_HUILE'].loc[df_analyse_rend['D_HUILE'].isnull()]=-1
df_analyse_rend['SMALLAI'].loc[df_analyse_rend['SMALLAI'].isnull()]=-1
df_analyse_rend['D_SUCRE'].loc[df_analyse_rend['D_SUCRE'].isnull()]=-1
df_analyse_rend['Q5_0A'].loc[df_analyse_rend['Q5_0A'].isnull()]=-1
df_analyse_rend['Q9_15'].loc[df_analyse_rend['Q9_15'].isnull()]=-1
df_analyse_rend['Q2_NBPERS_F_2A'].loc[df_analyse_rend['Q2_NBPERS_F_2A'].isnull()]=-1
df_analyse_rend['Q2_NBPERS_F_59A'].loc[df_analyse_rend['Q2_NBPERS_F_59A'].isnull()]=-1
df_analyse_rend['Q10_9'].loc[df_analyse_rend['Q10_9'].isnull()]=-1
df_analyse_rend['Q10_8'].loc[df_analyse_rend['Q10_8'].isnull()]=-1
df_analyse_rend['Q9_16'].loc[df_analyse_rend['Q9_16'].isnull()]=-1
df_analyse_rend['Q7_8'].loc[df_analyse_rend['Q7_8'].isnull()]=-1
df_analyse_rend['Q7_7'].loc[df_analyse_rend['Q7_7'].isnull()]=-1
df_analyse_rend['Q6_0A'].loc[df_analyse_rend['Q6_0A'].isnull()]=-1
df_analyse_rend['Q7_0B'].loc[df_analyse_rend['Q7_0B'].isnull()]=-1
df_analyse_rend['Q7_0A'].loc[df_analyse_rend['Q7_0A'].isnull()]=-1
df_analyse_rend['Q6_0B'].loc[df_analyse_rend['Q6_0B'].isnull()]=-1
df_analyse_rend['TOTADULTE'].loc[df_analyse_rend['TOTADULTE'].isnull()]=-1
df_analyse_rend['TOTMOINS5'].loc[df_analyse_rend['TOTMOINS5'].isnull()]=-1
df_analyse_rend['Q9_14'].loc[df_analyse_rend['Q9_14'].isnull()]=-1
df_analyse_rend['Q2_NBPERS_F_6M'].loc[df_analyse_rend['Q2_NBPERS_F_6M'].isnull()]=-1
df_analyse_rend['ADBASE2'].loc[df_analyse_rend['ADBASE2'].isnull()]=-1
df_analyse_rend['Q9_13'].loc[df_analyse_rend['Q9_13'].isnull()]=-1
df_analyse_rend['Q9_12'].loc[df_analyse_rend['Q9_12'].isnull()]=-1
df_analyse_rend['S_ADBASE1'].loc[df_analyse_rend['S_ADBASE1'].isnull()]=-1
df_analyse_rend['PULSES'].loc[df_analyse_rend['PULSES'].isnull()]=-1
df_analyse_rend['ADBASE1'].loc[df_analyse_rend['ADBASE1'].isnull()]=-1
df_analyse_rend['Q7_16'].loc[df_analyse_rend['Q7_16'].isnull()]=-1
df_analyse_rend['Q7_15'].loc[df_analyse_rend['Q7_15'].isnull()]=-1
df_analyse_rend['Q7_14'].loc[df_analyse_rend['Q7_14'].isnull()]=-1
df_analyse_rend['Q10_11'].loc[df_analyse_rend['Q10_11'].isnull()]=-1
df_analyse_rend['PROTEISMALL'].loc[df_analyse_rend['PROTEISMALL'].isnull()]=-1
df_analyse_rend['Q7_13'].loc[df_analyse_rend['Q7_13'].isnull()]=-1
df_analyse_rend['Q7_12'].loc[df_analyse_rend['Q7_12'].isnull()]=-1
df_analyse_rend['VIAND_POISS'].loc[df_analyse_rend['VIAND_POISS'].isnull()]=-1
df_analyse_rend['Q7_11'].loc[df_analyse_rend['Q7_11'].isnull()]=-1
df_analyse_rend['Q2_0A'].loc[df_analyse_rend['Q2_0A'].isnull()]=-1
df_analyse_rend['Q2_0C'].loc[df_analyse_rend['Q2_0C'].isnull()]=-1
df_analyse_rend['LAITIERS'].loc[df_analyse_rend['LAITIERS'].isnull()]=-1
df_analyse_rend['Q2_NBPERS_M_6M'].loc[df_analyse_rend['Q2_NBPERS_M_6M'].isnull()]=-1
df_analyse_rend['Q2_NBPERS_M_2A'].loc[df_analyse_rend['Q2_NBPERS_M_2A'].isnull()]=-1
df_analyse_rend['Q2_NBPERS_M_59A'].loc[df_analyse_rend['Q2_NBPERS_M_59A'].isnull()]=-1
df_analyse_rend['OTHER'].loc[df_analyse_rend['OTHER'].isnull()]=-1
df_analyse_rend['Q9_11'].loc[df_analyse_rend['Q9_11'].isnull()]=-1
df_analyse_rend['Q10_10'].loc[df_analyse_rend['Q10_10'].isnull()]=-1
df_analyse_rend['Q7_9'].loc[df_analyse_rend['Q7_9'].isnull()]=-1
df_analyse_rend['Q10_12'].loc[df_analyse_rend['Q10_12'].isnull()]=-1
df_analyse_rend['PC_PROTEIN'].loc[df_analyse_rend['PC_PROTEIN'].isnull()]=-1
df_analyse_rend['PC_LEGUMES'].loc[df_analyse_rend['PC_LEGUMES'].isnull()]=-1
df_analyse_rend['PC_CER'].loc[df_analyse_rend['PC_CER'].isnull()]=-1
df_analyse_rend['PCDEPNALIM'].loc[df_analyse_rend['PCDEPNALIM'].isnull()]=-1
df_analyse_rend['PCDEPALIM'].loc[df_analyse_rend['PCDEPALIM'].isnull()]=-1
df_analyse_rend['DEPTOT'].loc[df_analyse_rend['DEPTOT'].isnull()]=-1
df_analyse_rend['DEPALIM'].loc[df_analyse_rend['DEPALIM'].isnull()]=-1
df_analyse_rend['Q10_15'].loc[df_analyse_rend['Q10_15'].isnull()]=-1
df_analyse_rend['Q10_17'].loc[df_analyse_rend['Q10_17'].isnull()]=-1
df_analyse_rend['Q10_20'].loc[df_analyse_rend['Q10_20'].isnull()]=-1
df_analyse_rend['Q10_21'].loc[df_analyse_rend['Q10_21'].isnull()]=-1
df_analyse_rend['Q10_22'].loc[df_analyse_rend['Q10_22'].isnull()]=-1
df_analyse_rend['Q10_23'].loc[df_analyse_rend['Q10_23'].isnull()]=-1
df_analyse_rend['Q10_24'].loc[df_analyse_rend['Q10_24'].isnull()]=-1
df_analyse_rend['ACTIFS'].loc[df_analyse_rend['ACTIFS'].isnull()]=-1
df_analyse_rend['PLUSDE15ANS'].loc[df_analyse_rend['PLUSDE15ANS'].isnull()]=-1
df_analyse_rend['HWDDS'].loc[df_analyse_rend['HWDDS'].isnull()]=-1
df_analyse_rend['Q10_1A'].loc[df_analyse_rend['Q10_1A'].isnull()]=-1
df_analyse_rend['Q10_5A'].loc[df_analyse_rend['Q10_5A'].isnull()]=-1
df_analyse_rend['Q10_13'].loc[df_analyse_rend['Q10_13'].isnull()]=-1
df_analyse_rend['Q10_2A'].loc[df_analyse_rend['Q10_2A'].isnull()]=-1
df_analyse_rend['Q10_3A'].loc[df_analyse_rend['Q10_3A'].isnull()]=-1
df_analyse_rend['Q10_4A'].loc[df_analyse_rend['Q10_4A'].isnull()]=-1
df_analyse_rend['PC_FRUIT'].loc[df_analyse_rend['PC_FRUIT'].isnull()]=-1
df_analyse_rend['PC_PULSES'].loc[df_analyse_rend['PC_PULSES'].isnull()]=-1
df_analyse_rend['PC_LAIT'].loc[df_analyse_rend['PC_LAIT'].isnull()]=-1
df_analyse_rend['Q10_14'].loc[df_analyse_rend['Q10_14'].isnull()]=-1
df_analyse_rend['PC_SUCRE'].loc[df_analyse_rend['PC_SUCRE'].isnull()]=-1
df_analyse_rend['Q7_10'].loc[df_analyse_rend['Q7_10'].isnull()]=-1
df_analyse_rend['PC_HUILE'].loc[df_analyse_rend['PC_HUILE'].isnull()]=-1
df_analyse_rend['PC_OTHER'].loc[df_analyse_rend['PC_OTHER'].isnull()]=-1
df_analyse_rend['Q6_2_A'].loc[df_analyse_rend['Q6_2_A'].isnull()]=-1
df_analyse_rend['VENT_LAIT'].loc[df_analyse_rend['VENT_LAIT'].isnull()]=-1
df_analyse_rend['PROD_LAIT'].loc[df_analyse_rend['PROD_LAIT'].isnull()]=-1
df_analyse_rend['NB_REPAS_AD'].loc[df_analyse_rend['NB_REPAS_AD'].isnull()]=-1
df_analyse_rend['Q7_3'].loc[df_analyse_rend['Q7_3'].isnull()]=-1
df_analyse_rend['Q7_2'].loc[df_analyse_rend['Q7_2'].isnull()]=-1
df_analyse_rend['Q6_4'].loc[df_analyse_rend['Q6_4'].isnull()]=-1
df_analyse_rend['Q6_3_B'].loc[df_analyse_rend['Q6_3_B'].isnull()]=-1
df_analyse_rend['Q7_4'].loc[df_analyse_rend['Q7_4'].isnull()]=-1
df_analyse_rend['Q7_5'].loc[df_analyse_rend['Q7_5'].isnull()]=-1
df_analyse_rend['Q7_6'].loc[df_analyse_rend['Q7_6'].isnull()]=-1
df_analyse_rend['Q9_9'].loc[df_analyse_rend['Q9_9'].isnull()]=-1
df_analyse_rend['POS_CAPRIN'].loc[df_analyse_rend['POS_CAPRIN'].isnull()]=-1
df_analyse_rend['POS_OVIN'].loc[df_analyse_rend['POS_OVIN'].isnull()]=-1
df_analyse_rend['POS_BOVIN'].loc[df_analyse_rend['POS_BOVIN'].isnull()]=-1
df_analyse_rend['POS_CAMELIN'].loc[df_analyse_rend['POS_CAMELIN'].isnull()]=-1
df_analyse_rend['Q9_10'].loc[df_analyse_rend['Q9_10'].isnull()]=-1
df_analyse_rend['Q4_8_2'].loc[df_analyse_rend['Q4_8_2'].isnull()]=-1
df_analyse_rend['Q4_8_1'].loc[df_analyse_rend['Q4_8_1'].isnull()]=-1
df_analyse_rend['Q6_2_B'].loc[df_analyse_rend['Q6_2_B'].isnull()]=-1
df_analyse_rend['PC_PROD'].loc[df_analyse_rend['PC_PROD'].isnull()]=-1
df_analyse_rend['PC_DON'].loc[df_analyse_rend['PC_DON'].isnull()]=-1
df_analyse_rend['PC_BLE'].loc[df_analyse_rend['PC_BLE'].isnull()]=-1
df_analyse_rend['PC_MIL'].loc[df_analyse_rend['PC_MIL'].isnull()]=-1
df_analyse_rend['PC_SORG'].loc[df_analyse_rend['PC_SORG'].isnull()]=-1
df_analyse_rend['PC_MAIS'].loc[df_analyse_rend['PC_MAIS'].isnull()]=-1
df_analyse_rend['PC_RIZ'].loc[df_analyse_rend['PC_RIZ'].isnull()]=-1
df_analyse_rend['PC_ACHAT'].loc[df_analyse_rend['PC_ACHAT'].isnull()]=-1
df_analyse_rend['LHG'].loc[df_analyse_rend['LHG'].isnull()]=-1
df_analyse_rend['Q4_6_1'].loc[df_analyse_rend['Q4_6_1'].isnull()]=-1
df_analyse_rend['Q4_6_2'].loc[df_analyse_rend['Q4_6_2'].isnull()]=-1
df_analyse_rend['Q8_1_1'].loc[df_analyse_rend['Q8_1_1'].isnull()]=-1
df_analyse_rend['Q8_20'].loc[df_analyse_rend['Q8_20'].isnull()]=-1
df_analyse_rend['Q10_18'].loc[df_analyse_rend['Q10_18'].isnull()]=-1
df_analyse_rend['REVENU3'].loc[df_analyse_rend['REVENU3'].isnull()]=-1
df_analyse_rend['Q10_19'].loc[df_analyse_rend['Q10_19'].isnull()]=-1
df_analyse_rend['Q4_1A'].loc[df_analyse_rend['Q4_1A'].isnull()]=-1
df_analyse_rend['Q4_2A'].loc[df_analyse_rend['Q4_2A'].isnull()]=-1
df_analyse_rend['Q4_3A'].loc[df_analyse_rend['Q4_3A'].isnull()]=-1
df_analyse_rend['REV_PERCAP'].loc[df_analyse_rend['REV_PERCAP'].isnull()]=-1
df_analyse_rend['REVENU_MENS'].loc[df_analyse_rend['REVENU_MENS'].isnull()]=-1
df_analyse_rend['Q4_4A'].loc[df_analyse_rend['Q4_4A'].isnull()]=-1
df_analyse_rend['REVENU2'].loc[df_analyse_rend['REVENU2'].isnull()]=-1
df_analyse_rend['Q10_16'].loc[df_analyse_rend['Q10_16'].isnull()]=-1
df_analyse_rend['Q10_7'].loc[df_analyse_rend['Q10_7'].isnull()]=-1
df_analyse_rend['REVENU1'].loc[df_analyse_rend['REVENU1'].isnull()]=-1
df_analyse_rend['Q11_11'].loc[df_analyse_rend['Q11_11'].isnull()]=-1
df_analyse_rend['Q4_5_1'].loc[df_analyse_rend['Q4_5_1'].isnull()]=-1
df_analyse_rend['Q4_5_2'].loc[df_analyse_rend['Q4_5_2'].isnull()]=-1
df_analyse_rend['Q4_7_2'].loc[df_analyse_rend['Q4_7_2'].isnull()]=-1
df_analyse_rend['Q4_7_1'].loc[df_analyse_rend['Q4_7_1'].isnull()]=-1
df_analyse_rend['Q8_1_2'].loc[df_analyse_rend['Q8_1_2'].isnull()]=-1
df_analyse_rend['RAP_FEMINITE'].loc[df_analyse_rend['RAP_FEMINITE'].isnull()]=-1
df_analyse_rend['DISPO_CER_EQIV'].loc[df_analyse_rend['DISPO_CER_EQIV'].isnull()]=-1
df_analyse_rend['SUM_CER_EQIV'].loc[df_analyse_rend['SUM_CER_EQIV'].isnull()]=-1
df_analyse_rend['Q7_1'].loc[df_analyse_rend['Q7_1'].isnull()]=-1
df_analyse_rend['DISPO_CER_PARPER'].loc[df_analyse_rend['DISPO_CER_PARPER'].isnull()]=-1
df_analyse_rend['SUM_CER_DON'].loc[df_analyse_rend['SUM_CER_DON'].isnull()]=-1
df_analyse_rend['SUM_CER_PARPER'].loc[df_analyse_rend['SUM_CER_PARPER'].isnull()]=-1
df_analyse_rend['Q5_5_4'].loc[df_analyse_rend['Q5_5_4'].isnull()]=-1
df_analyse_rend['SUM_CER_ACHAT'].loc[df_analyse_rend['SUM_CER_ACHAT'].isnull()]=-1
df_analyse_rend['Q5_5_3'].loc[df_analyse_rend['Q5_5_3'].isnull()]=-1
df_analyse_rend['SUM_BLE'].loc[df_analyse_rend['SUM_BLE'].isnull()]=-1
df_analyse_rend['Q5_5_1'].loc[df_analyse_rend['Q5_5_1'].isnull()]=-1
df_analyse_rend['SUM_CER_PROD'].loc[df_analyse_rend['SUM_CER_PROD'].isnull()]=-1
df_analyse_rend['Q5_5_2'].loc[df_analyse_rend['Q5_5_2'].isnull()]=-1
df_analyse_rend['SUM_CEREALES'].loc[df_analyse_rend['SUM_CEREALES'].isnull()]=-1
df_analyse_rend['DISPO_CER'].loc[df_analyse_rend['DISPO_CER'].isnull()]=-1
df_analyse_rend['Q6_1_B'].loc[df_analyse_rend['Q6_1_B'].isnull()]=-1


# Quantidication des NA restants 
temp = pd.DataFrame(df_analyse_rend.isnull().sum(),columns=['Nb']).sort_values('Nb', ascending = False)
temp =  100*df_analyse_rend.isnull().sum()/len(df_analyse_rend)



###########################################################################
# Analyses descriptives : 
# https://fxjollois.github.io/cours-2016-2017/analyse-donnees-massives-tp4.html

temp=df_analyse_rend.describe()

# Analyse des rendements

liste=["HY_Rend_tot_cowpea","HY_Rend_tot_groundnut","HY_Rend_tot_maize",
       "HY_Rend_tot_millet","HY_Rend_tot_sorghum","HY_Rend_tot"]
stats=[]
for i in liste : 
    temp=df_analyse_rend.loc[df_analyse_rend[i]>0]
    temp.boxplot(column = i, by = "FCS_BIN") 
    temp.hist(column = i, by = "FCS_BIN")
    stats.append([i,temp.groupby("FCS_BIN")[i].agg(['count', np.mean, np.std, np.median, np.min, np.max])])

# Commentaire : Il y a des valeurs extremes dans les rendements. 
# Ces valeurs extremes correspondent à la réalité ou erreur de calcul?
# Elles sont obervées uniquement sur 2013. 
# Est ce qu'après une grande secheresse nous avons un grand rendement?

# Analyse des extrèmes

temp=df_analyse_rend.loc[df_analyse_rend["HY_Rend_tot"]>0]
temp=temp.describe()

temp=df_analyse_rend.loc[df_analyse_rend["HY_Rend_tot"]>=20000]
sns.distplot(temp['HY_Rend_tot'])
sns.displot(temp, x="HY_Rend_tot", col="YEAR", facet_kws=dict(margin_titles=True),)
temp.groupby("YEAR")["HY_Rend_tot"].agg(['count', np.mean, np.std, np.median, np.min, np.max])

# Suppression de la valeur extreme 60000 observée sur 2013 uniquement

df_analyse_rend=df_analyse_rend.loc[df_analyse_rend["HY_Rend_tot"]<59000]
temp=df_analyse_rend.describe()

# Analyse de la distribution finale

temp=df_analyse_rend.loc[df_analyse_rend["HY_Rend_tot"]>=2000]
sns.distplot(temp['HY_Rend_tot'])
sns.displot(temp, x="HY_Rend_tot", col="YEAR", facet_kws=dict(margin_titles=True),)
temp.groupby("YEAR")["HY_Rend_tot"].agg(['count', np.mean, np.std, np.median, np.min, np.max])

liste=["HY_Rend_tot_cowpea","HY_Rend_tot_groundnut","HY_Rend_tot_maize",
       "HY_Rend_tot_millet","HY_Rend_tot_sorghum","HY_Rend_tot"]
stats=[]
for i in liste : 
    temp=df_analyse_rend.loc[df_analyse_rend[i]>0]
    temp.boxplot(column = i, by = "FCS_BIN") 
    pyplot.show()
    #temp.hist(column = i, by = "FCS_BIN")
    
    a=temp.loc[temp["FCS_BIN"]==0]
    b=temp.loc[temp["FCS_BIN"]==1]
    pyplot.hist([a[i],b[i]],label=['0', '1'])
    pyplot.legend(loc='upper right')
    pyplot.show()
    
    stats.append([i,temp.groupby("FCS_BIN")[i].agg(['count', np.mean, np.std, np.median, np.min, np.max])])

# Commentaire :Résultats surprenants compte tenu du fait que les rendements moyens sont
# généralement plus élevés en moyenne sur les menage en IA le contraire est observé sur
# la médiane. 

# Analyse Q2_5
df_analyse_rend["Q2_5"].loc[df_analyse_rend["Q2_5"]>35].describe()

# Suppression de la valeur extreme 35 pers

df_analyse_rend=df_analyse_rend.loc[df_analyse_rend["Q2_5"]<=35]
df_analyse_rend["Q2_5"].describe()

a=df_analyse_rend.loc[df_analyse_rend["FCS_BIN"]==0]
b=df_analyse_rend.loc[df_analyse_rend["FCS_BIN"]==1]
pyplot.hist([a["Q2_5"],b["Q2_5"]],label=['0', '1'])
pyplot.legend(loc='upper right')
pyplot.show()


# Analyse TAILMEN
df_analyse_rend["TAILMEN"].describe()
df_analyse_rend["EQUIV_AD"].describe()
df_analyse_rend["S_LAITIERS"].loc[df_analyse_rend["S_LAITIERS"]>-1].describe()
df_analyse_rend["S_LAITIERS"].loc[df_analyse_rend["S_LAITIERS"]>-1].value_counts()

###########################################################################
# Sauvegarde de la base
df_analyse_rend.to_csv('C:/0 - Data/df_analyse_rend.csv', sep = ';')

###########################################################################
# Creation de listes de noms de colonnes selon leur type

col_obj = [col for col in df_analyse_rend.select_dtypes(include=object).columns.tolist()]
col_num = [col for col in df_analyse_rend.select_dtypes(include=float).columns.tolist()]
col_int = [col for col in df_analyse_rend.select_dtypes(include=int).columns.tolist()]

a=df_analyse_rend.dtypes



###########################################################################
# Analyse des correlations
df_corr = df_analyse_rend.corr()
# df_corr = df_corr.where(np.triu(np.ones(df_corr.shape),k=1).astype(np.bool))
df_corr = df_corr.unstack().reset_index()
df_corr.columns =['VAR1','VAR2','Correlation']
df_corr.dropna(subset = ["Correlation"], inplace = True)
df_corr["Correlation"]=df_corr["Correlation"].abs() 
df_corr.sort_values(by='Correlation', ascending=False, inplace=True) 

df_corr.to_csv('C:/0 - Data/df_corr.csv', sep = ';')

# Ici il faudra mettre les variables qu'on garde ou qu'on supprime selon cette analyse


# Créer une variable avec la possession de 'animaux'
'''
POS_ANNIMAUX
POS_CAMELIN
POS_OVIN
POS_CAPRIN
'''

###########################################################################
# Listes
Liste_Class=["Q4_3","POS_BOVIN","REVENU_MENS","Q4_5_1","Rend_Pos","Q2_1","Q2_2","Q2_3","Q2_4"]


'''Q4_3	- Caprins
Q4_5_1	- Vaches			
Q2_1	2.1- Sexe du chef de ménage		
Q2_2	2.2- Age du chef de ménage		
Q2_3	2.3- Statut matrimonial du chef de ménage		
Q2_4	2.4- Niveau d'éducation du CM	'''	

###########################################################################
# Creation bases Train / Test = Y continue

print("Dataset has {} entries and {} features".format(*df_analyse_rend.shape))

df_model_X=df_analyse_rend[[col for col in Liste_Class]]
df_model_Y=df_analyse_rend[['FCS_BIN']]

from sklearn.model_selection import train_test_split
rd_seed=0
X_train, X_test, y_train, y_test  = train_test_split(df_model_X, df_model_Y, test_size=0.2, random_state=rd_seed) #, stratify=df_model_Y
#print(df_train_X.shape,"\n",df_valid_X.shape,"\n",df_train_Y.shape,"\n",df_valid_Y.shape)
y_train.value_counts(normalize=True) 
y_test.value_counts(normalize=True) 


###########################################################################
# Arbre de decision ,"EQUIV_AD"

#instanciation de l'arbre
from sklearn.tree import DecisionTreeClassifier
arbreFirst = DecisionTreeClassifier(max_depth =5, min_samples_split=30,min_samples_leaf=10)

#construction de l'arbre
#Liste_Class=["MOUGHATAA","REVENU_MENS"]
X_train_Deci=X_train[Liste_Class]
X_test_Deci=X_test[Liste_Class]
arbreFirst.fit(X = X_train_Deci, y = y_train['FCS_BIN'])

#affichage graphique de l'arbre - depuis sklearn 0.21
#https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree
from sklearn.tree import plot_tree
plot_tree(arbreFirst,feature_names = list(X_train_Deci.columns),filled=True)

#affichage plus grand pour une meilleure lisibilité
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plot_tree(arbreFirst,feature_names = list(X_train_Deci.columns),filled=True)
plt.show()

#affichage sous forme de règles - plus facile à appréhender quand l'arbre est très grand
from sklearn.tree import export_text
tree_rules = export_text(arbreFirst,feature_names = list(X_train_Deci.columns),show_weights=True)

#importance des variables
impVarFirst={"Variable":X_train_Deci.columns,"Importance":arbreFirst.feature_importances_}
print(pd.DataFrame(impVarFirst).sort_values(by="Importance",ascending=False))

#prédiction sur l'échantillon test
predFirst = arbreFirst.predict(X=X_test_Deci)

#distribution des predictions
print(np.unique(predFirst,return_counts=True))

#rapport de prédiction
from sklearn import metrics
print(metrics.classification_report(y_test,predFirst))
















