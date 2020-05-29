filenames = ['food52_links.txt', 'allRecipes_links.txt', 'chefKoch_Links.txt', 'lecker_Links.txt', 'eatSmarter_links.txt'
             , 'essenUndTrinken_links.txt', 'kochBar_links.txt' , 'epicurious_links.txt',
             'xiachufang_links.txt', 'xinshipu_links.txt']

with open('~/PATH, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
