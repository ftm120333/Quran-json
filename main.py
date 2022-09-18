
import json

if __name__ == '__main__':
    mushaf = {}
    setOfSurah = []
    surahNamesCheckList = [] #contains surahs that were added used for lookup only
    f = open('hafs.json', "r", encoding='utf-8')

    verses = json.loads(f.read())

    for verse in verses:
        if verse["jozz"] not in surahNamesCheckList:
            setOfSurah.append({ "jozz":verse["jozz"],"page": verse["page"],"aya_text_emlaey": verse["aya_text_emlaey"]})
            surahNamesCheckList.append(verse["jozz"])

    # surah.clear()

    with open('jozz-info.json', 'w', encoding='utf-8') as fp:
        json.dump(setOfSurah, fp, ensure_ascii=False)

    f.close()