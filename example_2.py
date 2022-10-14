import spacy
import requests
import re
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

# download file
file_url = "https://www.gutenberg.org/cache/epub/19942/pg19942.txt"
example_file = requests.get(file_url)
text = example_file.text
print(text)

# find start_end
start_str = "CANDIDE]"
end_str = "FOOTNOTES"
start_point = text.find(start_str) + 30
end_point = text.find(end_str)
print(f"start index is {start_point} , end is {end_point}")
story = text[start_point : end_point]

# find romance number
def int_to_Roman(num) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
    
# find chapter position
chapter = range(30)
chapter_position = []
for i in chapter:
  if i == 4:
    # for hendle V position
    X_round_search = "TEMPEST, SHIPWRECK, EARTHQUAKE,"
    position = re.search(X_round_search, story).start()
    print(story[position - 5: position + 5], position)
    chapter_position.append(position - 1)
    continue
  if i == 9:
    # for hendle X position
    X_round_search = "IN WHAT DISTRESS CANDIDE"
    position = re.search(X_round_search, story).start()
    print(story[position - 5: position + 5], position)
    chapter_position.append(position - 1)
    continue
  position = re.search(f"{int_to_Roman(i + 1)}", story).start()
  chapter_position.append(position)
  print(story[position: position + 10] , position)

# find name and save file
for i, v in enumerate(chapter_position):
  chaper_text = ""
  if i == 29:
    chaper_text = story[chapter_position[i] - 1 : end_point]
  elif i == 4 or i == 9:
    chaper_text = story[chapter_position[i] - 5 : end_point]
  else:
    chaper_text = story[chapter_position[i] - 1 : chapter_position[i + 1]]

  # save file
  f = open(f"{int_to_Roman(i+1)}.txt", "a")
  f.write(chaper_text)
  f.close()
  article = nlp(chaper_text)
  person_list = []
  print("============")
  print(i)
  for i in article.ents:
    if i.label_ == 'PERSON':
      person_list.append(i.text)
  
  print(set(person_list))