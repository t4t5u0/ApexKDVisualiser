import matplotlib.pyplot as plt
import pandas as pd
import japanize_matplotlib
from math import ceil

# CSVの形式
# 一行目をシーズンで固定する
# 他の行は自由


IS_SAVE = True

def main():

    df = pd.read_csv('TamagoDamage.csv') # 書き換える

    season = df["シーズン"]

    indexis: list[str] = list(df.columns)[1:]

    rows = ceil(len(indexis)/2)

    fig, axes = plt.subplots(
        nrows=rows, ncols=2, figsize=(6, rows*2/0.96))
    fig.suptitle("TamagoDamage 戦績") # 書き換える
    plt.subplots_adjust(wspace=0.4, hspace=0.6)

    for i, index in enumerate(indexis):
        axes[i//2, i % 2].plot(season, df[index])
        axes[i//2, i % 2].set_title(index)

    if rows * 2 > len(indexis):
        axes[(i+1)//2, (i+1) % 2].axis('off')

    fig.tight_layout(rect=[0,0,1,0.96])

    if IS_SAVE:
        plt.savefig("t4t5u0.png")
    else:
        plt.show()


if __name__ == "__main__":
    main()
