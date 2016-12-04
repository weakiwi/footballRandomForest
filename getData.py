#coding=utf-8
import requests
import string
import csv
import re
import codecs

team_code = "1419"

r = requests.get('http://zq.win007.com/jsData/teamInfo/teamDetail/tdl' + team_code  + '.js')
tmp = r.content
m = re.findall(r"(\[\d{7}.*.\];)", tmp)[0]
m = m.split('],[')
csv_header = ["fouls", "yellow_cards", "red_cards", "possession_rate", "shots", "shot_on target", "passing", "passing_success", "passing_success_rate",  "crossing", "corners", "offside", "unkown", "head", "head_success", "save", "slide_tackle", "shot_out_of target", "blocked_shots", "thorw-in", "stars", "hometeam", "funny_rating"]
with open(team_code + ".csv", "a+") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(csv_header)
for i in m:
    i = re.sub(r"\^.*?'", "", i)
    i = re.sub(r"[\]\[;\']", "", i)
    i = re.sub(r"#[0-9A-Za-z]{6},", "", i)
    with open(team_code + '.csv', 'a+') as f:
        f_csv = csv.writer(f)
        tmp = i.split(",")
        if tmp[2] == team_code:
            tmp.append(1)
        else:
            tmp.append(0)
        del tmp[0:8]
        #tmp = tmp[8:19]
        tmp_1 = 0
        for i in tmp:
            if i == "0":
                tmp_1 += 1
        if tmp_1 > 7:
            continue
        game_degree = lambda x:abs(int(x[0])-int(x[1]))
        if game_degree(tmp) < 3:
            tmp.append(1)
        else:
            tmp.append(0)
        del tmp[0:2]
        tmp = [ float(i) for i in tmp]
        f_csv.writerow(tmp)

