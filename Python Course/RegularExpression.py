import re
pattern = r"[A-Z]+yclone"
text = '''
sjwkbw wknw akwma akanksha aak aa ka aks VV jig co GCM UCO UC hi call whwvna UVM vo BN IB bsivamakavakia v chal wbbaababaNkWohw iwbw a oaajaiana abajajanabjaa wjaanakajabj shnwkasbbsnskwokeh njdbekbekwnb EQ eb ejeb BN websh jeb Cyclone Dyclone

'''
#match = re.search(pattern, text)
#print(match)
matches = re.finditer(pattern, text)
print(matches)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])