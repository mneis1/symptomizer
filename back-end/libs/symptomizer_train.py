from sklearn.linear_model import LogisticRegressionCV
import pandas as pd


class Classifier:
    def __init__(self):
        self.logReg = LogisticRegressionCV()

    def split_dia_sym(self):
        data = pd.read_csv("/Users/marcneisser/symptomizer/back-end/data/normalized/sym_dis_frame_finished.csv")
        diaData = data.values[:, 0]
        symData = data.values[:, 1:]
        return diaData, symData

    def train_lr(self, sym, dia):
        self.logReg.fit(sym, dia)

    def predict(self, pred_syms):
        predInfo = self.logReg.predict(pred_syms)
        return predInfo
