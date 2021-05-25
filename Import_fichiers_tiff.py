###########################################################################
# Ce que fait ce programme
# Importe les fichiers cartes (Crop Mask + Hist Yield) dans des listes
# Croise les cartes avec les données ménages pour ajouter le rendement pour chaque ménage
###########################################################################
# Librairies

import os
os.chdir(r'C:\Users\lebce\OneDrive\Documents\DataForGood')
print(os.getcwd())

import Import_fichiers_sav as fs
import pandas as pd
#import unicodedata
import geopandas as gpd                 
import rasterio
from rasterio.plot import show
from rasterio.merge import merge
import numpy as np
import scipy.special
import gdal                            
import matplotlib.cm
import folium                           
from folium import plugins
from math import sqrt
import copy

###########################################################################
# Fonctions

def Calcul_Rend(nbPixels,matrice,row,col,df,max_row,max_col) :
    seq = [t for t in range(-nbPixels,nbPixels+1,1)]
    rent_list_def = [0 for k in df.index]
    for ligne in seq :  
        for colonne in seq : 
            #print("ligne :" + str(ligne))
            #print("colonne :" + str(colonne))
            row2=row+ligne
            col2=col+colonne
            
            #Recode les valeurs abérrantes
            row2[row2<0]=0
            row2[row2>=max_row]=max_row-1
            
            col2[col2<0]=0
            col2[col2>=max_col]=max_col-1

            coords_list_def = [(row2[k], col2[k]) for k in df.index]
            rent_list_temp = [matrice[0][coords] for coords in coords_list_def]
            rent_list_def = [rent_list_def[i]+rent_list_temp[i] for i in range(len(rent_list_def))]
    return rent_list_def

###########################################################################
# Import des fichiers : Crop Mask + Hist Yield

monRep=r'C:\0 - Data\fusion\Crop masks'
liCropMask = []
liCropMask_np = []
for path, subdirs, files in os.walk(monRep):
    for name in files:
        #print(os.path.join(path, name))
        fileExtension=name[len(name)-4:len(name)]
        if fileExtension==".tif" : 
            #print(os.path.join(path, name))
            rast_rend = rasterio.open(os.path.join(path, name))
            annee=name[0:4]
            temp=name[name.find('_')+1:len(name)]
            prod=name[name.find('_')+1:len(temp)-2]
            liCropMask.append([annee,prod,path,name,rast_rend,rast_rend.height,rast_rend.width])
            liCropMask_np.append([rast_rend.read(1)])

monRep=r'C:\0 - Data\fusion\Historical Yields'
liHistYield = []
liHistYield_np = []
for path, subdirs, files in os.walk(monRep):
    for name in files:
        #print(os.path.join(path, name))
        fileExtension=name[len(name)-4:len(name)]
        if fileExtension==".tif" : 
            #print(os.path.join(path, name))
            rast_rend = rasterio.open(os.path.join(path, name))
            annee=name[0:4]
            temp=name[name.find('_')+1:len(name)]
            prod=name[name.find('_')+1:len(temp)-2]
            liHistYield.append([annee,prod,path,name,rast_rend,rast_rend.height,rast_rend.width])
            liHistYield_np.append([rast_rend.read(1)])
            
# nettoyage
del monRep ,rast_rend,path, subdirs, files,fileExtension, name, annee, temp,prod


# transformation des cartes en DF / listes utilisées dans la suite du programme
List_drop=['path','rast_rend']
df_HistYield = pd.DataFrame(liHistYield,columns=["annee","prod","path","name","rast_rend","height","width"])
df_HistYield=df_HistYield.drop(List_drop,axis=1)
list_annee_HY=list(df_HistYield['annee'].unique())
list_prod_HY=list(df_HistYield['prod'].unique())
list_name_HY=list(df_HistYield['name'].unique())
df_HistYield["CATE"]=df_HistYield["annee"].astype(str)+"_"+df_HistYield["prod"]

# nettoyage
del List_drop

###########################################################################
# remplacer par 0

for i in range(len(liHistYield_np)) : 
    a = np.min(liHistYield_np[i][0])
    mask = (liHistYield_np[i][0] == a)
    liHistYield_np[i][0][mask] = 0

del a, mask, i

for i in range(len(liCropMask_np)) : 
    a = np.min(liCropMask_np[i][0])
    mask = (liCropMask_np[i][0] == a)
    liCropMask_np[i][0][mask] = 0

del a, mask, i

###########################################################################
# traitement des ratios (crop mask) et des rendements (hist yield)

liHYCM = liHistYield.copy()
liHYCM_np = copy.deepcopy(liHistYield_np)
for i in range(len(liCropMask_np)) : 
    liHYCM_np[i][0] = liCropMask_np[i][0]*250*250/10000*liHistYield_np[i][0]



#Test :
#liCropMask_np[4][0][(310, 1700)]
#liHistYield_np[4][0][(310, 1700)]
#liHYCM_np[4][0][(310, 1700)]

###########################################################################
# chargement de la base des ménages : 

#liste=[203108.0,31113.0,100101.0,100114.0,100103.0,203613.0,100115.0,203614.0,
#      203601.0,10610.0,100113.0,203605.0,31103.0,31105.0,203612.0,100102.0,31008.0,
#      203606.0,203611.0,10604.0,203615.0,31104.0,203602.0,31101.0,31109.0,203607.0,
#      31107.0,31111.0,203608.0,203603.0,31106.0,31110.0]

#df_analyse=fs.df_analyse.loc[fs.df_analyse.NUMQUEST.isin(liste),:]

df_analyse=fs.df_analyse
df_moughataa=fs.df_moughataa

###########################################################################
# calcul des rendements par annee et prod pour chaque ménage 

def Calcul_Rend_df(df_analyse,LATITUDE,LONGITUDE,pixel) :
    # Nb pixels autour du menage
    for i in range(len(liHYCM)) :
        temp=liHYCM[i][0]+"_"+liHYCM[i][1] # annee + prod + zone
        df_analyse["HY_row_"+temp],df_analyse["HY_col_"+temp] = liHYCM[0][4].index(pd.to_numeric(df_analyse[LONGITUDE], errors='coerce'), 
                                  pd.to_numeric(df_analyse[LATITUDE], errors='coerce'))
        max_row=liHYCM[i][5]
        max_col=liHYCM[i][6]
        df_analyse.loc[:,"HY_Rdm_"+temp] = Calcul_Rend(pixel,liHYCM_np[i],df_analyse["HY_row_"+temp],df_analyse["HY_col_"+temp],df_analyse,max_row,max_col)
    
    #liHistYield_np[6][0][(310, 1700)]
    
    del max_row, max_col, temp, i, pixel #, coords_list, rent_list
    
    ###########################################################################
    # calcul de la somme des rendements
    # HistYield
    
    df_analyse["HY_Rend_tot_cowpea"]=0
    df_analyse["HY_Rend_tot_groundnut"]=0
    df_analyse["HY_Rend_tot_maize"]=0
    df_analyse["HY_Rend_tot_millet"]=0
    df_analyse["HY_Rend_tot_sorghum"]=0
    
    for prod in range(len(list_prod_HY)) :
        df_analyse.loc[df_analyse["FICHIER"]=="June-11",'HY_Rend_tot_'+list_prod_HY[prod]]= df_analyse["HY_Rdm_2010_"+list_prod_HY[prod]] 
        df_analyse.loc[df_analyse["FICHIER"]=="June-12",'HY_Rend_tot_'+list_prod_HY[prod]]= df_analyse["HY_Rdm_2011_"+list_prod_HY[prod]] 
        df_analyse.loc[df_analyse["FICHIER"]=="June-13",'HY_Rend_tot_'+list_prod_HY[prod]]= df_analyse["HY_Rdm_2012_"+list_prod_HY[prod]] 
        df_analyse.loc[df_analyse["FICHIER"]=="June-14",'HY_Rend_tot_'+list_prod_HY[prod]]= df_analyse["HY_Rdm_2013_"+list_prod_HY[prod]] 
        df_analyse.loc[df_analyse["FICHIER"]=="June-15",'HY_Rend_tot_'+list_prod_HY[prod]]= df_analyse["HY_Rdm_2014_"+list_prod_HY[prod]] 
    
    del prod
    
    df_analyse["HY_Rend_tot"]=df_analyse["HY_Rend_tot_cowpea"]+df_analyse["HY_Rend_tot_groundnut"]+df_analyse["HY_Rend_tot_maize"]+df_analyse["HY_Rend_tot_millet"]+df_analyse["HY_Rend_tot_sorghum"]
    
    ###########################################################################
    # Variables à supprimer
    list = [col for col in df_analyse.columns if col.startswith('HY_col')]
    df_analyse=df_analyse.drop(list,axis=1)
    list = [col for col in df_analyse.columns if col.startswith('HY_row')]
    df_analyse=df_analyse.drop(list,axis=1)
    list = [col for col in df_analyse.columns if col.startswith('HY_Rdm')]
    df_analyse=df_analyse.drop(list,axis=1)
    
    return df_analyse

df_analyse=Calcul_Rend_df(df_analyse,"LATITUDE","LONGITUDE",3)
df_moughataa=Calcul_Rend_df(df_moughataa,"Lat_MOUGHATAA","Long_MOUGHATAA",5)

###########################################################################
# Suppression des menages hors cartes de rendement
longmin, latmin = liHistYield[0][4].xy(0, 0)
longmax, latmax = liHistYield[0][4].xy(liHistYield[0][5], liHistYield[0][6])

df_analyse=df_analyse.loc[df_analyse["LATITUDE"].astype(float)<latmin]
df_analyse=df_analyse.loc[df_analyse["LATITUDE"].astype(float)>latmax]

df_analyse=df_analyse.loc[df_analyse["LONGITUDE"].astype(float)>longmin]
df_analyse=df_analyse.loc[df_analyse["LONGITUDE"].astype(float)<longmax]

###########################################################################
# Estimation des rendements

temp=df_analyse.loc[df_analyse["HY_Rend_tot"]>0]
Liste=['YEAR','HY_Rend_tot']
temp = temp[Liste].set_index('YEAR').notna().sum(level=0)
temp2=df_analyse["HY_Rend_tot"].loc[df_analyse["HY_Rend_tot"]>0].mean()


temp_mou=df_moughataa.loc[df_moughataa["HY_Rend_tot"]>0]
Liste=['YEAR','HY_Rend_tot']
temp_mou = temp_mou[Liste].set_index('YEAR').notna().sum(level=0)
temp2_mou=df_moughataa["HY_Rend_tot"].loc[df_moughataa["HY_Rend_tot"]>0].mean()

############################################################################
# Export des données en csv
df_analyse.to_csv('C:/0 - Data/df_analyse_tiff.csv', sep = ';')
df_moughataa.to_csv('C:/0 - Data/df_moughataa_tiff.csv', sep = ';')





