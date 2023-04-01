dat=['19.06.1919']
notik=["Cēsu kaujas"]
notikaprak=['Cēsu kaujas bija viens no nozīmīgākajiem pavērsiena punktiem Latvijas Neatkarības kara gaitā. Kaujas noslēdzās ar Igaunijas armijas un Ziemeļlatvijas brigādes pārliecinošu uzvaru.']
a=(input("Ievadi datumu(dd.mm.gggg) vai notikumu(piem. Cēsu kaujas) par kuru vēlies uzzināt! - "))
if a in dat:
    print(notik[dat.index(a)])
    while True:
        jane=(input("Vai vēlies uzzināt vairāk par šo notikumu? Ievaid 'Jā' vai 'Nē'!"))
        if jane == 'Jā':
            print(notikaprak[dat.index(a)])
            break
        if jane == 'Nē':
            break
if a in notik:
    print(dat[notik.index(a)])
    while True:
        jane=(input("Vai vēlies uzzināt vairāk par šo notikumu? Ievaid 'Jā' vai 'Nē'!"))
        if jane == 'Jā':
            print(notikaprak[notik.index(a)])
            break
        if jane == 'Nē':
            break        