__author__ = 'maud'

import csv
import json


def import_file(data_path):
    data = []
    current_str = ""
    last_char = ""
    total = 0
    json_data = []
    outfile = open("intel.csv", "w")
    outwriter = csv.writer(outfile, quotechar='"', escapechar="\\", quoting=csv.QUOTE_NONNUMERIC)
    outwriter.writerow(["ts", "text", "userid", "nb_followers"])

    with open(data_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if c == "{" and last_char == "}":
                if "intel" in current_str or "Intel" in current_str:
                    total += 1
                    print total
                    try:
                        jsonobj = json.loads(current_str)
                        if "lang" in jsonobj:
                            lang = jsonobj["lang"]
                            if lang == "en":
                                ts = jsonobj["created_at"]
                                text = jsonobj["text"]
                                text = text.encode("utf-8")
                                userid = jsonobj["user"]["id"]
                                userfollowers = jsonobj["user"]["followers_count"]
                                new_tweet = [ts, text, userid, userfollowers]

                                outwriter.writerow(new_tweet)
                                json_data.append(new_tweet)
                    except UnicodeDecodeError:
                        print"ERROR"

                current_str = "{"
            else:
                current_str += c
                last_char = c

    return json_data