import re
import csv
first_one = "system.cpu.dcache.overallMissRate::total     0.225653                       # miss rate for overall accesses (Ratio)" #just for viewing
second_one = "system.cpu.icache.overallMissRate::total     0.104797                       # miss rate for overall accesses (Ratio)"
third_one = "system.l2.overallMissRate::total                    1                       # miss rate for overall accesses (Ratio)"
#filepath = "stats_18.txt"
stats_directory = "/home/johnj/Downloads/cache_outputs_458/cache_outputs"
combinations_path = "combinations.csv"
output_data = "outputs.csv"
initial_count = 1
final_count = 432

f = open(output_data, "w")
f.close()
def cpi_calculator(filepath):
  with open(filepath, 'r') as file:
    filedata = file.read()

  finaltag1 = "^system.cpu.dcache.overall_misses::total.*# number of overall misses$"
  finaltag2 = "^system.cpu.icache.overall_misses::total.*# number of overall misses$"
  finaltag3 = "^system.l2.overall_misses::total.*# number of overall misses$"

  value = re.split("\n", filedata)
  array1 = []
  # print(value)s
  for i in range(0, len(value)):
    # print(" loop " + str(i))

    #print(value[i])
    dcache = re.match(finaltag1, value[i])
    if dcache is None:
      if i == 376:
        pass


    else:
      # print(t.group())
      array1.append(dcache.group())
    # print(array1)
    icache = re.match(finaltag2, value[i])
    if icache is None:
      if i == 376:
        pass


    else:
      # print(t.group())
      array1.append(icache.group())
    # print(array1)
    l2cache = re.match(finaltag3, value[i])
    if l2cache is None:
      if i == 376:
        pass


    else:
      # print(t.group())
      array1.append(l2cache.group())
    # print(array1)

    # print(t)
  #print(" this is the array value ",array1)
  variable = []
  for mom in range(len(array1)):
    #print(array1[mom])
    noterm = re.findall("\d+\.*\d*", array1[mom])
    variable.append(noterm)
  #variable = re.split("[0-9]", array1[0])
  #print("\n this is the variable value ",variable)
  numerator = ((float(variable[0][0]) + float(variable[1][0]))*6) + (float(variable[2][1])*50)
  denominator = 500000000
  cpi = 1 + numerator/denominator
  #print(cpi)
  return cpi

with open(combinations_path, 'r') as file:
  reader = csv.reader(file)
  row_list = list(reader)
for file in range(initial_count  ,final_count + 1):
  stats_location = stats_directory + "/stats_" + str(file) + ".txt"
  #print(stats_location)
  flow = cpi_calculator(stats_location)
  #print(flow)
  variables = row_list[file-1][3]
  #print(type(variables),"we were the initial terms ")
  term1 = re.search("\d+\.*\d*", str(row_list[file-1][3]))
  term2 = re.search("\d+\.*\d*", str(row_list[file-1][13]))
  term3 = re.search("\d+\.*\d*", str(row_list[file-1][15]))

  row_list[file-1][3] = term1.group()
  row_list[file-1][13] = term2.group()
  row_list[file-1][15] = term3.group()
  #printvariables_1 = row_list[file-1][3]
  #print(type(printvariables_1),"wems")
  pre_line = ",".join(row_list[file - 1])
  #print(pre_line)
  f = open(output_data, "a")
  f.write(pre_line + "," + "cpi_value " + "," + str(flow) + "\n")
  f.close()

print(" cpi values along with the cache parameters are added into the new csv")

