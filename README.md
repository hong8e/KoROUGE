# KoROUGE
Calculating ROUGE score for Korean

## 1. Requirements and Installation
* Python version >= 3.6
* To install KoROUGE
```bash
pip install konlpy
pip install -U git+https://github.com/pltrdy/pyrouge
cd files2rouge
python setup_rouge.py
python setup.py install
```

## 2.Run
* All sentences in the system summary and gold summary must start with <t> and end with <\t> \
  e.g. <t> 나는 학교에 간다 <\t> <t> 나는 공부한다. <\t>
```bash
python KoROUGE.py $system_summary $gold_summary
# Basically, KoROUGE calculate ROUGE with morpheme-level automatically,
# if you don't want to analyze word into morphemes just add options --no_morpheme_analyze
```
