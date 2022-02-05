
import pandas as pd
from pandas.api.types import is_numeric_dtype

def remove_blanks(df:pd.DataFrame, col):
  """
  :param df: the dataframe to clean
  :param col: the column to clean
  :return: the dataframe after cleaning
  """

  if not(is_numeric_dtype(df[col])):
      print(col," -- ", is_numeric_dtype(df[col]))
      try:
        df[col] = df[col].apply(lambda x : x[1:] if x.startswith(" ") else x)
      except:
          print("No pude con ", col)


def OrganizarDataFrame(filename:str,cols:list()=None):
    if cols!=None:
        df=pd.DataFrame(pd.read_spss(filename,usecols=cols))
        df.columns = df.columns.str.lower()
    else:
        df=pd.DataFrame(pd.read_spss(filename))
        df.columns = df.columns.str.lower()
    return df

def MapeoDiccionario(df,col,dict_fix:dict()):
    df[col] = df[col].map(dict_fix)

def ApplyDiccionario(df,col,dict_fix:dict()):
    df[col] = df[col].apply(lambda x: FixValues(x,dict_fix))

def FixValues(x,dic_fix:dict()):
  if x in dic_fix.keys():
    return dic_fix[x]
  else:
    return x