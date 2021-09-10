import pandas as pd
from datetime import datetime
data = []
columns = ["Type","Option","Entry","Entry Time","Exit","Exit Time"]

odf = pd.DataFrame(data,columns=columns)

time = datetime.now()
#odf.append(["call","BNFSEP21",100,time],columns=["Type","Option","Entry","Entry Time"],ignore_index=True)
odf = odf.append({"Type":"call","Option":"BNFSEP2136000CALL","Entry":"100","Entry Time":time},ignore_index=True)
odf = odf.append({"Type":"call","Option":"BNFSEP2136000PUT","Entry":"105","Entry Time":time},ignore_index=True)
print(odf)
odf.loc[odf.Option == "BNFSEP2136000PUT",["Exit","Exit Time"]] = [80,time] 
odf.loc[odf.Option == "BNFSEP2136000CALL",["Exit","Exit Time"]] = [110,time] 
print(odf)
