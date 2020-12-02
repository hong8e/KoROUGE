# KoROUGE
Calculating ROUGE score for Korean

## 1. Requirements and Installation
* Python version >= 3.6
* To install KoROUGE
'''bash
pip install konlpy
pip install -U git+https://github.com/pltrdy/pyrouge
cd files2rouge
python setup_rouge.py
python setup.py install
'''

## 2.Run
'''bash
python KoROUGE.py $system_summary $gold_summary
'''
