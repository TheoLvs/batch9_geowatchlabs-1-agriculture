###########################################################################
# Librairies
import pandas as pd
import numpy as np
import os
import unicodedata

###########################################################################
# Fonctions
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    only_ascii= only_ascii.decode('utf-8')
    return only_ascii

###########################################################################
# Afficher tous les fichiers du repertoire Mauritania FSMS data
# dans df_run

from os import walk

monRepertoire=r"C:\0 - Data\Mauritania FSMS data"

df_run = pd.DataFrame(columns=['Repertoire','Fichier','Total','Extension'], dtype = str)
i=0
for (repertoire, sousRepertoires, fichiers) in walk(monRepertoire):
    for name in fichiers:
        df_run.loc[i,"Repertoire"]=str(repertoire)
        df_run.loc[i,"Fichier"]=str(name)
        df_run.loc[i,"Total"]=os.path.join(str(repertoire),name)
        filename, file_extension = os.path.splitext(os.path.join(str(repertoire),str(sousRepertoires),name))
        df_run.loc[i,"Extension"]=file_extension
        i=i+1

# nettoyage
del monRepertoire , fichiers , i , filename , file_extension , name , repertoire , sousRepertoires

############################################################################
# Exploration des fichiers du repertoire Mauritania FSMS data

# Affichage de tous les types de fichiers
df_run.Extension.value_counts()

# division des fichiers par extension
df_run_sav=df_run.loc[df_run.Extension==".sav"]
# df_run_sps=df_run.loc[df_run.Extension==".sps"]
# df_run_xls=df_run.loc[df_run.Extension==".xls"]
# df_run_xlsx=df_run.loc[df_run.Extension==".xlsx"]
# df_run_xml=df_run.loc[df_run.Extension==".xml"]
# df_run_csv=df_run.loc[df_run.Extension==".csv"]

############################################################################
# Lecture des fichiers sav 

import pyreadstat

#df1, meta1 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2011\Decembre11\Données_FSMS_nov11_26_12.sav")
#df2, meta2 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2011\Janvier11\Données\FSMS_2011_4-2-11_URBAN.sav")
#df3, meta3 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2011\Janvier11\Données\FSMS_2011_RURAL_FINAL.sav")
df4, meta4 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2011\Juin11\Données_FSMS_16_08_11.sav")
#df5, meta5 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2012\Analyse croise SA_NUT\RIM_FSMS_SMART_juil2012.sav")
#df6, meta6 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2012\Decembre\Donnes_FSMSdec12_HH_commun.sav")
df7, meta7 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2012\Juin\Données_FSMS_juil_12.sav")
#df8, meta8 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2013\Decembre\Données FSMS 13Dec_20_01_14.sav")
df9, meta9 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2013\Juin\FSMS_HH_juil13b_1.sav")
#df10, meta10 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2014\Decembre\Données_FSMS_24_06_15.sav")
df11, meta11 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2014\Juin\Données_FSMS_juin_2014.sav")
#df12, meta12 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2015\Decembre\Données FSMS Jan16_18_02.sav")
df13, meta13 = pyreadstat.read_sav(r"C:\0 - Data\Mauritania FSMS data\2015\Juin\Données_FSMS_juin_15.sav")
# globals()["df" + str(n)], globals()["meta" + str(n)] = pyreadstat.read_sav(file, apply_value_formats=True)

# Ajout de la date
df4["FICHIER"]="June-11"
df7["FICHIER"]="June-12"
df9["FICHIER"]="June-13"
df11["FICHIER"]="June-14"
df13["FICHIER"]="June-15"

# Ajout num questionnaire
df4["QUEST"]="Q4"
df7["QUEST"]="Q7"
df9["QUEST"]="Q9"
df11["QUEST"]="Q11"
df13["QUEST"]="Q13"

# Ajout annee
df4["year"]="2011"
df7["year"]="2012"
df9["year"]="2013"
df11["year"]="2014"
df13["year"]="2015"

# Ajout mois
df4["month"]="Juin"
df7["month"]="Juin"
df9["month"]="Juin"
df11["month"]="Juin"
df13["month"]="Juin"

############################################################################
# Modification des noms des colonnes des df: 
# Majuscules sans accent de toutes les tables df

# Noms de colonnes dans listes
Lst_NomCol_df4=[c for c in df4]
Lst_NomCol_df7=[c for c in df7]
Lst_NomCol_df9=[c for c in df9]
Lst_NomCol_df11=[c for c in df11]
Lst_NomCol_df13=[c for c in df13]

# Suppression accents + mise en majuscule
Lst_NomCol_df4=[remove_accents(string) for string in Lst_NomCol_df4]
Lst_NomCol_df4=[string.upper() for string in Lst_NomCol_df4]
Lst_NomCol_df7=[remove_accents(string) for string in Lst_NomCol_df7]
Lst_NomCol_df7=[string.upper() for string in Lst_NomCol_df7]
Lst_NomCol_df9=[remove_accents(string) for string in Lst_NomCol_df9]
Lst_NomCol_df9=[string.upper() for string in Lst_NomCol_df9]
Lst_NomCol_df11=[remove_accents(string) for string in Lst_NomCol_df11]
Lst_NomCol_df11=[string.upper() for string in Lst_NomCol_df11]
Lst_NomCol_df13=[remove_accents(string) for string in Lst_NomCol_df13]
Lst_NomCol_df13=[string.upper() for string in Lst_NomCol_df13]

# Remplacement des noms de colonne
df4.columns = [Lst_NomCol_df4]
df7.columns = [Lst_NomCol_df7]
df9.columns = [Lst_NomCol_df9]
df11.columns = [Lst_NomCol_df11]
df13.columns = [Lst_NomCol_df13]

df4.columns = ['/'.join(x) for x in df4.columns.values]
df7.columns = ['/'.join(x) for x in df7.columns.values]
df9.columns = ['/'.join(x) for x in df9.columns.values]
df11.columns = ['/'.join(x) for x in df11.columns.values]
df13.columns = ['/'.join(x) for x in df13.columns.values]

# nettoyage
del Lst_NomCol_df4,Lst_NomCol_df7,Lst_NomCol_df9,Lst_NomCol_df11,Lst_NomCol_df13

############################################################################
# Analyse des colonnes des df

# Noms de colonnes dans listes
Lst_NomCol_df4=[c for c in df4]
Lst_NomCol_df7=[c for c in df7]
Lst_NomCol_df9=[c for c in df9]
Lst_NomCol_df11=[c for c in df11]
Lst_NomCol_df13=[c for c in df13]

# Noms de colonnes dans une dataframe
Df_Lst_NomCol_df4=pd.DataFrame(Lst_NomCol_df4)
Df_Lst_NomCol_df4["QUEST"]="df4"
Df_Lst_NomCol_df7=pd.DataFrame(Lst_NomCol_df7)
Df_Lst_NomCol_df7["QUEST"]="df7"
Df_Lst_NomCol_df9=pd.DataFrame(Lst_NomCol_df9)
Df_Lst_NomCol_df9["QUEST"]="df9"
Df_Lst_NomCol_df11=pd.DataFrame(Lst_NomCol_df11)
Df_Lst_NomCol_df11["QUEST"]="df11"
Df_Lst_NomCol_df13=pd.DataFrame(Lst_NomCol_df13)
Df_Lst_NomCol_df13["QUEST"]="df13"

# Rassemblement des noms de colonne
List_col_df = pd.concat([Df_Lst_NomCol_df4,Df_Lst_NomCol_df7,Df_Lst_NomCol_df9,Df_Lst_NomCol_df11,Df_Lst_NomCol_df13])

# Tableau avec noms de colonnes et présence dans les differents questionnaires
Tab_col=pd.crosstab([List_col_df[0]], List_col_df["QUEST"], margins=True)

# nettoyage
del Df_Lst_NomCol_df4,Df_Lst_NomCol_df7,Df_Lst_NomCol_df9,Df_Lst_NomCol_df11,Df_Lst_NomCol_df13,Lst_NomCol_df4,Lst_NomCol_df7,Lst_NomCol_df9,Lst_NomCol_df11,Lst_NomCol_df13

############################################################################
# Reconstitution des questionnaires à partir des meta données
# Objectif : Comprendre les colonnes à partir des questionnaires
# Retait des accents et minuscules dans les noms de colonne

# Commentaire : on pourrait mettre le code qui suit dans une boucle mais je ne
# sais pas comment créer des noms de table avec l'indice utilisé dans la boucle

# Q4
col_names=meta4.column_names
col_names=[remove_accents(string) for string in col_names]
col_names=[string.upper() for string in col_names]
col_lab=meta4.column_labels
df_col_names=pd.DataFrame(col_names,columns=["col_names"])
df_col_lab=pd.DataFrame(col_lab,columns=["col_lab4"])
col=pd.concat([df_col_names,df_col_lab],axis=1)
var_lab=meta4.variable_value_labels
df_var_lab=pd.DataFrame(list(var_lab.items()),columns=["col_names","var_lab4"])
quest4=col.merge(df_var_lab,how='left',on='col_names')
quest4["ID4"]="Q4"

# Q7
col_names=meta7.column_names
col_names=[remove_accents(string) for string in col_names]
col_names=[string.upper() for string in col_names]
col_lab=meta7.column_labels
df_col_names=pd.DataFrame(col_names,columns=["col_names"])
df_col_lab=pd.DataFrame(col_lab,columns=["col_lab7"])
col=pd.concat([df_col_names,df_col_lab],axis=1)
var_lab=meta7.variable_value_labels
df_var_lab=pd.DataFrame(list(var_lab.items()),columns=["col_names","var_lab7"])
quest7=col.merge(df_var_lab,how='left',on='col_names')
quest7["ID7"]="Q7"

# Q9
col_names=meta9.column_names
col_names=[remove_accents(string) for string in col_names]
col_names=[string.upper() for string in col_names]
col_lab=meta9.column_labels
df_col_names=pd.DataFrame(col_names,columns=["col_names"])
df_col_lab=pd.DataFrame(col_lab,columns=["col_lab9"])
col=pd.concat([df_col_names,df_col_lab],axis=1)
var_lab=meta9.variable_value_labels
df_var_lab=pd.DataFrame(list(var_lab.items()),columns=["col_names","var_lab9"])
quest9=col.merge(df_var_lab,how='left',on='col_names')
quest9["ID9"]="Q9"

# Q11
col_names=meta11.column_names
col_names=[remove_accents(string) for string in col_names]
col_names=[string.upper() for string in col_names]
col_lab=meta11.column_labels
df_col_names=pd.DataFrame(col_names,columns=["col_names"])
df_col_lab=pd.DataFrame(col_lab,columns=["col_lab11"])
col=pd.concat([df_col_names,df_col_lab],axis=1)
var_lab=meta11.variable_value_labels
df_var_lab=pd.DataFrame(list(var_lab.items()),columns=["col_names","var_lab11"])
quest11=col.merge(df_var_lab,how='left',on='col_names')
quest11["ID11"]="Q11"

# Q13
col_names=meta13.column_names
col_names=[remove_accents(string) for string in col_names]
col_names=[string.upper() for string in col_names]
col_lab=meta13.column_labels
df_col_names=pd.DataFrame(col_names,columns=["col_names"])
df_col_lab=pd.DataFrame(col_lab,columns=["col_lab13"])
col=pd.concat([df_col_names,df_col_lab],axis=1)
var_lab=meta13.variable_value_labels
df_var_lab=pd.DataFrame(list(var_lab.items()),columns=["col_names","var_lab13"])
quest13=col.merge(df_var_lab,how='left',on='col_names')
quest13["ID13"]="Q13"


# nettoyage
del col_names,col_lab,df_col_names,df_col_lab,col,df_var_lab,var_lab

############################################################################
# Rassemblement des questionnaires reconsitués 

questtot = quest4.merge(quest7,how='outer', on='col_names')
questtot = questtot.merge(quest9,how='outer',on='col_names')
questtot = questtot.merge(quest11,how='outer',on='col_names')
questtot = questtot.merge(quest13,how='outer',on='col_names')


questtot["T_PRESENCE_NUM"]=questtot["ID4"].notna()*1+questtot["ID7"].notna()*1+questtot["ID9"].notna()*1+questtot["ID11"].notna()*1+questtot["ID13"].notna()*1

questtot.ID4[questtot.ID4.isna()] = " "
questtot.ID7[questtot.ID7.isna()] = " "
questtot.ID9[questtot.ID9.isna()] = " "
questtot.ID11[questtot.ID11.isna()] = " "
questtot.ID13[questtot.ID13.isna()] = " "
questtot["T_PRESENCE"]=questtot["ID4"]+"_"+questtot["ID7"]+"_"+questtot["ID9"]+"_"+questtot["ID11"]+"_"+questtot["ID13"]


#temp = pd.read_csv("C:/0 - Data/Statut.csv",sep=';')
#questtot = questtot.merge(temp,how='left',on='col_names')


############################################################################
# Nettoyage suite à une analyse manuelle de questtot

# Rename
df4=df4.rename(columns = {'PONDERATIONS': 'PONDERATION', 
                      'VILLAGE': 'CODEVILLAGE',
                      'WILAYA': 'CODREG',
                      'COMMUNE': 'COMMUNE',
                      'EXTRAP': 'EXTRAPOLATION',
                      'MILIEU': 'MILIEU',
                      'VILLAG0': 'NOMVILLAGE',
                      'STRATE': 'STRATES',
                      'Q2_6_1_M' : 'Q2_NBPERS_M_5A',
                      'Q2_6_1_F' : 'Q2_NBPERS_F_5A',
                      'Q2_6_2_M' : 'Q2_NBPERS_M_14A',
                      'Q2_6_2_F' : 'Q2_NBPERS_F_14A',
                      'Q2_6_3_M' : 'Q2_NBPERS_M_18A',
                      'Q2_6_3_F' : 'Q2_NBPERS_F_18A',
                      'Q2_6_4_M' : 'Q2_NBPERS_M_64A',
                      'Q2_6_4_F' : 'Q2_NBPERS_F_64A',
                      'Q2_6_5_M' : 'Q2_NBPERS_M_100A',
                      'Q2_6_5_F' : 'Q2_NBPERS_F_100A',
                      'SUM_SORGHO' : 'SUM_SORG'
                      })

df7=df7.rename(columns = {'ID01': 'IDENT', 
                          'WILAYA': 'CODREG', 
                      'COMMUNE': 'COMMUNE',
                      'MILIEU': 'MILIEU',
                      'Q2_0': 'Q2_NOM_CHEF',
                      'VILLAG0': 'NOMVILLAGE',
                      'PONDERATION1': 'EXTRAPOLATION',
                      'PONDERATION2': 'PONDERATION',
                      'Q10_A_E$5': 'Q10_16',
                      'Q10_A_E$2': 'Q10_18',
                      'Q10_A_E$1': 'Q10_7',
                      'Q10_A_E$3': 'Q10_25',
                      'Q10_A_E$4': 'Q10_19',
                      'Q11_1_8$1': 'Q11_1',
                      'Q11_1_8$2': 'Q11_2',
                      'Q11_1_8$5': 'Q11_3',
                      'Q11_1_8$6': 'Q11_4',
                      'Q11_1_8$7': 'Q11_5',
                      'Q11_1_8$8': 'Q11_6',
                      'Q11_9_16$1': 'Q11_7',
                      'Q11_9_16$3': 'Q11_9',
                      'Q11_9_16$4': 'Q11_10',
                      'Q11_9_16$5': 'Q11_11',
                      'Q11_9_16$6': 'Q11_8',
                      'Q9_1_8$1': 'Q9_1',
                      'Q9_1_8$2': 'Q9_2',
                      'Q9_1_8$3': 'Q9_3',
                      'Q9_1_8$4': 'Q9_4',
                      'Q9_1_8$5': 'Q9_5',
                      'Q9_1_8$6': 'Q9_6',
                      'Q9_1_8$7': 'Q9_7',
                      'Q9_1_8$8': 'Q9_8_A',
                      'Q9_9_16$1': 'Q9_8',
                      'Q9_1_8$9': 'Q9_8_B',
                      'Q9_9_16$2': 'Q9_9_2',
                      'Q9_9_16$3': 'Q9_9_3',
                      'Q9_9_16$4': 'Q9_9_4',
                      'Q9_9_16$5': 'Q9_9_5',
                      'Q9_9_16$6': 'Q9_9_6',
                      'Q9_9_16$7': 'Q9_9_7',
                      'Q9_9_16$8': 'Q9_9_8',
                      'Q9_9_16$9': 'Q9_9_9',
                      'Q2_6_1_M' : 'Q2_NBPERS_M_5A',
                      'Q2_6_1_F' : 'Q2_NBPERS_F_5A',
                      'Q2_6_2_M' : 'Q2_NBPERS_M_14A',
                      'Q2_6_2_F' : 'Q2_NBPERS_F_14A',
                      'Q2_6_3_M' : 'Q2_NBPERS_M_18A',
                      'Q2_6_3_F' : 'Q2_NBPERS_F_18A',
                      'Q2_6_4_M' : 'Q2_NBPERS_M_64A',
                      'Q2_6_4_F' : 'Q2_NBPERS_F_64A',
                      'Q2_6_5_M' : 'Q2_NBPERS_M_100A',
                      'Q2_6_5_F' : 'Q2_NBPERS_F_100A'
                      })

df9=df9.rename(columns = {'CODREG': 'CODREG',
                      'EXTRAPOL': 'EXTRAPOLATION',
                      'MILIEU': 'MILIEU',
                      'Q2_0B': 'Q2_NOM_CHEF',
                      'PONDERATION': 'PONDERATION',
                      'Q6_1A': 'Q6_1_A',
                      'Q6_1B': 'Q6_1_B',
                      'Q6_2A': 'Q6_2_A',
                      'Q6_2B': 'Q6_2_B',
                      'Q6_3A': 'Q6_3_A',
                      'Q6_3B': 'Q6_3_B',
                      'Q8_1A': 'Q8_1_1',
                      'Q8_1B': 'Q8_1_2',
                      'TAILMEN': 'TAILMENOLD',
                      'TAILMENAG': 'TAILMEN',
                      'STRATE': 'STRATES',
                      'Q2_6M1' : 'Q2_NBPERS_M_6M',
                      'Q2_6M2' : 'Q2_NBPERS_M_2A',
                      'Q2_6M3' : 'Q2_NBPERS_M_5A',
                      'Q2_6M4' : 'Q2_NBPERS_M_14A',
                      'Q2_6M5' : 'Q2_NBPERS_M_59A',
                      'Q2_6M6' : 'Q2_NBPERS_M_100A',
                      'Q2_6F1' : 'Q2_NBPERS_F_6M',
                      'Q2_6F2' : 'Q2_NBPERS_F_2A',
                      'Q2_6F3' : 'Q2_NBPERS_F_5A',
                      'Q2_6F4' : 'Q2_NBPERS_F_14A',
                      'Q2_6F5' : 'Q2_NBPERS_F_59A',
                      'Q2_6F6' : 'Q2_NBPERS_F_100A',
                      'PROD_LAIT13' : 'PROD_LAIT',
                      })

df11=df11.rename(columns = {'EXTRAPOL': 'EXTRAPOLATION',
                       'MILIEU': 'MILIEU',
                       'Q2_0B': 'Q2_NOM_CHEF',
                       'NOMVILL': 'NOMVILLAGE',
                       'PONDERATION': 'PONDERATION',
                       'Q6_1A': 'Q6_1_A',
                       'Q6_1B': 'Q6_1_B',
                       'Q6_2A': 'Q6_2_A',
                       'Q6_2B': 'Q6_2_B',
                       'Q6_3A': 'Q6_3_A',
                       'Q6_3B': 'Q6_3_B',
                       'Q8_1A': 'Q8_1_1',
                       'Q8_1B': 'Q8_1_2',
                       'Q7_2_1': 'Q7_21',
                       'Q7_2_2': 'Q7_22',
                       'Q7_2_3': 'Q7_23',
                       'TAILMEN': 'TAILMENOLD',
                       'TAILMENAG': 'TAILMEN',
                       'Q2_6M1' : 'Q2_NBPERS_M_6M',
                       'Q2_6M2' : 'Q2_NBPERS_M_2A',
                       'Q2_6M3' : 'Q2_NBPERS_M_5A',
                       'Q2_6M4' : 'Q2_NBPERS_M_14A',
                       'Q2_6M5' : 'Q2_NBPERS_M_59A',
                       'Q2_6M6' : 'Q2_NBPERS_M_100A',
                       'Q2_6F1' : 'Q2_NBPERS_F_6M',
                       'Q2_6F2' : 'Q2_NBPERS_F_2A',
                       'Q2_6F3' : 'Q2_NBPERS_F_5A',
                       'Q2_6F4' : 'Q2_NBPERS_F_14A',
                       'Q2_6F5' : 'Q2_NBPERS_F_59A',
                       'Q2_6F6' : 'Q2_NBPERS_F_100A',
                       'PROD_LAIT14' : 'PROD_LAIT',
                      })

df13=df13.rename(columns = {'WILAYA': 'CODREG', 
                       'COMMUNE': 'COMMUNE',
                       'EXTRAPOL': 'EXTRAPOLATION',
                       'MILIEU': 'MILIEU',
                       'Q2_0B1': 'Q2_NOM_CHEF',
                       'PONDERATIONS': 'PONDERATION',
                       'Q6_1A': 'Q6_1_A',
                       'Q6_1B': 'Q6_1_B',
                       'Q6_2A': 'Q6_2_A',
                       'Q6_2B': 'Q6_2_B',
                       'Q6_3A': 'Q6_3_A',
                       'Q6_3B': 'Q6_3_B',
                       'Q8_1A': 'Q8_1_1',
                       'Q8_1B': 'Q8_1_2',
                       'Q7_2A': 'Q7_21',
                       'Q7_2B': 'Q7_22',
                       'TAILMEN': 'TAILMENOLD',
                       'TAILMENAG': 'TAILMEN',
                       'STRATE': 'STRATES',
                       'Q2_6M1' : 'Q2_NBPERS_M_6M',
                       'Q2_6M2' : 'Q2_NBPERS_M_2A',
                       'Q2_6M3' : 'Q2_NBPERS_M_5A',
                       'Q2_6M4' : 'Q2_NBPERS_M_14A',
                       'Q2_6M5' : 'Q2_NBPERS_M_59A',
                       'Q2_6M6' : 'Q2_NBPERS_M_100A',
                       'Q2_6F1' : 'Q2_NBPERS_F_6M',
                       'Q2_6F2' : 'Q2_NBPERS_F_2A',
                       'Q2_6F3' : 'Q2_NBPERS_F_5A',
                       'Q2_6F4' : 'Q2_NBPERS_F_14A',
                       'Q2_6F5' : 'Q2_NBPERS_F_59A',
                       'Q2_6F6' : 'Q2_NBPERS_F_100A',
                       'PROD_LAIT14' : 'PROD_LAIT',
                      })



df4["HORS_NK"]=df4["HORS_NK"]-1.0
df4["Q7_1"]=df4["Q7_1"]-1.0
df4["Q11_1"]=df4["Q11_1"]-1.0
df4["Q11_2"]=df4["Q11_2"]-1.0
df4["Q11_3"]=df4["Q11_3"]-1.0
df4["Q11_4"]=df4["Q11_4"]-1.0
df4["Q11_5"]=df4["Q11_5"]-1.0
df4["Q11_7"]=df4["Q11_7"]-1.0
df4["Q11_8"]=df4["Q11_8"]-1.0
df4["Q11_10"]=df4["Q11_10"]-1.0
df4["Q11_11"]=df4["Q11_11"]-1.0

df4["TEMP"]=df4["Q2_2"]
df4["Q2_2"]=df4["Q2_1"]
df4["Q2_1"]=df4["TEMP"]

df4["Q11_12"]=df4["Q11_6"]

df4["TEMP"]=df4["PER.SOURCE8"]
df4["PER.SOURCE8"]=df4["PER.SOURCE9"]
df4["PER.SOURCE9"]=df4["TEMP"]
df4=df4.drop(["TEMP"],axis=1)

df7["TEMP"]=df7["Q2_2"]
df7["Q2_2"]=df7["Q2_1"]
df7["Q2_1"]=df7["TEMP"]

df7["TEMP"]=df7["PER.SOURCE8"]
df7["PER.SOURCE8"]=df7["PER.SOURCE9"]
df7["PER.SOURCE9"]=df7["TEMP"]
df7=df7.drop(["TEMP"],axis=1)

############################################################################
# Rassemblement des données des questionnaires (df)
df_final = pd.concat([df4,df7],ignore_index=True)
df_final = pd.concat([df_final,df9],ignore_index=True)
df_final = pd.concat([df_final,df11],ignore_index=True)
df_final = pd.concat([df_final,df13],ignore_index=True)

############################################################################
# Suppression des doublons
df_final.drop_duplicates(keep = 'first', inplace=True)

############################################################################
# Creation variable binaire sur le score alimentaire
df_final['FCS_BIN']=0
a=df_final.columns
df_final.loc[df_final.loc[:,'FCS']<=42,'FCS_BIN']= 1 

# Tx IA : (nombre de ménage avec SCA < 42) / (nombre de ménages de ladite localité)

############################################################################
# Ajout Latitude et longitude par MOUGHATAA sur toute la base

df_final['Lat_MOUGHATAA']=df_final['MOUGHATAA']
df_final['Long_MOUGHATAA']=df_final['MOUGHATAA']

dict_Lat_MOUGHATAA = {11.0: 16.2784747, 12.0: 15.8649341, 13.0: 15.7334621, 14.0: 16.6173344, 15.0: 17.3003756, 16.0: 18.16667, 21.0: 18.1010141, 22.0: 15.820043163754445, 23.0: 17.2451191, 24.0: 16.3954331, 31.0: 16.57271918625387, 32.0: 17.4454, 33.0: 16.8300923, 34.0: 15.9367211, 35.0: 16.6161559, 41.0: 16.1523684, 42.0: 15.5101724, 43.0: 16.0230248, 44.0: 16.4105634, 51.0: 17.0527177, 52.0: 16.3406075, 53.0: 16.5955353, 54.0: 17.71474532958353, 55.0: 16.1483748, 61.0: 17.5469954, 62.0: 16.5549676, 63.0: 16.9199893, 64.0: 17.9659462, 65.0: 16.920138, 66.0: 16.5132493, 71.0: 20.02785066600362, 72.0: 20.5182772, 73.0: 18.1073999, 74.0: 20.9335051, 81.0: 20.9131304, 91.0: 17.880401, 92.0: 18.444062, 93.0: 18.552316245823086, 101.0: 15.5435752, 102.0: 15.160547052532939, 111.0: np.nan, 112.0: 22.681150865092736, 113.0: 17.733, 121.0: 19.7435804, 131.0: 17.4926764, 132.0: 18.1207086, 133.0: 18.0649782, 134.0: 18.1049033, 135.0: 18.0029056, 136.0: 18.0711667, 137.0: 18.1111443, 138.0: 18.1240121, 139.0: 18.0724322}
dict_Long_MOUGHATAA = {11.0: -6.9895153, 12.0: -5.9488454, 13.0: -8.6657412, 14.0: -7.2663798, 15.0: -7.0254543, 16.0: -7.08333, 21.0: -15.9729818, 22.0: -9.414215664739915, 23.0: -10.6701655, 24.0: -10.1673276, 31.0: -11.651110675690276, 32.0: -11.3434, 33.0: -11.8387565, 34.0: -11.5191388, 35.0: -11.4002038, 41.0: -13.5039868, 42.0: -12.8502902, 43.0: -12.5785386, 44.0: -13.1359578, 51.0: -13.9152949, 52.0: -13.948088, 53.0: -14.2603202, 54.0: -12.962646152213226, 55.0: -13.7871497, 61.0: -14.697356, 62.0: -16.2353267, 63.0: -15.6601304, 64.0: -15.5187897, 65.0: -15.2355732, 66.0: -15.8099665, 71.0: -13.053667566088915, 72.0: -13.0543754, 73.0: -15.9726236, 74.0: -11.6170162, 81.0: -17.0501015, 91.0: -12.3324205, 92.0: -9.493115, 93.0: -11.429009475696759, 101.0: -11.7128739, 102.0: -12.188004896904182, 111.0: np.nan, 112.0: -12.713432427270869, 113.0: -13.8496, 121.0: -14.3855238, 131.0: -14.555831, 132.0: -15.9214875, 133.0: -15.9770728, 134.0: -15.9644337, 135.0: -15.9728613, 136.0: -16.0026068, 137.0: -16.0038402, 138.0: -15.940133, 139.0: -15.9099003}

df_final.loc[:,'Lat_MOUGHATAA'] = df_final['Lat_MOUGHATAA'].map(dict_Lat_MOUGHATAA)
df_final.loc[:,'Long_MOUGHATAA'] = df_final['Long_MOUGHATAA'].map(dict_Long_MOUGHATAA)

############################################################################
# Suppression de colonnes
List_drop=['OPERAT','CP','NUMEN','DATE_JOUR','DATE_MOIS','DATE_ANN_E','CODE_ENQ','CODE_CONT','AG_SAISIE','JOUR_SAISIE','MOIS_SAISIE','ANNEE_SAISIE','OBSERV$1','OBSERV$2','OBSERV$3','OBSERV$4','TAIL_CALC','TXDEP','Q3_1','Q3_2','Q3_3','Q3_4','Q3_5','Q3_6','Q3_7','Q3_8','Q3_9','Q3_10','Q3_11','Q3_12','Q3_13','Q3_14','Q3_15','PROD_LAIT1','VENT_LAIT1','PRODAGRI','VERIF','PRODUITS$01','PRODUITS$02','PRODUITS$03','PRODUITS$04','PRODUITS$05','PRODUITS$06','PRODUITS$07','PRODUITS$08','PRODUITS$09','PRODUITS$10','PRODUITS$11','PRODUITS$12','PRODUITS$13','PRODUITS$14','PRODUITS$15','NBCONSO$01','NBCONSO$02','NBCONSO$03','NBCONSO$04','NBCONSO$05','NBCONSO$06','NBCONSO$07','NBCONSO$08','NBCONSO$09','NBCONSO$10','NBCONSO$11','NBCONSO$12','NBCONSO$13','NBCONSO$14','NBCONSO$15','ACQUISIT$01','ACQUISIT$02','ACQUISIT$03','ACQUISIT$04','ACQUISIT$05','ACQUISIT$06','ACQUISIT$07','ACQUISIT$08','ACQUISIT$09','ACQUISIT$10','ACQUISIT$11','ACQUISIT$12','ACQUISIT$13','ACQUISIT$14','ACQUISIT$15','Q11_12','Q11_13','Q11_14','DATSAISIE','HDEB','HFIN','FAC1_1','FAC2_1','NFAC1_1','FAC1_2','FAC2_2','FAC3_2','NTI001','FAC1_3','FAC2_3','NTI002','FAC1_4','FAC2_4','NTI003','BLE_SR1','BLE_SR2','BLE_SR3','BLE_SR4','BLE_SR5','BLE_SR6','BLE_SR7','BLE_SR8','BLE_SR9','BLE_SR10','RIZ_SR1','RIZ_SR2','RIZ_SR3','RIZ_SR4','RIZ_SR5','RIZ_SR6','RIZ_SR7','RIZ_SR8','RIZ_SR9','RIZ_SR10','MIL_SR1','MIL_SR2','MIL_SR3','MIL_SR4','MIL_SR5','MIL_SR6','MIL_SR7','MIL_SR8','MIL_SR9','MIL_SR10','PATES_SR1','PATES_SR2','PATES_SR3','PATES_SR4','PATES_SR5','PATES_SR6','PATES_SR7','PATES_SR8','PATES_SR9','PATES_SR10','PAIN_SR1','PAIN_SR2','PAIN_SR3','PAIN_SR4','PAIN_SR5','PAIN_SR6','PAIN_SR7','PAIN_SR8','PAIN_SR9','PAIN_SR10','TUBERCULES_SR1','TUBERCULES_SR2','TUBERCULES_SR3','TUBERCULES_SR4','TUBERCULES_SR5','TUBERCULES_SR6','TUBERCULES_SR7','TUBERCULES_SR8','TUBERCULES_SR9','TUBERCULES_SR10','LEGUMINEUSES_SR1','LEGUMINEUSES_SR2','LEGUMINEUSES_SR3','LEGUMINEUSES_SR4','LEGUMINEUSES_SR5','LEGUMINEUSES_SR6','LEGUMINEUSES_SR7','LEGUMINEUSES_SR8','LEGUMINEUSES_SR9','LEGUMINEUSES_SR10','LEGUMES_SR1','LEGUMES_SR2','LEGUMES_SR3','LEGUMES_SR4','LEGUMES_SR5','LEGUMES_SR6','LEGUMES_SR7','LEGUMES_SR8','LEGUMES_SR9','LEGUMES_SR10','FRUITS_SR1','FRUITS_SR2','FRUITS_SR3','FRUITS_SR4','FRUITS_SR5','FRUITS_SR6','FRUITS_SR7','FRUITS_SR8','FRUITS_SR9','FRUITS_SR10','VIANDE_SR1','VIANDE_SR2','VIANDE_SR3','VIANDE_SR4','VIANDE_SR5','VIANDE_SR6','VIANDE_SR7','VIANDE_SR8','VIANDE_SR9','VIANDE_SR10','POISSON_SR1','POISSON_SR2','POISSON_SR3','POISSON_SR4','POISSON_SR5','POISSON_SR6','POISSON_SR7','POISSON_SR8','POISSON_SR9','POISSON_SR10','LAITIERS_SR1','LAITIERS_SR2','LAITIERS_SR3','LAITIERS_SR4','LAITIERS_SR5','LAITIERS_SR6','LAITIERS_SR7','LAITIERS_SR8','LAITIERS_SR9','LAITIERS_SR10','SUCRE_SR1','SUCRE_SR2','SUCRE_SR3','SUCRE_SR4','SUCRE_SR5','SUCRE_SR6','SUCRE_SR7','SUCRE_SR8','SUCRE_SR9','SUCRE_SR10','HUILE_SR1','HUILE_SR2','HUILE_SR3','HUILE_SR4','HUILE_SR5','HUILE_SR6','HUILE_SR7','HUILE_SR8','HUILE_SR9','HUILE_SR10','CONDIMENTS_SR1','CONDIMENTS_SR2','CONDIMENTS_SR3','CONDIMENTS_SR4','CONDIMENTS_SR5','CONDIMENTS_SR6','CONDIMENTS_SR7','CONDIMENTS_SR8','CONDIMENTS_SR9','CONDIMENTS_SR10','SOURCE1','SOURCE2','SOURCE3','SOURCE4','SOURCE5','SOURCE6','SOURCE7','SOURCE8','SOURCE9','SOURCE10','PER.SOURCE10','ID02','RECODR','NUMORD','CLUSTER','SAISIE','CLUSTER2','SELECT','NUMDR','COLDATE','DATECOL','CODE_CE','DATE','OBS$1','OBS$2','OBS$3','Q4_9','Q4_10','Q6_5$1','Q6_5$2','Q6_5$3','Q7_2$1','Q7_2$2','Q8_17','Q8_18OT$1','Q8_18OT$2','Q8_18OT$3','Q8_18$1','Q8_18$2','Q8_18$3','Q8_19$1','Q8_19$2','PRODUITS$16','NBCONSO$16','ACQUISIT$16','DATCOL','EVO_BOV','EVO_OV','EVO_CAP','EVO_CAM','FILTER_$','SUM_CEREALES1','ACT1_A1','ACT1_A2','ACT1_A3','ACT1_A4','ACT1_A5','ACT1_A6','ACT1_A7','ACT1_A8','ACT1_A9','ACT1_A10','ACT1_A11','ACT1_A12','ACT1_A13','ACT1_A14','ACT1_A15','ACT1_A16','ACT1_A17','ACT1_A18','ACT1_A19','ACT1_A20','ACT1_A21','ACT1_A22','ACT1_A23','ACT1_A24','ACT1_A25','ACT1_A26','ACT2_A1','ACT2_A2','ACT2_A3','ACT2_A4','ACT2_A5','ACT2_A6','ACT2_A7','ACT2_A8','ACT2_A9','ACT2_A10','ACT2_A11','ACT2_A12','ACT2_A13','ACT2_A14','ACT2_A15','ACT2_A16','ACT2_A17','ACT2_A18','ACT2_A19','ACT2_A20','ACT2_A21','ACT2_A22','ACT2_A23','ACT2_A24','ACT2_A25','ACT2_A26','ACT3_A1','ACT3_A2','ACT3_A3','ACT3_A4','ACT3_A5','ACT3_A6','ACT3_A7','ACT3_A8','ACT3_A9','ACT3_A10','ACT3_A11','ACT3_A12','ACT3_A13','ACT3_A14','ACT3_A15','ACT3_A16','ACT3_A17','ACT3_A18','ACT3_A19','ACT3_A20','ACT3_A21','ACT3_A22','ACT3_A23','ACT3_A24','ACT3_A25','ACT3_A26','ACTOT1A','ACTOT2A','ACTOT3A','ACTOT4A','ACTOT5A','ACTOT6A','ACTOT7','ACTOT8A','ACTOT9A','ACTOT10A','ACTOT11A','ACTOT12A','ACTOT13A','ACTOT14A','ACTOT15','ACTOT16A','ACTOT17A','ACTOT18A','ACTOT19A','ACTOT20A','ACTOT21A','ACTOT22A','ACTOT23A','ACTOT24A','ACTOT25','ACTOT26A','ACTIVITE1','ACTIVITE2','ACTIVITE3','ACTIVITE4','ACTIVITE5','ACTIVITE6','ACTIVITE7','ACTIVITE8','ACTIVITE9','ACTIVITE10','ACTIVITE11','NCSI','COND_SR1','COND_SR2','COND_SR3','COND_SR4','COND_SR5','COND_SR6','COND_SR7','COND_SR8','COND_SR9','COND_SR10','OTH_SR1','OTH_SR2','OTH_SR3','OTH_SR4','OTH_SR5','OTH_SR6','OTH_SR7','OTH_SR8','OTH_SR9','OTH_SR10','SECTION1','NORDRE','TODAY','SUBMISSIONDATE','SUBSCRIBERID','CODEKIP','ACCORD','SECTION2','SECTION4','VARIZ1','VARIZ2','VARIZ3','VARIZ4','SECTION5','Q5_0C','VERIF2','VERIF3','VERIF4','VERIF5','VERIF6','Q5_6','Q5_7','SECTION6','Q6_5','SECTION7','SECTION8','VER_ADBASE1','VER_ADBASE2','VER_PULSES','VER_LEGUMES','VER_FRUIT','VER_PROTSMALL_N','VER_PROTSMALL','S_VIAND_POISS_N','D_VIAND_POISS_N','VER_VIANDPOISS_N','VER_VIANDPOISS','SMALLAI_N','S_SMALLAI_N','VER_SMALLAI_N','VER_SMALLAI','D_LAITIERS_N','VER_LAITIERS_N','VER_LAITIERS','VER_SUCRE','VER_HUILE','VER_OTHER','SECTION9','CHOCS1GENERATED_TABLE_LIST_LABEL_301','CHOCS1RESERVED_NAME_FOR_FIELD_LIST_LABELS_302','CHOCS2GENERATED_TABLE_LIST_LABEL_311','CHOCS2RESERVED_NAME_FOR_FIELD_LIST_LABELS_312','SECTION10','STRATEG1GENERATED_TABLE_LIST_LABEL_322','STRATNAL1GENERATED_TABLE_LIST_LABEL_329','STRATNAL1RESERVED_NAME_FOR_FIELD_LIST_LABELS_330','STRATNAL2GENERATED_TABLE_LIST_LABEL_340','STRATNAL2RESERVED_NAME_FOR_FIELD_LIST_LABELS_341','CSI_BRUT','SECTION11','Q11AGENERATED_TABLE_LIST_LABEL_353','Q11ARESERVED_NAME_FOR_FIELD_LIST_LABELS_354','Q11BGENERATED_TABLE_LIST_LABEL_361','Q11BRESERVED_NAME_FOR_FIELD_LIST_LABELS_362','METAINSTANCEID','KEY','Q6_51','Q6_52','Q6_53','TXDEP1','TXDEP2','MIGRATOR','PROD_LAIT13A','TAUXACTIV1','TAUXACTIV2','DIV_CEREAL','DIV_TUBER','DIV_LEGUMINEUSE','DIV_VEGETABLE','DIV_FRUITS','DIV_VIANDE_POISSON','DIV_LAIT','DIV_HUILE','DIV_SUCRE','DIV_CONDIMENT','COPING7','COPING8','COPING9','COPING10','COPING11','COPING12','COPING13','COPING14','COPING15','COPING16','COPING17','COPING18','COPING19','COPING20','COPING21','COPING22','COPING23','COPING24','CLASS_PCDEPALIM','COPING_CAPA','CLASS_FS','FS_CLASSIF','FRUITS1','LEGUMES1','HUILE1','SUCRE1','ADBASE1_SR1','ADBASE1_SR2','ADBASE1_SR3','ADBASE1_SR4','ADBASE1_SR5','ADBASE1_SR6','ADBASE1_SR7','ADBASE1_SR8','ADBASE1_SR9','ADBASE2_SR1','ADBASE2_SR2','ADBASE2_SR3','ADBASE2_SR4','ADBASE2_SR5','ADBASE2_SR6','ADBASE2_SR7','ADBASE2_SR8','ADBASE2_SR9','PULSES_SR1','PULSES_SR2','PULSES_SR3','PULSES_SR4','PULSES_SR5','PULSES_SR6','PULSES_SR7','PULSES_SR8','PULSES_SR9','PROTEISMALL_SR1','PROTEISMALL_SR2','PROTEISMALL_SR3','PROTEISMALL_SR4','PROTEISMALL_SR5','PROTEISMALL_SR6','PROTEISMALL_SR7','PROTEISMALL_SR8','PROTEISMALL_SR9','VIAND_POISS_SR1','VIAND_POISS_SR2','VIAND_POISS_SR3','VIAND_POISS_SR4','VIAND_POISS_SR5','VIAND_POISS_SR6','VIAND_POISS_SR7','VIAND_POISS_SR8','VIAND_POISS_SR9','SMALLAI_SR1','SMALLAI_SR2','SMALLAI_SR3','SMALLAI_SR4','SMALLAI_SR5','SMALLAI_SR6','SMALLAI_SR7','SMALLAI_SR8','SMALLAI_SR9','OTHER_SR1','OTHER_SR2','OTHER_SR3','OTHER_SR4','OTHER_SR5','OTHER_SR6','OTHER_SR7','OTHER_SR8','OTHER_SR9','HNO','PRGNUT','START','END','DEVICEID','FSMS_JUIN14','INTRO','ENDINTER','ZD','FID_LZ2013','LZCODE','ALHZ','LHZA','LHZ2','ENKET','INTRO8','CHOCS1GENERATED_TABLE_LIST_LABEL_307','CHOCS1RESERVED_NAME_FOR_FIELD_LIST_LABELS_308','CHOCS2GENERATED_TABLE_LIST_LABEL_317','CHOCS2RESERVED_NAME_FOR_FIELD_LIST_LABELS_318','INTRO9','STRATEG1GENERATED_TABLE_LIST_LABEL_330','STRATNAL1GENERATED_TABLE_LIST_LABEL_337','STRATNAL1RESERVED_NAME_FOR_FIELD_LIST_LABELS_338','Q11AGENERATED_TABLE_LIST_LABEL_361','Q11ARESERVED_NAME_FOR_FIELD_LIST_LABELS_362','PROD_LAIT14A','VENT_LAIT14','ACTOT1','ACTOT2','ACTOT3','ACTOT4','ACTOT5','ACTOT6','ACTOT8','ACTOT9','ACTOT10','ACTOT11','ACTOT12','ACTOT13','ACTOT14','ACTOT16','NTI004','NTI005','NTI006','VULNECO','NTI007','NORDO','DUREE','DUREE2','FSMS_MAI15','Q5_0B1','Q6_5A','Q6_5B','Q6_6C','Q7_17','SECTION8BIS','FIES1','FIES2','FIES3','FIES4','FIES5','FIES6','FIES7','FIES7A','FIES8','FIES8A','SECTIONXX','CSI_HNO','CSI_HNO1']
df_final=df_final.drop(List_drop,axis=1)



############################################################################
# Ajout Lat Long Gpe3

df_lat_long = pd.read_csv("C:/0 - Data/standardized_aggregated_dataset.csv")
df_lat_long["latlong_id"]=df_lat_long["numquest"].astype(str)+df_lat_long["ident"].astype(str)+df_lat_long["year"].astype(str)+df_lat_long["month"].astype(str)+df_lat_long["commune"]

df_lat_long=df_lat_long[['latlong_id','latitude','longitude','numquest','year','month']]
df_lat_long=df_lat_long.rename(columns = {'latitude': 'Lat_Gpe3', 'longitude': 'Long_Gpe3'})

df_final["latlong_id"]=df_final["NUMQUEST"].astype(str)+df_final["IDENT"].astype(str)+df_final["YEAR"].astype(str)+df_final["MONTH"].astype(str)+df_final["COMMUNE"].astype(str)

df_final = pd.merge(df_final, df_lat_long, how="left", on=["latlong_id"])

'''
temp = pd.merge(df_lat_long, df_final, how="left", on=["latlong_id"])
temp=temp[temp.PONDERATION.isna()]
temp=temp[temp.month_x=="Juin"]

temp=temp[temp.month_x=="Juin"]
'''

# Calcul des valeurs manquantes
Liste=['YEAR','LATITUDE','LONGITUDE','Lat_Gpe3','Long_Gpe3','Lat_MOUGHATAA','Long_MOUGHATAA']
temp = df_final[Liste].set_index('YEAR').isna().sum(level=0)

############################################################################
# Ajout Latitude et longitude de la MOUGHATAA pour les questionnaires q4 et q7 sans lat ni long

df_final.loc[df_final.loc[:,'QUEST']=="Q4",'LATITUDE']= df_final['Lat_Gpe3']
df_final.loc[df_final.loc[:,'QUEST']=="Q4",'LONGITUDE']= df_final['Long_Gpe3']

df_final.loc[df_final.loc[:,'QUEST']=="Q7",'LATITUDE']= df_final['Lat_Gpe3']
df_final.loc[df_final.loc[:,'QUEST']=="Q7",'LONGITUDE']= df_final['Long_Gpe3']

############################################################################
# Suppression de colonnes
List_drop=['Lat_Gpe3','Long_Gpe3']
df_final=df_final.drop(List_drop,axis=1)

############################################################################
# Creation tables finales
df_analyse=df_final[df_final.LATITUDE.notna()]
df_moughataa=df_final[df_final.Lat_MOUGHATAA.notna()]

############################################################################
# Export des données en csv
questtot.to_csv('C:/0 - Data/EntetesQuest.csv', sep = ';')
df_analyse.to_csv('C:/0 - Data/df_analyse_sav.csv', sep = ';')
df_moughataa.to_csv('C:/0 - Data/df_moughataa_sav.csv', sep = ';')

'''



a=df_lat_long[['year','month']].value_counts()



temp=df4.NUMEN.value_counts
temp=df4.loc[df4['NUMQUEST']==607.0]

a=df4.groupby(by=['NUMEN']).count()



df_analyse=df_analyse[['FCS','FCS_BIN','LATITUDE','LONGITUDE','IDENT','NOMVILLAGE','CODREG',
                      'MOUGHATAA','COMMUNE','FICHIER','QUEST','NUMQUEST','Q5_0A']]

df_analyse=df_final[['Lat_MOUGHATAA','Long_MOUGHATAA','MOUGHATAA','FICHIER']]
df_analyse=df_final[df_final.Lat_MOUGHATAA.isna()]
a=df_final[['CODREG','MOUGHATAA']].value_counts() 
df_analyse=df_analyse[['Lat_MOUGHATAA','Long_MOUGHATAA','MOUGHATAA','FICHIER']]

liste=[203108.0,31113.0,100101.0,100114.0,100103.0,203613.0,100115.0,203614.0,
      203601.0,10610.0,100113.0,203605.0,31103.0,31105.0,203612.0,100102.0,31008.0,
      203606.0,203611.0,10604.0,203615.0,31104.0,203602.0,31101.0,31109.0,203607.0,
      31107.0,31111.0,203608.0,203603.0,31106.0,31110.0]

a=df_analyse.loc[df_analyse.NUMQUEST.isin(liste),:]
a=a[['FCS','FCS_BIN','LATITUDE','LONGITUDE','IDENT','NOMVILLAGE','CODREG',
                      'MOUGHATAA','COMMUNE','FICHIER','QUEST','Long_MOUGHATAA','Lat_MOUGHATAA']]
liste=[203108.0,31113.0,100101.0,100114.0,100103.0,203613.0,100115.0,203614.0,
      203601.0,10610.0,100113.0,203605.0,31103.0,31105.0,203612.0,100102.0,31008.0,
      203606.0,203611.0,10604.0,203615.0,31104.0,203602.0,31101.0,31109.0,203607.0,
      31107.0,31111.0,203608.0,203603.0,31106.0,31110.0]

a=df13.loc[df13.NUMQUEST.isin(liste),:]
a=a[['LATITUDE','LONGITUDE']]


'''





