#
# wk1ex2a.py
#

import random          # importeer de module met de naam random


def rps():
    """ this plays a game of rock-paper-scissors in Dutch ("steen"-"papier"-"schaar")
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """
    print("Welkom bij steen, papier, schaar!\
        Kan jij mij verslaan? ")
    user = input("Kies je wapen [steen, papier, schaar]: ")
    comp = random.choice(['steen', 'papier', 'schaar'])
    print()

    print('De gebruiker (jij) koos', user)
    print('De computer (ik)   koos', comp)
    print()
#user wint van comp steen > schaar
    if user == 'steen' and comp == 'schaar':
        print('Mijn schaar is geplet! Hoe kon je dat doen?\
            De gebruiker wint!')
#user wint can comp papier > steen
    elif user == 'papier' and comp == 'steen':
        print ('Een papiertje vernietigd mijn steen? Hoe is dat mogelijk?\
            De gebruiker wint!')
#user wint van comp schaar > papier
    elif user == 'schaar' and comp == 'papier':
        print('Een schaar? Nu is mijn papiertje stuk :( \
            De gebruiker wint!')
# comp wint steen tegen schaar
    elif comp == 'steen' and user == 'schaar':
        print ('Een schaar? Een steen en hij is weg! \
            De computer wint!')

  #comp wint papier tegen steen 
    elif comp == 'papier' and user == 'steen':
        print ('Een steen? Ik vermorzel het!\
        De computer wint!')

  #comp wint schaar tegen papier  
    elif comp == 'schaar' and user == 'papier':
        print('Jou papiertje? Die knip is zo doormidden!\
            De computer wint!')

    elif comp == 'steen' and user == 'steen':
        print ('We hadden het zelfde idee! Een steen kan helaas geen steen kapot maken!\
            Het is gelijkspel!')
    elif comp == 'schaar' and user == 'schaar':
        print ('Twee scharen kunnen weinig met elkaar doen.\
            Het is gelijkspel!')
    elif comp == 'papier' and user == 'papier':
        print ('Twee floppige papiertjes.. die kunnen niet veel doen.\
            Het is gelijkspel!')
