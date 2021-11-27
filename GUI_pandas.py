import pandas as pd
import numpy as np 

class Gui_pandas():

    def __init__ (self, ruta):
        self.ruta = ruta
  
    #------------------------------------------------------
    def connect(self):
        # connect by unpacking dictionary credentials
        data=pd.read_csv(self.ruta)
        return data
    
    def analyze_data(self):
        data = self.connect()
        X = data.iloc[:, 2:21].values
        r, c = X.shape

        dicc_X = {}

        good_intentions = []
        bad_intentions = []

        for i in range(0,r):
            for j in range(0,c):
                if X[i][j] == "()" or pd.isna(X[i][j]):
                    continue
                else:
                    characters = "() "
                    for x in range(len(characters)):
                        X[i][j] = X[i][j].replace(characters[x],"")
                    
                    lista_X = X[i][j].split('|')
                    if int(lista_X[1])<100:
                        good_intentions.append((j+1,lista_X[0],lista_X[1]))
                    else:
                        bad_intentions.append((j+1,lista_X[0],lista_X[1]))
        
        return good_intentions, bad_intentions
    

 