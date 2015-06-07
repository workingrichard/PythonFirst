import os;
import modFile
import AccessMariaDB

print('Hello World')

fname = modFile.outputFile(20)
print("get it: " + fname)

contents = modFile.readFile(fname)
print("lines: " + str(len(contents)))

for s in contents:
    print(s)

print("testing yield return....");
for s in modFile.readFileYield(fname):
    print(s.replace("\r\n", "").replace("\n",""))

AccessMariaDB.ReadURLTask()


