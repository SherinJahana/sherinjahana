import sys,datetime,os,platform

print("_"*80)
print(" "*32,"system details ;)")
print("_"*80)

print("current username     : ",os.getlogin())
print('opertaing system is  : ',platform.system)
print("version is           : ",platform.version())
print("current processor is : ",platform.processor())
print("platform is          :",platform.platform())
print("architecture is      : ",platform.architecture())
print("machine number is    : ",platform.machine())
print("mother board is      : ","a clock frequency of around 3.00-4.00 Gigahertz or GHz. A processor’s...")

print("_"*80)

print("date and time        : ",datetime.datetime.now())
print("")