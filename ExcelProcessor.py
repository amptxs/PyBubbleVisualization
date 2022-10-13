import pandas as pd


# Прочитать файл xlsx
def readExcel():
    return pd.read_excel('data/Data.xlsx', sheet_name=None, engine='openpyxl', header=[0, 1])


# Имена листов
def sheetsNames(data_frame):
    for sheet in data_frame.keys():
        print(sheet)


# Листы
def sheetsPrint(data_frame):
    for sheet in data_frame.keys():
        print(data_frame[sheet])


# Нормализуем данные
def normalize(data_frame):
    frame_keys = data_frame.keys()
    dfLoc = pd.read_excel('data/Location.xlsx', engine='openpyxl')
    for sheet in frame_keys:
        data_frame[sheet].columns = data_frame[sheet].columns.map('_'.join)
        data_frame[sheet] = data_frame[sheet].rename(columns=lambda x: x if not 'Unnamed' in str(x) else x.partition("_Unnamed")[0])
        data_frame[sheet]['Имя'] = str(sheet)
        if dfLoc.loc[dfLoc['wells_name'] == str(sheet), 'x'].values.size > 0:
            x = dfLoc.loc[dfLoc['wells_name'] == str(sheet), 'x'].values[0]
            y = dfLoc.loc[dfLoc['wells_name'] == str(sheet), 'y'].values[0]
            data_frame[sheet]['X'] = x
            data_frame[sheet]['Y'] = y
        data_frame[sheet] = data_frame[sheet][data_frame[sheet]['Дебит_нефти,т/сут'].notna()]
        data_frame[sheet] = data_frame[sheet].astype({'Дебит_нефти,т/сут': int})
    return data_frame


# Объединить листы
def sheetsConcat(data_frame):
    return pd.concat(data_frame, ignore_index=True)




