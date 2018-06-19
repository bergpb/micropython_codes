#import apmode
import connectwifi
import displayinf

connectwifi.connect()
#apmode.activeAp()

while True:
    displayinf.getAllInformations()