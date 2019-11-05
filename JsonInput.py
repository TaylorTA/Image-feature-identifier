import json
import os
import pandas as pd

# this finds our json files
path_to_json = 'json/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

# here I define my pandas Dataframe with the columns I want to get from the json
jsons_data = pd.DataFrame(columns=['q', 'timestamp', 'images'])

# we need both the json and an index number so use enumerate()
curr = 0;
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)

        # here you need to know the layout of your json and each json has to have
        # the same structure (obviously not the structure I have here)
        if json_text:
            for i in range(len(json_text)):
                q = json_text[i]['q']
                timestamp = json_text[i]['timestamp']
                images = json_text[i]['images']
                # here I push a list of data into a pandas DataFrame at row given by 'index'
                jsons_data.loc[curr] = [q, timestamp, images]
                curr = curr+1

# now that we have the pertinent json data in our DataFrame let's look at it
print(jsons_data)
print(type(jsons_data))
target = 'logo';
mask = jsons_data.applymap(lambda x: target in str(x))
print (mask)
df1 = jsons_data[mask.any(axis=1)]
print (df1)