import os
src = "exer7"
files = os.listdir(src)
i = 1
for file in files:
    if file.endswith(".jpg"):
        os.rename(f"exer7/{file}", f"exer7/{i}.png")   
        i += 1