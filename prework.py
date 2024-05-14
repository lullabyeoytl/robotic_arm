import subprocess as sps 
import  sys
p=sps.Popen(["powershell.exe","imgprew.ps1"],stdout=sys.stdout)
p.communicate()
