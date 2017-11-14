
import pandas as pd
import cs689_utils

titanicfile = ""

titanic_ppl = pd.read_csv (titanicfile)

for ttnc_person in titanic_ppl.Name:
    famname = ttnc_person.split(',')[0]
    print (ttnc_person + " was on the Titanic and the family name was " + famname)

