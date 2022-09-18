

import json


if __name__ == '__main__':
    mushaf = {}
    setOfSurah_ar = []
    setOfSurah_en = []
    f = open('hafs.json', "r", encoding='utf-8')

    verses = json.loads(f.read())

    for verse in verses:
        # print(verse['sura_name_ar'])
      if verse['sura_name_ar'] not in setOfSurah_ar:
          setOfSurah_ar.append(       verse['sura_name_ar'], )

      if verse['sura_name_en'] not in setOfSurah_en:
         setOfSurah_en.append(verse['sura_name_en'],
                          )

    mushaf['sura_names_ar'] = setOfSurah_ar
    mushaf['sura_names_en'] = setOfSurah_en

    print(setOfSurah_ar)
    print(setOfSurah_en)

    with open('surah.json', 'w', encoding='utf-8') as fp:
         json.dump(mushaf, fp, ensure_ascii=False,indent=2)

    f.close()