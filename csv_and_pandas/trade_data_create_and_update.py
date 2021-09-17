import pandas as pd
from datetime import datetime
data = []
columns = ["Type","Option","Entry","Entry Time","Exit","Exit Time"]

odf = pd.DataFrame(data,columns=columns)

time = datetime.now()
#odf.append(["call","BNFSEP21",100,time],columns=["Type","Option","Entry","Entry Time"],ignore_index=True)
odf = odf.append({"Type":"CE","Option":"BNFSEP2136000CE","Entry":"100","Entry Time":time},ignore_index=True)
odf = odf.append({"Type":"PE","Option":"BNFSEP2136000PE","Entry":"105.76","Entry Time":time},ignore_index=True)
odf = odf.append({"Type":"PE","Option":"BNFSEP2136200PE","Entry":"102.76","Entry Time":time},ignore_index=True)
odf = odf.append({"Type":"CE","Option":"BNFSEP2136000CE","Entry":"150","Entry Time":time},ignore_index=True)

print(odf)
odf.loc[odf.Option == "BNFSEP2136000PE",["Exit","Exit Time"]] = [80,time] 
odf.loc[odf.Option == "BNFSEP2136000CE",["Exit","Exit Time"]] = [110,time]
print(odf)

print(odf.loc[odf["Type"] == "CE"]["Option"].to_list())


test_list = map(float,odf["Entry"].to_list())

print(sum(test_list))
