import csv
import os
import shutil
benchmark_directory = "/home/johnj/gem5/m5out/benchmarks/458.sjeng"  #location of bench mark directory
gem5_directory = '/home/johnj/gem5'    # location of the gem5  directory
initial_count = 3
final_count = 5
instruction_count = "1000"
benchmark_location = benchmark_directory + "/src/benchmark"
argument_location = benchmark_directory + "/data/test.txt"
output_directory = "/home/johnj/gem5/m5out/benchmarks/458.sjeng/m5out"
combination_data = "combinations.csv"
try:
    os.mkdir(benchmark_directory + "/cache_outputs")
except OSError as error:
    print("\n folder already exists neglecting command")
with open(combination_data, 'r') as file:
    reader = csv.reader(file)
    row_list = list(reader)
    for i in range (initial_count - 1,final_count ):
        l2_data_size = row_list[i][3]
        l2_data_aso_str = row_list[i][5]
        l2_data_block_str = row_list[i][7]
        l1_data_size = row_list[i][9]
        l1_inst_size = row_list[i][11]
        #l1_inst_block_str = row_list[i][13]
        #l1_data_block_str = row_list[i][15]
        l1_data_aso_str = row_list[i][17]
        l1_ist_aso_str = row_list[i][19]
        command_part1 = "time " +  gem5_directory + "/build/X86/gem5.opt -d " + output_directory + " " + gem5_directory + "/configs/example/se.py -c "
        command_part2 = benchmark_location + " -o "+ argument_location + " -I "+ instruction_count +  " --cpu-type=TimingSimpleCPU --caches --l2cache "
        command_part3 = "--l1d_size="+ l1_data_size + " --l1i_size=" + l1_inst_size + " --l2_size=" + l2_data_size
        command_part4 = " --l1d_assoc="+ l1_data_aso_str + " --l1i_assoc=" + l1_ist_aso_str + " --l2_assoc=" + l2_data_aso_str + " --cacheline_size=" + l2_data_block_str
        #print(command_part1+command_part2+command_part3+command_part4)
        #os.system(command_part1+command_part2+command_part3+command_part4)
        src_stats_path = benchmark_directory + "/m5out/stats.txt"
        dst_stats_path = benchmark_directory + "/cache_outputs/" + "/stats_" + str(i+1) + ".txt"
        shutil.copy(src_stats_path, dst_stats_path)
        print('Copied stats file with default values ' + str(i) + '   iteration')

