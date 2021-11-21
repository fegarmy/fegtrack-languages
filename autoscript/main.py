import csv

file = open("Translation request for FEGtrack.csv", mode="r", encoding="utf-8")
reader = csv.reader(file, delimiter=',', quotechar='|')

for row in reader:
    if row[0] == '"Zeitstempel"':
        continue
    cuttedArray = row[2:]
    tosave = """
const LABELS = {{
  ADD_NEW_WALLET: {},
  WALLET_NAME: {},
  WALLET_ADDRESS: {},
  CANCEL: {},
  SAVE: {},
  RESET: {},
  DELETE: {},
  SEARCH: {},
  CLOSE: {},
  PLATINUM: {},
  GOLD: {},
  RED: {},
  BLUE: {},
  YELLOW: {},
  GREEN: {},
  REFLECTIONS: {},
  EDIT_REFLECTIONS: {},
  EDIT_STAKING_REFLECTIONS: {},
  STAKED: {},
  REWARDS_FROM: {},
  EDIT_WALLET: {},
  SETTINGS: {},
  THEME: {},
  LANGUAGE: {},
  SINCE: {},
  POOL_SHARE: {},
  UNCLAIMED: {},
  COPY_NOTICE: {},
  WALLET_DESIGN: {},
}}

export {{LABELS}};

    """.format(*cuttedArray)
    country = row[1].strip("\"")
    f = open(country+".js", "w",encoding="utf-8")
    f.write(tosave)
    f.close()

