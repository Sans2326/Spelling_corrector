from spellchecker import SpellChecker

spell = SpellChecker()
incorrect = list(map(str,input().split()))

# find those words that may be misspelled
misspelled = spell.unknown(incorrect)
#print(misspelled)
c = 'a'
print("corrected words: ")
while c!='q':
    for word in misspelled:
        # Get the one `most likely` answer
        print(spell.correction(word))
        c = input("press any key to check for candidate words else press q ")
        if c!='q':
            # Get a list of `likely` options
            print(spell.candidates(word))
            c = 'q'
print("THANKYOU!")