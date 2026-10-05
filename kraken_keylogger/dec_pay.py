d_url = "thpt:s//amhsrefoamtsre.sycuoc/ih/nes.1tha" # i revesed it first manually
good = ""
def reverse2(letters):
    global good
    letters = letters[::-1]
    good += letters
tgme3 = ""
for m in d_url:
    tgme3 += m
    if len(tgme3) % 2 == 0 and len(tgme3) != 0:
        reverse2(tgme3)
        tgme3 = ""
    else:
        ...
print(good)