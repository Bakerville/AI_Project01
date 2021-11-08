from algorithm import BFS,DFS,GBFS,A_star
from read_write import read_maze, write_file, result_maze
result_maze('maze_1/maze_1.txt')
result_maze('maze_2/maze_2.txt')
result_maze('maze_3/maze_3.txt')
result_maze('maze_4/maze_4.txt')
result_maze('maze_5/maze_5.txt')
filename = input("Nhap duong dan den file me cung (nhan Enter neu muon exit): ")
if(filename==""):
    exit()
matrix, nodes, pointed_nodes, start, end, start_index, end_index, size, h = read_maze(filename)
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