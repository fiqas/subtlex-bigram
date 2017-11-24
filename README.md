# subtlex-bigram
A small python script that extracts frequency of character bigrams in subtlex corpora.

Instruction:
1. Download CSV file:

http://crr.ugent.be/programs-data/subtitle-frequencies/subtlex-pl

2. Run script (I recommend using terminal in Linux):

python3 count_char_bigrams.py bigrams.txt capital_bigrams.txt < subtlex-pl.csv

bigrams.txt - contains all bigrams LOWERCASED
capital_bigrams.txt - contains all bigrams as they are in original (upper- and lowercased)

If you want it modified to work with n-grams, hit me up.
