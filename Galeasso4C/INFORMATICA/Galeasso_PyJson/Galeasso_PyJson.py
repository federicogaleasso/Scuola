#GALEASSO FEDERICO 4C 28/4/2023 ESERCIZIO IN CLASSE - PY e JSON

import json

with open("./bookmarks-2023-04-28.json") as fp:
	data=json.load(fp)

print(data["children"][0]["children"][0]["children"][2]["title"], "\nuri:", data["children"][0]["children"][0]["children"][2]["uri"])
