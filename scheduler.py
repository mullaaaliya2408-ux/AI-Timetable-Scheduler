import random,pandas as pd
from data import teachers,days,periods
subjects=[("Python","Theory"),("AI","Theory"),("DBMS","Theory"),("ML","Theory"),("Flutter","Lab"),("DS","Theory")]
def generate():
    table=pd.DataFrame(index=days,columns=periods)
    used={}
    for d in days:
        for p in periods:
            while True:
                sub,typ=random.choice(subjects)
                t=[k for k,v in teachers.items() if sub in v][0]
                if (d,p,t) not in used:
                    table.loc[d,p]=f"{sub}\n({t})"
                    used[(d,p,t)]=1
                    break
    return table
