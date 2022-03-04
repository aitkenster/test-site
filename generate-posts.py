import requests
import os
# create directory name
for x in range(500):
  resp = requests.get("http://hipsum.co/api/?type=hipster-centric&sentences=1")
  str_ipsum = resp.json()[0]
  words = str_ipsum.split(" ")
  dir_name = "_".join(words[0:3])

  # create dir
  path = os.path.join("./content/blog", dir_name)
  try:
    os.mkdir(path)
  except:
    continue



  # get content for file
  resp = requests.get("http://hipsum.co/api/?type=hipster-centric&sentences=4")
  str_ipsum = resp.json()[0]

  # create file
  file = open('content/blog/' + dir_name + '/index.md', 'w')

  # add content to file
  file.write(str_ipsum)
  file.close


