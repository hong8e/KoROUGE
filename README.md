# KoROUGE
Calculating ROUGE score for Korean \
Given two files (system, reference) with the same number of lines, KoROUGE calculates the average ROUGE scores of each line.

## 1. Requirements and Installation
* Python version >= 3.6
* To install KoROUGE
```
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
  e.g. <t> 나는 학교에 간다 <\t> <t> 나는 공부한다. <\t>
```bash
KoROUGE $system_summary $gold_summary
# Basically, KoROUGE automatically analyzes words into morphemes and calcuate ROUGE scores,
# if you want to calculate ROUGE with word-level just add options "--no_morpheme_analyze".
```
* Options
```
usage: KoROUGE [-h] [-nm] [-nl] [-n N_GRAM] [-s SAVETO] system reference

positional arguments:
  system                Path to system summary file
  reference             Path to reference file

optional arguments:
  -h, --help            show this help message and exit
  -nm, --no_morpheme_analyze
                        Turn off morphological analyzer
  -nl, --no_rouge_l     Do not calculate ROUGE-L
  -n N_GRAM, --n_gram N_GRAM
                        Change max-ngram
  -s SAVETO, --saveto SAVETO
                        File to save scores
```
