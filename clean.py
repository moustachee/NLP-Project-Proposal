import json

with open("data.json") as json_file:
    data = json.load(json_file)
        
    text = open("Output.txt", "w")

    for dict_number in range(len(data)-1):
    	
    	reviews = data[dict_number]['review']
    	serieName = data[dict_number]['serieName']
    	text.write(serieName.upper()+"\n")
    	for index in range(len(reviews)-1):
			review = reviews[index].encode("utf-8")
			if(review!="\n"):
				text.write(review+"\n")

    text.close()