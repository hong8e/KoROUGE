
import argparse
import files2rouge
from konlpy.tag import Komoran

def num_to_alpha(n):
    char = ''
    if n == '<t>' or n == '</t>':
        return n
    if n == 0:
        return 'a'
    while n > 0:
        char = chr(97+n%26) + char
        n = int(n / 26)
    return char

def change_to_numbers(lines1, lines2):
    vocab = set()
    for line in lines1:
        vocab.update(map(lambda x: x.lower(), line.split()))
    for line in lines2:
        vocab.update(map(lambda x: x.lower(), line.split()))
    embedding = {key:value for value, key in enumerate(list(vocab))}
    embedding['<t>'] = '<t>'
    embedding['</t>'] = '</t>'
    lines1 = [' '.join([num_to_alpha(embedding[key.lower()]) for key in line.split()]).replace('<t> ', '').replace('</t>', '.') for line in lines1]
    lines2 = [' '.join([num_to_alpha(embedding[key.lower()]) for key in line.split()]).replace('<t> ', '').replace('</t>', '.') for line in lines2]
    return lines1, lines2

def morph_analyze(lines, k):
    for i, line in enumerate(lines):
        try:
            sents = line[4:-5].split(' </t> <t> ')
            for j, sent in enumerate(sents):
                sents[j] = k.morphs(sent)
            lines[i] = '<t> ' + ' </t> <t> '.join([' '.join(sent) for sent in sents]) + ' </t>'
        except:
            lines[i] = ''
    return lines


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str)
    parser.add_argument('target', type=str)
    parser.add_argument('--no_morpheme_analyze', action='store_true')
    args = parser.parse_args()
    
    k = Komoran()
    lines1 = []
    lines2 = []
    with open(args.source, 'r') as f:
        lines1 = f.readlines()
    with open(args.target, 'r') as f:
        lines2 = f.readlines()
    lines1 = [line1.strip() for line1 in lines1]
    lines2 = [line2.strip() for line2 in lines2]

    if not args.no_morpheme_analyze:
        print('morph analizing')
        lines1 = morph_analyze(lines1, k)
        lines2 = morph_analyze(lines2, k)
    newlines1, newlines2 = change_to_numbers(lines1, lines2)
    with open(args.source + '.vocab', 'w') as f:
        f.write('\n'.join(newlines1))
    with open(args.target + '.vocab', 'w') as f:
        f.write('\n'.join(newlines2))
    print('calculating rouge')
    files2rouge.run(args.source + '.vocab', args.target + '.vocab', '-c 95 -r 1000 -n 3 -a')

if __name__=='__main__':	
	main()

