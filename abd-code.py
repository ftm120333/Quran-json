
import json


if __name__ == '__main__':
    mushaf = {}
    listOfVerses = []
    f = open('hafs.json', "r", encoding='utf-8')

    verses = json.loads(f.read())

    for pageNo in range(1,605):
        mushaf[str(pageNo)]={"verses":[]}
    for verse in verses:
        # print(verse['sura_name_ar'])
        mushaf[str(verse["page"])]["verses"].append({'jozz': verse['jozz'], 'sura_name_en': verse['sura_name_en'],
                       'sura_name_ar': verse['sura_name_ar'], 'aya_no': verse['aya_no'],
                        'aya_text_emlaey': verse['aya_text_emlaey']})

    # print(mushaf)

    with open('index.json', 'w', encoding='utf-8') as fp:
         json.dump(mushaf, fp, ensure_ascii=False)

    f.close()