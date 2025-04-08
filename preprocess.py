import pandas as pd
import numpy as np


def prepr(df, save):
    height = 0.17857 / 2
    radius = 0.025
    heightNeed = 50e-6 / 2
    radiusNeed = 3.5e-6

    alpha = np.arctan(df["Points:1"] / df["Points:0"])
    df["Points:0"] = radiusNeed * np.cos(alpha)
    df["Points:1"] = radiusNeed * np.sin(alpha)
    df["Points:2"] = df["Points:2"] * heightNeed / height

    data = df[['Points:0', 'Points:1', 'Points:2']].copy()
    data.to_csv(save, index=False, header=False)


prepr(pd.read_csv("save_init.csv"), "initial.csv")
prepr(pd.read_csv("save_res.csv"), "result.csv")
