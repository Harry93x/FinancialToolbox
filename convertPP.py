#!/usr/bin/python3
import xlrd
import csv
import sys
import getopt

# input configuration
iColDate = 0
iColTransactionType = 1
iColAmount = 3
iColDescription = 6

transactionType = 'Repayment'
descriptionType = 'Interest'

#output configuration
outHeader = ['Datum', 'Typ', 'Wert']
outType = 'Zinsen'
outDelimiter = ';'

def localize_floats(row):
    return [
        str(el).replace('.', ',') if isinstance(el, float) else el 
        for el in row
    ]

def main(argv):
  inputfile = ''
  outputfile = ''
  try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
    print('convertPP.py -i <inputfile> -o <outputfile>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print('convertPP.py -i <inputfile> -o <outputfile>')
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg

  inWorkbook = xlrd.open_workbook(inputfile)
  inWorksheet = inWorkbook.sheet_by_index(0)
  #alternatively by workheet name inWorksheet = inWorkbook.sheet_by_name('Worksheet')

  interests = []
  concatInterests = []

  iRow = 0

  while iRow < inWorksheet.nrows:
    if inWorksheet.cell(iRow, iColTransactionType).value == transactionType:
      if inWorksheet.cell(iRow, iColDescription).value == descriptionType:
        #print('p0: ', inWorksheet.cell(iRow,iColDate).value, inWorksheet.cell(iRow,iColTransactionType).value, inWorksheet.cell(iRow,iColAmount).value, inWorksheet.cell(iRow,iColDescription).value)
        lastDate = inWorksheet.cell(iRow,iColDate).value
        interest = inWorksheet.cell(iRow,iColAmount).value
        #print('p1: ', lastDate, interest, iRow)
        interests.append([lastDate, interest])
    iRow += 1
  #print('px: ', interests)
  #print(interests[0][0], interests[1][0])

  iRow = 0

  while iRow < len(interests):
    lastDate = interests[iRow][0]
    interest = interests[iRow][1]
    #print('p3: ', lastDate, iRow, len(interests))

    if iRow < len(interests) - 1 and interests[iRow + 1][0] == lastDate:
      while interests[iRow + 1][0] == lastDate:
        #print('p4: ', interests[iRow + 1][0], lastDate)
        iRow += 1
        interest += interests[iRow][1]
        #print('p5: ', iRow, interest)
        if iRow >= len(interests) - 1:
          break
      concatInterests.append([lastDate, outType, interest])
    else:
      concatInterests.append([lastDate, outType, interest])
    
    iRow += 1
    if iRow > len(interests) - 1:
      break

  with open(outputfile, 'w', newline='') as outFile:
    csv_writer = csv.writer(outFile,  delimiter=outDelimiter)
    csv_writer.writerow(outHeader)
    for row in concatInterests:
      csv_writer.writerow(localize_floats(row))

if __name__ == "__main__":
   main(sys.argv[1:])
