#Thuat toan BFS
def BFS(matrix,start,end):
    path=[]
    explored={}
    frontier={}
    frontier[start]=None
    k=start
    while True:
        if len(frontier)==0:
            result='No path'
            cost = len(explored)
            return cost,0,result
        res=list(frontier.keys())[0]
        point=frontier.pop(res)
        explored[res]=point
        value=0
        k=0
        for i in matrix[res]:
            if (i!=0):
                check1=k in frontier
                check2=k in explored
                if (check1==False and check2==False):
                    if k==end:
                        path_len = 0
                        path.append(k)
                        path.append(res)
                        while True:
                            value=explored[res]
                            res=value
                            if (value==None):
                                path.reverse()
                                for i in range(len(path)-1):
                                    x = path[i]
                                    y = path[i+1]
                                    path_len+= matrix[x][y]
                                cost = len(explored)
                                return cost, path_len, path
                            path.append(value)
                        return
                    frontier[k]=res
            k+=1
    return cost, len(explored), path

#Thuat toan DFS

def DFS(matrix,start,end):
    path=[]
    explored={}
    frontier={}
    frontier[start]=None
    k=start
    while True:
        if len(frontier)==0:
            result='No path'
            cost = len(explored)
            return cost, 0, result
        res=list(frontier.keys())[0]
        point=frontier.pop(res)
        explored[res]=point
        value=0
        if res==end:
            path.append(res)
            while True:
                path_len = 0
                value=explored[res]
                res=value
                if (value==None):
                    path.reverse()
                    for i in range(len(path)-1):
                        x = path[i]
                        y = path[i+1]
                        path_len+= matrix[x][y]
                    cost = len(explored)
                    return cost, path_len, path
                path.append(value)
            return
        k=0
        temp={}
        for i in matrix[res]:
            if (i!=0):
                check2=k in explored
                if (check2==False):
                    temp[k]=res
            k+=1
        temp.update(frontier)
        frontier=temp
    return cost, len(explored), path

#Thuat toan GBFS

def GBFS(matrix, start,end,h):
    path = []
    explored = {}
    frontier  = {}
    frontier[start] = [None, h[start]]
    while True:
        if(len(frontier)==0):
            result = 'No path'
            cost = len(explored)
            return cost, 0, result
        res = list(frontier.keys())[0]
        point = frontier.pop(res)
        explored[res] = point
        k = 0
        value = 0
        for i in matrix[res]:
            if(i!=0):
                check1 = k in frontier
                check2 = k in explored
                if(check1 == False and check2 == False):
                    if(k == end):
                        path_len = 0
                        path.append(k)
                        path.append(res)
                        while True:
                            value = explored[res][0]
                            res = value
                            if(value == None):
                                path.reverse()
                                for i in range(len(path)-1):
                                    x = path[i]
                                    y = path[i+1]
                                    path_len+= matrix[x][y]
                                cost = len(explored)
                                return cost, path_len, path
                            path.append(value)
                        return
                    frontier[k]=[res,h[k]]
            k+=1
        frontier = dict(sorted(frontier.items(), key= lambda item: item[1][1]))
    return cost, len(explored), path

#Thuat toan A*

def A_star(matrix,start,end,h):
    path=[]
    explored={}
    frontier={}
    frontier[start]=[None,0,h[start]]
    while True:
        if len(frontier)==0:
            result='No path'
            cost = len(explored)
            return cost, 0, result
        res = list(frontier.keys())[0]
        point = frontier.pop(res)
        explored[res] = point
        value = 0
        if (res == end):
            path_len = 0
            path.append(res)
            while True:
                value=explored[res][0]
                res=value
                if (value==None):
                    path.reverse()
                    for i in range(len(path)-1):
                        x = path[i]
                        y = path[i+1]
                        path_len+= matrix[x][y]
                    cost = len(explored)
                    return cost, path_len, path
                path.append(value)
            return
        k = 0
        for i in matrix[res]:
            if(i!=0):
                check1 = k in frontier
                check2 = k in explored
                newval = i + explored[res][1] + h[k]
                if(check2 == False):
                    if(check1 == True):
                        if(frontier[k][2]>newval):
                            frontier[k] = [res, i + explored[res][1], newval]
                    elif(check1 == False):
                        frontier[k]=[res, i + explored[res][1], newval]
            k+=1
        frontier = dict(sorted(frontier.items(), key=lambda item: item[1][2]))
    return cost, len(explored), path