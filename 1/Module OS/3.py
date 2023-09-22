"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""
import os
for i in range(2,11, 2):
    folder_2 = "target/" + str(i)
    new = "target/Steeluv" + str(i)
    os.rename(folder_2, new)