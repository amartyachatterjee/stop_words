# stop_words
A compendium of assorted English stop words collected from several different sources. This has the ability to take in domain-specific stop words as well.

## **Installation**
```
pip install git+https://github.com/amartyachatterjee/stop_words.git

pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.8.0/en_core_web_lg-3.8.0-py3-none-any.whl
```

## **Usage**
```
from pathlib import Path
from stop_words.stop_words.stop_words import CustomStopWords

nltk_data_path = Path("C:/path/to/nltk_data")

my_stop = CustomStopWords(domain_specific_stops=['stp1','custstop'],
                          nltk_data_path=nltk_data_path)

print(f'''English stops: {my_stop.english_stops}''')
print(f'''domain stops: {my_stop.domain_specific_stops}''')
```
