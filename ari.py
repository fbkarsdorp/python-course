import os

from preprocess import readcorpusfile, tokenise, splitsentences

def prepare_text(filename):
    return splitsentences(tokenise(readcorpusfile(filename)))

def extract_counts(text):
    n_chars, n_words, n_sents = 0, 0, 0
    for sentence in text:
        n_sents += 1
        for word in sentence:
            n_words += 1
            n_chars += len(word)
    return n_chars, n_words, n_sents

def ARI(n_chars, n_words, n_sents):
    """Compute the Automated Readability Index. This is where the 
    real computation is done."""
    return 4.71 * (n_chars / n_words) + 0.5 * (n_words / n_sents) - 21.43

def compute_ARI(text):
    "Compute the Automated Readability Index."
    n_chars, n_words, n_sents = extract_counts(text)
    return ARI(n_chars, n_words, n_sents)

if __name__ == '__main__':
    for filename in os.listdir('data/gutenberg'):
        print 'ARI %s: %.3f' % (
            filename, compute_ARI(prepare_text(os.path.join('data/gutenberg', filename))))
    