import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import io

def diversity_calc(csv_path):
    df = pd.read_csv(csv_path)

    # 多様度指数Hの計算
    pop = df.iloc[:,1].sum()
    H = 0
    for i in range(len(df)):
        Pi = df.iloc[i,1] / pop
        H -= Pi * math.log2(Pi)
    H = f"{H:.2f}"

    # グラフ作成
    plt.rcParams['font.family'] = "IPAexGothic" # 日本語対応のフォントに変更
    plt.style.use("ggplot")
    fig, ax = plt.subplots()
    plt.barh(df.iloc[:,0] ,df.iloc[:,1])
    plt.xlabel("個体数")
    plt.savefig("/django/project/media/csv/graph.svg", bbox_inches='tight')
    graph = f"/media/csv/graph.svg"
    return H, graph