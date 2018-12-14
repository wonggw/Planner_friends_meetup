import pandas as pd
import numpy as np
import operator

today_date=12
total_date=31
data_dict={}
avail_dict={}
values=[]
Ndates=[]
avail_datas=[]
avail_dates=[]
name_weight=[]
name_list=[]
score=0
score_dates={}

def normalize_meanstd(a, axis=None): 
	# axis param denotes axes along which mean & std reductions are to be performed
	mean = np.mean(a, axis=axis, keepdims=True)
	std = np.sqrt(((a - mean)**2).mean(axis=axis, keepdims=True))
	return (a - mean) / std

df=pd.read_csv(filepath_or_buffer = "data.csv")
#print (df)
for index, row in df.iterrows():
	data_dict[row['Names']]=row['Dates Unavailable']
	#print row['Names'], row['Dates Unavailable']

#print (data_dict)

total_dates=np.arange(1,total_date+1)
#print (total_dates)

for key, value in data_dict.items():
	
	values=value.split(",")
	for i in range(len(values)):
		Ndate=values[i].split("-")
		if Ndate[0] == "nil":
			Ndate = -1
			break
		Ndate=np.arange(int(Ndate[0]),int(Ndate[1])+1)
		Ndates=np.append(Ndates,Ndate)
	dates_equal=np.in1d(total_dates,Ndates)
	Ndates=[]
	#print(key,dates_equal)
	for i in range(len(dates_equal)):
		if i<today_date:
			continue
		#print (dates_equal[i])
		if dates_equal[i]==False:
			avail_dates=np.append(avail_dates,i+1)
			try:
				avail_dict[i+1].append(key)
			except:
				avail_dict[i+1]=[key]

	#avail_dict[key]=avail_dates
	len_avail_dates=len(avail_dates)
	avail_datas=np.append(avail_datas,len_avail_dates)
	name_list=np.append(name_list,key)
	#print (len_avail_dates)
	avail_dates=[]

#print (avail_dict)
#print (avail_datas)
norm_datas=normalize_meanstd(avail_datas)
for i in range(len(norm_datas)):
	postnorm_datas=(-np.amin(norm_datas)+norm_datas[i])*0.1+1
	name_weight=np.append(name_weight,postnorm_datas)
	#print (postnorm_datas)
#print (name_weight)
#print (name_list)

for key, value in avail_dict.items():
	for y in range(len(value)):
		for x in range(len(name_list)):
			if name_list[x]==value[y]:
				#print (name_weight[x])
				score+=name_weight[x]
	#print(key,value)
	score_dates[key]=score
	score=0
date_chosen=max(score_dates.iteritems(), key=operator.itemgetter(1))[0]


#print ("Date chosen:",date_chosen)






