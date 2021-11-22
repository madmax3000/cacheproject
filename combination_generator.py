import math
stat_path = 'combinations.csv'
block_values = [5,6]
associativity = []
l1_inst = [17,16]
l1_data = [13,14]
l2_data = [20,19]
value = 0
for i in range (len(l2_data)):
    #print("first loop in",str(i))
    for x in range (len(block_values)):
        #print(x)
        #print(len(block_values))
        a2 = l2_data[x]
        index_a2  = a2 - block_values[x]
        acc_l2_data_limit = int(math.log(index_a2, 2))
        l2_data_aso = []
        for l in range (3):                                 #(acc_l2_data_limit + 1):
            l2_data_aso.append(2 ** l)
        #l2_data_aso.append(index_a2)
        print(l2_data_aso , " this is l2 associativity")
        for y in range(len(l2_data_aso)):
            for j in range (len(l1_data)):
                for z in range(len(l1_inst)):
                    #print(" second loop in",str(j))
                    #for k in range (len(block_values)):
                     #   for w in range (len(block_values)):
                    #print(" third loop in",str(k))
                    a = l1_data[j]
                    b = l1_inst[z]
                    index_a = a - block_values[x]
                    index_b = b - block_values[x]

                    acc_l1_ist_limit = int(math.log(index_a,2))
                    acc_l1_data_limit = int(math.log(index_b, 2))

                    l1_ist_aso = []
                    for l in range (3):#(acc_l1_ist_limit + 1):
                        l1_ist_aso.append(2**l)
                    #l1_ist_aso.append(index_a)
                    #l1_ist_aso.remove(0)
                    print(l1_ist_aso)
                    l1_data_aso = []
                    for l in range (3) : # (acc_l1_data_limit + 1):
                        l1_data_aso.append(2**l)
                    #l1_data_aso.append(index_b)
                    #l1_data_aso.remove(0)
                    print(l1_data_aso)
                    #print(" two loops done")
                    for m in range(len(l1_data_aso)):
                        #print("4th loop status",str(m))
                        for n in range(len(l1_data_aso)):
                            #print("5th loop status",(n))
                            value = value + 1
                            print(value)
                            value_str = str(value)
                            l2_data_str = str(2**l2_data[i])
                            l2_data_aso_str = str(l2_data_aso[y])
                            l2_data_block_str = str(2**block_values[x])
                            l1_data_str = str(2**l1_data[j])
                            l1_inst_str = str(2**l1_inst[z])
                            l1_inst_block_str = str(2**block_values[x])
                            l1_data_block_str = str(2**block_values[x])
                            l1_data_aso_str = str(l1_data_aso[m])
                            l1_ist_aso_str = str(l1_ist_aso[n])



                            #print(l1_data_aso[m])


                            block_values_k = str(block_values[x])
                            f = open(stat_path, "a")
                            f.write("iteration no ," + str(value) + "," +" l2_data_size," + l2_data_str + "B," + "l2_associativity ," + l2_data_aso_str + "," +  "l2_block_size ," + l2_data_block_str + "," + "l1_data_size,"+ l1_data_str + "B,"+ "l1_inst_size," + l1_inst_str + "B," + "l1_inst_block_size," + l1_inst_block_str + "," + "l1_data_block_size," + l1_data_block_str + "," + "l1_data_asociativity," + l1_data_aso_str +","+ " l1_ist_aso_str," + l1_ist_aso_str + "\n" )  # writing back into the file
                            f.close()






