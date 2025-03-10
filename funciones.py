def Funcion_1(archivo):
    import pandas as pd
    import os
    extension = os.path.splitext(archivo)[1].lower()
# Cargar el archivo según su extensión
    if extension == '.csv':
        df= pd.read_csv(archivo)
        return (df)
    elif extension == '.xlsx':
        df= pd.read_excel(archivo)
        return (df)
    else:
            raise ValueError(f"Este formato no está soportado para esta función: {extension}")
    

def Funcion_2(df):
    Data_Type=df.columns.dtype
    for columna in df.columns:
        if (Data_Type == 'object') | (Data_Type == 'datetime') | (Data_Type == 'category'):  
            df[columna].fillna("Este_es_un_valor_nulo", inplace=True)
        elif (Data_Type == 'float') | (Data_Type == 'float64') | (Data_Type == 'int') |(Data_Type == 'int64'):
            if columna.isnumeric() and int(columna) % 2 == 0:  
                df[columna].fillna(df[columna].mean(), inplace=True)
            else:  
                df[columna].fillna(99, inplace=True)
    return df

def Funcion_3(df):
    #Valores nulos por columna
    valores_nulos_cols = df.isnull().sum()
    #Valores nulos por dataframe
    valores_nulos_df = df.isnull().sum().sum()
    
    return("Valores nulos por columna", valores_nulos_cols,
            "Valores nulos por dataframe", valores_nulos_df)
    
def Funcion_4(df):
    import pandas as pd
    cuantitativos = df.select_dtypes(include=['float', 'float64', 'int', 'int64'])
    cualitativos = df.select_dtypes(include=['object', 'datetime', 'category'])
    for columnas in cuantitativos:
        
            percentile25 = cuantitativos.quantile(0.25) #Q1
            percentile75 = cuantitativos.quantile(0.75) #Q3
            iqr = percentile75 - percentile25
            Limite_Superior_iqr = percentile75 + 1.5*iqr
            Limite_Inferior_iqr = percentile25 - 1.5*iqr
            print("Limite superior permitido", Limite_Superior_iqr)
            print("Limite inferior permitido", Limite_Inferior_iqr)
            cuanti_limpio = cuantitativos[(cuantitativos<=Limite_Superior_iqr)&(cuantitativos>=Limite_Inferior_iqr)]
            df_limpio1 = cuanti_limpio.fillna(round(cuanti_limpio.mean(),1))
            df_limipio = pd.concat([cualitativos, df_limpio1], axis=1)
    return df_limipio