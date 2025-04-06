s = input()
xau = s.split() 
do_dai_xau = 0
for tu in xau:
    if len(tu) > do_dai_xau:
        do_dai_xau = len(tu)
print(do_dai_xau)
