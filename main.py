
import json


if __name__ == '__main__':
    mushaf = {}
    listOfVerses = []
    f = open('hafs.json', "r")

    data = json.loads(f.read())
    for x in range(1,605):
        verses = {}
        for j in range(6236):
           if x == data[j]['page']:
               verse = {}
               verse['jozz'] = data[j]['jozz']
               verse['sura_name_en'] = data[j]['sura_name_en']
               verse['sura_name_ar'] = data[j]['sura_name_ar']
               verse['aya_no'] = data[j]['aya_no']
               verse['aya_text_emlaey'] = data[j]['aya_text_emlaey']
               listOfVerses.append(verse)
        verses['verses'] = listOfVerses
       # print(listOfVerses[0])

        mushaf[str(x)] = verses
   # print(mushaf)

    with open('mushaf_ident2.json', 'w') as fp:
         json.dump(mushaf, fp, indent= 4)

   # print(verses)
    #mushaf['verses']
               #res_count = data[2]['sura_name_en']
    #print(data['id'])
    #print(res_count)
    f.close()