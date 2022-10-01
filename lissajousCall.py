import sys
import numpy as np

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from PySide6.QtGui import Qt

import pyqtgraph as pg


# 自作のライブラリ
from plotsingleUi import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.p1 = self.set_graph_ui()

        self.startTimer()
        self.spinBox_x.valueChanged.connect(self.startTimer)
        self.spinBox_x.valueChanged.connect(self.graphClear)
        self.spinBox_y.valueChanged.connect(self.startTimer)
        self.spinBox_y.valueChanged.connect(self.graphClear)

        self.i = 0
        self.samplingNum = 2000


    def graphClear(self):
        self.p1.clear()

    def lissajous(self,i):
        m = self.spinBox_x.value()
        n = self.spinBox_y.value()
        t = np.linspace(-np.pi,np.pi,self.samplingNum)
        x = np.sin(m * t[i])
        y = np.sin(n * t[i])
        return x, y

    def startTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.plot_xy)  # QTimer が timeout した場合に呼び出す関数を登録
        self.timer.start(1)  # タイマーをスタートさせる



    def set_graph_ui(self):
        """_summary_

        Returns:
            _type_: _description_
            軸やレジェンドなどを設定してGraphオブジェクトを返す
        """
        setprop = lambda x: (x.setAutoVisible(y=True),
                             x.enableAutoRange(False),
                             x.showAxis('right'),
                             x.showAxis('left'),
                             x.showAxis('top'),
                             x.getAxis('top').setHeight(50),
                             x.getAxis('bottom').setHeight(50),
                             x.getAxis('right').setWidth(50),
                             x.getAxis('left').setWidth(50),
                             x.showGrid(x=True, y=True, alpha = 1),
                             x.setAutoVisible(y=True),
                             x.setXRange(-1, 1, padding=0.1),
                             x.setYRange(-1, 1, padding=0.1),
                             x.addLegend(offset=(10,10)),
                             x.setTitle('<font size=\'14\' color=\'#FFFFFF\'>'+ 'Lissajous' +'</font>'),
                             x.setLabel('left'  , text='y', units='', **styles),
                             x.setLabel('bottom', text='x', units='', **styles),
                             x.setLabel('right'  , text='y', units='', **styles),
                             x.setLabel('top', text='x', units='', **styles),
                             )
        '''
        Macの場合、フォントはFont Bookの正式名称の下にある「ファミリー」を使用する。
        ときどき、non-localizedといわれる以下のメッセージが出力される。

        qt.qpa.fonts: Populating font family aliases took 512 ms. Replace uses of "ヒラギノ角ゴシック"
        with its non-localized name "Hiragino Sans" to avoid this cost.

        この場合は、指示通りにHiragino Sansを設定すれば問題はない。
        '''
        self.fontCssLegend = '<style type="text/css"> p {font-family: Helvetica, HackGen35 Console NFJ; font-size: 15pt; color: "#ffffff"} </style>'
        styles = {'color':'white',
                  'font-size':'30px',
                  'font-style':'bold',
                  'font-family': 'Helvetica, HackGen35 Console NFJ'
                  }

        p1 = self.graphicsView.addPlot()
        setprop(p1)
        return p1

    def plot_xy(self):
        if self.i < self.samplingNum-1:
            x,y = self.lissajous(self.i)
            self.p1.plot([x],[y],
                         clear=True,
                         pen='#0F0',
                         alpha=1,
                         symbolBrush='#0F0',
                         symbolSize=10,
                         name=self.fontCssLegend + '<p>Plotポイント</p>'
                         )
            self.i  += 1
        else:
            self.i = 0


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
