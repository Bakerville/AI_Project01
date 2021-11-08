import numpy as np
import math
from algorithm import BFS,DFS,GBFS,A_star
def read_maze(filename):
    matrix = []
    nodes = []
    start = []
    end = []
    pointed_nodes = []
    start_index = 0
    end_index = 0
    count = 0
    size = []
    with open(filename) as f:
        line = f.readlines()
        f.close()
    for i in range(len(line)):
        line[i] = line[i].replace("\n","")
    line[0] = int(line[0])
    count = line[0]
    line.pop(0)
    for i in range(count):
        node = line[0].split()
        for j in range(3):
            node[j] = int(node[j])
        pointed_nodes.append(node)
        line.pop(0)
    row = len(line)
    size.append(row)
    column = len(line[0])
    size.append(column)
    for i in range(row):
        for j in range(column):
            if(line[i][j] == ' '):
                if(i == 0 or i==row-1):
                    end.append(i)
                    end.append(j)
                    nodes.append([i,j])
                    end_index = len(nodes)-1
                elif(j==0 or j == column-1):
                    end.append(i)
                    end.append(j)
                    nodes.append([i,j])
                    end_index = len(nodes)-1
                else:
                    nodes.append([i,j])
            elif(line[i][j]=='S'):
                start.append(i)
                start.append(j)
                nodes.append([i,j])
                start_index = len(nodes)-1
            elif(line[i][j]=='+'):
                nodes.append([i,j])
    point = []
    node = []
    for i in pointed_nodes:
        point.append(i.pop())
        node.append(i)
    for i in nodes:
        distance = []
        node_1 = [i[0]+1,i[1]]
        node_2 = [i[0]-1,i[1]]
        node_3 = [i[0],i[1]+1]
        node_4 = [i[0],i[1]-1]
        for j in nodes:
            if(i==j):
                distance.append(0)
            elif(j==node_1 or j ==node_2 or j==node_3 or j==node_4):
                if(j in node):
                    distance.append(point[node.index(j)])
                else:
                    distance.append(1)
            else:
                distance.append(0)
        matrix.append(distance)
    matrix = np.array(matrix)
    h = []
    for i in nodes:
        value = ((i[0]-end[0])**2) + ((i[1]-end[1])**2)
        value = math.sqrt(value)
        h.append(value)
    return matrix, nodes,pointed_nodes, start, end, start_index, end_index,size,h
def write_file(filename, path,cost,len_path,start,end,nodes,pointed_nodes, num_row, num_col):
    f = open(filename, 'w')
    if(path=='No path'):
        f.write('No path')
        f.write("\n")
        f.write('Do dai duong di la: ' + str(len_path))
        f.write("\n")
        f.write("Chi phi thuc hien: " + str(cost))
        f.close()
        return
    else:
        newpath = []
        for i in path:
            newpath.append(nodes[i])
        result = []
        for i in range(num_row):
            line =""
            for j in range(num_col):
                value = ""
                if [i,j] == start:
                    value = "S"
                elif [i,j] == end:
                    value = "E"
                elif [i,j] in newpath:
                    value = "O"
                elif [i,j] in pointed_nodes:
                    value = "+"
                elif [i,j] in nodes:
                    value = " "
                else:
                    value = "x"
                line+=value
            result.append(line)
        for i in range(num_row):
            f.write(result[i])
            f.write("\n")
        f.write('Do dai duong di la: '+str(len_path))
        f.write("\n")
        f.write("Chi phi thuc hien: "+str(cost))
        f.close()
def result_maze(filename):
    matrix, nodes,pointed_nodes, start, end, start_index, end_index,size,h = read_maze(filename)
    cost_BFS,len_path_BFS, path_BFS = BFS(matrix, start_index, end_index)
    cost_DFS,len_path_DFS, path_DFS = DFS(matrix, start_index, end_index)
    cost_GBFS, len_path_GBFS, path_GBFS = GBFS(matrix, start_index, end_index,h)
    cost_A, len_path_A, path_A = A_star(matrix, start_index, end_index,h)
    name = filename.replace('.txt',"") + '_BFS' +'.txt'
    write_file(name,path_BFS,cost_BFS,len_path_BFS,start,end,nodes,pointed_nodes,size[0],size[1])
    name = filename.replace('.txt',"") + '_DFS' +'.txt'
    write_file(name,path_DFS,cost_DFS,len_path_DFS, start,end,nodes,pointed_nodes,size[0],size[1])
    name = filename.replace('.txt',"") + '_GBFS' +'.txt'
    write_file(name,path_GBFS,cost_GBFS,len_path_GBFS, start,end,nodes,pointed_nodes,size[0],size[1])
    name = filename.replace('.txt',"") + '_A_star' +'.txt'
    write_file(name,path_A,cost_A,len_path_A, start,end,nodes,pointed_nodes,size[0],size[1])