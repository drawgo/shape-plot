import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
import os
from matplotlib import font_manager as fm, rcParams
from datetime import datetime as dt

def logtime(msg=''):
    '''
    Função para loggar o timestamp durante a execução do código.
    '''
    return print("["+str(dt.now().date())+' '+str("{:02d}".format(dt.now().hour))+':'+str("{:02d}".format(dt.now().minute))+':'+str("{:02d}".format(dt.now().second))+"]"+"    "+msg)

logtime('Reading PP vias shapefile.')
pp_via = gpd.read_file('data/pp_vias.shp')

def plt_map(name="bsb-print-original", bg_color='#F2EDEB', plt_color='#262626', title_color='#737272', sign_color='#A6A4A4'):
    '''
    Função que plota o gráfico de Brasília.

    Parâmetros:
    name      - nome do arquivo de saida
    bg_color  - cor do fundo
    plt_color - cor do plot
    '''
    logtime('Starting the plot of '+name+' file')
    # n=1.5
    fig, ax = plt.subplots(figsize=(43.3, 29.52))
    pp_via.plot(color=plt_color, ax=ax, linewidth=0.05)
    fig.set_facecolor(bg_color)

    fpath = os.path.join(rcParams["datapath"],
                         "/Users/giovannisantin/Library/Fonts/Cinematografica-Regular-trial.ttf")
    prop = fm.FontProperties(fname=fpath, size='large')
    # plt.text(0.9, 0.1, "Rosto de Brasília", transform=fig.transFigure,
    plt.text(0.6, 0.13,
    '''
    ROSTO DA
    CAPITAL
    '''
    , transform=fig.transFigure,
                 fontproperties=prop, color=title_color, **{'ha': 'center'})

    # fpath = os.path.join(rcParams["datapath"],
    #                      "/System/Library/Fonts/Supplemental/Arial.ttf")
    # prop = fm.FontProperties(fname=fpath, size=2)
    # plt.text(0.99, 0.01, "by @gigiosantin", transform=fig.transFigure, rotation=90,
    #              fontproperties=prop, color=title_color, **{'ha': 'center'})

    ax.axes.get_xaxis().set_ticks([])
    ax.axes.get_yaxis().set_ticks([])
    ax.set_position([0, 0, 1, 1])
    ax.set_aspect('equal', anchor=(0.2, 0.5))
    plt.axis('off')
    logtime(' ├─ Saving rendered map')
    plt.savefig('plots/'+name+'.png',
                facecolor=fig.get_facecolor(), edgecolor='none', dpi=300);
    logtime(' └─ Finish')

if __name__ == '__main__':
    plt_map(name='original')
    plt_map(name='blue-tile', bg_color='#F2F2F2', plt_color='#032CA6', title_color='#4970BF', sign_color='#96ACD9')
    plt_map(name='blue-tile-reverse', bg_color='#032CA6', plt_color='#F2F2F2', title_color='#96ACD9', sign_color='#4970BF')
    plt_map(name='black-gold', bg_color='#0D0807', plt_color='#F2D43D', title_color='#F2CA52', sign_color='#8C8B88')
