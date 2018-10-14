#!/usr/local/bin/python3

import zipfile
import os
import shutil
import bs4

#

root_path = "/data/lib"
file_list = root_path + "/ziplist.lst" 
dest_path = "/tmp"
all_file_list = []

with open(file_list,"r") as infile:
    for line in infile:
        all_file_list.append(line.strip())

for file in all_file_list:
    filshrt = os.path.basename(file)[:-4]
    with open(file[:-4] + ".lst", "w") as ouf:
        tmpdir = dest_path + "/" + filshrt
        if not os.path.exists(tmpdir):
            os.makedirs(tmpdir)
        with zipfile.ZipFile(file) as zip_file:
            zip_file.extractall(path=tmpdir)
            for fb2 in os.listdir(tmpdir):
                with open(tmpdir+"/"+fb2, 'rb') as inf:                                                                                                                                                                     
                    data = inf.read()
                    soup = bs4.BeautifulSoup(data,"lxml")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                    t_i = soup.find('title-info') 
                    author = ""                                                                                                                                                                                              
                    for aur in t_i.find_all('author'):
                        l_n = aur.find('last-name')
                        if l_n:
                            aul = l_n.text
                        f_n = aur.find('first-name')
                        if f_n:
                            auf = f_n.text
                    author = author + aul + " " + auf + " "
                    bt = t_i.find('book-title')
                    genre = t_i.find('genre')
                    if genre:
                        gr = genre.text
                    else:
                        gr = ""
                    ouf.write("{0}::{1}::{2}::{3}::{4}\n".format(filshrt,fb2,author.strip(),bt.text,gr))
        shutil.rmtree(tmpdir)
