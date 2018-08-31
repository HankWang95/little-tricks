import csv
import json


def main():
	l = []
	i = 1
	country_list = {}
	end_list = []
	print("start")
	with open('t.csv') as f:
		f_csv = csv.DictReader(f)
		for row in f_csv:
			l.append(row)
			if i == 10:
				print(l)
	# l : [dict(name:xxx, country:xxx, subcountry:xxx), dict(.....)]
	subcountry_list = {}
	for row in l:
		if row['subcountry'] not in subcountry_list:
			subcountry_list[row['subcountry']] = {'label':row['subcountry'], 'children':[], 'value':row['subcountry']}
		subcountry_list[row['subcountry']]['children'].append({'label':row['name'], 'value':row['name']})

	# print(subcountry_list)
	for row in l:
		if row['country'] not in country_list:
			country_list[row['country']] = {'label':row['country'], 'children':[], 'value':row['country']}
			country_list[row['country']]['children'].append(subcountry_list[row['subcountry']])

		if subcountry_list[row['subcountry']] not in country_list[row['country']]['children']:
			country_list[row['country']]['children'].append(subcountry_list[row['subcountry']])

	for row in country_list:
		
		end_list.append({'label':country_list[row]['label'], 'value':country_list[row]['label'], 'children':country_list[row]['children']})


	print(len(subcountry_list))
	print(len(l))
	print(len(end_list))

	print(country_list["China"]['children'])
	data = {}
	data['children'] = end_list

	with open('data.json', 'w') as f:
		json.dump(data, f)


main()