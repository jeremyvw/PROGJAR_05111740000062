import logging
import requests
import threading
from datetime import datetime
import os

def download(url=None,nama=None):

    if (url is None):
        return False

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ff = requests.get(url)

    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = nama
        ekstensi = tipe[content_type]
        logging.warning(f"Writing {namafile}.{ekstensi},Download time = {current_time} ")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

if __name__=='__main__':

    threads = []

    t = threading.Thread(target=download, args=('https://c1-ebgames.eb-cdn.com.au/merchandising/images/packshots/fb0031d637344013b25c4d13eba0ee95_Original.jpg','Gambar 1',))
    threads.append(t)
    t = threading.Thread(target=download, args=('https://nintendoeverything.com/wp-content/uploads/kirby-1.jpg','Gambar 2',))
    threads.append(t)
    t = threading.Thread(target=download, args=('https://www.ssbwiki.com/images/a/ae/Kirby_SSBB.jpg','Gambar 3',))
    threads.append(t)

    for thr in threads:
        thr.start()