dat=['19.06.1919','18.11.1918']
notik=["Cēsu kaujas",'Latvijas Republikas proklamēšanas diena']
notikaprak=['Cēsu kaujas bija viens no nozīmīgākajiem pavērsiena punktiem Latvijas Neatkarības kara gaitā. Kaujas noslēdzās ar Igaunijas armijas un Ziemeļlatvijas brigādes pārliecinošu uzvaru.','Latvijas Tautas padomes (LTP) formāls solis 1918. gada 18. novembrī, ar kuru suverēnā valsts vara Latvijā pārgāja LTP rokās un tika dibināta neatkarīga valsts']
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
elif a in notik:
    print(dat[notik.index(a)])
    while True:
        jane=(input("Vai vēlies uzzināt vairāk par šo notikumu? Ievaid 'Jā' vai 'Nē'!"))
        if jane == 'Jā':
            print(notikaprak[notik.index(a)])
            break
        if jane == 'Nē':
            break        
else:
    print("Datums nav atbilstošs, mēģini to ievadīt vēlreiz.")
