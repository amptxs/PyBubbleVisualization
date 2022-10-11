import pandas as pd


# Прочитать файл xlsx
def readExcel(path):
    return pd.read_excel(path, sheet_name=None, engine='openpyxl')


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
    for sheet in frame_keys:
        data_frame[sheet] = data_frame[sheet].iloc[1:]
        data_frame[sheet]['Имя'] = str(sheet)
        data_frame[sheet] = data_frame[sheet][data_frame[sheet]['Добыча нефти,т'].notna()]
        data_frame[sheet] = data_frame[sheet].astype({'Добыча нефти,т': int})
    return data_frame


# Объединить листы
def sheetsConcat(data_frame):
    return pd.concat(data_frame, ignore_index=True)




