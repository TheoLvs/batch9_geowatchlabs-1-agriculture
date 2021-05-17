###########################################################################
# Ce que fait ce programme
# Importe les fichiers cartes (Crop Mask + Hist Yield) dans des listes
# Croise les cartes avec les données ménages pour ajouter le rendement pour chaque ménage

###########################################################################
# Librairies

import os
os.chdir(r'C:\Users\lebce\OneDrive\Documents\DataForGood')
print(os.getcwd())

import FichiersFSMS as fs
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

df_CropMask = pd.DataFrame(liCropMask,columns=["annee","prod","path","name","rast_rend","height","width"])
df_CropMask=df_CropMask.drop(List_drop,axis=1)
list_annee_CM=list(df_CropMask['annee'].unique())
list_prod_CM=list(df_CropMask['prod'].unique())
list_name_CM=list(df_CropMask['name'].unique())

df_HistYield["CATE"]=df_HistYield["annee"].astype(str)+"_"+df_HistYield["prod"]
df_CropMask["CATE"]=df_CropMask["annee"].astype(str)+"_"+df_CropMask["prod"]

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
# chargement de la base des ménages

liste=[203108.0,31113.0,100101.0,100114.0,100103.0,203613.0,100115.0,203614.0,
      203601.0,10610.0,100113.0,203605.0,31103.0,31105.0,203612.0,100102.0,31008.0,
      203606.0,203611.0,10604.0,203615.0,31104.0,203602.0,31101.0,31109.0,203607.0,
      31107.0,31111.0,203608.0,203603.0,31106.0,31110.0]

df_analyse=fs.df_analyse.loc[fs.df_analyse.NUMQUEST.isin(liste),:]

#df_analyse=fs.df_analyse

'''
df_analyse["LATITUDE2"]=pd.to_numeric(df_analyse["LATITUDE"], errors='coerce')

a=df_analyse["LATITUDE"].astype('int64')
a=float(df_analyse["LATITUDE"])


DataFrame.astype
Cast argument to a specified dtype.

to_datetime
Convert argument to datetime.

to_timedelta
Convert argument to timedelta.

numpy.ndarray.astype
Cast a numpy array to a specified type.

DataFrame.convert_dtypes
Convert dtypes.
'''

###########################################################################
# calcul des coordonnées sur toute la base Rendements

# calcul des rendements par annee, prod et zone pour chaque ménage 
for i in range(len(liHistYield)) :
    temp=liHistYield[i][0]+"_"+liHistYield[i][1] # annee + prod + zone
    df_analyse["HY_row_"+temp],df_analyse["HY_col_"+temp] = liHistYield[0][4].index(pd.to_numeric(df_analyse["LONGITUDE"], errors='coerce'), 
                              pd.to_numeric(df_analyse["LATITUDE"], errors='coerce'))
    max_row=liHistYield[i][5]
    max_col=liHistYield[i][6]
    df_analyse.loc[df_analyse["HY_row_"+temp]< 0 , ["HY_row_"+temp]]=0
    df_analyse.loc[df_analyse["HY_row_"+temp]> max_row , ["HY_row_"+temp]]=0
    
    df_analyse.loc[df_analyse["HY_col_"+temp]< 0 , ["HY_col_"+temp]]=0
    df_analyse.loc[df_analyse["HY_col_"+temp]> max_col , ["HY_col_"+temp]]=0
    
    #df_analyse["HY_Rend_"+temp]=liHistYield_np[i][0][df_analyse["HY_row_"+temp]][df_analyse["HY_col_"+temp]]
    coords_list = [(df_analyse["HY_row_"+temp][k], df_analyse["HY_col_"+temp][k]) for k in df_analyse.index]
    rent_list = [liHistYield_np[i][0][coords] for coords in coords_list]
    df_analyse.loc[:,"HY_Rend_"+temp] = rent_list

#liHistYield_np[6][0][(310, 1700)]

del max_row, max_col, temp, i, coords_list, rent_list

###########################################################################
# calcul des coordonnées sur toute la base taux de rendement

for i in range(len(liCropMask)) :
    temp=liCropMask[i][0]+"_"+liCropMask[i][1] # annee + prod 
    df_analyse["CM_row_"+temp],df_analyse["CM_col_"+temp] = liCropMask[0][4].index(pd.to_numeric(df_analyse["LONGITUDE"], errors='coerce'), 
                              pd.to_numeric(df_analyse["LATITUDE"], errors='coerce'))
    max_row=liCropMask[i][5]
    max_col=liCropMask[i][6]
    df_analyse.loc[df_analyse["CM_row_"+temp]< 0 , ["CM_row_"+temp]]=0
    df_analyse.loc[df_analyse["CM_row_"+temp]> max_row , ["CM_row_"+temp]]=0
    
    df_analyse.loc[df_analyse["CM_col_"+temp]< 0 , ["CM_col_"+temp]]=0
    df_analyse.loc[df_analyse["CM_col_"+temp]> max_col , ["CM_col_"+temp]]=0

    coords_list = [(df_analyse["CM_row_"+temp][k], df_analyse["CM_col_"+temp][k]) for k in df_analyse.index]
    rent_list = [liCropMask_np[i][0][coords] for coords in coords_list]
    df_analyse.loc[:,"CM_Rend_"+temp] = rent_list
    
del max_row, max_col, temp, i, coords_list, rent_list


###########################################################################
# calcul des coordonnées sur toute la base taux de rendement

# somme des rendements par prod pour chaque ménage en fonction de la date
df_analyse["HY_Rend_tot_cowpea"]=0
df_analyse["HY_Rend_tot_groundnut"]=0
df_analyse["HY_Rend_tot_maize"]=0
df_analyse["HY_Rend_tot_millet"]=0
df_analyse["HY_Rend_tot_sorghum"]=0

for prod in range(len(list_prod_HY)) :
    df_analyse.loc[df_analyse["FICHIER"]=="June-11",'HY_Rend_tot_'+list_prod_HY[prod]]= df_analyse["HY_Rend_2010_"+list_prod_HY[prod]] 
    df_analyse.loc[df_analyse["FICHIER"]=="June-12",'HY_Rend_tot_'+list_prod_HY[prod]]= df_analyse["HY_Rend_2011_"+list_prod_HY[prod]] 
    df_analyse.loc[df_analyse["FICHIER"]=="June-13",'HY_Rend_tot_'+list_prod_HY[prod]]= df_analyse["HY_Rend_2012_"+list_prod_HY[prod]] 
    df_analyse.loc[df_analyse["FICHIER"]=="June-14",'HY_Rend_tot_'+list_prod_HY[prod]]= df_analyse["HY_Rend_2013_"+list_prod_HY[prod]] 
    df_analyse.loc[df_analyse["FICHIER"]=="June-15",'HY_Rend_tot_'+list_prod_HY[prod]]= df_analyse["HY_Rend_2014_"+list_prod_HY[prod]] 

del prod

df_analyse["HY_Rend_tot"]=df_analyse["HY_Rend_tot_cowpea"]+df_analyse["HY_Rend_tot_groundnut"]+df_analyse["HY_Rend_tot_maize"]+df_analyse["HY_Rend_tot_millet"]+df_analyse["HY_Rend_tot_sorghum"]

# affichage des résultats
# list = [col for col in df_analyse.columns if col.startswith('HY_Rend_tot_')]
# a=df_analyse[list]

# del a, list

# somme des rendements par prod pour chaque ménage en fonction de la date
df_analyse["CM_Rend_tot_cowpea"]=0
df_analyse["CM_Rend_tot_groundnut"]=0
df_analyse["CM_Rend_tot_maize"]=0
df_analyse["CM_Rend_tot_millet"]=0
df_analyse["CM_Rend_tot_sorghum"]=0

for prod in range(len(list_prod_HY)) :
    df_analyse.loc[df_analyse["FICHIER"]=="June-11",'CM_Rend_tot_'+list_prod_CM[prod]]= df_analyse["CM_Rend_2010_"+list_prod_CM[prod]] 
    df_analyse.loc[df_analyse["FICHIER"]=="June-12",'CM_Rend_tot_'+list_prod_CM[prod]]= df_analyse["CM_Rend_2011_"+list_prod_CM[prod]] 
    df_analyse.loc[df_analyse["FICHIER"]=="June-13",'CM_Rend_tot_'+list_prod_CM[prod]]= df_analyse["CM_Rend_2012_"+list_prod_CM[prod]] 
    df_analyse.loc[df_analyse["FICHIER"]=="June-14",'CM_Rend_tot_'+list_prod_CM[prod]]= df_analyse["CM_Rend_2013_"+list_prod_CM[prod]] 
    df_analyse.loc[df_analyse["FICHIER"]=="June-15",'CM_Rend_tot_'+list_prod_CM[prod]]= df_analyse["CM_Rend_2014_"+list_prod_CM[prod]] 

del prod

df_analyse["CM_Rend_tot"]=df_analyse["CM_Rend_tot_cowpea"]+df_analyse["CM_Rend_tot_groundnut"]+df_analyse["CM_Rend_tot_maize"]+df_analyse["CM_Rend_tot_millet"]+df_analyse["CM_Rend_tot_sorghum"]

# affichage des résultats
# list = [col for col in df_analyse.columns if col.startswith('CM_Rend_tot_')]
# a=df_analyse[list]

# del a, list

###########################################################################
# créer une carte par champ et par année
temp=df_analyse.loc[df_analyse["HY_Rend_tot"]>0]













