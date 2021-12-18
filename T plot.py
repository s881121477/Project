# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:39:12 2021

@author: Yongsheng
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi


def T_pic(result):
    labels = ['F-P1', 'P1-P2', 'P2-P3', 'P3-P1', 'P1-F']
    result = result.groupby(['number']).mean().reset_index()
    # print(result)
    kinds = result.apply(list).iloc[:, 0]
    # print(kinds)
    # kindst = list(result.iloc[:, 0])
    # print(kindst)
    # kindst=result.groupby(['number']).agg('mean').reset_index().apply(list)
    # print(kindst)
    result = pd.concat([result, result[['F-P1']]], axis=1)
    centers = np.array(result.iloc[:, 1:])
    # print(centers)
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))
    # plot and line
    for i in range(len(kinds)):
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, centers[i], linewidth=1, label=kinds[i])
        # print(kinds[i])
        # print(kinds[i])
        cg = ['F-P1', 'P1-P2', 'P2-P3', 'P3-P1', 'P1-F']
        N = len(cg)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]
        plt.title('Player Ability Plot')
        plt.fill(angles, centers[i], facecolor='b', alpha=0.25)
        plt.legend()
        plt.xticks(angles[:-1], cg)
        plt.yticks([0, 1, 2, 3, 4, 5], color="grey", size=8)
        plt.ylim(0, 5)
        plt.savefig(fname='t' + str(kinds[i]) + '.png', bbox_inches='tight', dpi=150)
        plt.show()


# show id data
def data_show(df):
    df = df.groupby(['number']).mean().reset_index().apply(list)
    print(df)


if __name__ == '__main__':
    df = pd.read_excel("T.xls")
    del df['總計時']
    # df=df[['編號','起點到1號','1號到2號','2號到3號','3號到1號','1號到起點']]
    df_r = df.rename(columns={'編號': 'number', '起點到1號': 'F-P1', '1號到2號': 'P1-P2', '2號到3號': "P2-P3", '3號到1號': 'P3-P1',
                              '1號到起點': 'P1-F'})
    df_r_sort = df_r.sort_values(by='number').round(2)
    df_r_sort['number'].astype('int')
    df_r_sort['F-P1'].astype('float')
    df_r_sort['P1-P2'].astype('float')
    df_r_sort['P2-P3'].astype('float')
    df_r_sort['P3-P1'].astype('float')
    df_r_sort['P1-F'].astype('float')

    T_pic(df_r_sort)
    data_show(df_r_sort)
