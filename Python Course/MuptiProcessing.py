import concurrent.futures
import requests
import multiprocessing

#Multiprocessing is a Python module that provides a simple way to run multiple processes in parallel. It allows you to take advantage of multiple cores or processors on your system and can significantly improve the performance of your code. In this repl, we'll take a closer look at the multiprocessing module and its various functions and how they can be used in Python.

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 


url = "https://picsum.photos/2000/3000"
#pros = []
#for i in range(50):
#  
#  # downloadFile(url, i)
#  p = multiprocessing.Process(target=downloadFile, args=[url, i])
#  p.start()
#  pros.append(p)

#for p in pros:
#  p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url for i in range(5)]
  l2 = [i for i in range(5)]
  results = executor.map(downloadFile, l1, l2)
  for r in results:
    print(r)