import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
import warnings
from collections import Counter
#warnings.filterwarnings('ignore')
#%matplotlib inline

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Descriptive Stats Tool', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

# read file and make df
def knowFileExt(datafile):
    return datafile.split(".")[-1]

def file2df(datafile):
    if (knowFileExt(datafile) == 'xlsx'):
        df = pd.read_excel(datafile)
    elif (knowFileExt(datafile) == 'csv'):
        df = pd.read_csv(datafile, encoding='utf-8')
    else:
        raise Exception  # raise error
    return df

def float2int(df, ms):  # float, int 구분
    for column in df.columns:
        if (df[column].dtypes != 'O'):
            if np.array_equal(df[column].dropna(), df[column].dropna().astype(int)):  # int values
                #df[column] = df[column].astype(int)
                ms.loc[column].type = np.arange(5, dtype='i').dtype
            else:
                ms.loc[column].type = np.arange(5, dtype='f').dtype
    return ms

def makeMS(df):  # 명세서 만들기
    ms = df.dtypes.to_frame(name="type")
    name = []
    for i in range(len(ms)):
        if (df[ms.iloc[i].name].dtypes == 'O'):
            name.append("명목")
        else:
            name.append("비율")
    ms["name"] = name
    return ms

def countUnique(df):  # 유일한 값 개수
    unique_list = []
    for i in range(len(df.columns)):
        unique_list.append(len(df.iloc[:, i].unique()))

    unique_series = pd.Series(unique_list, index=df.columns, name='유일한 값 개수')
    return unique_series

def multipleMostCommon_before(df, columnName):  # 열별로 최빈값 알아내기
    commonList = Counter(df[columnName]).most_common()
    mode_list = []
    modeNum = commonList[0][1]
    for i in range(len(commonList)):
        if commonList[i][1] < modeNum:
            break
        elif commonList[i][1] == modeNum:
            mode_list.append(commonList[i][0])
    return mode_list

def knowMostCommon_before(df):  # 최빈값(not used)
    modelist = []
    for i in range(len(df.columns)):
        modelist.append(multipleMostCommon(df, df.columns[i]))
    mode_series = pd.Series(modelist, index=df.columns, name='최빈값')
    return mode_series

def knowMostCommon(df):
    modelist = []
    for column in df.columns:
        temp = df[column].mode().astype(str).values.tolist()
        if len(temp) < 5: 
            modelist.append(str(temp))
        else:
            modelist.append(str(temp[0]))
        #modelist.append() # [str, str]
    mode_series = pd.Series(modelist, index=df.columns, name='최빈값')
    mode_series = mode_series.astype(str)
    return mode_series

def know_numericOrNon(ms, num):
    numericList = []
    nonNumericList = []
    for i in range(len(ms)):
        if ms.iloc[i].type != 'O':
            numericList.append(ms.iloc[i].name)
        else:
            nonNumericList.append(ms.iloc[i].name)
    if (num == 0):
        return numericList
    elif (num == 1):
        return nonNumericList
    else:
        return
 
def ds(df, ms):
    summary = df.describe()  # 1사분위수, 2사분위수, 3사분위수, 중앙값, 평균
    colName_series = ms.loc[:, 'name'].rename("구분").astype(str)
    count_series = df.count().rename("데이터 수").apply(lambda x : "{:,}".format(x))
    #unique_series = countUnique(df).rename("유일한 값 개수").astype(str)
    unique_series = countUnique(df).rename("유일한 값 개수").apply(lambda x : "{:,}".format(x))
    #null_series = df.isnull().sum().rename("결측치 수").astype(str)
    null_series = df.isnull().sum().rename("결측치 수").apply(lambda x : "{:,}".format(x))

    #mean_series = summary.loc['mean', :].rename("평균")
    mean_series = summary.loc['mean', :].rename("평균").apply(lambda x : "{:,}".format(round(x, 2)))
    #median_series = summary.loc['50%'].rename("중앙값")
    median_series = summary.loc['50%'].rename("중앙값").apply(lambda x : "{:,}".format(round(x, 2)))
    
    mode_series = knowMostCommon(df).rename("최빈값").astype(str)
    
    max_series_num = df.max(numeric_only=True).rename("최댓값")
    max_series = max_series_num.apply(lambda x : "{:,}".format(round(x, 2)))
    min_series_num = df.min(numeric_only=True).rename("최솟값")
    min_series = min_series_num.apply(lambda x : "{:,}".format(round(x, 2)))
    #range_series = (max_series - min_series).rename("범위")
    range_series = (max_series_num - min_series_num).rename("범위").apply(lambda x : "{:,}".format(round(x, 2)))
    per1_series = summary.loc['25%'].rename("1사분위수").apply(lambda x : "{:,}".format(round(x, 2)))
    per2_series = summary.loc['50%'].rename("2사분위수").apply(lambda x : "{:,}".format(round(x, 2)))
    per3_series = summary.loc['75%'].rename("3사분위수").apply(lambda x : "{:,}".format(round(x, 2)))
    std_series = summary.loc['std'].rename("표준편차").apply(lambda x : "{:,}".format(round(x, 2)))
    kurtosis_series = df.kurtosis(numeric_only=True).rename("첨도").dropna().apply(lambda x : "{:,}".format(round(x, 2)))
    skew_series = df.skew(numeric_only=True).rename("왜도").apply(lambda x : "{:,}".format(round(x, 2)))
    final = pd.concat([colName_series, count_series, unique_series, null_series, mean_series, \
                       median_series, mode_series, max_series, min_series, range_series, per1_series, \
                       per2_series, per3_series, std_series, kurtosis_series, skew_series], axis=1, ignore_index=False).T
    final.fillna("해당 없음", inplace=True)
    return final

def run():
    df = file2df(datafile)  # dataframe 읽기
    ms = float2int(df, makeMS(df)) # 명세서 만들기
    final = ds(df, ms) # 기술통계 산출
    final = final[df.columns] # 컬럼 정렬
    final.to_csv(outputfile, encoding='utf-8-sig')

def getCSV():
    global ms
    global df

    import_file_path = filedialog.askopenfilename()
    df = file2df(import_file_path)
    ms = float2int(df, makeMS(df))
    print("file2df complete")
    print(df.head())

browseButton_CSV = tk.Button(text="      Import File(.xlsx, .csv)     ", command=getCSV, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_CSV)

def cal_stats():
    global read_file
    global ms
    global df

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    #read_file.to_excel(export_file_path, index=None, header=True)
    final = ds(df, ms) # 기술통계 산출
    final = final[df.columns] # 컬럼 정렬
    final.to_csv(export_file_path, encoding='utf-8-sig')
    print(final)
    print("complete")

saveAsButton_Stats = tk.Button(text='Descriptive stats', command=cal_stats, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_Stats)


def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()


exitButton = tk.Button(root, text='       Exit Application     ', command=exitApplication, bg='brown', fg='white',
                       font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()
