# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:39:52 2022

@author: jgarciah2
"""
"""
'           .---.        .-----------
'          /     \  __  /    ------
'         / /     \(..)/    -----
'        //////   ' \/ `   ---
'       //// / // :    : ---
'      // /   /  /`    '--
'     // /        //..\\
'   o===|========UU====UU=====-  -==========================o
'                '//||\\`
'                       DEVELOPED BY JGH
'
'   -=====================|===o  o===|======================-
'-----------------------------------------------------------------------------
' Module    : comparartiempos
' DateTime  : 28/03/2022
' Author    : José García Herruzo
' Purpose   : Check kart times per grand prix
'-----------------------------------------------------------------------------
"""

import pandas as pd
import math
import numpy as np

str_File='C:\\Users\jgarciah2\Downloads\T1.csv'
df_1=pd.read_csv(str_File, sep=";",encoding='ISO-8859-1')

str_File='C:\\Users\jgarciah2\Downloads\T2.csv'
df_2=pd.read_csv(str_File, sep=";",encoding='ISO-8859-1')


str_File='C:\\Users\jgarciah2\Downloads\T3.csv'
df_3=pd.read_csv(str_File, sep=";",encoding='ISO-8859-1')


df_1['T1_ms']=df_1['Minuto']*60*1000+df_1['segundo']*1000+df_1['centesima']
df_2['T2_ms']=df_2['Minuto']*60*1000+df_2['segundo']*1000+df_2['centesima']
df_3['T3_ms']=df_3['Minuto']*60*1000+df_3['segundo']*1000+df_3['centesima']

print(df_1.info())

def xp_strTiempos(int_ms):
    """ Purpose   : Unify time series
        DateTime  : 
        Author    : José García Herruzo
      @Arg:
          int_ms --> milisecond
      @get:
          var --> unified time value min:sec:milisecond  
          """    
    temporal, minutos=np.modf(int_ms/1000/60)
    temporal, segundos=np.modf(temporal*60)
    ms=temporal*1000
    var='{}:{}:{}'.format(int(minutos),int(segundos),int(ms))
    
    return var
def xp_myFunction2(df_temp1,df_temp2,df_temp3, lst_k):
    """ Purpose   : Check time per race
        DateTime  : 
        Author    : José García Herruzo
      @Arg:
          df_temp1 --> race 1 data
          df_temp2 --> race 2 data
          df_temp3 --> race 3 data
          lst_k --> list of kart numbers
      @get:
          lst_def --> Result
          """      
    lst_def=list()
    
    # use kart number as index
    df_temp1=df_temp1.set_index('Kart')   
    df_temp2=df_temp2.set_index('Kart')    
    df_temp3=df_temp3.set_index('Kart')
       
    for item in lst_k:
       
        lst_nom=list()
        lst_value=list() 
        
        lst_nom.append('Kart')
        lst_value.append(item)
        
        try:        
            lst_nom.append(df_temp1.loc[int(item)]['Piloto'])
            lst_value.append(xp_strTiempos(df_temp1.loc[int(item)]['T1_ms']))
        except:
            lst_nom.append('Tanda 1')
            lst_value.append('Null')
        try:        
            lst_nom.append(df_temp2.loc[int(item)]['Piloto'])
            lst_value.append(xp_strTiempos(df_temp2.loc[int(item)]['T2_ms']))
        except:
            lst_nom.append('Tanda 2')
            lst_value.append('Null')
        try:
            lst_nom.append(df_temp3.loc[int(item)]['Piloto'])
            lst_value.append(xp_strTiempos(df_temp3.loc[int(item)]['T3_ms']))
        except:
            lst_nom.append('Tanda 3')
            lst_value.append('Null')

        df_temp=pd.DataFrame(lst_nom,lst_value)        
        print(df_temp.transpose())        
        lst_def.append(df_temp)
    
    return lst_def

set_kart1=set(df_1['Kart'])   
set_kart2=set(df_2['Kart'])   
set_kart3=set(df_3['Kart'])   

# hay que sacar los datos individuales de cada lista

set_kart11=set_kart2.difference(set_kart1)
set_kart1.update(set_kart11)
set_kart12=set_kart3.difference(set_kart1)
set_kart1.update(set_kart12)
lst_kart=list(set_kart1)

lst=xp_myFunction2(df_1,df_2,df_3,lst_kart)





    