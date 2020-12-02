# KoROUGE
Calculating ROUGE score for Korean

## 1. Requirements and Installation
* Python version >= 3.6
* To install KoROUGE
```bash
pip install konlpy
pip install -U git+https://github.com/pltrdy/pyrouge

git clone https://github.com/pltrdy/files2rouge.git     
cd files2rouge
python setup_rouge.py
python setup.py install

git clone https://github.com/hong8e/KoROUGE.git
cd KoROUGE
python setup.py install
```

## 2.Run
* All sentences in the system summary and gold summary must start with <t> and end with <\t> \
  e.g. \<t> 나는 학교에 간다 <\t> \<t> 나는 공부한다. <\t>
```bash
KoROUGE $system_summary $gold_summary
# Basically, KoROUGE automatically analyzes words into morphemes and calcuate ROUGE scores,
# if you want to calculate ROUGE with word-level just add options "--no_morpheme_analyze".
```
