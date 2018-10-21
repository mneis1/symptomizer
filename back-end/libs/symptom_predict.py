from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import pandas as pd
import numpy as np
import json as jsn



def prep_data(path):
    ##"/Users/marcneisser/symptomizer/back-end/data/normalized/sym_dis_frame_finished.csv" is path on local
    data = pd.read_csv(path ,encoding='utf-8')
    diaData = data.values[:, 0]
    symData = data.values[:, 2:]
    diaData = diaData.astype('int')
    diaName = data.values[:, 1]
    return symData, diaData, diaName


def justFitIt(logisticReg, symptom_data, diagnosis_data):
    logisticReg.fit(symptom_data, diagnosis_data)


def justDoIt(logReg, predData):
    ##predData should be a 1d array
    result_data = logReg.predict_proba([predData])
    return result_data


def cleanData(diagnosis_names, probability_values):
    combined = np.vstack((diagnosis_names, probability_values)).T
    combined = combined[combined[:, 1].argsort()]
    combined = np.flip(combined, axis=0)
    return combined

def doItAll(data_path, prediction_data):
    lr = LogisticRegression(solver='newton-cg', multi_class='multinomial')
    symData, diaData, diaName = prep_data(data_path)
    justFitIt(lr, symData, diaData)
    resData = justDoIt(lr, prediction_data)
    finalData = cleanData(diaName, resData)
    return finalData