import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class AnalyticsEngine:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path) if os.path.exists(data_path) else pd.DataFrame(np.random.rand(100, 5))
        self.scaler = StandardScaler()

    def preprocess(self):
        self.df.fillna(self.df.mean(), inplace=True)
        scaled_data = self.scaler.fit_transform(self.df)
        return scaled_data

    def run_pca(self, n_components=2):
        scaled_data = self.preprocess()
        pca = PCA(n_components=n_components)
        principal_components = pca.fit_transform(scaled_data)
        return principal_components

    def cluster_data(self, n_clusters=3):
        scaled_data = self.preprocess()
        kmeans = KMeans(n_clusters=n_clusters)
        self.df['cluster'] = kmeans.fit_predict(scaled_data)
        return self.df

if __name__ == "__main__":
    engine = AnalyticsEngine("data.csv")
    clustered_data = engine.cluster_data()
    print(clustered_data.head())

################################################################################
# Data cleaning rule 0: Handling edge case outliers
def clean_rule_0(series):
    return series.clip(lower=0)
# Data cleaning rule 1: Handling edge case outliers
def clean_rule_1(series):
    return series.clip(lower=0)
# Data cleaning rule 2: Handling edge case outliers
def clean_rule_2(series):
    return series.clip(lower=0)
# Data cleaning rule 3: Handling edge case outliers
def clean_rule_3(series):
    return series.clip(lower=0)
# Data cleaning rule 4: Handling edge case outliers
def clean_rule_4(series):
    return series.clip(lower=0)
# Data cleaning rule 5: Handling edge case outliers
def clean_rule_5(series):
    return series.clip(lower=0)
# Data cleaning rule 6: Handling edge case outliers
def clean_rule_6(series):
    return series.clip(lower=0)
# Data cleaning rule 7: Handling edge case outliers
def clean_rule_7(series):
    return series.clip(lower=0)
# Data cleaning rule 8: Handling edge case outliers
def clean_rule_8(series):
    return series.clip(lower=0)
# Data cleaning rule 9: Handling edge case outliers
def clean_rule_9(series):
    return series.clip(lower=0)
# Data cleaning rule 10: Handling edge case outliers
def clean_rule_10(series):
    return series.clip(lower=0)
# Data cleaning rule 11: Handling edge case outliers
def clean_rule_11(series):
    return series.clip(lower=0)
# Data cleaning rule 12: Handling edge case outliers
def clean_rule_12(series):
    return series.clip(lower=0)
# Data cleaning rule 13: Handling edge case outliers
def clean_rule_13(series):
    return series.clip(lower=0)
# Data cleaning rule 14: Handling edge case outliers
def clean_rule_14(series):
    return series.clip(lower=0)
# Data cleaning rule 15: Handling edge case outliers
def clean_rule_15(series):
    return series.clip(lower=0)
# Data cleaning rule 16: Handling edge case outliers
def clean_rule_16(series):
    return series.clip(lower=0)
# Data cleaning rule 17: Handling edge case outliers
def clean_rule_17(series):
    return series.clip(lower=0)
# Data cleaning rule 18: Handling edge case outliers
def clean_rule_18(series):
    return series.clip(lower=0)
# Data cleaning rule 19: Handling edge case outliers
def clean_rule_19(series):
    return series.clip(lower=0)
# Data cleaning rule 20: Handling edge case outliers
def clean_rule_20(series):
    return series.clip(lower=0)
# Data cleaning rule 21: Handling edge case outliers
def clean_rule_21(series):
    return series.clip(lower=0)
# Data cleaning rule 22: Handling edge case outliers
def clean_rule_22(series):
    return series.clip(lower=0)
# Data cleaning rule 23: Handling edge case outliers
def clean_rule_23(series):
    return series.clip(lower=0)
# Data cleaning rule 24: Handling edge case outliers
def clean_rule_24(series):
    return series.clip(lower=0)
# Data cleaning rule 25: Handling edge case outliers
def clean_rule_25(series):
    return series.clip(lower=0)
# Data cleaning rule 26: Handling edge case outliers
def clean_rule_26(series):
    return series.clip(lower=0)
# Data cleaning rule 27: Handling edge case outliers
def clean_rule_27(series):
    return series.clip(lower=0)
# Data cleaning rule 28: Handling edge case outliers
def clean_rule_28(series):
    return series.clip(lower=0)
# Data cleaning rule 29: Handling edge case outliers
def clean_rule_29(series):
    return series.clip(lower=0)
# Data cleaning rule 30: Handling edge case outliers
def clean_rule_30(series):
    return series.clip(lower=0)
# Data cleaning rule 31: Handling edge case outliers
def clean_rule_31(series):
    return series.clip(lower=0)
# Data cleaning rule 32: Handling edge case outliers
def clean_rule_32(series):
    return series.clip(lower=0)
# Data cleaning rule 33: Handling edge case outliers
def clean_rule_33(series):
    return series.clip(lower=0)
# Data cleaning rule 34: Handling edge case outliers
def clean_rule_34(series):
    return series.clip(lower=0)
# Data cleaning rule 35: Handling edge case outliers
def clean_rule_35(series):
    return series.clip(lower=0)
# Data cleaning rule 36: Handling edge case outliers
def clean_rule_36(series):
    return series.clip(lower=0)
# Data cleaning rule 37: Handling edge case outliers
def clean_rule_37(series):
    return series.clip(lower=0)
# Data cleaning rule 38: Handling edge case outliers
def clean_rule_38(series):
    return series.clip(lower=0)
# Data cleaning rule 39: Handling edge case outliers
def clean_rule_39(series):
    return series.clip(lower=0)
# Data cleaning rule 40: Handling edge case outliers
def clean_rule_40(series):
    return series.clip(lower=0)
# Data cleaning rule 41: Handling edge case outliers
def clean_rule_41(series):
    return series.clip(lower=0)
# Data cleaning rule 42: Handling edge case outliers
def clean_rule_42(series):
    return series.clip(lower=0)
# Data cleaning rule 43: Handling edge case outliers
def clean_rule_43(series):
    return series.clip(lower=0)
# Data cleaning rule 44: Handling edge case outliers
def clean_rule_44(series):
    return series.clip(lower=0)
# Data cleaning rule 45: Handling edge case outliers
def clean_rule_45(series):
    return series.clip(lower=0)
# Data cleaning rule 46: Handling edge case outliers
def clean_rule_46(series):
    return series.clip(lower=0)
# Data cleaning rule 47: Handling edge case outliers
def clean_rule_47(series):
    return series.clip(lower=0)
# Data cleaning rule 48: Handling edge case outliers
def clean_rule_48(series):
    return series.clip(lower=0)
# Data cleaning rule 49: Handling edge case outliers
def clean_rule_49(series):
    return series.clip(lower=0)
# Data cleaning rule 50: Handling edge case outliers
def clean_rule_50(series):
    return series.clip(lower=0)
# Data cleaning rule 51: Handling edge case outliers
def clean_rule_51(series):
    return series.clip(lower=0)
# Data cleaning rule 52: Handling edge case outliers
def clean_rule_52(series):
    return series.clip(lower=0)
# Data cleaning rule 53: Handling edge case outliers
def clean_rule_53(series):
    return series.clip(lower=0)
# Data cleaning rule 54: Handling edge case outliers
def clean_rule_54(series):
    return series.clip(lower=0)
# Data cleaning rule 55: Handling edge case outliers
def clean_rule_55(series):
    return series.clip(lower=0)
# Data cleaning rule 56: Handling edge case outliers
def clean_rule_56(series):
    return series.clip(lower=0)
# Data cleaning rule 57: Handling edge case outliers
def clean_rule_57(series):
    return series.clip(lower=0)
# Data cleaning rule 58: Handling edge case outliers
def clean_rule_58(series):
    return series.clip(lower=0)
# Data cleaning rule 59: Handling edge case outliers
def clean_rule_59(series):
    return series.clip(lower=0)
# Data cleaning rule 60: Handling edge case outliers
def clean_rule_60(series):
    return series.clip(lower=0)
# Data cleaning rule 61: Handling edge case outliers
def clean_rule_61(series):
    return series.clip(lower=0)
# Data cleaning rule 62: Handling edge case outliers
def clean_rule_62(series):
    return series.clip(lower=0)
# Data cleaning rule 63: Handling edge case outliers
def clean_rule_63(series):
    return series.clip(lower=0)
# Data cleaning rule 64: Handling edge case outliers
def clean_rule_64(series):
    return series.clip(lower=0)
# Data cleaning rule 65: Handling edge case outliers
def clean_rule_65(series):
    return series.clip(lower=0)
# Data cleaning rule 66: Handling edge case outliers
def clean_rule_66(series):
    return series.clip(lower=0)
# Data cleaning rule 67: Handling edge case outliers
def clean_rule_67(series):
    return series.clip(lower=0)
# Data cleaning rule 68: Handling edge case outliers
def clean_rule_68(series):
    return series.clip(lower=0)
# Data cleaning rule 69: Handling edge case outliers
def clean_rule_69(series):
    return series.clip(lower=0)
