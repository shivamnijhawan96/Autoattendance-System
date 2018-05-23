from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import Attendance, Base

engine = create_engine('sqlite:///attendance.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



import glob
import os
names= []
roll_nos= []
for i in glob.glob(os.path.join(os.getcwd(),"knn_examples\\train\\*\\")):
    print(i)
    _= i.split('\\')[8].replace('\\', '')
    print(_)
    #x, y= _.split('_')[0], _.split('_')[1]
    #names.append(x)
    #roll_nos.append(y)

print(names)
print(roll_nos)

#for i in range(len(names)):
 #   s1 = Attendance(name=names[i], roll_no=roll_nos[i])

 #   session.add(s1)
#session.commit()
