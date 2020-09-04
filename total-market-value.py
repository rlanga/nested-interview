import csv
import re

def is_in_wandsworth(postcode: str) -> bool:
  codes = {'SW11 1', 'SW11 2', 'SW11 3', 'SW11 6', 'SW11 8',\
    'SW12 8', 'SW15 2', 'SW17 0', 'SW17 7', 'SW17 8', 'SW18 1',\
      'SW18 2', 'SW18 3', 'SW18 4', 'SW18 4', 'SW18 5', 'SW19 5',\
        'SW19 6', 'SW19 7', 'SW19 8'}

  if postcode in codes:
    return True
  else:
    return False


def is_in_islington(postcode: str) -> bool:
  codes = {'N1 0', 'N1 1', 'N1 2', 'N1 3', 'N1 4',\
    'N1 5', 'N1 6', 'N1 7', 'N1 8', 'N1 9', 'N5 1',\
      'N5 2', 'N7 0', 'N7 6', 'N7 7', 'N7 8', 'N7 9'}

  if postcode in codes:
    return True
  else:
    return False


def solution():
  with open('pp-2020.csv', 'r') as pp_data:
    csvfile = csv.reader(pp_data, delimiter=',')
    total_values = {"wandsworth": 0, "islington": 0}

    # price = row[1] postcode = row[3]

    # Match the post-code against the patterns in the post-code lists
    # e.g. N1 0
    postcode_regex = re.compile(r"[a-zA-Z]{1,2}\d{1,2}\s\d{1}")

    for row in csvfile:
      valid_postcode = re.match(postcode_regex, row[3])
      if valid_postcode:
        if is_in_wandsworth(valid_postcode.group()):
          total_values["wandsworth"] += int(row[1])

        if is_in_islington(valid_postcode.group()):
          total_values["islington"] += int(row[1])

    return total_values

if __name__ == "__main__":
    print(solution()) 