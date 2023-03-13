import csv
import json
import wget 
import pandas as pd 
import zstandard as zstd
import io

url = "https://files.pushshift.io/reddit/comments/RC_2008-01.zst"
response = wget.download(url, "./test.zst")

fh = open("./test.zst", 'rb')
dctx = zstd.ZstdDecompressor(max_window_size=2147483648)
stream_reader = dctx.stream_reader(fh)
f = io.TextIOWrapper(stream_reader, encoding='utf-8')

res = []

for i, l in enumerate(f):
    res.append(l.strip())
fo = open('data.json', "w")
json.dump(res, fo, ensure_ascii=False, indent=4)
fo.close()

