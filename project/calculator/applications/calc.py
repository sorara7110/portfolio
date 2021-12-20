import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io

def diversity_calc(csv_path):
    df = pd.read_csv(csv_path)

    # 多様度指数Hの計算
    # 正しい形式か確認
    try:
        data = df.iloc[:,1:]
        pop = data.sum().values
        Pi = data / pop
        h = -Pi * np.log2(Pi)
        H = h.sum()
    except TypeError:
        graph = "error"
        return graph

    # グラフ作成
    plt.rcParams['font.family'] = "IPAexGothic" # 日本語対応のフォントに変更
    plt.style.use("ggplot")
    fig, ax = plt.subplots()
    plt.barh(data.columns, H)
    plt.xlabel("多様度指数H'")
    plt.savefig("/django/project/media/csv/graph.svg", bbox_inches='tight')
    graph = f"/media/csv/graph.svg"

    # 表作成
    H = [list(np.round(H, 2))]
    columns = data.columns
    fig, ax = plt.subplots()
    plt.table(cellText=H, colLabels=columns, loc="center")
    plt.axis("off")
    plt.axis('tight')
    plt.savefig("/django/project/media/csv/table.svg", bbox_inches='tight')
    table = f"/media/csv/table.svg"
    return graph, table