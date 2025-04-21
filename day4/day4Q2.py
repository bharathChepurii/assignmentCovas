from pkg.day4file2 import File
import datetime
fs=File(".")
print(fs.getmaxsizeFile(2)) 
print(fs.getlatestFiles(datetime.date(2024,4,1)))
