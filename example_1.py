import requests
import base64
import re


# download file
file_url = "https://gist.githubusercontent.com/tm-korn-boonchuay/7f0792b5863a113f62e78ab3af735665/raw/fe403a5be297789915ba128913460752d312261c/data"
example_file = requests.get(file_url)

# decode base64 & extract str
encoding = 'utf-8'
text_value = base64.b64decode(example_file.text)
decoeded = str(text_value, encoding)
decoeded = decoeded.split('----------')
for i in decoeded:
  print(i)
  
# detect Date format in long string
month_master = ('january','feb','march','april','may','june','july','august','september','october','november','december')
for i in decoeded:
  for m in month_master:
    try:
      text = re.search(m,i)
      start_index = text.start()
      end_index = text.end()

      # search for dd mmmm yyyy
      if((i[start_index -2].isdigit() and i[start_index -3].isdigit() and i[start_index -4] == " ")):
        print(i[start_index -3 : end_index + 6])
      # search for d mmmm yyyy
      elif((i[start_index -2].isdigit() and i[start_index -3] == " ")):
        print(i[start_index -3 : end_index + 6])
      # search for mmmm d, yyyy
      elif((i[end_index + 1].isdigit() and i[end_index + 2] == ",")):
        print(i[start_index : end_index + 9])
      # search for mmmm dd, yyyy
      elif((i[end_index + 1].isdigit() and i[end_index + 2].isdigit() and i[end_index + 3] == "," )):
        print(i[start_index : end_index + 9])


    except:
      pass
