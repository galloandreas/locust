import csv, sys, getopt


def main(argv): 
    status = True
    threshold = 0

    try:
      opts, arg = getopt.getopt(argv,"ht:",["threshold="])
    except getopt.GetoptError:
      print('readResult.py -t <threshold>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('readResult.py -t <threshold>')
            sys.exit()
        elif opt in ("-t", "--threshold"):
            threshold = int(arg)  
    print('Threshold "', threshold)

    with open("examples_requests.csv") as f:
        records = csv.DictReader(f)
        for row in records:
                if row["Name"] != "Total" :
                    if int(row["# failures"]) > threshold :
                        status = False
    print(status)

if __name__ == "__main__":
   main(sys.argv[1:])