import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi



#T plot method
def T_pic(result):
    
    #draw 
    labels = ['起點到1號',	'1號到2號',	'2號到3號',	'3號到1號'	,'1號到起點']
    kinds = list(result.iloc[:, 0])
    result = pd.concat([result, result[['起點到1號']]], axis=1)
    centers = np.array(result.iloc[:, 1:])
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))
    #plot and line
    for i in range(len(kinds)):
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True) 
        ax.plot(angles, centers[i], linewidth=1, label=kinds[i])
        cg=['F-P1','P1-P2','P2-P3','P3-P1','P1-F']
        N=len(cg)
        angles=[n/float(N)*2*pi for n in range(N)]
        angles+=angles[:1]
        plt.title('Player Ability Plot')
        plt.fill(angles,centers[i],facecolor='b',alpha=0.25)
        plt.legend()
        plt.xticks(angles[:-1],cg)
        plt.yticks([0,1,2,3,4,5],color="grey",size=8)
        plt.ylim(0, 5)
        plt.show()
        
#show id data
def data_show():
    df=pd.read_excel("T型模式取樣_Data_202006151720.xls",sheet_name=0,usecols=("G:H"))
    df_sort=df.sort_values(by='編號')
    print(df_sort)



#call funtion
if __name__ == '__main__':
    result = pd.read_excel("T型模式取樣_Data_202006151720.xls",sheet_name=0,usecols=("B:G"))
    df_result=result[['編號','起點到1號','1號到2號','2號到3號','3號到1號','1號到起點']]
    df_result_sort=df_result.sort_values(by='編號')
    T_pic(df_result_sort)
    data_show()
    

