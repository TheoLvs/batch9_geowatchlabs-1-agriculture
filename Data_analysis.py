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

###########################################################################
# Chargement de la base
df_analyse_rend=ti.df_analyse.copy()
df_moughataa_rend=ti.df_moughataa.copy()

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

###########################################################################
# Quantification et elimination des NA

temp = pd.DataFrame(df_analyse_rend.isnull().sum(),columns=['Nb']).sort_values('Nb', ascending = False)
temp =  100*df_analyse_rend.isnull().sum()/len(df_analyse_rend)

# Suppression des variables incompletes ou sans signifiation
df_analyse_rend=df_analyse_rend.drop(['MIGRATION','year','IDENT','Long_Gpe3','month','numquest',
                                     'STRATE','STRATE1','NOMVILLAGE','COMMUNE','STRATES','ALTITUDE',
                                     'ACCURACY','DEPNALIM','FCG_RECODED','COPING_STRATEGY','LHZ','latlong_id',
                                     'Lat_MOUGHATAA','Long_MOUGHATAA','PONDERATION','YEAR','LONGITUDE','QUEST',
                                     'NUMQUEST','LATITUDE','FCG_28_42','EXTRAPOLATION','MONTH'], axis=1)

# Suppression des variables liées au score IA
df_analyse_rend=df_analyse_rend.drop(["ADBASE","LEGUMINEUSE","FRUITS","LEGUMES","VIANDE_POISSON","LAIT",
                                      "HUILE","SUCRE"], axis=1)

# Remplacement des NA par 0
df_analyse_rend['Q2_8$2'].loc[df_analyse_rend['Q2_8$2'].isnull()]=0
df_analyse_rend['Q2_11'].loc[df_analyse_rend['Q2_11'].isnull()]=0
df_analyse_rend['Q2_83'].loc[df_analyse_rend['Q2_83'].isnull()]=0
df_analyse_rend['Q2_8$1'].loc[df_analyse_rend['Q2_8$1'].isnull()]=0
df_analyse_rend['Q2_82'].loc[df_analyse_rend['Q2_82'].isnull()]=0
df_analyse_rend['S_FRUIT'].loc[df_analyse_rend['S_FRUIT'].isnull()]=0
df_analyse_rend['Q9_9_8'].loc[df_analyse_rend['Q9_9_8'].isnull()]=0
df_analyse_rend['Q11_1_8$3'].loc[df_analyse_rend['Q11_1_8$3'].isnull()]=0
df_analyse_rend['Q10_25'].loc[df_analyse_rend['Q10_25'].isnull()]=0
df_analyse_rend['Q2_7_1564'].loc[df_analyse_rend['Q2_7_1564'].isnull()]=0
df_analyse_rend['Q9_9_9'].loc[df_analyse_rend['Q9_9_9'].isnull()]=0
df_analyse_rend['Q9_8_A'].loc[df_analyse_rend['Q9_8_A'].isnull()]=0
df_analyse_rend['Q9_9_7'].loc[df_analyse_rend['Q9_9_7'].isnull()]=0
df_analyse_rend['Q9_9_6'].loc[df_analyse_rend['Q9_9_6'].isnull()]=0
df_analyse_rend['Q11_9_16$2'].loc[df_analyse_rend['Q11_9_16$2'].isnull()]=0
df_analyse_rend['Q9_9_4'].loc[df_analyse_rend['Q9_9_4'].isnull()]=0
df_analyse_rend['Q9_9_3'].loc[df_analyse_rend['Q9_9_3'].isnull()]=0
df_analyse_rend['Q9_9_2'].loc[df_analyse_rend['Q9_9_2'].isnull()]=0
df_analyse_rend['Q9_8_B'].loc[df_analyse_rend['Q9_8_B'].isnull()]=0
df_analyse_rend['Q9_9_5'].loc[df_analyse_rend['Q9_9_5'].isnull()]=0
df_analyse_rend['Q11_1_8$4'].loc[df_analyse_rend['Q11_1_8$4'].isnull()]=0
df_analyse_rend['Q11_9_16$8'].loc[df_analyse_rend['Q11_9_16$8'].isnull()]=0
df_analyse_rend['Q11_9_16$7'].loc[df_analyse_rend['Q11_9_16$7'].isnull()]=0
df_analyse_rend['Q2_9_1564'].loc[df_analyse_rend['Q2_9_1564'].isnull()]=0
df_analyse_rend['Q7_95'].loc[df_analyse_rend['Q7_95'].isnull()]=0
df_analyse_rend['Q7_87'].loc[df_analyse_rend['Q7_87'].isnull()]=0
df_analyse_rend['Q7_80'].loc[df_analyse_rend['Q7_80'].isnull()]=0
df_analyse_rend['Q7_81'].loc[df_analyse_rend['Q7_81'].isnull()]=0
df_analyse_rend['Q7_82'].loc[df_analyse_rend['Q7_82'].isnull()]=0
df_analyse_rend['Q7_83'].loc[df_analyse_rend['Q7_83'].isnull()]=0
df_analyse_rend['Q7_84'].loc[df_analyse_rend['Q7_84'].isnull()]=0
df_analyse_rend['Q7_85'].loc[df_analyse_rend['Q7_85'].isnull()]=0
df_analyse_rend['Q7_86'].loc[df_analyse_rend['Q7_86'].isnull()]=0
df_analyse_rend['Q7_88'].loc[df_analyse_rend['Q7_88'].isnull()]=0
df_analyse_rend['Q7_96'].loc[df_analyse_rend['Q7_96'].isnull()]=0
df_analyse_rend['Q7_93'].loc[df_analyse_rend['Q7_93'].isnull()]=0
df_analyse_rend['Q7_89'].loc[df_analyse_rend['Q7_89'].isnull()]=0
df_analyse_rend['Q7_91'].loc[df_analyse_rend['Q7_91'].isnull()]=0
df_analyse_rend['Q7_90'].loc[df_analyse_rend['Q7_90'].isnull()]=0
df_analyse_rend['Q7_99'].loc[df_analyse_rend['Q7_99'].isnull()]=0
df_analyse_rend['Q7_98'].loc[df_analyse_rend['Q7_98'].isnull()]=0
df_analyse_rend['Q7_97'].loc[df_analyse_rend['Q7_97'].isnull()]=0
df_analyse_rend['Q7_94'].loc[df_analyse_rend['Q7_94'].isnull()]=0
df_analyse_rend['Q7_92'].loc[df_analyse_rend['Q7_92'].isnull()]=0
df_analyse_rend['Q2_NBPERS_F_64A'].loc[df_analyse_rend['Q2_NBPERS_F_64A'].isnull()]=0
df_analyse_rend['Q2_NBPERS_M_64A'].loc[df_analyse_rend['Q2_NBPERS_M_64A'].isnull()]=0
df_analyse_rend['Q2_NBPERS_M_18A'].loc[df_analyse_rend['Q2_NBPERS_M_18A'].isnull()]=0
df_analyse_rend['Lat_Gpe3'].loc[df_analyse_rend['Lat_Gpe3'].isnull()]=0
df_analyse_rend['Q2_NBPERS_F_18A'].loc[df_analyse_rend['Q2_NBPERS_F_18A'].isnull()]=0
df_analyse_rend['Q7_0B3'].loc[df_analyse_rend['Q7_0B3'].isnull()]=0
df_analyse_rend['Q2_81'].loc[df_analyse_rend['Q2_81'].isnull()]=0
df_analyse_rend['Q7_23'].loc[df_analyse_rend['Q7_23'].isnull()]=0
df_analyse_rend['Q6_3_A'].loc[df_analyse_rend['Q6_3_A'].isnull()]=0
df_analyse_rend['S_ADBASE2'].loc[df_analyse_rend['S_ADBASE2'].isnull()]=0
df_analyse_rend['PC_VENTLAIT'].loc[df_analyse_rend['PC_VENTLAIT'].isnull()]=0
df_analyse_rend['Q7_0C'].loc[df_analyse_rend['Q7_0C'].isnull()]=0
df_analyse_rend['Q11_2A'].loc[df_analyse_rend['Q11_2A'].isnull()]=0
df_analyse_rend['Q7_0B2'].loc[df_analyse_rend['Q7_0B2'].isnull()]=0
df_analyse_rend['Q2_7B'].loc[df_analyse_rend['Q2_7B'].isnull()]=0
df_analyse_rend['Q2_9'].loc[df_analyse_rend['Q2_9'].isnull()]=0
df_analyse_rend['Q2_7A'].loc[df_analyse_rend['Q2_7A'].isnull()]=0
df_analyse_rend['Q2_10'].loc[df_analyse_rend['Q2_10'].isnull()]=0
df_analyse_rend['Q2_8'].loc[df_analyse_rend['Q2_8'].isnull()]=0
df_analyse_rend['NB_REPAS_AD'].loc[df_analyse_rend['NB_REPAS_AD'].isnull()]=0
df_analyse_rend['S_LAITIERS'].loc[df_analyse_rend['S_LAITIERS'].isnull()]=0
df_analyse_rend['D_FRUIT'].loc[df_analyse_rend['D_FRUIT'].isnull()]=0
df_analyse_rend['S_SMALLAI'].loc[df_analyse_rend['S_SMALLAI'].isnull()]=0
df_analyse_rend['S_VIAND_POISS'].loc[df_analyse_rend['S_VIAND_POISS'].isnull()]=0
df_analyse_rend['S_PROTEISMALL'].loc[df_analyse_rend['S_PROTEISMALL'].isnull()]=0
df_analyse_rend['Q6_2_A'].loc[df_analyse_rend['Q6_2_A'].isnull()]=0
df_analyse_rend['D_ADBASE2'].loc[df_analyse_rend['D_ADBASE2'].isnull()]=0
df_analyse_rend['Q7_22'].loc[df_analyse_rend['Q7_22'].isnull()]=0
df_analyse_rend['D_LAITIERS'].loc[df_analyse_rend['D_LAITIERS'].isnull()]=0
df_analyse_rend['Q9_17'].loc[df_analyse_rend['Q9_17'].isnull()]=0
df_analyse_rend['S_LEGUMES'].loc[df_analyse_rend['S_LEGUMES'].isnull()]=0
df_analyse_rend['Q5_0B'].loc[df_analyse_rend['Q5_0B'].isnull()]=0
df_analyse_rend['D_PROTEISMALL'].loc[df_analyse_rend['D_PROTEISMALL'].isnull()]=0
df_analyse_rend['D_VIAND_POISS'].loc[df_analyse_rend['D_VIAND_POISS'].isnull()]=0
df_analyse_rend['CODEVILLAGE'].loc[df_analyse_rend['CODEVILLAGE'].isnull()]=0
df_analyse_rend['D_SMALLAI'].loc[df_analyse_rend['D_SMALLAI'].isnull()]=0
df_analyse_rend['Q7_21'].loc[df_analyse_rend['Q7_21'].isnull()]=0
df_analyse_rend['Q6_3_B'].loc[df_analyse_rend['Q6_3_B'].isnull()]=0
df_analyse_rend['Q7_0B1'].loc[df_analyse_rend['Q7_0B1'].isnull()]=0
df_analyse_rend['Q6_4'].loc[df_analyse_rend['Q6_4'].isnull()]=0
df_analyse_rend['Q11_11'].loc[df_analyse_rend['Q11_11'].isnull()]=0
df_analyse_rend['D_LEGUMES'].loc[df_analyse_rend['D_LEGUMES'].isnull()]=0
df_analyse_rend['S_PULSES'].loc[df_analyse_rend['S_PULSES'].isnull()]=0
df_analyse_rend['Q6_2_B'].loc[df_analyse_rend['Q6_2_B'].isnull()]=0
df_analyse_rend['D_PULSES'].loc[df_analyse_rend['D_PULSES'].isnull()]=0
df_analyse_rend['PC_SORG'].loc[df_analyse_rend['PC_SORG'].isnull()]=0
df_analyse_rend['PC_MIL'].loc[df_analyse_rend['PC_MIL'].isnull()]=0
df_analyse_rend['PC_DON'].loc[df_analyse_rend['PC_DON'].isnull()]=0
df_analyse_rend['PC_ACHAT'].loc[df_analyse_rend['PC_ACHAT'].isnull()]=0
df_analyse_rend['PC_MAIS'].loc[df_analyse_rend['PC_MAIS'].isnull()]=0
df_analyse_rend['PC_PROD'].loc[df_analyse_rend['PC_PROD'].isnull()]=0
df_analyse_rend['PC_RIZ'].loc[df_analyse_rend['PC_RIZ'].isnull()]=0
df_analyse_rend['PC_BLE'].loc[df_analyse_rend['PC_BLE'].isnull()]=0
df_analyse_rend['S_SUCRE'].loc[df_analyse_rend['S_SUCRE'].isnull()]=0
df_analyse_rend['D_OTHER'].loc[df_analyse_rend['D_OTHER'].isnull()]=0
df_analyse_rend['S_HUILE'].loc[df_analyse_rend['S_HUILE'].isnull()]=0
df_analyse_rend['S_OTHER'].loc[df_analyse_rend['S_OTHER'].isnull()]=0
df_analyse_rend['D_ADBASE1'].loc[df_analyse_rend['D_ADBASE1'].isnull()]=0
df_analyse_rend['SMALLAI'].loc[df_analyse_rend['SMALLAI'].isnull()]=0
df_analyse_rend['D_HUILE'].loc[df_analyse_rend['D_HUILE'].isnull()]=0
df_analyse_rend['D_SUCRE'].loc[df_analyse_rend['D_SUCRE'].isnull()]=0
df_analyse_rend['Q5_0A'].loc[df_analyse_rend['Q5_0A'].isnull()]=0
df_analyse_rend['ADBASE2'].loc[df_analyse_rend['ADBASE2'].isnull()]=0
df_analyse_rend['S_ADBASE1'].loc[df_analyse_rend['S_ADBASE1'].isnull()]=0
df_analyse_rend['PULSES'].loc[df_analyse_rend['PULSES'].isnull()]=0
df_analyse_rend['ADBASE1'].loc[df_analyse_rend['ADBASE1'].isnull()]=0
df_analyse_rend['Q7_11'].loc[df_analyse_rend['Q7_11'].isnull()]=0
df_analyse_rend['Q7_16'].loc[df_analyse_rend['Q7_16'].isnull()]=0
df_analyse_rend['Q7_15'].loc[df_analyse_rend['Q7_15'].isnull()]=0
df_analyse_rend['Q7_14'].loc[df_analyse_rend['Q7_14'].isnull()]=0
df_analyse_rend['Q7_13'].loc[df_analyse_rend['Q7_13'].isnull()]=0
df_analyse_rend['Q7_12'].loc[df_analyse_rend['Q7_12'].isnull()]=0
df_analyse_rend['Q7_0B'].loc[df_analyse_rend['Q7_0B'].isnull()]=0
df_analyse_rend['Q7_10'].loc[df_analyse_rend['Q7_10'].isnull()]=0
df_analyse_rend['Q7_9'].loc[df_analyse_rend['Q7_9'].isnull()]=0
df_analyse_rend['Q2_0A'].loc[df_analyse_rend['Q2_0A'].isnull()]=0
df_analyse_rend['Q2_0C'].loc[df_analyse_rend['Q2_0C'].isnull()]=0
df_analyse_rend['Q2_NBPERS_M_6M'].loc[df_analyse_rend['Q2_NBPERS_M_6M'].isnull()]=0
df_analyse_rend['PC_OTHER'].loc[df_analyse_rend['PC_OTHER'].isnull()]=0
df_analyse_rend['PC_HUILE'].loc[df_analyse_rend['PC_HUILE'].isnull()]=0
df_analyse_rend['PC_SUCRE'].loc[df_analyse_rend['PC_SUCRE'].isnull()]=0
df_analyse_rend['PC_LAIT'].loc[df_analyse_rend['PC_LAIT'].isnull()]=0
df_analyse_rend['Q2_NBPERS_M_2A'].loc[df_analyse_rend['Q2_NBPERS_M_2A'].isnull()]=0
df_analyse_rend['PC_PROTEIN'].loc[df_analyse_rend['PC_PROTEIN'].isnull()]=0
df_analyse_rend['PC_FRUIT'].loc[df_analyse_rend['PC_FRUIT'].isnull()]=0
df_analyse_rend['PC_LEGUMES'].loc[df_analyse_rend['PC_LEGUMES'].isnull()]=0
df_analyse_rend['PC_PULSES'].loc[df_analyse_rend['PC_PULSES'].isnull()]=0
df_analyse_rend['PC_CER'].loc[df_analyse_rend['PC_CER'].isnull()]=0
df_analyse_rend['Q2_NBPERS_M_59A'].loc[df_analyse_rend['Q2_NBPERS_M_59A'].isnull()]=0
df_analyse_rend['Q2_NBPERS_F_6M'].loc[df_analyse_rend['Q2_NBPERS_F_6M'].isnull()]=0
df_analyse_rend['Q2_NBPERS_F_2A'].loc[df_analyse_rend['Q2_NBPERS_F_2A'].isnull()]=0
df_analyse_rend['Q2_NBPERS_F_59A'].loc[df_analyse_rend['Q2_NBPERS_F_59A'].isnull()]=0
df_analyse_rend['TOTADULTE'].loc[df_analyse_rend['TOTADULTE'].isnull()]=0
df_analyse_rend['PCDEPNALIM'].loc[df_analyse_rend['PCDEPNALIM'].isnull()]=0
df_analyse_rend['TOTMOINS5'].loc[df_analyse_rend['TOTMOINS5'].isnull()]=0
df_analyse_rend['TAILMENOLD'].loc[df_analyse_rend['TAILMENOLD'].isnull()]=0
df_analyse_rend['Q7_7'].loc[df_analyse_rend['Q7_7'].isnull()]=0
df_analyse_rend['Q7_8'].loc[df_analyse_rend['Q7_8'].isnull()]=0
df_analyse_rend['PROTEISMALL'].loc[df_analyse_rend['PROTEISMALL'].isnull()]=0
df_analyse_rend['LAITIERS'].loc[df_analyse_rend['LAITIERS'].isnull()]=0
df_analyse_rend['VIAND_POISS'].loc[df_analyse_rend['VIAND_POISS'].isnull()]=0
df_analyse_rend['Q10_17'].loc[df_analyse_rend['Q10_17'].isnull()]=0
df_analyse_rend['Q10_1A'].loc[df_analyse_rend['Q10_1A'].isnull()]=0
df_analyse_rend['HWDDS'].loc[df_analyse_rend['HWDDS'].isnull()]=0
df_analyse_rend['PLUSDE15ANS'].loc[df_analyse_rend['PLUSDE15ANS'].isnull()]=0
df_analyse_rend['Q10_24'].loc[df_analyse_rend['Q10_24'].isnull()]=0
df_analyse_rend['Q10_23'].loc[df_analyse_rend['Q10_23'].isnull()]=0
df_analyse_rend['Q10_22'].loc[df_analyse_rend['Q10_22'].isnull()]=0
df_analyse_rend['Q10_21'].loc[df_analyse_rend['Q10_21'].isnull()]=0
df_analyse_rend['Q10_20'].loc[df_analyse_rend['Q10_20'].isnull()]=0
df_analyse_rend['Q9_14'].loc[df_analyse_rend['Q9_14'].isnull()]=0
df_analyse_rend['Q10_15'].loc[df_analyse_rend['Q10_15'].isnull()]=0
df_analyse_rend['Q6_0A'].loc[df_analyse_rend['Q6_0A'].isnull()]=0
df_analyse_rend['Q9_15'].loc[df_analyse_rend['Q9_15'].isnull()]=0
df_analyse_rend['Q9_16'].loc[df_analyse_rend['Q9_16'].isnull()]=0
df_analyse_rend['Q10_8'].loc[df_analyse_rend['Q10_8'].isnull()]=0
df_analyse_rend['Q10_9'].loc[df_analyse_rend['Q10_9'].isnull()]=0
df_analyse_rend['Q10_10'].loc[df_analyse_rend['Q10_10'].isnull()]=0
df_analyse_rend['Q10_11'].loc[df_analyse_rend['Q10_11'].isnull()]=0
df_analyse_rend['Q10_12'].loc[df_analyse_rend['Q10_12'].isnull()]=0
df_analyse_rend['Q10_13'].loc[df_analyse_rend['Q10_13'].isnull()]=0
df_analyse_rend['Q10_14'].loc[df_analyse_rend['Q10_14'].isnull()]=0
df_analyse_rend['Q10_2A'].loc[df_analyse_rend['Q10_2A'].isnull()]=0
df_analyse_rend['ACTIFS'].loc[df_analyse_rend['ACTIFS'].isnull()]=0
df_analyse_rend['Q10_3A'].loc[df_analyse_rend['Q10_3A'].isnull()]=0
df_analyse_rend['DEPALIM'].loc[df_analyse_rend['DEPALIM'].isnull()]=0
df_analyse_rend['Q7_0A'].loc[df_analyse_rend['Q7_0A'].isnull()]=0
df_analyse_rend['PCDEPALIM'].loc[df_analyse_rend['PCDEPALIM'].isnull()]=0
df_analyse_rend['OTHER'].loc[df_analyse_rend['OTHER'].isnull()]=0
df_analyse_rend['Q9_11'].loc[df_analyse_rend['Q9_11'].isnull()]=0
df_analyse_rend['Q9_12'].loc[df_analyse_rend['Q9_12'].isnull()]=0
df_analyse_rend['Q9_13'].loc[df_analyse_rend['Q9_13'].isnull()]=0
df_analyse_rend['Q10_4A'].loc[df_analyse_rend['Q10_4A'].isnull()]=0
df_analyse_rend['DEPTOT'].loc[df_analyse_rend['DEPTOT'].isnull()]=0
df_analyse_rend['Q6_0B'].loc[df_analyse_rend['Q6_0B'].isnull()]=0
df_analyse_rend['Q10_5A'].loc[df_analyse_rend['Q10_5A'].isnull()]=0
df_analyse_rend['VENT_LAIT'].loc[df_analyse_rend['VENT_LAIT'].isnull()]=0
df_analyse_rend['PROD_LAIT'].loc[df_analyse_rend['PROD_LAIT'].isnull()]=0
df_analyse_rend['Q7_3'].loc[df_analyse_rend['Q7_3'].isnull()]=0
df_analyse_rend['Q7_2'].loc[df_analyse_rend['Q7_2'].isnull()]=0
df_analyse_rend['Q7_4'].loc[df_analyse_rend['Q7_4'].isnull()]=0
df_analyse_rend['POS_CAPRIN'].loc[df_analyse_rend['POS_CAPRIN'].isnull()]=0
df_analyse_rend['POS_CAMELIN'].loc[df_analyse_rend['POS_CAMELIN'].isnull()]=0
df_analyse_rend['POS_OVIN'].loc[df_analyse_rend['POS_OVIN'].isnull()]=0
df_analyse_rend['Q7_6'].loc[df_analyse_rend['Q7_6'].isnull()]=0
df_analyse_rend['Q9_9'].loc[df_analyse_rend['Q9_9'].isnull()]=0
df_analyse_rend['Q9_10'].loc[df_analyse_rend['Q9_10'].isnull()]=0
df_analyse_rend['POS_BOVIN'].loc[df_analyse_rend['POS_BOVIN'].isnull()]=0
df_analyse_rend['Q7_5'].loc[df_analyse_rend['Q7_5'].isnull()]=0
df_analyse_rend['Q4_8_2'].loc[df_analyse_rend['Q4_8_2'].isnull()]=0
df_analyse_rend['Q4_8_1'].loc[df_analyse_rend['Q4_8_1'].isnull()]=0
df_analyse_rend['LHG'].loc[df_analyse_rend['LHG'].isnull()]=0
df_analyse_rend['Q8_1_2'].loc[df_analyse_rend['Q8_1_2'].isnull()]=0
df_analyse_rend['Q8_1_1'].loc[df_analyse_rend['Q8_1_1'].isnull()]=0
df_analyse_rend['Q4_6_1'].loc[df_analyse_rend['Q4_6_1'].isnull()]=0
df_analyse_rend['Q4_6_2'].loc[df_analyse_rend['Q4_6_2'].isnull()]=0
df_analyse_rend['RAP_FEMINITE'].loc[df_analyse_rend['RAP_FEMINITE'].isnull()]=0
df_analyse_rend['Q8_20'].loc[df_analyse_rend['Q8_20'].isnull()]=0
df_analyse_rend['Q4_5_2'].loc[df_analyse_rend['Q4_5_2'].isnull()]=0
df_analyse_rend['Q4_5_1'].loc[df_analyse_rend['Q4_5_1'].isnull()]=0
df_analyse_rend['Q10_19'].loc[df_analyse_rend['Q10_19'].isnull()]=0
df_analyse_rend['Q2_NOM_CHEF'].loc[df_analyse_rend['Q2_NOM_CHEF'].isnull()]=0
df_analyse_rend['Q4_1A'].loc[df_analyse_rend['Q4_1A'].isnull()]=0
df_analyse_rend['Q4_2A'].loc[df_analyse_rend['Q4_2A'].isnull()]=0
df_analyse_rend['Q4_3A'].loc[df_analyse_rend['Q4_3A'].isnull()]=0
df_analyse_rend['Q10_7'].loc[df_analyse_rend['Q10_7'].isnull()]=0
df_analyse_rend['Q4_4A'].loc[df_analyse_rend['Q4_4A'].isnull()]=0
df_analyse_rend['Q10_16'].loc[df_analyse_rend['Q10_16'].isnull()]=0
df_analyse_rend['REV_PERCAP'].loc[df_analyse_rend['REV_PERCAP'].isnull()]=0
df_analyse_rend['REVENU_MENS'].loc[df_analyse_rend['REVENU_MENS'].isnull()]=0
df_analyse_rend['REVENU3'].loc[df_analyse_rend['REVENU3'].isnull()]=0
df_analyse_rend['REVENU2'].loc[df_analyse_rend['REVENU2'].isnull()]=0
df_analyse_rend['REVENU1'].loc[df_analyse_rend['REVENU1'].isnull()]=0
df_analyse_rend['Q10_18'].loc[df_analyse_rend['Q10_18'].isnull()]=0
df_analyse_rend['Q4_7_1'].loc[df_analyse_rend['Q4_7_1'].isnull()]=0
df_analyse_rend['Q4_7_2'].loc[df_analyse_rend['Q4_7_2'].isnull()]=0
df_analyse_rend['Q2_1'].loc[df_analyse_rend['Q2_1'].isnull()]=0

# Quantidication des NA restants 
temp = pd.DataFrame(df_analyse_rend.isnull().sum(),columns=['Nb']).sort_values('Nb', ascending = False)
temp =  100*df_analyse_rend.isnull().sum()/len(df_analyse_rend)

###########################################################################
# Analyse des correlations
df_corr = df_analyse_rend.corr()
df_corr = df_corr.where(np.triu(np.ones(df_corr.shape),k=1).astype(np.bool))
df_corr = df_corr.unstack().reset_index()
df_corr.columns =['VAR1','VAR2','Correlation']
df_corr.dropna(subset = ["Correlation"], inplace = True)
df_corr["Correlation"]=df_corr["Correlation"].abs() 
df_corr.sort_values(by='Correlation', ascending=False, inplace=True) 
df_corr.head(50)

# Ici il faudra mettre les variables qu'on garde ou qu'on supprime selon cette analyse

###########################################################################
# Analyses descriptives : Sur quelques variables mais il faudra mettre toutes les variables
import pandas_profiling

dt_temp=df_analyse_rend[['FCS','FCS_BIN','MOUGHATAA','FICHIER','Q5_0A','Q6_1_A',
                         'HY_Rend_tot_cowpea','HY_Rend_tot_groundnut','HY_Rend_tot_sorghum',
                         'HY_Rend_tot_maize','HY_Rend_tot_millet','HY_Rend_tot']]

profile = pandas_profiling.ProfileReport(dt_temp, title="Pandas Profiling Report", explorative=True)
profile.to_widgets()
profile.to_notebook_iframe()
profile.to_file("your_report.html")

###########################################################################
# Analyses des outliers des variables continues




###########################################################################
# Creation de listes de noms de colonnes selon leur type

col_obj = [col for col in df_analyse_rend.select_dtypes(include=object).columns.tolist()]
col_num = [col for col in df_analyse_rend.select_dtypes(include=float).columns.tolist()]
col_int = [col for col in df_analyse_rend.select_dtypes(include=int).columns.tolist()]

a=df_analyse_rend.dtypes

###########################################################################
# Classification : CAH et KNN

df_classif=df_analyse_rend[['FCS_BIN','MOUGHATAA','Q5_0A','Q6_1_A',
                         'HY_Rend_tot_cowpea','HY_Rend_tot_groundnut','HY_Rend_tot_sorghum',
                         'HY_Rend_tot_maize','HY_Rend_tot_millet']]

#Center #Reduce
df_classif_cr = df_classif.sub(df_classif.mean())
df_classif_cr = df_classif_cr.div(df_classif.std()) 
df_classif_cr.describe()

#librairies pour la CAH
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

#générer la matrice des liens
Z = linkage(df_classif_cr,method='ward',metric='euclidean')

#affichage du dendrogramme
plt.title("CAH")
dendrogram(Z,labels=df_classif.index,orientation='left',color_threshold=0)
plt.show()

#matérialisation des 4 classes (hauteur t = 7)
plt.title('CAH avec matérialisation des 4 classes')
dendrogram(Z,labels=df_classif.index,orientation='left',color_threshold=7)
plt.show()
#découpage à la hauteur t = 7 ==> identifiants de 4 groupes obtenus
groupes_cah = fcluster(Z,t=70,criterion='distance')
print(groupes_cah)
#index triés des groupes
import numpy as np
idg = np.argsort(groupes_cah)
#affichage des observations et leurs groupes
print(pd.DataFrame(df_classif.index[idg],groupes_cah[idg]))
a=pd.DataFrame(df_classif.index[idg],groupes_cah[idg])

#k-means sur les données centrées et réduites
from sklearn import cluster
kmeans = cluster.KMeans(n_clusters=4)
kmeans.fit(df_classif_cr)
#index triés des groupes
idk = np.argsort(kmeans.labels_)
#affichage des observations et leurs groupes
print(pd.DataFrame(df_classif.index[idk],kmeans.labels_[idk]))
#distances aux centres de classes des observations
print(kmeans.transform(df_classif_cr))
#correspondance avec les groupes de la CAH
pd.crosstab(groupes_cah,kmeans.labels_)

#librairie pour évaluation des partitions
from sklearn import metrics
#utilisation de la métrique "silhouette"
#faire varier le nombre de clusters de 2 à 10
res = np.arange(9,dtype="double")
for k in np.arange(9):
    km = cluster.KMeans(n_clusters=k+2)
    km.fit(df_classif_cr)
    res[k] = metrics.silhouette_score(df_classif_cr,km.labels_)
print(res)
#graphique
import matplotlib.pyplot as plt
plt.title("Silhouette")
plt.xlabel("# of clusters")
plt.plot(np.arange(2,11,1),res)
plt.show()


#moyenne par variable
m = df_classif.mean()
#TSS
TSS = df_classif.shape[0]*df_classif.var(ddof=0)
print(TSS)
#data.frame conditionnellement aux groupes
gb = df_classif.groupby(kmeans.labels_)
#effectifs conditionnels
nk = gb.size()
print(nk)
#moyennes conditionnelles
mk = gb.mean()
print(mk)
#pour chaque groupe écart à la moyenne par variable
EMk = (mk-m)**2
#pondéré par les effectifs du groupe
EM = EMk.multiply(nk,axis=0)
#somme des valeurs => BSS
BSS = np.sum(EM,axis=0)
print(BSS)
#carré du rapport de corrélation
#variance expliquée par l'appartenance aux groupes
#pour chaque variable
R2 = BSS/TSS
print(R2)


###########################################################################
# Creation bases Train / Test = Y continue

print("Dataset has {} entries and {} features".format(*df_analyse_rend.shape))

df_model_X=df_analyse_rend[['MOUGHATAA','Q5_0A','Q6_1_A',
                         'HY_Rend_tot_cowpea','HY_Rend_tot_groundnut','HY_Rend_tot_sorghum',
                         'HY_Rend_tot_maize','HY_Rend_tot_millet']]
df_model_Y=df_analyse_rend[['FCS']]

from sklearn.model_selection import train_test_split
rd_seed=0
X_train, X_test, y_train, y_test  = train_test_split(df_model_X, df_model_Y, test_size=0.1, random_state=rd_seed) #, stratify=df_model_Y
#print(df_train_X.shape,"\n",df_valid_X.shape,"\n",df_train_Y.shape,"\n",df_valid_Y.shape)
y_train.value_counts(normalize=True) 
y_test.value_counts(normalize=True) 

###########################################################################
# XGBoost = Y continue
# https://blog.cambridgespark.com/hyperparameter-tuning-in-xgboost-4ff9100a3b2f

import xgboost as xgb

dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

from sklearn.metrics import mean_absolute_error


import numpy as np
# "Learn" the mean from the training data
mean_train = np.mean(y_train)
# Get predictions on the test set
df_mean_test=y_test
df_mean_test['mean_train']=mean_train[0]

# Compute MAE
mae_baseline = mean_absolute_error(df_mean_test['FCS'], df_mean_test['mean_train'])
print("Baseline MAE is {:.2f}".format(mae_baseline))



params = {
    # Parameters that we are going to tune.
    'max_depth':6,
    'min_child_weight': 1,
    'eta':.3,
    'subsample': 1,
    'colsample_bytree': 1,
    # Other parameters
    'objective':'reg:linear',
}

params['eval_metric'] = "mae"
num_boost_round = 999

model = xgb.train(
    params,
    dtrain,
    num_boost_round=num_boost_round,
    evals=[(dtest, "Test")],
    early_stopping_rounds=10
)

print("Best MAE: {:.2f} with {} rounds".format(model.best_score,model.best_iteration+1))


cv_results = xgb.cv(
    params,
    dtrain,
    num_boost_round=num_boost_round,
    seed=42,
    nfold=5,
    metrics={'mae'},
    early_stopping_rounds=10
)
cv_results
cv_results['test-mae-mean'].min()


print(model.feature_importances_)
	
# plot feature importance
from xgboost import plot_importance
plot_importance(model)

y_pred = model.predict(dtest)
df_y_pred = pd.DataFrame(y_pred)


###########################################################################
# Regression lineaire multiple = Y continue
# http://eric.univ-lyon2.fr/~ricco/tanagra/fichiers/fr_Tanagra_Python_StatsModels.pdf
# http://eric.univ-lyon2.fr/~ricco/tanagra/fichiers/fr_Tanagra_Regression_Lasso_Python.pdf
# X_train, X_test, y_train, y_test 

dfXy_train=pd.concat([X_train,y_train],axis=1)
dfXy_train.columns

#régression avec formule
import statsmodels.formula.api as smf

#instanciation
reg = smf.ols('FCS ~ MOUGHATAA + Q6_1_A + HY_Rend_tot_cowpea', data = dfXy_train)
res = reg.fit()
print(res.summary())
print(res.rsquared)
F = res.mse_model / res.mse_resid
print(F)

#Hypotheses à vérifier

#Linéarité
#Normalité des résidus
#Homogénéité de la variance des résidus
#Indépendance des résidus
#Absence de valeurs aberrantes


###########################################################################
# Creation bases Train / Test = Y binaire

print("Dataset has {} entries and {} features".format(*df_analyse_rend.shape))

df_model_X=df_analyse_rend[['MOUGHATAA','Q5_0A','Q6_1_A',
                         'HY_Rend_tot_cowpea','HY_Rend_tot_groundnut','HY_Rend_tot_sorghum',
                         'HY_Rend_tot_maize','HY_Rend_tot_millet']]
df_model_Y=df_analyse_rend[['FCS_BIN']]



from sklearn.model_selection import train_test_split
rd_seed=0
X_train, X_test, y_train, y_test  = train_test_split(df_model_X, df_model_Y, test_size=0.1,stratify=df_model_Y, random_state=rd_seed) #, 
print(X_train.shape,"\n",X_test.shape,"\n",y_train.shape,"\n",y_test.shape)
y_train.value_counts(normalize=True) 
y_test.value_counts(normalize=True) 

###########################################################################
# XGBoost  = Y binaire
# X_train, X_test, y_train, y_test

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

param_test = {'learning_rate':[0.01,0.05],'n_estimators':range(1,201,100)}
gsearch = GridSearchCV(
    estimator = GradientBoostingClassifier(
        learning_rate=0.05, 
        max_depth=11,
        min_samples_split=800, 
        min_samples_leaf=30, 
        random_state=10,
       #max_features=12
        ),
    param_grid = param_test, 
    scoring='roc_auc',
    n_jobs=4,
    cv=5)

gsearch.fit(X_train, y_train)
a=gsearch.cv_results_ 
gsearch.best_params_, gsearch.best_score_


gbm_tuned = GradientBoostingClassifier(
    learning_rate=0.05, 
    n_estimators=101,
    max_depth=11, 
    min_samples_split=800,
    min_samples_leaf=30,  
    random_state=10, 
   #max_features=12
    )


gbm_tuned.fit(X_train, y_train)

# Prévision de l'échantillon test
yChap = gbm_tuned.predict(X_test)
yChap2=pd.DataFrame(yChap)

yChap.shape

y_test2=np.matrix(y_test)

y_test2.shape
# matrice de confusion
table=pd.crosstab(yChap,y_test2)
table=pd.crosstab(yChap2,y_test)
print(table)

# Erreur de prévision sur le test
print("Precision de test gbm opt = %f" % (gbm_tuned_3.score(df_valid_X,df_valid_Y)))

dtrain_predictions = gbm_tuned_3.predict(df_train_X)
print("Accuracy : %.4g" % metrics.accuracy_score(df_train_Y.values, dtrain_predictions))

###########################################################################
# regression logistique  = Y binaire
# X_train, X_test, y_train, y_test

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import roc_curve

clt = LogisticRegression(solver='liblinear',random_state=0)
regLog2 = clt.fit(X_train,y_train)
print(clt.classes_)

imp={"Var" : X_train.columns, "Coef" : clt.coef_[0]}
print(pd.DataFrame.from_dict(imp).sort_values(by="Coef",ascending=False))
a=pd.DataFrame.from_dict(imp).sort_values(by="Coef",ascending=False)

prob = regLog2.predict_proba(X_test)


probas_ = regLog2.predict_proba(X_test)
fpr, tpr, thresholds = roc_curve(y_test, probas_[:,1])
yChap = regLog2.predict(X_test)
metrics.auc(fpr,tpr)
print(1-metrics.accuracy_score(y_test,yChap))

list_res_acc = [['regLog2',1-metrics.accuracy_score(y_test,yChap)]]

###########################################################################
# Lasso = Y binaire
# X_train, X_test, y_train, y_test
# http://eric.univ-lyon2.fr/~ricco/tanagra/fichiers/fr_Tanagra_Regression_Lasso_Python.pdf


dfXy_train=pd.concat([X_train,y_train],axis=1)
dfXy_train.columns

#centrer et réduire les données d'apprentissage
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
ZTrain =sc.fit_transform(dfXy_train)

#régression Lasso, paramètres par défaut (alpha = 1.0)
from sklearn.linear_model import Lasso
regLasso1 = Lasso(fit_intercept=False,normalize=False)
print(regLasso1)

#apprentissage
regLasso1.fit(ZTrain[:,:8],ZTrain[:,8])
#les coefficients
print(regLasso1.coef_)

#lasso path (10 valeurs de alpha à tester)
my_alphas = np.array([0.001,0.01,0.02,0.025,0.05,0.1,0.25,0.5,0.8,1.0])

#obtention des valeurs des coefs. corresp.
from sklearn.linear_model import lasso_path
alpha_for_path, coefs_lasso, _ = lasso_path(ZTrain[:,:8],ZTrain[:,8],alphas=my_alphas)

#dim. matrice des coefficients
print(coefs_lasso.shape) #(16, 10)

#jeu de couleurs pour faire joli
import matplotlib.cm as cm
couleurs = cm.rainbow(np.linspace(0,1,16))
#graphique lasso path (une courbe par variable)
for i in range(coefs_lasso.shape[0]):
 plt.plot(alpha_for_path,coefs_lasso[i,:],c=couleurs[i])

plt.xlabel('Alpha')
plt.ylabel('Coefficients')
plt.title('Lasso path')
plt.show()

#nombre de coefs. non-nuls pour chaque alpha
nbNonZero = np.apply_along_axis(func1d=np.count_nonzero,arr=coefs_lasso,axis=0)

#affichage mieux organisé alpha vs. nombre de coefs non-nuls 
print(pd.DataFrame({'alpha':alpha_for_path,'Nb non-zero coefs':nbNonZero}))

#ou sous forme graphique
plt.plot(alpha_for_path,nbNonZero)
plt.xlabel('Alpha')
plt.ylabel('Nb. de variables')
plt.title('Nb. variables vs. Alpha')
plt.show()

#nom des variables
nom_var = dfXy_train.columns[:8]
#coefficients pour alpha=0.25 (colonne n°3)
coefs25 = coefs_lasso[:,3]
#affichage des coefficients pour alpha = 0.25
print(pd.DataFrame({'Variables':nom_var,'Coefficients':coefs25}))


#outil pour la détection de la solution la plus performante en validation croisée
#random_state = 0 pour fixer l’initialisation du générateur de nombre aléatoire
#cv = 5 pour 5-fold validation croisée
from sklearn.linear_model import LassoCV
lcv = LassoCV(alphas=my_alphas,normalize=False,fit_intercept=False,random_state=0,cv=5)

#lancement sur l'échantillon d'apprentissage
lcv.fit(ZTrain[:,:8],ZTrain[:,8])

#valeurs des alphas qui ont été testés
print(lcv.alphas_) #[1. 0.8 0.5 0.25 0.1 0.05 0.025 0.02 0.01 0.001]
#valeurs des MSE en validation croisée
print(lcv.mse_path_)

#moyenne mse en validation croisée pour chaque alpha
avg_mse = np.mean(lcv.mse_path_,axis=1)
#alphas vs. MSE en cross-validation
print(pd.DataFrame({'alpha':lcv.alphas_,'MSE':avg_mse}))

#sous-forme graphique
plt.plot(lcv.alphas_,avg_mse)
plt.xlabel('Alpha')
plt.ylabel('MSE')
plt.title('MSE vs. Alpha')
plt.show()

#best alpha
print(lcv.alpha_) #0.01

#transformation des variables des données test
ZTest = sc.transform(dfXy_train)

#prediction avec ce modèle
ypzLasso = lcv.predict(ZTest[:,:8])

#dé-standardization de la prédiction, [-1] parce que y est en dernière position
ypLasso = ypzLasso*np.sqrt(sc.var_[-1]) + sc.mean_[-1]

#performances en prédiction
from sklearn.metrics import mean_squared_error
print(mean_squared_error(yTest,ypLasso)) #0.31204589721406967
























