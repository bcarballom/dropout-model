# --- Extracted from 1. Preparar DataFrame.ipynb ---
import pandas as pd
import os

# 1) ACCEDER A LOS ARCHIVOS EN LA CARPETA ('DATA')

# Definir la ruta donde se encuentran los archivos
root_path = os.getcwd()
folder_path = os.path.join(root_path,'data')   

# Obtener una lista de todos los archivos en la carpeta
file_list = [file for file in os.listdir(folder_path) if file.endswith('.csv') and 'respuestas' in file]

# Verificar que la lista de archivos no esté vacía
if not file_list:
    raise ValueError("No se encontraron archivos CSV que coincidan con el criterio especificado en la carpeta.")

print("Archivos encontrados:", file_list)

# 2) CREAR EL DATAFRAME

import re

# Obtener el dato del año del nombre del archivo con una función
def extract_year(file_name):
    match = re.search(r'(\d{4})', file_name)
    return match.group(0) if match else None

# Especificar el nombre de las columnas a mantener
columnas_adicionales = [
    'EMPLID', 'EDAD', 'GENERO', 'CARRERA', 'UNIDAD', 'BACH_PROMEDIO', 'PUNTAJE_ADM',
    'P005_O001V', 'P005_O002V', 'P006_O001V', 'P006_O002V', 'P006_O003V', 'P006_O004V', 'P006_O005V',
    'P006_O006V', 'P006_O007V', 'P006_O008V', 'P006_O009V', 'P007_O001V', 'P008_O001V', 'P008_O002V',
    'P009_O001V', 'P010_O001V', 'P010_O002V', 'P011_O001V', 'P012_O001V', 'P013_O001V', 'P014_O001V',
    'P015_O001V', 'P015_O002V', 'P015_O003V', 'P015_O004V', 'P015_O005V', 'P016_O001V', 'P017_O001V', 
    'P018_O001V', 'P018_O002V', 'P019_O001V', 'P020_O001V', 'P021_O001V', 'P022_O001V', 'P023_O001V', 
    'P024_O001V', 'P024_O002V', 'P025_O001V', 'P026_O001V', 'P027_O001V', 'P027_O002V', 'P027_O003V', 
    'P027_O004V', 'P027_O005V', 'P027_O006V', 'P027_O007V', 'P027_O008V', 'P027_O009V', 'P027_O010V', 
    'P027_O011V', 'P027_O012V', 'P027_O013V', 'P027_O014V', 'P028_O001V', 'P029_O001V', 'P030_O001V', 
    'P031_O001V', 'P031_O002V', 'P031_O003V', 'P032_O001V', 'P032_O002V', 'P032_O003V', 'P033_O001V', 
    'P033_O002V', 'P033_O003V', 'P033_O004V', 'P033_O005V', 'P033_O006V', 'P033_O007V', 'P033_O008V', 
    'P033_O009V', 'P033_O010V', 'P034_O001V', 'P034_O002V', 'P034_O003V', 'P034_O004V', 'P034_O005V', 
    'P034_O006V', 'P034_O007V', 'P034_O008V', 'P034_O009V', 'P035_O001V', 'P035_O002V', 'P035_O003V', 
    'P035_O004V', 'P035_O005V', 'P036_O001V', 'P036_O002V', 'P036_O003V', 'P036_O004V', 'P036_O005V', 
    'P036_O006V', 'P036_O007V', 'P037_O001V', 'P037_O002V', 'P037_O003V', 'P037_O004V', 'P037_O005V', 
    'P037_O006V', 'P037_O007V', 'P037_O008V', 'P038_O001V', 'P039_O001V', 'P040_O001V', 'P040_O002V', 
    'P041_O001V', 'P041_O002V', 'P041_O003V', 'P041_O004V', 'P041_O005V', 'P041_O006V', 'P042_O001V', 
    'P043_O001V', 'P044_O001V', 'P045_O001V', 'P046_O001V', 'P046_O002V', 'P046_O003V', 'P046_O004V', 
    'P046_O005V', 'P046_O006V', 'P046_O007V', 'P046_O008V', 'P046_O009V', 'P046_O010V', 'P047_O001V', 
    'P047_O002V', 'P047_O003V', 'P047_O004V', 'P047_O005V', 'P047_O006V', 'P047_O007V', 'P047_O008V', 
    'P048_O001V', 'P048_O002V', 'P048_O003V', 'P048_O004V', 'P048_O005V', 'P048_O006V', 'P049_O001V', 
    'P049_O002V', 'P049_O003V', 'P049_O004V', 'P049_O005V', 'P049_O006V', 'P049_O007V', 'P049_O008V', 
    'P049_O009V', 'P049_O010V', 'P049_O011V', 'P050_O001V', 'P050_O002V', 'P050_O003V', 'P050_O004V', 
    'P050_O005V', 'P050_O006V', 'P050_O007V', 'P050_O008V', 'P050_O009V', 'P050_O010V', 'P050_O011V', 
    'P051_O001V', 'P051_O002V', 'P051_O003V', 'P051_O004V', 'P051_O005V', 'P052_O001V', 'P052_O002V', 
    'P052_O003V', 'P052_O004V', 'P052_O005V', 'P052_O006V', 'P052_O007V', 'P052_O008V', 'P052_O009V', 
    'P052_O010V', 'P053_O001V', 'P054_O001V', 'P055_O001V', 'P055_O002V', 'P055_O003V', 'P055_O004V', 
    'P055_O005V', 'P056_O001V', 'P056_O002V', 'P056_O003V', 'P056_O004V', 'P056_O005V', 'P056_O006V', 
    'P056_O007V', 'P056_O008V', 'P056_O009V', 'P056_O010V', 'P057_O001V', 'P058_O001V', 'P059_O001V', 
    'P059_O002V', 'P060_O001V', 'P060_O002V', 'P003_O001V', 'P004_O001V'
]

# Crear una lista para almacenar los dataframes
data_frames = []

# Leer y almacenar cada archivo en la lista de dataframes
for file in file_list:
    file_path = os.path.join(folder_path, file)
    year = extract_year(file)
    df = pd.read_csv(file_path, low_memory=False)
    df['Año'] = year  # Agregar la columna del año
    
    # Mantener solo las columnas especificadas
    columnas_a_mantener = columnas_adicionales + ['Año']
    
    # Verificar qué columnas existen realmente en el DataFrame y filtrar
    columnas_presentes = [col for col in columnas_a_mantener if col in df.columns]
    df = df[columnas_presentes]
    
    data_frames.append(df)
    
# Unir todos los dataframes en uno solo
df = pd.concat(data_frames, ignore_index=True)

# Eliminar duplicados y reverificar el resultado:
filas_antes = df.shape[0]  # Guardar el número de filas antes de eliminar duplicados
df = df.drop_duplicates()   # Eliminar filas  duplicadas
filas_despues = df.shape[0]   # Guardar el número de filas después
eliminadas = filas_antes - filas_despues # Calcular  cuántas filas se eliminaron
print(f"Se eliminaron {eliminadas} filas duplicadas (de {filas_antes} totales).")
print(f"DataFrame final: {filas_despues} filas.")

# 2) COMPLETAR EL DATAFRAME CON LOS DATOS DE DESERCIÓN

#  cargar el archivo de deserción
df_desercion = pd.read_excel(os.path.join(folder_path, 'Deserción.xlsx'))

# Convertir a string para asegurar coincidencias
df['EMPLID'] = df['EMPLID'].astype(str) 
df_desercion['EMPLID'] = df_desercion['EMPLID'].astype(str) 

# Copiar el df antes del merge (para identificar después quiénes no respondieron)
df_original = df.copy()

# Realizar la unión con los datos de deserción por la clave 'EMPLID'
df = pd.merge(df, df_desercion, on='EMPLID', how='left')

# Imputar valor 0 en los NaN del campo 'DESERCION' (alumnos que no desertaron pero  respodieron el cuestionario)
df['DESERCION'] = df['DESERCION'].fillna(0)

# Verificación de valores nulos en 'DESERCION'
na_count = df['DESERCION'].isna().sum()
print(f"Valores nulos en 'DESERCION' después de la imputación: {na_count}")

# Eliminar duplicados que surgieron tras el merge
filas_antes_merge = df.shape[0]
df = df.drop_duplicates()
filas_despues_merge = df.shape[0]
print(f"Se eliminaron {filas_antes_merge - filas_despues_merge} filas duplicadas tras el merge (se generaron durante la unión).")
print(f"DataFrame final post-merge: {filas_despues_merge} filas.")

# Ver EMPLIDs que aparecen más de una vez después del merge
duplicados = df['EMPLID'].value_counts()
duplicados = duplicados[duplicados > 1]
print(f"Total de duplicados por EMPLID: {duplicados.sum() - len(duplicados)}")

# Eliminar  registros repetidos (con 'EMPLID' y 'SEMESTRE ABANDONO')
df['SEMESTRE ABANDONO'] = pd.to_numeric(df['SEMESTRE ABANDONO'], errors='coerce') # Asegurar que SEMESTRE ABANDONO sea numérico
duplicados = df[df.duplicated(subset='EMPLID', keep=False)] # Detectar duplicados por EMPLID
print(f"Guardados {duplicados.shape[0]} registros duplicados por EMPLID con posibles abandonos múltiples.")
# Quedarse solo con la fila que tenga el mayor 'SEMESTRE ABANDONO' por EMPLID
df = df.sort_values(by='SEMESTRE ABANDONO', ascending=False)  # Mayor primero
df = df.drop_duplicates(subset='EMPLID', keep='first')  # Conservar solo el mayor por EMPLID

# Confirmar resultado
print(f"DataFrame final depurado: {df.shape[0]} filas (una por EMPLID con abandono máximo)")
print(f"EMPLIDs únicos: {df['EMPLID'].nunique()}")

# 3) COMPLETAR EL DATAFRAME CON LOS DATOS DE CAMBIOS DE PROGRAMA

# Cargar tabla de cambios de programa
cambios_programa = pd.read_excel(os.path.join(folder_path, 'Cambio_Programa.xlsx'))

# Asegurar que los EMPLID sean strings
df['EMPLID'] = df['EMPLID'].astype(str)
cambios_programa['EMPLID'] = cambios_programa['EMPLID'].astype(str)

# Contar número de cambios por EMPLID
conteo_cambios = cambios_programa['EMPLID'].value_counts().to_dict()
df['CAMBIO_PROGRAMA'] = df['EMPLID'].map(conteo_cambios).fillna(0).astype(int)

# Conservar solo la fila con el último cambio de programa por estudiante
# Suponiendo que SEMESTRE ABANDONO indica el orden temporal
cambios_programa['SEMESTRE ABANDONO'] = pd.to_numeric(cambios_programa['SEMESTRE ABANDONO'], errors='coerce')
cambios_unicos = cambios_programa.sort_values('SEMESTRE ABANDONO', ascending=False).drop_duplicates('EMPLID')

# Merge con los campos relevantes desde la tabla depurada
df = df.merge(
    cambios_unicos[['EMPLID', 'SEMESTRE ABANDONO', 'SEMESTRE PLAN', 'ETNIA']],
    on='EMPLID',
    how='left',
    suffixes=('', '_nueva')
)

# Si ya tenías estos campos en df, completar nulos con los nuevos valores
for col in ['SEMESTRE ABANDONO', 'SEMESTRE PLAN', 'ETNIA']:
    df[col] = df[col].combine_first(df[f"{col}_nueva"])

# Eliminar columnas auxiliares
df.drop(columns=[f"{col}_nueva" for col in ['SEMESTRE ABANDONO', 'SEMESTRE PLAN', 'ETNIA']], inplace=True)

# Eliminar filas duplicadas completas
filas_antes = df.shape[0]
df = df.drop_duplicates()
filas_despues = df.shape[0]
print(f"Se eliminaron {filas_antes - filas_despues} filas duplicadas (de {filas_antes} totales).")
print(f"DataFrame final: {filas_despues} filas.")


# 3) RESCARTAR DATOS DE UNA COLUMNA (TELEFONO)

# 1. Asignar lada 644 a los teléfonos que inician con 4, asumiento que son de 7 digitos y les falta la lada

# Asegurarse de que la columna de teléfono esté en formato de texto, extraer la lada del número de teléfono y crear columna 'Lada'
df['P003_O001V'] = df['P003_O001V'].astype(str).str.replace(r'\D', '', regex=True) #Aseguramos que la columna P003_O001V contenga solo caracteres numéricos mediante str.replace(r'\D', '', regex=True), eliminando cualquier carácter no numérico.
df['Lada'] = df['P003_O001V'].str[:3]

# Filtrar los números de celular que empiezan con los prefijos especificados
prefijos = ['410', '411', '412', '413', '414', '415', '416', '417', '418', '419']
mask_prefijos = df['P003_O001V'].str.startswith(tuple(prefijos))

# Asignar la lada 644 a los números filtrados
df.loc[mask_prefijos, 'Lada'] = '644'

# Verificar cuántas filas fueron afectadas por la actualización
filas_afectadas = df[mask_prefijos].shape[0]
print(f"Filas afectadas con Lada '644': {filas_afectadas}")

# 2. Asignar lada 644 a los teléfonos que inician con 044, asumiento que son de la ciudad  y usaban 13 digitos

# Filtrar los números que comienzan con '044'
mask_044 = df['P003_O001V'].str.startswith('044')

# Asignar la lada 644 a estos números
df.loc[mask_044, 'Lada'] = '644'

# Eliminar el prefijo '044' y quedarte con los 10 dígitos restantes del número de teléfono
df.loc[mask_044, 'P003_O001V'] = df.loc[mask_044, 'P003_O001V'].str[3:]

# Verificar cuántas filas fueron afectadas por la actualización
filas_afectadas = df[mask_044].shape[0]
print(f"Filas afectadas con Lada '644' y modificación de número: {filas_afectadas}")

# 3. Asignar lada 644 a los teléfonos que inician con 1 pero y dicen el nombre del Estado en el domicilio, asumiendo que son de 5 digitos y les falta la lada

# Filtrar los números de teléfono que empiezan con '1'
mask_prefijo = df['P003_O001V'].str.startswith('1')

# Definir las variaciones del estado "Sonora"
estados = ['Son.', 'Son', 'son', 'son.', 'Sonora', 'sonora']

# Filtrar las filas que contienen variaciones del estado "Sonora"
mask_estados = df['P004_O001V'].str.contains('|'.join(estados), case=False, na=False)

# Aplicar ambas condiciones simultáneamente
df.loc[mask_prefijo & mask_estados, 'Lada'] = '644'

# Verificar cuántas filas fueron afectadas por la actualización
filas_afectadas = df[mask_prefijo & mask_estados].shape[0]
print(f"Filas afectadas con Lada '644': {filas_afectadas}")

# 4. Asignar lada 644 a los teléfonos que inician con 01, para extraer la lada

# Filtrar los números de celular que empiezan con '01'
mask_01 = df['P003_O001V'].str.startswith('01')

# Asignar la lada 644 a estos números
df.loc[mask_01, 'Lada'] = '644'

# Extraer los tres dígitos siguientes a '01' para obtener la lada real y sobrescribir la columna 'Lada'
df.loc[mask_01, 'Lada'] = df.loc[mask_01, 'P003_O001V'].str[2:5]  # Extrae dígitos 2, 3 y 4

# Verificar cuántas filas fueron afectadas
filas_afectadas = df[mask_01].shape[0]
print(f"Filas afectadas con Lada actualizada: {filas_afectadas}")

# 5. Asignar lada 644 a los teléfonos que inician con 1 y tienen más de 7 digitos, para extraer la lada

# Filtrar los números de celular que empiezan con '1' y tienen más de 7 dígitos
mask_1_y_largo = df['P003_O001V'].str.startswith('1') & (df['P003_O001V'].str.len() > 7)

# Asignar la lada 644 a estos números inicialmente
df.loc[mask_1_y_largo, 'Lada'] = '644'

# Extraer los tres dígitos siguientes al primer dígito '1' para obtener la lada real y actualizar la columna 'Lada'
df.loc[mask_1_y_largo, 'Lada'] = df.loc[mask_1_y_largo, 'P003_O001V'].str[1:4]  # Extrae dígitos 2, 3 y 4

# Verificar cuántas filas fueron afectadas
filas_afectadas = df[mask_1_y_largo].shape[0]
print(f"Filas afectadas con Lada actualizada: {filas_afectadas}")

# 6. Asignar lada 644 a los teléfonos que inician con 1

# Filtrar los números de celular que empiezan con '1'
mask_1 = df['P003_O001V'].str.startswith('1')

# Asignar la lada 644 a estos números
df.loc[mask_1, 'Lada'] = '644'

# Verificar cuántas filas fueron afectadas
filas_afectadas = df[mask_1].shape[0]
print(f"Filas afectadas con Lada actualizada: {filas_afectadas}")

# 7. Asignar lada 622 a los teléfonos que inician con 22

# Filtrar los números de celular que empiezan con '22'
mask_22 = df['P003_O001V'].str.startswith('22')

# Asignar la lada 644 a estos números
df.loc[mask_22, 'Lada'] = '622'

# Verificar cuántas filas fueron afectadas por la actualización
filas_afectadas = df[mask_22].shape[0]
print(f"Filas afectadas con Lada '622': {filas_afectadas}")

# COMBINAR el df con la tabla de dimensiones 'lada_to_location' para obtener campos de Ciudad y Estado

# Cargar el archivo de mapeo de ladas a ubicaciones con codificación especificada
try:
    with open(os.path.join(folder_path, 'lada_to_location.csv'), 'r', encoding='utf-8-sig') as file:
        lada_to_location = pd.read_csv(file)
except UnicodeDecodeError:
    try:
        lada_to_location = pd.read_csv(os.path.join(folder_path, 'lada_to_location.csv'), encoding='ISO-8859-1')
    except UnicodeDecodeError:
        try:
            lada_to_location = pd.read_csv(os.path.join(folder_path, 'lada_to_location.csv'), encoding='Windows-1252')
        except UnicodeDecodeError:
            print("Error al leer el archivo CSV con codificaciones comunes. Verifica el archivo y la codificación.")

# Asegurarse de que la columna 'Lada' en lada_to_location  esté en formato de texto
lada_to_location['Lada'] = lada_to_location['Lada'].astype(str)

# Unir el DataFrame principal con el DataFrame de mapeo por la columna 'Lada'
df = df.merge(lada_to_location, on='Lada', how='left')  

# Verificar duplicados por EMPLID generados después del merge
emplids_antes = df['EMPLID'].nunique()
filas_antes = df.shape[0]

# Eliminar duplicados por EMPLID (conservando la primera ocurrencia)
df = df.drop_duplicates(subset='EMPLID', keep='first')

# Confirmar cambio
filas_despues = df.shape[0]
print(f"Se eliminaron {filas_antes - filas_despues} filas duplicadas por EMPLID generadas después del merge.")
print(f"DataFrame final con 1 fila por estudiante: {df.shape[0]} filas, {df['EMPLID'].nunique()} EMPLIDs únicos.")

# Verificación posterior al merge
campos_nuevos = ['Ciudad', 'Estado']
campos_existentes = [col for col in campos_nuevos if col in df.columns]

if campos_existentes:
    filas_completas = df[campos_existentes].notnull().all(axis=1).sum()
    filas_incompletas = df.shape[0] - filas_completas
    print(f"Merge completado: se asignaron Ciudad y Estado en {filas_completas} de {df.shape[0]} registros.")
    print(f"{filas_incompletas} registros tienen valores nulos en ambos campos ('Ciudad' y 'Estado').")
else:
    print("Atención: No se encontraron columnas 'Ciudad' y 'Estado' tras el merge.")

# COMPLEMENTAR REGISTROS VACIOS EN CIUDAD/ESTADO CON DATOS DEL DOMICILIO

from unidecode import unidecode

# Función para buscar coincidencias parciales en el domicilio y actualizar las columnas correspondientes
def actualizar_por_domicilio(df, lada_to_location):
    # Normalizar el DataFrame 'lada_to_location' quitando acentos y poniendo en minúsculas
    lada_to_location['Ciudad_Normalizada'] = lada_to_location['Ciudad'].apply(lambda x: unidecode(str(x)).lower())
    lada_to_location['Estado_Normalizado'] = lada_to_location['Estado'].apply(lambda x: unidecode(str(x)).lower())
    
    # Normalizar las columnas relevantes del DataFrame df
    df['P004_O001V_Normalizado'] = df['P004_O001V'].apply(lambda x: unidecode(str(x)).lower())
    
    # Conjunto de estados válidos
    estados_validos = set(lada_to_location['Estado_Normalizado'].unique())
    
    # Lista de estados que deben ser excluidos (para evitar que entienda que el estado es Colima porque solo se refiere a la colonia)
    estados_excluidos = {'Col.', 'col.', 'colonia', 'colon', 'col', 'colim', 'colim.', 'co.'}

    # Recorrer el DataFrame original en busca de coincidencias
    for i, domicilio_normalizado in df['P004_O001V_Normalizado'].items():
        if pd.isna(df.loc[i, 'Lada']) or pd.isna(df.loc[i, 'Ciudad']) or pd.isna(df.loc[i, 'Estado']):
            # Normalizar el domicilio (quitar acentos y pasar a minúsculas)
            domicilio_normalizado = unidecode(str(domicilio_normalizado)).lower()
            
            # Leer el domicilio de derecha a izquierda
            palabras_domicilio = domicilio_normalizado.split()[::-1]  # Dividir en palabras e invertir el orden
            
            # Variable para rastrear si se encontró alguna coincidencia
            encontrado = False
            
            # Buscar coincidencias en las ciudades y estados
            for _, row in lada_to_location.iterrows():
                ciudad_normalizada = row['Ciudad_Normalizada']
                estado_normalizado = row['Estado_Normalizado']
                
                # Verificar si alguna palabra del domicilio coincide parcialmente con la ciudad
                for palabra in palabras_domicilio:
                    if ciudad_normalizada in palabra:
                        df.loc[i, 'Ciudad'] = row['Ciudad']
                        df.loc[i, 'Estado'] = row['Estado']
                        df.loc[i, 'Lada'] = row['Lada']
                        encontrado = True
                        break
                
                # Verificar si alguna palabra coincide parcialmente con el estado si no se encontró ciudad
                if not encontrado:
                    for palabra in palabras_domicilio:
                        if estado_normalizado in palabra and estado_normalizado not in estados_excluidos:
                            if estado_normalizado in estados_validos:
                                df.loc[i, 'Estado'] = row['Estado']
                                if pd.isna(df.loc[i, 'Lada']):
                                    df.loc[i, 'Lada'] = row['Lada']
                            break

            # Si no se encontró ciudad o estado, usar el valor de la columna 'UNIDAD'
            if pd.isna(df.loc[i, 'Ciudad']):
                unidad = df.loc[i, 'UNIDAD']
                if unidad == 'OBREGON':
                    df.loc[i, 'Ciudad'] = "Ciudad Obregón"
                elif unidad == 'NAVOJOA':
                    df.loc[i, 'Ciudad'] = "Navojoa"
                elif unidad == 'GUAYMAS':
                    df.loc[i, 'Ciudad'] = "Guaymas"
                elif unidad == 'EMPALME':
                    df.loc[i, 'Ciudad'] = "Empalme"
                else:
                    df.loc[i, 'Ciudad'] = None  # Si no es ninguno de estos, deja NaN

            # Si no se encontró estado, usar el valor de la columna 'UNIDAD'
            if pd.isna(df.loc[i, 'Estado']):
                unidad = df.loc[i, 'UNIDAD']
                if unidad == 'OBREGON':
                    df.loc[i, 'Estado'] = "Sonora"
                elif unidad == 'NAVOJOA':
                    df.loc[i, 'Estado'] = "Sonora"
                elif unidad == 'GUAYMAS':
                    df.loc[i, 'Estado'] = "Sonora"
                elif unidad == 'EMPALME':
                    df.loc[i, 'Estado'] = "Sonora"
                else:
                    df.loc[i, 'Estado'] = None  # Si no es ninguno de estos, deja NaN

    # Eliminar columna de normalización
    df.drop(columns=['P004_O001V_Normalizado'], inplace=True)

    return df

# Contar las filas con NaN en 'Ciudad', 'Estado' y 'Lada' antes de la actualización
filas_con_nan_antes = {
    'Ciudad': df['Ciudad'].isna().sum(),
    'Estado': df['Estado'].isna().sum(),
}

# Llamar a la función para actualizar el DataFrame df
df = actualizar_por_domicilio(df, lada_to_location)

# Contar las filas con valores NaN en 'Ciudad', 'Estado' y 'Lada' después de la actualización
filas_con_nan_despues = {
    'Ciudad': df['Ciudad'].isna().sum(),
    'Estado': df['Estado'].isna().sum(),
}

# Calcular la diferencia
filas_modificadas = {
    'Ciudad': filas_con_nan_antes['Ciudad'] - filas_con_nan_despues['Ciudad'],
    'Estado': filas_con_nan_antes['Estado'] - filas_con_nan_despues['Estado'],
}

print(f"Filas con 'Ciudad' NaN antes: {filas_con_nan_antes['Ciudad']}")
print(f"Filas con 'Ciudad' NaN después: {filas_con_nan_despues['Ciudad']}")
print(f"Filas actualizadas en 'Ciudad': {filas_modificadas['Ciudad']}")

print(f"Filas con 'Estado' NaN antes: {filas_con_nan_antes['Estado']}")
print(f"Filas con 'Estado' NaN después: {filas_con_nan_despues['Estado']}")
print(f"Filas actualizadas en 'Estado': {filas_modificadas['Estado']}")

# OBTENER COORDENADAS

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
from geopy.distance import geodesic
import time

# Inicializar el geolocalizador con tiempo de espera más largo y retries
geolocator = Nominatim(user_agent="geoapi", timeout=10)

# Función para obtener coordenadas con manejo de errores y reintentos
def obtener_coordenadas(ciudad, max_intentos=3):
    for intento in range(max_intentos):
        try:
            location = geolocator.geocode(f"{ciudad}, México")
            if location:
                return location.latitude, location.longitude
            else:
                return None, None
        except (GeocoderTimedOut, GeocoderUnavailable) as e:
            if intento == max_intentos - 1:  # Si es el último intento
                print(f"Error: No se pudo obtener coordenadas para {ciudad} después de {max_intentos} intentos")
                return None, None
            print(f"Intento {intento + 1} falló para {ciudad}. Reintentando...")
            time.sleep(2)  # Esperar 2 segundos antes de reintentar

# Extraer las ciudades únicas del DataFrame
columna_ciudad = "Ciudad"
ciudades_unicas = df[columna_ciudad].dropna().unique()

# Crear un diccionario para almacenar las coordenadas y evitar buscar repetidamente
coordenadas_dict = {}

# Procesar cada ciudad con reintento y pausa entre solicitudes
for ciudad in ciudades_unicas:
    print(f"Obteniendo coordenadas para: {ciudad}")
    coordenadas_dict[ciudad] = obtener_coordenadas(ciudad)
    time.sleep(1)  # Pausa de 1 segundo entre solicitudes para evitar sobrecarga

# Crear las nuevas columnas de Latitud y Longitud en el DataFrame original
df['Latitud'] = df[columna_ciudad].map(lambda x: coordenadas_dict[x][0] if x in coordenadas_dict else None)
df['Longitud'] = df[columna_ciudad].map(lambda x: coordenadas_dict[x][1] if x in coordenadas_dict else None)

# Verificar si hay ciudades sin coordenadas
ciudades_sin_coordenadas = df[df['Latitud'].isnull()]
if not ciudades_sin_coordenadas.empty:
    print("\nNo se encontraron coordenadas para las siguientes ciudades:")
    print(ciudades_sin_coordenadas[columna_ciudad].unique())
else:
    print("\nTodas las ciudades tienen coordenadas.")

# Imputar UNIDAD basándose en Ciudad

# Diccionario de mapeo explícito
ciudad_a_unidad = {
    'Ciudad Obregón': 'OBREGON',
    'Navojoa': 'NAVOJOA',
    'Guaymas': 'GUAYMAS',
    'Empalme': 'EMPALME'
}

# Contar cuántos NaN había antes
num_nan_unidad_antes = df['UNIDAD'].isna().sum()

# Imputar valores en UNIDAD solo si está nulo y la ciudad está en el diccionario
df['UNIDAD'] = df.apply(
    lambda row: ciudad_a_unidad[row['Ciudad']] if pd.isna(row['UNIDAD']) and row['Ciudad'] in ciudad_a_unidad else row['UNIDAD'],
    axis=1
)

# Contar cuántos NaN quedan
num_nan_unidad_despues = df['UNIDAD'].isna().sum()
num_imputados = num_nan_unidad_antes - num_nan_unidad_despues

print(f"Se imputaron {num_imputados} valores faltantes en 'UNIDAD' usando la ciudad como referencia.")

# CALCULAR DISTANCIA AL CAMPUS:

# Coordenadas de cada campus
coordenadas_campus = {
    "OBREGON": (27.49213, -109.97236),
    "NAVOJOA": (27.05561, -109.46021),
    "GUAYMAS": (27.96751, -110.91968),
    "EMPALME": (27.96160, -110.79476)
}

# Asegurarte de que las columnas 'Ciudad', 'Latitud', 'Longitud' y 'UNIDAD' existan en el DataFrame
if not all(col in df.columns for col in ['Ciudad', 'Latitud', 'Longitud', 'UNIDAD']):
    raise ValueError("El DataFrame no tiene las columnas necesarias: 'Ciudad', 'Latitud', 'Longitud', y 'UNIDAD'.")

# Crear un diccionario con coordenadas de ciudades válidas
ciudades_coordenadas = {
    ciudad: (lat, lon) for ciudad, lat, lon in zip(df['Ciudad'], df['Latitud'], df['Longitud']) 
    if pd.notnull(lat) and pd.notnull(lon)
}

# Verificar si hay ciudades con coordenadas faltantes
ciudades_sin_coordenadas = set(df['Ciudad']) - set(ciudades_coordenadas.keys())
if ciudades_sin_coordenadas:
    print("Las siguientes ciudades no tienen coordenadas válidas y no se calculará la distancia:")
    print(ciudades_sin_coordenadas)

# Función para calcular la distancia entre la ciudad del estudiante y el campus correspondiente
def calcular_distancia(row):
    ciudad = row['Ciudad']
    unidad = row['UNIDAD']
    
    # Verificar si la ciudad y la unidad tienen coordenadas válidas
    if ciudad in ciudades_coordenadas and unidad in coordenadas_campus:
        coords_ciudad = ciudades_coordenadas[ciudad]
        coords_campus = coordenadas_campus[unidad]
        return geodesic(coords_ciudad, coords_campus).kilometers
    else:
        return None

# Aplicar la función a cada fila del DataFrame
df['Distancia_Campus'] = df.apply(calcular_distancia, axis=1)

# Verificar filas con distancias nulas
distancias_nulas = df[df['Distancia_Campus'].isnull()]
if not distancias_nulas.empty:
    print("Algunas filas tienen distancias nulas. Verificar las ciudades y unidades no mapeadas:")
    print(distancias_nulas[['Ciudad', 'UNIDAD']].drop_duplicates())
else:
    print("Todas las distancias al campus fueron calculadas exitosamente.")

# DETECCION DE OUTLIERS EN DISTANCIA CAMPUS E IMPUTACION DE MODA/MEDIANA SEGUN CAMPUS

# Función para imputar valores de outliers

def imputar_outliers_distancia(df, columna_distancia='Distancia_Campus', columna_unidad='UNIDAD'):
    # Para cada grupo (campus) en la columna UNIDAD
    for campus, grupo in df.groupby(columna_unidad):
        # Calcular el primer y tercer cuartil y el IQR
        Q1 = grupo[columna_distancia].quantile(0.25)
        Q3 = grupo[columna_distancia].quantile(0.75)
        IQR = Q3 - Q1
        
        # Definir los límites inferior y superior (usando el factor 1.5)
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Filtrar los valores que NO son outliers para calcular la moda
        valores_validos = grupo[(grupo[columna_distancia] >= lower_bound) & (grupo[columna_distancia] <= upper_bound)][columna_distancia]
        
        if not valores_validos.empty:
            mode_valores = valores_validos.mode()
            if not mode_valores.empty:
                impute_value = mode_valores.iloc[0]
            else:
                # Si no se encuentra modo, se usa la mediana
                impute_value = valores_validos.median()
        else:
            impute_value = grupo[columna_distancia].median()
        
        # Identificar las filas outlier en este grupo y reemplazarlas
        mask = (df[columna_unidad] == campus) & ((df[columna_distancia] < lower_bound) | (df[columna_distancia] > upper_bound))
        df.loc[mask, columna_distancia] = impute_value
        
        print(f"Para la UNIDAD '{campus}':")
        print(f"  Límite inferior: {lower_bound:.2f}, Límite superior: {upper_bound:.2f}")
        print(f"  Valor imputado: {impute_value:.2f}, Outliers imputados: {mask.sum()}")
        print("-----------------------------------------------------")
        
    return df

# Aplicar la función al DataFrame
df = imputar_outliers_distancia(df)

# Mostrar resumen de la variable después de la imputación
print("Resumen de 'Distancia_Campus' después de la imputación:")
print(df['Distancia_Campus'].describe())

# Eliminar columnas que ya no se necesitan
columnas_a_eliminar = ['Lada', 'P003_O001V', 'P004_O001V']
df.drop(columns=columnas_a_eliminar, inplace=True, errors='ignore')

# Verificar que se eliminaron
print(f"Columnas eliminadas: {', '.join(columnas_a_eliminar)}")
print(f"Columnas restantes en el DataFrame: {df.shape[1]}")

# INSPECCION ANTES DE INICIAR CONVERSIÓN DEL TIPO DE DATOS E IMPUTACION DE VALORES

# Obtener una visión general rápida de la estructura del df,  tipo de datos, y el uso de memoria.
df.info()

# Obtener listas de columnas por tipo de dato
float64_columns = df.select_dtypes(include='float64').columns
int64_columns = df.select_dtypes(include='int64').columns
object_columns = df.select_dtypes(include='object').columns

print(f"Columnas float64 ({len(float64_columns)}):")
print(float64_columns.tolist())

print(f"\nColumnas int64 ({len(int64_columns)}):")
print(int64_columns.tolist())

print(f"\nColumnas object ({len(object_columns)}):")
print(object_columns.tolist())


# 1. Convertir una columna de tipo object a tipo string e imputar No aplica y Desconocido
# Lista de columnas a convertir a tipo string
columns_to_convert = [
    'EMPLID', 'CARRERA', 'UNIDAD', 'GENERO', 'Ciudad',
    'Estado', 'P052_O010V', 'P047_O008V', 'P006_O008V',
    'P006_O009V', 'P010_O002V', 'P060_O002V', 'P005_O002V'
]

# Identificar valores perdidos en las columnas especificadas antes de la conversión
missing_values_before_conversion = df[columns_to_convert].isna().sum()

# Mostrar valores perdidos antes de la conversión
print("\nValores perdidos en las columnas especificadas antes de la conversión:")
print(missing_values_before_conversion[missing_values_before_conversion > 0])

# Imputación de valores para columnas específicas
# Columnas a rellenar con "No aplica" por ser las opciones de "Especifica" (preguntas abiertas)
columns_no_aplica = [
    'P006_O008V', 'P006_O009V', 'P052_O010V', 'P047_O008V',
    'P060_O002V', 'P010_O002V', 'P005_O002V'
]

# Columnas a rellenar con "Desconocido" 
columns_desconocido = [
    'EMPLID', 'CARRERA', 'UNIDAD', 'GENERO', 'Ciudad', 'Estado'
]

# Rellenar valores nulos con "No aplica"
df[columns_no_aplica] = df[columns_no_aplica].fillna("No aplica")

# Rellenar valores nulos con "Desconocido"
df[columns_desconocido] = df[columns_desconocido].fillna("Desconocido")

# Convertir todas las columnas a tipo string después de la imputación
df[columns_to_convert] = df[columns_to_convert].astype('string')

# Identificar valores imputados con "No aplica"
conteo_no_aplica = (df[columns_no_aplica] == "No aplica").sum()

# Identificar valores imputados con "Desconocido"
conteo_desconocido = (df[columns_desconocido] == "Desconocido").sum()

# Mostrar resultados
print("\nImputación completada:")
print("Total de valores imputados con 'No aplica' por columna (por ser las opciones de respueste en preguntas donde pide Especificar):")
print(conteo_no_aplica[conteo_no_aplica > 0])

print("\nTotal de valores imputados con 'Desconocido' por columna (valores nulos):")
print(conteo_desconocido[conteo_desconocido > 0])

# Verificar si todavía hay valores perdidos
missing_values_after_imputation = df[columns_to_convert].isna().sum()
if missing_values_after_imputation.sum() > 0:
    print("\nAún hay valores perdidos en las columnas después de la imputación:")
    print(missing_values_after_imputation[missing_values_after_imputation > 0])
else:
    print("\nNo hay valores perdidos después de la imputación.")

# 2. Convertir la columna 'Año' a formato de fecha
# Identificar y mostrar valores perdidos en la columna 'Año' antes de la conversión
missing_values_before = df['Año'].isna().sum()
print(f"\nValores perdidos en la columna 'Año' antes de la conversión: {missing_values_before}")

# Convertir la columna 'Año' a formato de fecha
df['Año'] = pd.to_datetime(df['Año'].astype(str) + '-01-01', format='%Y-%m-%d', errors='coerce').dt.year

# Identificar y mostrar valores perdidos en la columna 'Año' después de la conversión
missing_values_after = df['Año'].isna().sum()
print(f"\nValores perdidos en la columna 'Año' después de la conversión: {missing_values_after}")

# Verificar el tipo de dato y las primeras filas
print("\nTipo de dato de la columna 'Año':", df['Año'].dtype)
print("\nMuestra de las primeras filas de la columna 'Año' para confirmar:")
print(df['Año'].head())

import numpy as np

# 3.Imputar con 0 las respuestas a las preguntas: P008_O002V (Cuantos cigarrillos fumas); P013_O001V (Cuantas horas trabajas); P018_O002V (Cuantos hijos tienes)

cols_to_impute = ['P008_O002V', 'P013_O001V', 'P018_O002V']
for col in cols_to_impute:
    # Verificar valores perdidos antes de la imputación
    missing_before = df[col].isna().sum()
    print(f"\n Columna '{col}':")
    print(f"Valores perdidos antes de la imputación: {missing_before}")
    
    # Mostrar valores únicos no nulos antes de imputar
    print(f"Valores únicos antes de imputar:")
    print(df[col].dropna().unique())

    # Reemplazar valores no numéricos o vacíos por NaN
    df[col] = df[col].replace(['---', 'N/A', 'n/a', 's/n', '', ' '], np.nan)

    # Imputar valores NaN con 0
    df[col] = df[col].fillna(0)

    # Convertir a tipo numérico
    df[col] = pd.to_numeric(df[col], errors='coerce')

    # Verificar valores perdidos después de la imputación y conversión
    missing_after = df[col].isna().sum()
    print(f"Valores perdidos después de la imputación: {missing_after}")

# Verificar los tipos de datos después de la conversión
int64_columns = df.select_dtypes(include='int64').columns
print(f"\nColumnas int64 ({len(int64_columns)}): {int64_columns.tolist()}")

# LIMPIEZA DE VALORES EXTREMOS (datos irreales o errores de captura en las tres columnas anteriores)

# Función para limpiar valores extremos
def limpiar_valores_irreales(df):

    # P008_O002V – cigarrillos por día
    df['P008_O002V'] = df['P008_O002V'].astype(str).str.lstrip('0')  # eliminar ceros a la izquierda
    df['P008_O002V'] = pd.to_numeric(df['P008_O002V'], errors='coerce')
    df.loc[df['P008_O002V'] > 40, 'P008_O002V'] = np.nan  # umbral razonable
    df['P008_O002V'] = df['P008_O002V'].fillna(0).astype(int)

    # P013_O001V – horas trabajadas
    df['P013_O001V'] = pd.to_numeric(df['P013_O001V'], errors='coerce')
    df.loc[df['P013_O001V'] > 84, 'P013_O001V'] = np.nan  # máx 12 h/día x 7 días
    df['P013_O001V'] = df['P013_O001V'].fillna(0).astype(int)

    # P018_O002V – hijos
    df['P018_O002V'] = df['P018_O002V'].astype(str).str.lstrip('0')
    df['P018_O002V'] = pd.to_numeric(df['P018_O002V'], errors='coerce')
    df.loc[df['P018_O002V'] > 10, 'P018_O002V'] = np.nan
    df['P018_O002V'] = df['P018_O002V'].fillna(0).astype(int)

    return df

# Aplicar limpieza
df = limpiar_valores_irreales(df)

# Verificar
for col in ['P008_O002V', 'P013_O001V', 'P018_O002V']:
    print(f"\n{col} después de limpiar:")
    print(df[col].describe())


# 4. Rellenar Valores Nulos para el resto de las variables

# Identificar columnas con valores nulos
columnas_con_nulos = df.columns[df.isnull().any()]

# Contadores por tipo de imputación
cols_imputadas_cero = []
cols_imputadas_NA = []
cols_imputadas_desconocido = []
cols_imputadas_moda = []

# Guardar la columna ETNIA antes de la imputación
df_etnia = df[['ETNIA']].copy()

# Rellenar valores nulos según grupo
for col in columnas_con_nulos:  
    if col in ['P014_O001V', 'P015_O002V', 'P015_O001V', 'P015_O003V', 'P015_O004V',
               'P015_O005V', 'P016_O001V', 'P043_O001V', 'P042_O001V', 'P027_O001V', 'P027_O002V',
               'P027_O003V', 'P027_O004V', 'P027_O005V', 'P027_O006V', 'P027_O007V',
               'P027_O008V', 'P027_O009V', 'P027_O010V', 'P027_O011V', 'P027_O012V',
               'P027_O013V', 'P027_O014V', 'P026_O001V', 'P024_O001V', 'P024_O002V',
               'P018_O001V', 'P044_O001V', 'P008_O001V', 'P009_O001V', 'P007_O001V',
               'P010_O001V', 'P006_O001V', 'P006_O002V', 'P006_O003V', 'P006_O004V',
               'P051_O001V', 'P051_O002V', 'P051_O003V', 'P051_O004V', 'P051_O005V',  
               'P006_O005V', 'P006_O006V', 'P006_O007V', 'P019_O001V']:
        df[col] = df[col].fillna("0")
        cols_imputadas_cero.append(col)

    elif col in ['P011_O001V', 'P017_O001V', 'P039_O001V', 'P048_O001V', 'P048_O002V', 
                 'P048_O003V', 'P048_O004V', 'P048_O005V', 'P048_O006V']:
        df[col] = df[col].fillna("NA")
        cols_imputadas_NA.append(col)

    elif col in ['P057_O001V', 'P058_O001V', 'P059_O001V', 'P059_O002V', 'P060_O001V', 
                 'P020_O001V', 'P022_O001V']:
        df[col] = df[col].fillna("Desconocido")
        cols_imputadas_desconocido.append(col)

    else:
        mode_value = df[col][df[col] != 0].mode(dropna=True).iloc[0] if not df[col][df[col] != 0].mode(dropna=True).empty else None
        if mode_value is not None:
            df[col] = df[col].fillna(mode_value)
            cols_imputadas_moda.append(col)

# Restaurar ETNIA
df['ETNIA'] = df_etnia['ETNIA']

# Verificación
print("\nTipos de imputación aplicados:")
print(f"Columnas imputadas con '0': {len(cols_imputadas_cero)} → {cols_imputadas_cero}")
print(f"Columnas imputadas con 'NA': {len(cols_imputadas_NA)} → {cols_imputadas_NA}")
print(f"Columnas imputadas con 'Desconocido': {len(cols_imputadas_desconocido)} → {cols_imputadas_desconocido}")
print(f"Columnas imputadas con moda (sin considerar 0): {len(cols_imputadas_moda)} → {cols_imputadas_moda}")

# Verificación de nulos
print("\nValores nulos en 'ETNIA' después de la imputación (no debe cambiarse):", df['ETNIA'].isna().sum())

nulos_restantes = df.isna().sum()
nulos_finales = nulos_restantes[nulos_restantes > 0]

if nulos_finales.empty:
    print("No hay columnas con valores nulos después de la imputación.")
else:
    print("Aún hay columnas con valores nulos:")
    print(nulos_finales)

# 4. Cambiar el dato numérico de las respuestas 'No' con valor de 2, a valor de 0 (columnas: 'P005_O001V', 'P007_O001V', 'P008_O001V', 'P012_O001V', 'P018_O001V', 'P026_O001V', 'P042_O001V', 'P043_O001V') para mantener consistencia

# Lista de columnas que contienen las respuestas
columnas_respuestas = ['P005_O001V', 'P007_O001V', 'P008_O001V', 'P012_O001V', 
                       'P018_O001V', 'P026_O001V', 'P042_O001V', 'P043_O001V',
                       'P051_O001V', 'P051_O002V', 'P051_O003V', 'P051_O004V', 'P051_O005V']

# Reemplazar los valores de 2 por 0 en las columnas especificadas
df[columnas_respuestas] = df[columnas_respuestas].replace(2, 0)

# Verificar cuántas filas fueron afectadas por la actualización
filas_afectadas = df[columnas_respuestas].shape[0]
print(f"Filas afectadas: {filas_afectadas}")

# 5. Cambiar el dato numerico de las respuestas 'No aplica' con valor de 5, a valor de 0 (columnas: 'P055_O001V', 'P055_O002V', P055_O003V', 'P055_O004V', 'P055_O005V') ##

# Lista de columnas a modificar
columnas = ['P055_O001V', 'P055_O002V', 'P055_O003V', 'P055_O004V', 'P055_O005V']

# Cambiar el valor numérico 5 a 0 donde el valor es 'No aplica'
for columna in columnas:
    df[columna] = df[columna].replace(5, 0)

# Verificar cuántas filas fueron afectadas por la actualización
filas_afectadas = df[columnas].shape[0]
print(f"Filas afectadas: {filas_afectadas}")

# 6. Cambiar el dato numérico de las respuestas 'No había' con valor de 5, a valor de 0 (preguntas: 'P048_O001V', 'P048_O002V', 'P048_O003V', 'P048_O004V', 'P048_O005V', 'P048_O006V') ##

# Lista de columnas a actualizar
columnas = ['P048_O001V', 'P048_O002V', 'P048_O003V', 'P048_O004V', 'P048_O005V', 'P048_O006V']

# Cambiar valor 5 a 0 solo si el valor es 5 en las columnas especificadas
for columna in columnas:
    df[columna] = df[columna].replace(5, 0)

# Verificar cuántas filas fueron afectadas por la actualización
filas_afectadas = df[columnas].shape[0]
print(f"Filas afectadas: {filas_afectadas}")

# 7. Cambiar el dato numérico de las respuestas 'Lo ignoro' con valor de 13 a valor de 0
columns_to_update = ['P024_O001V', 'P024_O002V']

for column in columns_to_update:
    df[column] = df[column].replace(13, 0)

# Verificar cuántas filas fueron afectadas por la actualización
filas_afectadas = df[columns_to_update].shape[0]
print(f"Filas afectadas: {filas_afectadas}")

# 8. Cambiar el dato numérico de las respuestas 'No aplica' con valor de -1, a valor de 0 (columnas: 'P014_O001V', 'P016_O001V')                                                                                                                                        # Lista de columnas a modificar
columnas = ['P014_O001V', 'P016_O001V']

# Cambiar el valor numérico 5 a 0 donde el valor es 'No aplica'
for columna in columnas:
    df[columna] = df[columna].replace(-1, 0)

# Verificar cuántas filas fueron afectadas por la actualización
filas_afectadas = df[columnas].shape[0]
print(f"Filas afectadas: {filas_afectadas}")

# 9. AJUSTAR DATOS ABERRANTES EN EL CAMPO DE EDAD (EDAD > 80 o EDAD < 15)
# 1) Calcular la moda de la columna EDAD 
mode_edad = df['EDAD'].mode(dropna=True)[0]  # Toma el primer valor si hay varias modas

# 2) Contar cuántos outliers se van a imputar
outliers_mask = (df['EDAD'] < 15) | (df['EDAD'] > 80)
num_outliers = df[outliers_mask].shape[0]
print(f"Registros con valores de EDAD fuera de [15, 80]: {num_outliers}")

# 3) Reemplazar (imputar) la edad con la moda para esos registros
df.loc[outliers_mask, 'EDAD'] = mode_edad

# 4) Verificar resultado
print("Número de registros después de imputar outliers:", df.shape[0])
print(df['EDAD'].describe())

# CLASIFICACIÓN DE CARRERAS

# Definir listas manuales
programas_condicionados = ["PLEIN", "PLPSIC", "PICIA","PIIS ","PLA","PLCP","PINSO","PIMEC","PLEI","PLAET","PLCIE","PLDG","PLEF","PIBS","PIELM","PLTAL","PLARQ","PIETR","PIMAN","PLGDA","PPADI","PMVZO","PCIEF","PLDCF","PLED"]  # Agregar más

# Clasificación por condición (aceptado/condicionado) y nivel (lic, ing, etc.)
def clasificar_programa(codigo):
    """
    Devuelve:
    - CATEGORIA_CARRERA: Condicionado / Aceptado
    - NIVEL_CARRERA: Licenciatura, Ingeniería, Profesional Asociado, Desconocido
    - RISK_CARRERA: número arbitrario para representar mayor riesgo en condicionados
    """
    codigo = str(codigo).strip().upper()

    # Clasificación por condición
    categoria = "Condicionado" if codigo in programas_condicionados else "Aceptado"
    riesgo = 1 if categoria == "Condicionado" else 0

    # Clasificación por nivel de carrera (puedes ajustar o expandir reglas)
    if codigo.startswith("I") or "ING" in codigo:
        nivel = "Engineering program"
    elif codigo.startswith("L") or codigo.startswith("ARQ") or codigo.startswith("MVZ"):
        nivel = "Bachelor's degree"
    elif codigo.startswith("PA"):
        nivel = "Associate degree"
    else:
        nivel = "Desconocido"

    return categoria, nivel, riesgo

# Desfragmentar el DataFrame antes de agregar nuevas columnas
df = df.copy()

# Aplicar clasificación a la columna CARRERA
df[['CATEGORIA_CARRERA', 'NIVEL_CARRERA', 'RISK_CARRERA']] = df['CARRERA'].astype(str).apply(
    lambda x: pd.Series(clasificar_programa(x))
)

# Verificación resultado
print(f"Columnas en el DataFrame: {df.shape[1]}")
print(df[['CARRERA', 'CATEGORIA_CARRERA', 'NIVEL_CARRERA', 'RISK_CARRERA']].head())

# UNIFICACIÓN  DE CARRERAS

# Diccionario de agrupación
agrupaciones = {
    "LEI": ["LEIN", "LEI", "PLEIN", "PLEI"],
    "IIS": ["PIIS", "IISIS"],
    "LA": ["PLA", "LADMI"],
    "LPS": ["LPSIC", "LPSC", "PLPSI"],
    "LCOPU": ["LCP", "PLCP"],
    "ISW": ["INSOF", "PINSO"],
    "IC": ["ICIVI", "PICIA", "PIC"],
    "IEM": ["PIMEC", "IMECA"], 
    "IELME": ["PIELM"],      
    "LCE": ["LCIED", "PLED"], 
    "MVZ": ["MVZOO", "PMVZO"], 
    "LAET": ["LADTU", "PLAET"], 
    "LCEF": ["LCIEF", "PLCIE", "PCIEF"], 
    "LDG": ["LDIGR", "PLDG"], 
    "LEF": ["LECFI", "PLEF"], 
    "IB": ["IBIOT"], 
    "IQ": ["IQUIM", "PIQ"], 
    "IBS": ["IBIOS", "PIBS"], 
    "ICA": ["ICIAM"], 
    "LTA": ["LTALI", "PLTAL"], 
    "ARQ": ["LARQ", "PLARQ"], 
    "IE": ["IETRO", "PIETR"], 
    "LDCFD": ["PLDCF"], 
    "IMAN": ["PIMAN"], 
    "LGDA": ["LGDAR", "PLGDA"], 
    "PADIN": ["PPADI"],
    # Programas sin grupo
    "LENF": ["LENF"], "LG": ["LG"], "LEM": ["LEM"], "IL": ["IL"], "LEAGC": ["LEAGC"], "LEIGI": ["LEIGI"], 
    "PAAI": ["PAAI"], "LDER": ["LDER"], "LAES": ["LAES"]
}

# Función para unificar nombres de carrera
def unificar_nombre(carrera):
    carrera = str(carrera).strip().upper()
    for nombre_unificado, variantes in agrupaciones.items():
        if carrera in [v.strip().upper() for v in variantes] or carrera == nombre_unificado:
            return nombre_unificado
    return carrera

# Función para clasificar área disciplinar
def clasificar_area(carrera):
    carrera = str(carrera).strip().upper()
    ingenierias = ['LDG','ISW','IE','IIS','IC','ARQ','IEM','IL','PIMAN','INSOF','PLDG','PLARQ','PINSO','PIMEC','PMAN','PIIS','PIETR','PIELM','PICIA','PIC','PAAI','LDIGR','LARQ','IMAN','IISIS','IETRO','IELME']
    sociales_humanidades = ['LPS','LCE','LCEF','PLGDA','LGDA','PLED','LPSC','LEIN','LEIGI','LEAGC','LDER','PPADI','PLPSI','PLEIN','PLEI','PLDCF','PLCIE','PCIEF','PADIN','LEI','LDCFD','LCIED','LPSIC','LADMI']
    naturales = ['LTA','IQ','IBS','ICA''IB','LENF','PMVZO','PLTAL','PIQ','PIBS','MVZ','LTALI','IQUIM','ICIAM','IBIOT','IBIOS']
    economico_admin = ['LEF','LA','LAET','LEM','LCP','LAES','PLEF','PLCP','PLAET','PLA','LG','LECFI','LCOPU','LCIEF','LADTU']

    if carrera in ingenierias:
        return 'Engineering and Technology'
    elif carrera in sociales_humanidades:
        return 'Social Sciences and Humanities'
    elif carrera in naturales:
        return 'Natural Resources'
    elif carrera in economico_admin:
        return 'Business & Economics'
    else:
        return 'Desconocido'

# Aplicar funciones
carrera_unificada = df["CARRERA"].astype(str).apply(unificar_nombre)
area_carrera = carrera_unificada.apply(clasificar_area)

# Reemplazar columna y evitar duplicados
cols_to_drop = [c for c in ['CARRERA', 'AREA_CARRERA'] if c in df.columns]
df = pd.concat([
    df.drop(columns=cols_to_drop),
    carrera_unificada.rename("CARRERA"),
    area_carrera.rename("AREA_CARRERA")
], axis=1)

# Desfragmentar el DataFrame para evitar warnings de rendimiento
df = df.copy()

# Verificación
print("\nVerificación de unificación de carrera y clasificación disciplinar:")
print(df[['CARRERA', 'AREA_CARRERA']].head())

# MUESTRA TOTAL DE REGISTROS EN EL DATAFRAME ##

# Contar registros por año
conteo_por_anio = df['Año'].value_counts().sort_index()

# Mostrar resultados
print("Conteo de registros por año en el dataframe:")
print(conteo_por_anio)

# ACTUALIZAR DF CON CAMBIOS (RECODIFICACION Y TRATAMIENTO DE VALORES NULOS) ##
# Guardar el dataframe combinado en un archivo nuevo
df.to_csv(os.path.join(folder_path, 'combined.csv'), index=False)

print(f"Columnas en el DataFrame: {df.shape[1]}")

# --- Extracted from 2. Normalización de variables.ipynb ---
# 1) CARGAR EL DATAFRAME COMBINADO Y DETECTAR COLUMNAS CON MEZCLA DE TIPOS

import pandas as pd

# Cargar con low_memory=False para evitar advertencias durante la inferencia de tipos
df = pd.read_csv('data/combined.csv', low_memory=False)

# Verificar el dataframe cargado:
filas_cargadas = df.shape[0]  # obtener el número de filas cargadas
print(f"DataFrame cargado: {filas_cargadas} filas.")
print(f"Columnas en el DataFrame: {df.shape[1]}")

# Detectar columnas con mezcla de tipos usando 'object' que deberían ser numéricas
mixed_type_cols = []

for col in df.columns:
    # Si tiene más de un tipo de dato (ej. int y str)
    tipos = df[col].map(type).value_counts()
    if len(tipos) > 1:
        mixed_type_cols.append((col, tipos))

# Mostrar un resumen
if mixed_type_cols:
    print("Columnas con tipos de datos mezclados detectadas:")
    for col, tipos in mixed_type_cols:
        print(f"Columna: '{col}' - Tipos detectados: {tipos.to_dict()}")
else:
    print("No se detectaron columnas con tipos de datos mezclados.")

# FASE 3. NORMALIZACION O ESTANDARIZACION (PREPARACION PARA EL MACHINE LEARNING)

#  0) VARIABLES CATEGORICAS (CADENAS DE TEXTO)

# GENERO: En la realidad de ITSON las mujeres (F) desertan menos que los hombres (M), por lo que se esperaría que tienen menor riesgo de deserción.
df['GENERO'] = df['GENERO'].astype(str).str.upper().map({'F': 0, 'M': 1})

# CARRERA: Se cree que un alumno condicionado tiene mayor riesgo de deserción.

# Verificación resultado
print(f"Columnas en el DataFrame: {df.shape[1]}")
print(df[['GENERO', 'CARRERA', 'RISK_CARRERA']].head())

import numpy as np

# 1. Convertir una columna de tipo object a tipo string e imputar No aplica y Desconocido
# Lista de columnas a convertir a tipo string
columns_to_convert = [
    'EMPLID', 'CARRERA', 'UNIDAD', 'Ciudad', 
    'Estado', 'P052_O010V', 'P047_O008V', 'P006_O008V',
    'P006_O009V', 'P010_O002V', 'P060_O002V', 'P005_O002V'
]

# Imputación de valores para columnas específicas (ya imputadas en el notebook anterior)
# Columnas a rellenar con "No aplica" por ser las opciones de "Especifica" (preguntas abiertas)
columns_no_aplica = [
    'P006_O008V', 'P006_O009V', 'P052_O010V', 'P047_O008V',
    'P060_O002V', 'P010_O002V', 'P005_O002V'
]

# Columnas a rellenar con "Desconocido" 
columns_desconocido = [
    'EMPLID', 'CARRERA', 'UNIDAD', 'GENERO', 'Ciudad', 'Estado'
]

# Rellenar valores nulos con "No aplica"
df[columns_no_aplica] = df[columns_no_aplica].fillna("No aplica")

# Rellenar valores nulos con "Desconocido"
df[columns_desconocido] = df[columns_desconocido].fillna("Desconocido")

# Convertir todas las columnas a tipo string después de la imputación
df[columns_to_convert] = df[columns_to_convert].astype('string')


# 2.Imputar con 0 las respuestas a las preguntas: P008_O002V (Cuantos cigarrillos fumas); P013_O001V (Cuantas horas trabajas); P018_O002V (Cuantos hijos tienes)

cols_to_impute = ['P008_O002V', 'P013_O001V', 'P018_O002V']
for col in cols_to_impute:
    # Verificar valores perdidos antes de la imputación
    missing_before = df[col].isna().sum()
    
    # Mostrar valores únicos no nulos antes de imputar

    # Reemplazar valores no numéricos o vacíos por NaN
    df[col] = df[col].replace(['---', 'N/A', 'n/a', 's/n', '', ' '], np.nan)

    # Imputar valores NaN con 0
    df[col] = df[col].fillna(0)

    # Convertir a tipo numérico
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 3. Rellenar Valores Nulos para el resto de las variables

# Identificar columnas con valores nulos
columnas_con_nulos = df.columns[df.isnull().any()]

# Contadores por tipo de imputación
cols_imputadas_cero = []
cols_imputadas_NA = []
cols_imputadas_desconocido = []
cols_imputadas_moda = []

# Guardar la columna ETNIA antes de la imputación
df_etnia = df[['ETNIA']].copy()

# Rellenar valores nulos según grupo
for col in columnas_con_nulos:  
    if col in ['P014_O001V', 'P015_O002V', 'P015_O001V', 'P015_O003V', 'P015_O004V',
               'P015_O005V', 'P016_O001V', 'P043_O001V', 'P042_O001V', 'P027_O001V', 'P027_O002V',
               'P027_O003V', 'P027_O004V', 'P027_O005V', 'P027_O006V', 'P027_O007V',
               'P027_O008V', 'P027_O009V', 'P027_O010V', 'P027_O011V', 'P027_O012V',
               'P027_O013V', 'P027_O014V', 'P026_O001V', 'P024_O001V', 'P024_O002V',
               'P018_O001V', 'P044_O001V', 'P008_O001V', 'P009_O001V', 'P007_O001V',
               'P010_O001V', 'P006_O001V', 'P006_O002V', 'P006_O003V', 'P006_O004V', 
               'P006_O005V', 'P006_O006V', 'P006_O007V', 'P019_O001V']:
        df[col] = df[col].fillna("0")
        cols_imputadas_cero.append(col)

    elif col in ['P051_O001V', 'P051_O002V', 'P051_O003V', 'P051_O004V', 'P051_O005V', 
                 'P011_O001V', 'P017_O001V', 'P039_O001V', 'P048_O001V', 'P048_O002V', 
                 'P048_O003V', 'P048_O004V', 'P048_O005V', 'P048_O006V']:
        df[col] = df[col].fillna("NA")
        cols_imputadas_NA.append(col)

    elif col in ['P057_O001V', 'P058_O001V', 'P059_O001V', 'P059_O002V', 'P060_O001V', 
                 'P020_O001V', 'P022_O001V']:
        df[col] = df[col].fillna("Desconocido")
        cols_imputadas_desconocido.append(col)

    else:
        mode_value = df[col][df[col] != 0].mode(dropna=True).iloc[0] if not df[col][df[col] != 0].mode(dropna=True).empty else None
        if mode_value is not None:
            df[col] = df[col].fillna(mode_value)
            cols_imputadas_moda.append(col)

# Restaurar ETNIA
df['ETNIA'] = df_etnia['ETNIA']

# Verificación
nulos_restantes = df.isna().sum()
nulos_finales = nulos_restantes[nulos_restantes > 0]

if nulos_finales.empty:
    print("No hay columnas con valores nulos después de la imputación.")
else:
    print("Aún hay columnas con valores nulos:")
    print(nulos_finales)

# 1) VARIABLES CUALITATIVAS NOMINALES A CODIFICAR CON ONE HOT ENCODING

# Lista  de variables categóricas nominales (con varias respuestas)
variables_categoricas = list(set([
    'P009_O001V', 'P010_O001V', 'P014_O001V', 'P017_O001V', 'P020_O001V', 'P022_O001V', 'P025_O001V', 'P031_O001V', 'P031_O002V', 'P031_O003V', 
    'P032_O001V', 'P032_O002V', 'P032_O003V', 'P053_O001V', 
    'P054_O001V', 'P058_O001V', 'P060_O001V', 
]))

# Verificar valores nulos solo en las variables categóricas seleccionadas
valores_nulos_categoricas = df[variables_categoricas].isnull().sum()
columnas_con_nulos_categoricas = valores_nulos_categoricas[valores_nulos_categoricas > 0]

# Mensaje claro según el resultado
if columnas_con_nulos_categoricas.empty:
    print("Las variables categóricas seleccionadas para One Hot Encoding no tienen valores nulos.")
else:
    print("Las siguientes variables categóricas tienen valores nulos y podrían causar errores en One Hot Encoding:")
    print(columnas_con_nulos_categoricas)

# Conteo de otros valores nulos en el dataframe
valores_nulos = df.isnull().sum()
columnas_con_nulos = valores_nulos[valores_nulos > 0]
if columnas_con_nulos.empty:
    print("No hay columnas con valores nulos en otras columnas del DataFrame")
else:
    print("Número de valores nulos en otras columnas del DataFrame:")
    print(columnas_con_nulos)

# Contar número de columnas antes del One-Hot Encoding
num_columnas_antes = df.shape[1]
print(f"Número de columnas antes del One-Hot Encoding: {num_columnas_antes}")

# Guardar nombres de columnas antes del One-Hot Encoding
columnas_antes = set(df.columns)

# Codificar las variables categóricas (One-Hot Encoding)
variables_categoricas_presentes = [col for col in variables_categoricas if col in df.columns]

for columna in variables_categoricas_presentes:
    dummies = pd.get_dummies(df[columna], prefix=columna, drop_first=False)
    df = pd.concat([df, dummies], axis=1)
    df.drop(columna, axis=1, inplace=True)

# Guardar nombres de columnas después del One-Hot Encoding
columnas_despues = set(df.columns)

# Determinar columnas nuevas creadas por el One-Hot Encoding
columnas_creadas = columnas_despues - columnas_antes

print(f"Columnas nuevas creadas ({len(columnas_creadas)}):")
print(sorted(columnas_creadas))

# Contar número de columnas después del One-Hot Encoding
num_columnas_despues = df.shape[1]
nuevas_columnas = num_columnas_despues - num_columnas_antes
print(f"Número de columnas nuevas agregadas (no repetidas): {nuevas_columnas}")
print(f"Número total de columnas después del One-Hot Encoding: {num_columnas_despues}")

# Verificar valores nulos después de la codificación
valores_nulos_actualizados = df.isnull().sum()
valores_nulos_presentes = valores_nulos_actualizados[valores_nulos_actualizados > 0]

print("\nNúmero de valores nulos en el DataFrame después de la codificación:")
print(valores_nulos_presentes if not valores_nulos_presentes.empty else "No hay valores nulos.")

# Buscar columnas candidatas para conversión a entero
columnas_a_convertir = []

for col in df.columns:
    valores_unicos = df[col].dropna().unique()
    
    # Si todos los valores son booleanos, 0, 1 o '0', '1', se considera dummy
    if set(valores_unicos).issubset({0, 1, True, False, '0', '1'}):
        columnas_a_convertir.append(col)

# Convertir a entero
for col in columnas_a_convertir:
    # Reemplazar valores nulos con un valor predeterminado antes de la conversión
    df[col] = df[col].fillna(0).astype(int)

# Verificación
print(f"Se convirtieron {len(columnas_a_convertir)} columnas a enteros.")
print(df[columnas_a_convertir].dtypes)

# 2) VARIABLES CUALITATIVAS ORDINALES

# Definir las columnas con las variables ordinales 
columns_to_check = list(set([
    'P011_O001V', 'P016_O001V', 'P019_O001V', 'P021_O001V', 'P023_O001V', 'P024_O001V', 
    'P024_O002V', 'P028_O001V', 'P029_O001V', 'P030_O001V', 'P033_O001V', 
    'P033_O002V', 'P033_O003V', 'P033_O004V', 'P033_O005V', 'P033_O006V', 'P033_O007V',
    'P033_O008V', 'P033_O009V', 'P033_O010V',
    'P034_O001V', 'P034_O002V', 'P034_O003V', 'P034_O004V', 'P034_O005V', 'P034_O006V', 
    'P034_O007V', 'P034_O008V', 'P034_O009V', 'P035_O001V', 'P035_O002V', 'P035_O003V', 
    'P035_O004V', 'P035_O005V', 'P036_O001V', 'P036_O002V', 'P036_O003V', 'P036_O004V', 
    'P036_O005V', 'P036_O006V', 'P036_O007V', 'P038_O001V', 'P040_O001V', 'P040_O002V', 
    'P045_O001V', 'P048_O001V', 'P048_O002V', 'P048_O003V', 'P048_O004V',
    'P048_O005V', 'P048_O006V', 'P049_O001V', 'P049_O002V', 'P049_O003V', 'P049_O004V', 
    'P049_O005V', 'P049_O006V', 'P049_O007V', 'P049_O008V', 'P049_O009V', 'P049_O010V', 
    'P049_O011V', 'P055_O001V', 'P055_O002V', 'P055_O003V', 'P055_O004V', 'P055_O005V',
    'P057_O001V', 'P059_O001V', 'P059_O002V', 'P039_O001V'
]))

# 1. Verificar valores nulos exclusivamente en esas columnas
nulos_ordinales = df[columns_to_check].isnull().sum()
columnas_con_nulos_ordinales = nulos_ordinales[nulos_ordinales > 0]

# Mensaje  según el resultado
if columnas_con_nulos_ordinales.empty:
    print("Las variables ordinales no tienen valores nulos.")
else:
    print("Las siguientes variables ordinales tienen valores nulos y podrían requerir imputación:")
    print(columnas_con_nulos_ordinales)

# Conteo de otros valores nulos en el dataframe
valores_nulos = df.isnull().sum()
columnas_con_nulos = valores_nulos[valores_nulos > 0]
if columnas_con_nulos.empty:
    print("No hay columnas con valores nulos en otras columnas del DataFrame")
else:
    print("Número de valores nulos en otras columnas del DataFrame:")
    print(columnas_con_nulos)

# 2. Reemplazar 'NA', 'Desconocido', o cualquier valor no válido por un valor válido (moda)
variables_sin_mapeo = list(set([
    'P011_O001V', # ¿Con qué frecuencia has perdido la noción del tiempo y después no recuerdas nada?
    'P039_O001V', # ¿Cómo valoras el desempeño de tus profesores del bachillerato?
    'P048_O002V', 'P048_O003V', 'P048_O004V', 'P048_O005V', 'P048_O006V', # ¿Con qué frecuencia utilizabas en el bachillerato los siguientes servicios?
    'P057_O001V', # ¿Cómo consideras tus posibilidades de encontrar trabajo relacionado con tu profesión?
    'P059_O001V', 'P059_O002V', # ¿Cómo percibes el desarrollo de tu vida profesional, una vez que concluyas tus estudios de licenciatura?
]))

for col in variables_sin_mapeo:
    if col in df.columns:
        if df[col].dtype == 'object':
            # Reemplaza 'NA' y 'Desconocido' con pd.NA
            df[col] = df[col].replace(['NA', 'Desconocido'], pd.NA)
            moda = df[col].mode(dropna=True)
            if not moda.empty:
                df[col] = df[col].fillna(moda[0])
            else:
                df[col] = df[col].fillna("Otro")
        else:
            # Asegura tipo numérico y reemplaza NaN con la moda
            df[col] = pd.to_numeric(df[col], errors='coerce')
            moda = df[col].mode(dropna=True)
            if not moda.empty:
                df[col] = df[col].fillna(moda[0])
            else:
                df[col] = df[col].fillna(0)

# Verificar los valores únicos después del reemplazo
print(df[variables_sin_mapeo].isnull().sum())
print("\nValores únicos en las columnas después de reemplazo:")
for column in variables_sin_mapeo:
    print(f"{column}: {df[column].unique()}")

# 3. Verificar el rango de los valores en las variables ordinales
for column in columns_to_check:
    df[column] = pd.to_numeric(df[column], errors='coerce')  # Convierte a numérico, y pone NaN en valores no convertibles
print("\nVerificación del rango de valores en las columnas ordinales después de la conversión:")
for column in columns_to_check:
    min_value = df[column].min()
    max_value = df[column].max()
    print(f"{column}: Min = {min_value}, Max = {max_value}")

# 4. Importar y crear un objeto MinMaxScaler
from sklearn.preprocessing import MinMaxScaler

# Crear un objeto MinMaxScaler
scaler = MinMaxScaler()

# Aplicar el MinMaxScaler solo a las columnas ordinales
df[columns_to_check] = scaler.fit_transform(df[columns_to_check])

# Verificar los primeros registros para confirmar la normalización
print(df[columns_to_check].head())

# Verificar los resultados después de la codificación ordinal
print("\nVerificación de los valores después de Ordinal Encoding:")
for column in columns_to_check:
    print(f"{column}: {df[column].unique()}")

#  3) VARIABLES CUANTITATIVAS
### Normalización (rango 0 a 1) de variables cuantitativas

# Asegurar consistencia en P013_O001V: si NO trabaja, entonces horas trabajadas = 0
df.loc[df['P012_O001V'] == '0', 'P013_O001V'] = 0
df['P013_O001V'] = pd.to_numeric(df['P013_O001V'], errors='coerce').fillna(0)
df.drop(columns=['P012_O001V'], inplace=True)

# Desfragmentar el DataFrame antes de agregar nuevas columnas
df = df.copy()

# Copiar columnas originales a preservar
df['EDAD_ESCALADA'] = df['EDAD']
df['BACH_PROMEDIO_ESCALADO'] = df['BACH_PROMEDIO']

# Lista de variables cuantitativas a normalizar
variables_cuantitativas = ['P013_O001V', 'P044_O001V', 'P018_O002V', 'P008_O002V',
                           'Distancia_Campus', 'BACH_PROMEDIO_ESCALADO', 'PUNTAJE_ADM', 'EDAD_ESCALADA']

# Crear el objeto MinMaxScaler
scaler = MinMaxScaler()

# Aplicar la normalización
df[variables_cuantitativas] = scaler.fit_transform(df[variables_cuantitativas])

# Mostrar verificación
print("\nPrimeras filas con columnas normalizadas:")
print(df[variables_cuantitativas].head())

# Asegurar que no haya valores nulos en las variables 
valores_nulos = df.isnull().sum()
columnas_con_nulos = valores_nulos[valores_nulos > 0]
if columnas_con_nulos.empty:
    print("No hay columnas con valores nulos en el DataFrame")
else:
    print("Número de valores nulos en cada columna con valores nulos:")
    print(columnas_con_nulos)

# Primero convertir las columnas numéricas a tipo float
numeric_columns = ['P051_O001V', 'P051_O002V', 'P051_O003V', 'P051_O004V', 'P051_O005V']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Reemplazar valores nulos con la moda de cada columna
for col in numeric_columns:
    df[col].fillna(df[col].mode(), inplace=True)

# Reemplazar valores nulos con la moda de cada columna
df['GENERO'] = df['GENERO'].replace('nan', df['GENERO'].mode()[0])

# Verificar nuevamente los valores nulos para confirmar el reemplazo
valores_nulos = df.isnull().sum()
columnas_con_nulos = valores_nulos[valores_nulos > 0]

if columnas_con_nulos.empty:
    print("No hay columnas con valores nulos en el DataFrame")
else:
    print("Número de valores nulos en cada columna con valores nulos:")
    print(columnas_con_nulos)

# BORRAR COLUMNAS QUE NO SE NORMALIZARON

# Contar columnas antes de la eliminación
columnas_antes = df.shape[1]

# Lista de columnas a eliminar 
columnas_a_eliminar = [
    "P005_O002V", "P006_O008V", "P006_O009V", "P010_O002V", # Preguntas abiertas
    "P047_O008V", "P052_O010V", "P060_O002V",  # Preguntas abiertas
    "PUNTAJE_ADM",  # Porque cambió la escala cuando ya no se aplica examen de admisión
    "ADEUDO"        # Porque solo se tiene para los estudiantes que desertaron
]

# Eliminar las columnas del DataFrame
df.drop(columns=columnas_a_eliminar, inplace=True, errors='ignore')

# Contar columnas después de la eliminación
columnas_despues = df.shape[1]

# Imprimir resultado
print(f"Se eliminaron {columnas_antes - columnas_despues} columnas.")

import os

# Guardar el dataframe combinado en un archivo nuevo
folder_path = './data'  
df.to_csv(os.path.join(folder_path, 'encoded.csv'), index=False)

# Verificar
filas_cargadas = df.shape[0] 
print(f"DataFrame guardado: {filas_cargadas} filas.")
print(f"Columnas en el DataFrame: {df.shape[1]}")

# --- Extracted from 3. Creación de variables.ipynb ---
# 1) CARGAR EL DATAFRAME NORMALIZADO

import pandas as pd

# Cargar con low_memory=False para evitar advertencias durante la inferencia de tipos
df = pd.read_csv('data/encoded.csv', low_memory=False)

# Verificar el dataframe cargado:
filas_cargadas = df.shape[0]  # obtener el número de filas cargadas
print(f"DataFrame cargado: {filas_cargadas} filas.")

# Detectar columnas con mezcla de tipos usando 'object' que deberían ser numéricas
mixed_type_cols = []

for col in df.columns:
    # Si tiene más de un tipo de dato (ej. int y str)
    tipos = df[col].map(type).value_counts()
    if len(tipos) > 1:
        mixed_type_cols.append((col, tipos))

# Mostrar un resumen
if mixed_type_cols:
    print("Columnas con tipos de datos mezclados detectadas:")
    for col, tipos in mixed_type_cols:
        print(f"Columna: '{col}' - Tipos detectados: {tipos.to_dict()}")
else:
    print("No se detectaron columnas con tipos de datos mezclados.")

# Verificar
filas_cargadas = df.shape[0] 
print(f"Columnas en el DataFrame: {df.shape[1]}")

# FASE 3. CREACION DE VARIABLES COMPUESTAS o RENOMBRADO DE SIMPLES

# Diccionario para variables compuestas y renombramiento
# Las claves son los nombres finales deseados, los valores son:
# - Una lista de variables simples (para las compuestas)
# - Un string (para renombrar variables simples)
variables_definidas = {
    'economic_burden': ['P013_O001V', 'P015_O001V', 'P015_O002V', 'P015_O003V', 'P019_O001V'],  # Compuesta
    'financial_independence': ['P015_O005V', 'P020_O001V_2.0', 'P020_O001V_3.0'],  # Compuesta
    'tuition_fee': ['P020_O001V_1.0','P020_O001V_4.0','P020_O001V_5.0', 'P020_O001V_6.0'],  # Compuesta
    'resources_academic_activities': 'P021_O001V',  
    'accessibility': ['P056_O010V','P056_O007V'],  # Compuesta
    'job_opportunity': 'P050_O007V', 
    'economic_restriction': 'P050_O011V',
    'economic_perception_itson_parents': ['P054_O001V_2.0', 'P054_O001V_3.0'], # Compuesta
    'perception_economic_terms': 'P059_O001V',  
    'economic constraint': 'P060_O001V_3.0',  
    'property_type_housing': ['P025_O001V_0.0', 'P025_O001V_1.0', 'P025_O001V_2.0', 'P025_O001V_3.0'],  # Compuesta
    'housing_company': 'P026_O001V', 
    'passive teaching': ['P035_O001V', 'P035_O002V'], 
    'active-critical-learning-practices': ['P035_O003V', 'P035_O004V', 'P035_O005V'], # Compuesta
    'teaching_performance': 'P039_O001V', 
    'cultural_activities': ['P049_O001V', 'P049_O005V', 'P049_O006V', 'P049_O007V', 'P049_O008V', 'P041_O001V'], 
    'services_academic_activities': ['P048_O002V', 'P048_O004V', 'P048_O005V', 'P048_O006V', 'P049_O009V', 'P041_O005V', 'P049_O010V'], # Compuesta
    'schooled_institution': ['P031_O001V_1.0', 'P031_O002V_1.0', 'P031_O003V_1.0'], 
    'previous_studies_open-line': ['P031_O001V_2.0', 'P031_O002V_2.0', 'P031_O003V_2.0', 'P031_O001V_3.0', 'P031_O002V_3.0', 'P031_O003V_3.0'], # Compuesta
    'public_institution': ['P032_O001V_1.0', 'P032_O002V_1.0', 'P032_O003V_1.0'], 
    'private_institution': ['P032_O001V_2.0', 'P032_O002V_2.0', 'P032_O003V_2.0'], 
    'prestige_quality': ['P056_O001V', 'P056_O002V', 'P056_O003V', 'P056_O005V'], 
    'academic_progress_performance': ['P029_O001V', 'P030_O001V', 'P038_O001V'], # Compuesta
    'habits_study_participation': ['P033_O001V', 'P033_O002V', 'P033_O003V', 'P033_O004V', 'P033_O005V', 'P033_O006V', 
                                      'P033_O007V', 'P033_O008V', 'P033_O009V', 'P033_O010V', 'P040_O001V', 'P040_O002V'], # Compuesta
    'physical_teaching_resources': ['P034_O004V', 'P034_O005V', 'P034_O006V', 'P034_O002V', 'P046_O001V', 'P046_O007V', 'P046_O009V', 'P046_O005V', 'P046_O008V','P034_O001V', 'P034_O009V', 'P034_O003V', 'P036_O001V', 'P036_O002V', 'P036_O007V', 'P036_O004V', 'P036_O005V'], # Compuesta
    'digital_teaching_resources': ['P034_O007V', 'P034_O008V', 'P036_O003V', 'P036_O006V', 'P046_O002V', 'P046_O003V', 'P046_O004V', 'P046_O006V', 'P046_O010V'], # Compuesta
    'techniques_study_organization': ['P037_O001V', 'P037_O002V', 'P037_O003V', 'P037_O004V', 'P037_O005V', 'P037_O006V', 'P037_O007V', 'P037_O008V', 'P047_O006V'], # Compuesta
    'academic_information_received': ['P050_O001V', 'P050_O005V', 'P050_O006V'], 
    'areas_reinforcement': ['P052_O001V', 'P052_O002V', 'P052_O003V', 'P052_O004V', 'P052_O006V', 'P052_O007V', 'P052_O005V', 'P052_O008V', 'P052_O009V'], # Compuesta
    'academic_limitation': 'P060_O001V_2.0', 
    'health_condition_special_needs': ['P005_O001V', 'P006_O007V', 'P006_O002V', 'P006_O003V', 'P006_O004V', 'P006_O005V', 'P006_O006V'], # Compuesta
    'practice_sport': 'P007_O001V', 
    'personal_limitation': ['P060_O001V_4.0', 'P060_O001V_5.0','P060_O001V_6.0'], # limitante personal u otro
    'intensity_tobacco_alcohol_consumption': ['P008_O001V', 'P008_O002V', 'P009_O001V_1.0', 'P009_O001V_2.0', 'P009_O001V_3.0', 'P009_O001V_4.0', 'P009_O001V_5.0', 'P009_O001V_6.0',
                                          'P010_O001V_1.0', 'P010_O001V_2.0', 'P010_O001V_3.0', 'P010_O001V_4.0', 'P010_O001V_5.0', 'P011_O001V'], # Compuesta
    'civil_family_burden': ['P017_O001V_1.0', 'P017_O001V_2.0', 'P017_O001V_3.0', 'P017_O001V_4.0', 'P017_O001V_5.0', 'P018_O001V', 'P018_O002V'], # Compuesta
    'educational_capital_father_mother': ['P024_O001V', 'P024_O002V'], # Compuesta
    'goods_services_housing': ['P027_O001V', 'P027_O002V', 'P027_O008V', 'P027_O004V', 'P027_O005V', 'P027_O011V', 'P027_O014V',
                                  'P027_O003V', 'P027_O009V', 'P027_O010V', 'P027_O012V', 'P027_O006V', 'P027_O007V', 'P027_O013V'], # Compuesta
    'educational_parental_assessment': ['P028_O001V', 'P053_O001V_1.0', 'P053_O001V_2.0', 'P053_O001V_3.0', 'P054_O001V_1.0'], # Compuesta
    'academic_parental_involvement': ['P055_O001V', 'P055_O002V', 'P055_O003V', 'P055_O004V', 'P055_O005V'], # Compuesta
    'lifestyle_free_time': ['P042_O001V', 'P043_O001V', 'P044_O001V', 'P045_O001V', 'P047_O005V', 'P047_O002V', 'P047_O003V', 
                                 'P047_O004V', 'P047_O001V', 'P047_O007V'], # Compuesta
    'vocational_influence': 'P050_O008V', 
    'single_option': 'P050_O010V', 
    'influence_outsiders': ['P050_O002V', 'P050_O003V', 'P050_O004V', 'P050_O009V'], # Compuesta
    'career_satisfaction': ['P051_O001V', 'P051_O002V'], 
    'uncertainty_election': ['P051_O003V', 'P051_O004V', 'P051_O005V'], 
    'public_institutional_labor_scope': ['P058_O001V_1.0', 'P058_O001V_2.0'], # Compuesta
    'work_field_private_entrepreneur': ['P058_O001V_3.0', 'P058_O001V_4.0', 'P058_O001V_5.0'], # Compuesta
    'expectation_professional_prestige': ['P057_O001V', 'P059_O002V'], # Compuesta
    'institutional_recreational_services': ['P048_O001V', 'P048_O003V', 'P049_O011V', 'P049_O002V', 'P049_O004V', 'P049_O003V', 'P041_O003V', 'P041_O002V', 'P041_O004V'], # Compuesta
    'social_environment_community': ['P056_O006V', 'P056_O004V', 'P056_O008V', 'P056_O009V'], 
    'public transport': ['P022_O001V_1.0', 'P022_O001V_2.0'], 
    'private_motorized_transport': ['P022_O001V_3.0', 'P022_O001V_5.0', 'P022_O001V_6.0', 'P022_O001V_7.0'], # Compuesta
    'non-motorized_transport': ['P022_O001V_4.0', 'P022_O001V_8.0'], 
    'university_transfer_time': 'P023_O001V', 
    'distance_campus': 'Distancia_Campus',
    'high-school_average': 'BACH_PROMEDIO_ESCALADO',
    'non_drinker': 'P009_O001V_0.0', 
    'morning_work_shift': 'P014_O001V_1.0',
    'evening_work_shift': 'P014_O001V_2.0', 
    'night_shift_work': 'P014_O001V_3.0', 
    'mixed_work_shift': 'P014_O001V_4.0', 
    'weekend_work_shift': 'P014_O001V_5.0', 
    'sporadic_work_shift': 'P014_O001V_6.0',
    'desire_work_experience': 'P015_O004V',
    'work-career_relationship': 'P016_O001V',
    'conditioned_career': 'RISK_CARRERA',
    'age': 'EDAD_ESCALADA',
    'gender': 'GENERO'
}

# Crear un DataFrame para almacenar las nuevas columnas
nuevas_columnas = pd.DataFrame(index=df.index)

# Procesar el diccionario y generar las nuevas columnas
for nueva_var, originales in variables_definidas.items():
    if isinstance(originales, list):  # Si es una lista, crear una variable compuesta
        # Asegurarse de que todas las columnas sean numéricas
        columnas_procesadas = df[originales].apply(pd.to_numeric, errors='coerce')
        # Calcular la media de las columnas
        nuevas_columnas[nueva_var] = columnas_procesadas.mean(axis=1)
    elif isinstance(originales, str):  # Si es un string, es una variable simple a renombrar
        # Convertir la columna a numérica y agregarla directamente
        nuevas_columnas[nueva_var] = pd.to_numeric(df[originales], errors='coerce')

# Combinar el DataFrame original con las nuevas columnas
df = pd.concat([df, nuevas_columnas], axis=1)

# Opcional: Eliminar las columnas originales utilizadas para las variables compuestas
columnas_a_eliminar = []
for originales in variables_definidas.values():
    if isinstance(originales, list):
        columnas_a_eliminar.extend(originales)
    elif isinstance(originales, str):
        columnas_a_eliminar.append(originales)

df.drop(columns=columnas_a_eliminar, inplace=True)

# Verificar
filas_dataframe = df.shape[0] 
print(f"Columnas en el DataFrame: {df.shape[1]}")

# INVERTIR VARIABLES QUE SU ESCALA INDICA QUE A MAS CERCA DEL '1' ES MENOR RIESGO DE DESERCIÓN

# Lista de variables que necesitan inversión
variables_a_invertir = [
    'financial_independence',
    'job_opportunity',
    'active-critical-learning-practices',
    'cultural_activities', 
    'services_academic_activities', 
    'schooled_institution', 
    'private_institution', 
    'prestige_quality',
    'habits_study_participation', 
    'physical_teaching_resources', 
    'digital_teaching_resources',
    'techniques_study_organization',
    'academic_information_received', 
    'practice_sport', 
    'educational_capital_father_mother', 
    'goods_services_housing', 
    'housing_company', 
    'educational_parental_assessment', 
    'academic_parental_involvement', 
    'lifestyle_free_time',
    'vocational_influence', 
    'influence_outsiders', 
    'career_satisfaction', 
    'public_institutional_labor_scope', 
    'work_field_private_entrepreneur',
    'expectation_professional_prestige',
    'institutional_recreational_services',
    'social_environment_community',
    'private_motorized_transport', 
    'non-motorized_transport',
    'high-school_average'
]

# Verificar que las variables a invertir están en el DataFrame
variables_existentes = [var for var in variables_a_invertir if var in df.columns]
variables_faltantes = [var for var in variables_a_invertir if var not in df.columns]

# Informar sobre variables que no se encuentran
if variables_faltantes:
    print(f"Las siguientes variables no están en el DataFrame y no se pueden invertir: {variables_faltantes}")

# Aplicar la inversión: 1 - valor actual
for var in variables_existentes:
    df[var] = 1 - df[var]

print("Inversión completada para las variables indicadas.")

# Verificar
filas_dataframe = df.shape[0] 
print(f"Columnas en el DataFrame: {df.shape[1]}")


# == COLUMNAS A ELIMINAR (No se integraron a variables)== #

# Contar columnas antes de la eliminación
columnas_antes = df.shape[1]

# Verificar qué columnas existen en el DataFrame antes de intentar eliminarlas
columnas_a_eliminar = [
    'P006_O001V', # otro tipo de problema (que especifica o no)
    'P010_O001V_0.0', # se genera al codificar las variables categóricas (One-Hot Encoding)
    'P014_O001V_0.0', # se genera al codificar las variables categóricas (One-Hot Encoding)
    'P017_O001V_NA', # se genera al codificar las variables categóricas (One-Hot Encoding)
    'P020_O001V_Desconocido',# se genera al codificar las variables categóricas (One-Hot Encoding)
    'P022_O001V_Desconocido', # se genera al codificar las variables categóricas (One-Hot Encoding)
    'P041_O006V', # pertenece a otro tipo de grupo (asumo)
    'P058_O001V_Desconocido', # se genera al codificar las variables categóricas (One-Hot Encoding)
    'P060_O001V_1.0', # se genera al codificar las variables categóricas (One-Hot Encoding)
    'P060_O001V_Desconocido',# se genera al codificar las variables categóricas (One-Hot Encoding)
]

# Asegurarse de que los nombres de las columnas no tengan espacios adicionales
df.columns = df.columns.str.strip()

# Filtrar solo las columnas que realmente existen en el DataFrame
columnas_existentes = [col for col in columnas_a_eliminar if col in df.columns]

# Eliminar las columnas que sí existen
df.drop(columns=columnas_existentes, inplace=True, errors='ignore')

# Verificar si las columnas fueron eliminadas correctamente
print("Columnas restantes:", df.columns.tolist())

# Verificar
filas_dataframe = df.shape[0] 
print(f"Columnas en el DataFrame: {df.shape[1]}")

# Contar columnas después de la eliminación
columnas_despues = df.shape[1]

# Imprimir resultado
print(f"Se eliminaron {columnas_antes - columnas_despues} columnas.")

# Asegurar que no haya valores nulos en las variables 
valores_nulos = df.isnull().sum()
columnas_con_nulos = valores_nulos[valores_nulos > 0]
if columnas_con_nulos.empty:
    print("No hay columnas con valores nulos en el DataFrame")
else:
    print("Número de valores nulos en cada columna con valores nulos:")
    print(columnas_con_nulos)

# == GUARDAR CAMBIOS DE VARIABLES COMPUESTAS  Y SIMPLES RENOMBRADAS == #

import os

# Guardar el dataframe con variables creadas en un archivo nuevo
folder_path = './data'  
df.to_csv(os.path.join(folder_path, 'preprocessed.csv'), index=False)

# Verificar
filas_cargadas = df.shape[0] 
print(f"DataFrame guardado: {filas_cargadas} filas.")
print(f"Columnas en el DataFrame: {df.shape[1]}")

