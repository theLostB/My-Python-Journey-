st = input("Enter your message: ")
words = st.split(" ")
coding = input("1 for Coding 0 for Dcoding: ")
coding = True if(coding=="1") else False
print(coding)
if(coding):
    nwords = []
    for word in words:
        if(len(words)>=3):
            r1 = "dhk"
            r2 = "vsh"
            stnew = r1+word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
    
else:
    nwords =[]
    for word in words:
        if(len(words)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(words[::-1])
    print(" ".join(nwords))