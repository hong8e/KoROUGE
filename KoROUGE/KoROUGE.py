
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
    # perl script uses "." as sentence marker. That's why we replace <t> and </t>.
    lines1 = [' '.join([num_to_alpha(embedding[key.lower()]).replace('<t> ', '').replace('</t>', '.') for key in line.split()]) for line in lines1]
    lines2 = [' '.join([num_to_alpha(embedding[key.lower()]).replace('<t> ', '').replace('</t>', '.') for key in line.split()]) for line in lines2]
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
    parser.add_argument('system', type=str, help="Path to system summary file")
    parser.add_argument('reference', type=str, help="Path to reference file")
    parser.add_argument('-nm', '--no_morpheme_analyze', action='store_true', help="Turn off morphological analyzer")
    parser.add_argument('-nl','--no_rouge_l', action='store_true', help="Do not calculate ROUGE-L")
    parser.add_argument('-n','--n_gram', default="3", type=str, help="Change max-ngram" )
    parser.add_argument('-s','--saveto', type=str, help="File to save scores")
    args = parser.parse_args()
    
    k = Komoran()
    lines1 = []
    lines2 = []
    with open(args.system, 'r') as f:
        lines1 = f.readlines()
    with open(args.reference, 'r') as f:
        lines2 = f.readlines()
    lines1 = [line1.strip() for line1 in lines1]
    lines2 = [line2.strip() for line2 in lines2]

    if not args.no_morpheme_analyze:
        print('morph analyzing')
        lines1 = morph_analyze(lines1, k)
        lines2 = morph_analyze(lines2, k)
    newlines1, newlines2 = change_to_numbers(lines1, lines2)
    with open(args.system + '.vocab', 'w') as f:
        f.write('\n'.join(newlines1))
    with open(args.reference + '.vocab', 'w') as f:
        f.write('\n'.join(newlines2))
    print('calculating rouge')
    if args.no_rouge_l:
        files2rouge.run(args.system + '.vocab', args.reference + '.vocab', '-c 95 -r 1000 -a -x -n ' + args.n_gram, saveto=args.saveto)
    else:
        files2rouge.run(args.system + '.vocab', args.reference + '.vocab', '-c 95 -r 1000 -a -n ' + args.n_gram, saveto=args.saveto)

if __name__=='__main__':	
	main()

