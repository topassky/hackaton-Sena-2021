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
        data = data.tail(n=5)
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
                        characters2 = "a.\xa0m."
                        Xfecha = data.iloc[i,1]
                        Xfecha = Xfecha.replace(characters2[x],"")
                        
                        good_intentions.append([
                            data.iloc[i,0],
                            Xfecha,
                        j+1,lista_X[0],lista_X[1]])
                    else:
                        bad_intentions.append([
                            data.iloc[i,0],
                            Xfecha,
                        j+1,lista_X[0],lista_X[1]])
        
        return good_intentions, bad_intentions

    def dataFrame_grafica(self):
        good_intentions, bad_intentions = self.analyze_data()
        #print(good_intentions)
        fecha = []
        hora = []
        camara = []
        sensor = []
        nivel_sensor = []
        for i in good_intentions:
            fecha.append(i[0])
            hora.append(i[1])
            camara.append(i[2])
            sensor.append(i[3])
            nivel_sensor.append(i[4])
        
        marco_datos = pd.DataFrame({'fecha':fecha,
                    'camara':camara, 'sensor':sensor,
                    'nivel_sensor': nivel_sensor}, index=hora)
       
        
        return marco_datos


