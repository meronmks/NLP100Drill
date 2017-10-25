# -*- coding: utf-8 -*-
# JSONデータの読み込み

import gzip
import json

if __name__ == "__main__":
    with gzip.open("jawiki-country.json.gz", "rt") as fi:
        for line in fi:
            obj = json.loads(line)
            if "イギリス" in obj["title"]:
                print(obj["text"])
