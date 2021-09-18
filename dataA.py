import pandas as pd
import plotly.express as px

rd=pd.read_csv("data.csv")
mean=rd.groupby("level")["attempt"].mean()


fig=px.bar(mean, x=mean, y=["Level 1","Level 2","Level 3","Level 4"], color=mean)

fig.show()