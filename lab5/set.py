it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# I. Find the length of the set it_companies
len_it_companies = len(it_companies)
print(len_it_companies)

# II. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# III. Insert multiple IT companies at once to the set it_companies
it_companies.update({'Spotify', 'LinkedIn', 'Tesla'})
print(it_companies)

# IV. Remove one of the companies from the set it_companies
it_companies.discard('Facebook')
print(it_companies)

# V. Difference between remove and discard: 
# it_companies.remove('Facebook')
# remove() raises a KeyError if the item does not exist; discard() does not.
print (it_companies)
