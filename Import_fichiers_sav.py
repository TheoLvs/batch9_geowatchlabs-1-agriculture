###########################################################################
# Librairies
import pandas as pd
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

df7=df7.rename(columns = {'WILAYA': 'CODREG', 
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

df_final['FCS_BIN']=0
a=df_final.columns
df_final.loc[df_final.loc[:,'FCS']<=42,'FCS_BIN']= 1 


# Tx IA : (nombre de ménage avec SCA < 42) / (nombre de ménages de ladite localité)

############################################################################
# Export des données en csv
df_final.to_csv('C:/0 - Data/DataEnquetes.csv', sep = ';')
questtot.to_csv('C:/0 - Data/EntetesQuest.csv', sep = ';')

############################################################################
# Selection de colonnes
df_analyse=df_final[df_final.LATITUDE.notna()]
df_analyse=df_analyse[['FCS','FCS_BIN','LATITUDE','LONGITUDE','IDENT','NOMVILLAGE','CODREG',
                      'MOUGHATAA','COMMUNE','FICHIER','QUEST','NUMQUEST','Q5_0A']]


'''
List_drop=['OPERAT','QUEST','IDENT','NUMEN','DATE_JOUR','DATE_MOIS','DATE_ANN_E',
           'CODE_ENQ','CODE_CONT','AG_SAISIE','JOUR_SAISIE','MOIS_SAISIE','ANNEE_SAISIE',
           'Q3_1','Q3_2','Q3_3','Q3_4','Q3_5','Q3_6','Q3_7','Q3_8','Q3_9','Q3_10','Q3_11',
           'Q3_12','Q3_13','Q3_14','Q3_15','Q11_12','Q11_13','Q11_14','FAC1_1','FAC2_1',
           'NFAC1_1','FAC1_2','FAC2_2','FAC3_2','NTI001','FAC1_3','FAC2_3','NTI002','FAC1_4',
           'FAC2_4','NTI003','PER.SOURCE10','ID01','ID02','CLUSTER','SAISIE','CLUSTER2','SELECT',
           'NUMDR','CODE_CE','EVO_BOV','EVO_OV','EVO_CAP','EVO_CAM','FILTER_$','SUM_SORG',
           'SUM_CEREALES1','SECTION1','NORDRE','SUBSCRIBERID','CODEKIP','SECTION2','SECTION4',
           'VARIZ1','VARIZ2','VARIZ3','VARIZ4','SECTION5','Q5_0C','VERIF2','VERIF3','VERIF4',
           'VERIF5','VERIF6','Q5_6','Q5_7','SECTION6','SECTION7','SECTION8','VER_ADBASE1',
           'VER_ADBASE2','VER_PULSES','VER_LEGUMES','VER_FRUIT','VER_PROTSMALL_N','VER_PROTSMALL',
           'VER_VIANDPOISS_N','VER_VIANDPOISS','VER_SMALLAI_N','VER_SMALLAI','VER_LAITIERS_N',
           'VER_LAITIERS','VER_SUCRE','VER_HUILE','VER_OTHER','SECTION9',
           'CHOCS1GENERATED_TABLE_LIST_LABEL_301','CHOCS1RESERVED_NAME_FOR_FIELD_LIST_LABELS_302',
           'CHOCS2GENERATED_TABLE_LIST_LABEL_311','CHOCS2RESERVED_NAME_FOR_FIELD_LIST_LABELS_312',
           'SECTION10','STRATEG1GENERATED_TABLE_LIST_LABEL_322','STRATNAL1GENERATED_TABLE_LIST_LABEL_329',
           'STRATNAL1RESERVED_NAME_FOR_FIELD_LIST_LABELS_330','STRATNAL2GENERATED_TABLE_LIST_LABEL_340',
           'STRATNAL2RESERVED_NAME_FOR_FIELD_LIST_LABELS_341','SECTION11',
           'Q11AGENERATED_TABLE_LIST_LABEL_353','Q11ARESERVED_NAME_FOR_FIELD_LIST_LABELS_354',
           'Q11BGENERATED_TABLE_LIST_LABEL_361','Q11BRESERVED_NAME_FOR_FIELD_LIST_LABELS_362',
           'KEY','COPING7','COPING8','COPING9','COPING10','COPING11','COPING12','COPING13','COPING14',
           'COPING15','COPING16','COPING17','COPING18','COPING19','COPING20','COPING21','COPING22',
           'COPING23','COPING24','COPING_STRATEGY','CLASS_PCDEPALIM','COPING_CAPA','CLASS_FS','FS_CLASSIF',
           'DEVICEID','FSMS_JUIN14','STRATEG1GENERATED_TABLE_LIST_LABEL_330',
           'STRATNAL1GENERATED_TABLE_LIST_LABEL_337','STRATNAL1RESERVED_NAME_FOR_FIELD_LIST_LABELS_338',
           'Q11AGENERATED_TABLE_LIST_LABEL_361','Q11ARESERVED_NAME_FOR_FIELD_LIST_LABELS_362','Q5_0B1',
           'Q7_17','SECTION8BIS','SECTIONXX']
df_final=df_final.drop(List_drop,axis=1)
'''





