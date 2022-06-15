print("SKRIV ETT NUMMER MELLAN 1 OCH 10000")
count = 0
k = int(input())
if k > 0 and k <= 10000:

    for x in range(0, 1000):
        for y in range(0, 1000):
            if x ** 3 + y ** 3 == k:
                print(x,y)
                count=1

else:
    count=1
    print('DUMMA FAN SKRIV ETT NUMMER MELLAN 1 OCH 10000!!!!!')
if count==0:
    print("tyvärr så finns det inga kubsumummor ifrån det där talet. jag ber väldigt mycket om ursäkt för detta problem och ber om ursäkt.dumfan")


