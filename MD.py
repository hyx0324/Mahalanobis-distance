import pandas as pd
import heapq
import os

#Find indexes of the largest datas
def get_max_index(k):

	#Data with the specific index
	index_msjl_data = msjl_data[msjl_data['index'].isin([k])]
	index_msjl_data = index_msjl_data.drop(['index'], axis=1)
	index_msjl_data = index_msjl_data.reset_index()

	#Delete the data with the specific index
	noindex_msjl_data = msjl_data[~msjl_data['index'].isin([k])]
	noindex_msjl_data = noindex_msjl_data.drop(['index'], axis=1)
	noindex_msjl_data = noindex_msjl_data.reset_index()

	#Calculate the Mahalanobis distance
	w = []
	for j in range(1111-n[k]):
		result = 0
		for i in range(n[k]):
			result += 1 / 7 * (index_msjl_data.loc[i] * noindex_msjl_data.loc[j])

		a = 0
		for i in range(7):
			a += result[i+1]

		b = 1 / n[k] * a
		w.append(b)

	#Get the indexes of the largest datas (after delete the specific index)
	max_w_index_list = list(map(w.index, heapq.nlargest(7-n[k], w)))
	return max_w_index_list


#Read the data
msjl_file_path = 'data.csv'
msjl_data = pd.read_csv(msjl_file_path)
#msjl_data.describe()

#copy the data
copy_msjl_data = msjl_data.copy()

#Count the number of each index
n = pd.value_counts(msjl_data['index'])

#Get dictionary of index
max_index = {}
for i in range(1, 105):
	if n[i] < 7:
		max_index[i] = get_max_index(i)

#Add the lines
for key in max_index:
	#Delete the line of the corresponding index
	new_msjl_data = msjl_data[~msjl_data['index'].isin([key])]
	new_msjl_data = new_msjl_data.reset_index()

	for value in max_index[key]:
		copy_msjl_data = copy_msjl_data.append(new_msjl_data.loc[value],
						ignore_index=True)
		copy_msjl_data.iloc[-1, 7] = key


#Sort rows
copy_msjl_data = copy_msjl_data.sort_values(by='index')
#Reset index
#copy_msjl_data = copy_msjl_data.reset_index()
#Save
copy_msjl_data.to_csv('Resutl3.csv')

print('Success')


