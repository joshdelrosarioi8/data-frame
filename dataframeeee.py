import pandas as pd
bare1 ={'Student':['Ice bear','Panda','Grizzly'],
        'Math':[80,95,79]}
bare2 ={'Student':['Ice bear','Panda','Grizzly'],
        'Electronics':[85,81,83]}
bare3 ={'Student':['Ice bear','Panda','Grizzly'],
        'Geas':[90,79,93]}
bare4 ={'Student':['Ice bear','Panda','Grizzly'],
        'ESAT':[93,89,88]}
bears1= pd.DataFrame(bare1,columns=['Student','Math'])
bears2= pd.DataFrame(bare2,columns=['Student','Electronics'])
bears3= pd.DataFrame(bare3,columns=['Student','Geas'])
bears4= pd.DataFrame(bare4,columns=['Student','ESAT'])

WeBareBears1= pd.merge(bears1,bears2,
                       on='Student')
WeBareBears2= pd.merge(WeBareBears1,bears3,
                       on='Student')
WeBareBears3= pd.merge(WeBareBears2,bears4,
                       on='Student')
