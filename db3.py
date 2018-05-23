
import glob
import os
for i in glob.glob(os.path.join(os.getcwd(),"knn_examples\\train\\*\\")):
    print(i.split('\\')[8].replace('\\', ''))

