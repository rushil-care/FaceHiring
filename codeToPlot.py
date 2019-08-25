# import gmplot package 
import gmplot 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('output.csv')
  
latitude_list = df['Latitude']
longitude_list = df['Longitude']
  
gmap3 = gmplot.GoogleMapPlotter(latitude_list[0], 
                                longitude_list[0], 13) 
  
# scatter method of map object  
# scatter points on the google map 
gmap3.scatter( latitude_list, longitude_list, '# FF0000', 
                              size = 40, marker = False ) 
  
# Plot method Draw a line in 
# between given coordinates 
gmap3.plot(latitude_list, longitude_list,  
           'cornflowerblue', edge_width = 2.5) 
  
gmap3.draw( "/Users/frankhart/Desktop/chalk-street/map.html" ) 

speed = np.array(df['Speed'][df['Speed']>0.0]) * 3.6
time = df['Time']

avg_speed = np.sum(speed)/len(speed)
max_speed = np.max(speed)

plt.plot(speed, time)
plt.show()