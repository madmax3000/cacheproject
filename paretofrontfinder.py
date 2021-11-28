import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

figure(figsize=(12, 12), dpi=100)
outputfile = "458_sat.csv"
initial_count = 1
final_count = 432
def plot_pareto_frontier(Xs, Ys, maxX=True, maxY=True):
    '''Pareto frontier selection process'''
    sorted_list = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxY)
    pareto_front = [sorted_list[0]]
    for pair in sorted_list[1:]:
        if maxY:
            if pair[1] >= pareto_front[-1][1]:
                pareto_front.append(pair)
        else:
            if pair[1] <= pareto_front[-1][1]:
                pareto_front.append(pair)

    '''Plotting process'''
    plt.scatter(Xs, Ys)
    pf_X = [pair[0] for pair in pareto_front]
    pf_Y = [pair[1] for pair in pareto_front]
    plt.plot(pf_X, pf_Y)
    plt.xlabel("cost")
    plt.ylabel("cpi")
    #plt.set_title('cost vs cpi pareto front')
    plt.grid('on')

    plt.show()
    return pareto_front
'''
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [4, 2, 7, 1, 5, 11, 2, 13 ,4]
plot_pareto_frontier(x, y)
'''
with open(outputfile, 'r') as file:
    reader = csv.reader(file)
    row_list = list(reader)
    cpi = []
    cost = []
    for i in range(initial_count -1 ,final_count):
        cpi.append(float(row_list[i][21]))
        #print(cpi)
        cost.append(float(row_list[i][23]))
        #print(cost)
    values = plot_pareto_frontier(cost,cpi, maxX=False, maxY=False)
    print(values)


