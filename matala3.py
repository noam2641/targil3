text = open('�צאט WhatsApp עם יום הולדת בנות לנויה.txt', 'r', encoding='utf-8')
id=0
data=list()
idan=dict()
counter=0
for line in text:
    if "נוצרה על ידי" in line:
        matadata={"chat_name":line[line.find(' "')+2:line.find('" ')], "creation_date": line[ :line.find('-')-1] , "num_of_participants":0 , "creator":line[line.find('" ')+15: ].strip()}
    if ":" in line[line.find('-')+2: ]: 
        if line[line.find('-')+2:line.find(': ')] not in idan:
            id=id+1
            idan[line[line.find('-')+2:line.find(': ')]]=id
        data.append({"datetime":line[ :line.find('-')-1], "id": idan[line[line.find('-')+2:line.find(': ')]] , "text":line[line.find(': ')+1: ].strip()})
        counter=counter+1
    if ":" and '-' not in line:
        data[counter-1]['text']=data[counter-1]['text']+" "+line.strip()
matadata['num_of_participants']=id
matadata['creator']=idan[matadata['creator']]
summary={"matadata":matadata, "messages":data}
import json
json1=json.dumps(summary, ensure_ascii=False, indent=5)
print(json1)
with open(matadata['chat_name']+'.txt' , 'w',encoding='utf-8') as f:
   f.write(json1)

