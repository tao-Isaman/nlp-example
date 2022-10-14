# NLP Example

## Setup
install library
```
pip install requests spacy collections
```

## Run Local
```
python example_1.py
python example_2.py
```

## Run Colab (Recommend)
click [here](https://colab.research.google.com/drive/1_moFBN-ZrZjH7ztJx5om533hu7eEpd0H#scrollTo=IMcnAKdXr9Il) to go the Colab Notebook try to clone and run all notebook is easier to run in local computer


## Problem A
Create and share a simple secret github gist to solve the below problem in Python:
Given a base64 encoded file, extract all dates that existed in the file and print to the stdout.
Note that dates have to be composed of three parts day, month, and year with any arbitrary
order. For instance:
1. 25 january 2022 is a date
2. January 25th, 2022 is also a date
3. 2022/1 is not a date
4. year 2022 is not a date
5. January 2022 is not a date


## Problem B
Create and share a simple secret github gist to solve the below problem in Python:
Given a long text file (book), extract:
1. The chapters in the book and save them in individual text files using the chapter number
as a file name without any metadata.
2. For each chapter, extract the names of the characters with dialog and output them as a
list.
Problem B Sample Run

### text
IV

HOW CANDIDE FOUND HIS OLD MASTER PANGLOSS, AND WHAT HAPPENED TO THEM.
Candide, yet more moved with compassion than with horror, gave to this
shocking beggar the two florins which he had received from the honest
Anabaptist James. The spectre looked at him very earnestly, dropped a
few tears, and fell upon his neck. Candide recoiled in disgust.
"Alas!" said one wretch to the other, "do you no longer know your dear
Pangloss?"
"What do I hear? You, my dear master! you in this terrible plight!
What
misfortune has happened to you? Why are you no longer in the most
magnificent of castles? What has become of Miss Cunegonde, the pearl
of
girls, and nature's masterpiece?"
"I am so weak that I cannot stand," said Pangloss.
Upon which Candide carried him to the Anabaptist's stable, and gave
him
a crust of bread. As soon as Pangloss had refreshed himself a little:
"Well," said Candide, "Cunegonde?"

### Output 1

4.txt (which would contain the text above)
### Output 2

[“Pangloss”, “Candide”]