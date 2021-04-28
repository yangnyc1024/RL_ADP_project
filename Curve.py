import numpy as np 
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


class Curve(object):
    def __init__(self, numbers, lo_bd, up_bd):
        self.numbers = numbers
        self.up_bd = up_bd
        self.lo_bd = lo_bd
        self.steps = (up_bd-lo_bd) // numbers
        self.seg_initial()
        self.curve_initial()
    
    def seg_initial(self):
        segments = []
        for i in range(self.lo_bd, self.up_bd+self.steps, self.steps):
            value = 50 - i // self.steps
            segments.append([i, value])
        self.segments = segments
    
    def seg_update(self, point_1, point_2):
        point_1_x = point_1[0]
        point_1_y = point_1[1]
        point_2_x = point_2[0]
        point_2_y = point_2[1]
        for i in range(self.numbers +1):
            curr = self.segments[i]
            curr_x = curr[0]
            curr_y = curr[1]
            if curr_x <= point_1_x and curr_y <= point_1_y:
                self.segments[i][1] = point_1_y
            elif curr_x >= point_2_x and curr_y >= point_2_y:
                self.segments[i][1] = point_2_y


    def curve_initial(self):
        df = pd.DataFrame (self.segments,columns=['x','y'])
        self.curve_df = df
        self.point_X = self.curve_df['x'].to_list()
        self.point_Y = self.curve_df['y'].to_list()

    def show_curve(self):
        sns.set_theme(style="darkgrid")   
        sns.lineplot(x='x', y='y',data=self.curve_df)
        plt.show()


    def curve_update(self, new_curve_Y, point_1, point_2):
        for i in range(len(new_curve_Y)):
            value = new_curve_Y[i]
            self.segments[i][1] = value
        self.seg_update(point_1, point_2)


    # def point_X(self):
    #     point_df = self.curve_df
    #     point_X = point_df['x'].to_list()
    #     return point_X

    # def point_Y(self):
    #     point_df = self.curve_df
    #     point_Y = point_df['y'].to_list()
    #     return point_Y
        


curve_1 = Curve(100, 0, 3000)

#print(curve_1.segments)
#curve_1.seg_update([50,100],[105,50])
print(curve_1.segments)

#print(curve_1.curve_df)
#curve_1.show_curve()

print(curve_1.point_X)
print(len(curve_1.segments)-1)
print(curve_1.numbers)
print(curve_1.steps)
