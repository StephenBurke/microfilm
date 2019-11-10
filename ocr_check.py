import re
print("ocr_check")
temp_word = ''
ocr_words = []
known_words = []
good_Words = []
good = True
breaking = 0
lengths = 0
known_words = open('/home/tyler/Desktop/words_alpha.txt','r').read().splitlines()
print(len(known_words))
print("checking")
with open('/home/tyler/Desktop/bigOne.txt', 'r') as f:
#with open('/home/tyler/Downloads/FullPageScan.txt', 'r') as f:
    for line in f:
        for word in line.split():
            a = re.sub(r'\W+', '', word)
            ocr_words.append(a)

for word in ocr_words:
    good = False
    for known in known_words:
        if word == known:
            good = True
            breaking+=1
            good_Words = []
            break
        else:
            good = False
lengths = len(ocr_words)
print(breaking)
print(lengths)
confidence_score = float(breaking)/float(lengths) * 100
print("confidence is "+ str(confidence_score))
