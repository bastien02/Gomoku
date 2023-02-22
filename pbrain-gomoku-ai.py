#!/usr/bin/env python3

import sys

map = [[]]
# isStarted = False # Si game started et pas finie, doit-on mettre ça ?

# KeyWord START
def start(list):
    global map

    # If there is more than 1 arg
    if (len(list) != 1):
        print ("ERROR message - format: [START int]", flush=True)
        return
    else:
        # If n isn't an int
        try:
            n = int(list[0])
            # If map size is negative
            if (n < 5):
                print ("ERROR message - size cannot be negative", flush=True)
                return
            # Gestion des maps autres que 20 à faire à la fin
        except ValueError:
            print ("ERROR message - size isn't an int", flush=True)
            return

    map = [[0 for i in range(n)] for j in range(n)]
    print("OK - everything is good", flush=True)

# KeyWord TURN
def turn(list):
    global map
    if (len(list) != 1):
        print ("ERROR message - format: [TURN int int]", flush=True)
        return
    cmd = list[0].split(',')
    map[int(cmd[0])][int(cmd[1])] = 2
    tmp = noopy()
    print (f"{tmp[0]:.0f},{tmp[1]:.0f}", flush=True)
    return

# KeyWord BOARD
def board():
    global map

    # for i in range (len(map)):
    #     for j in range (len(map[i])):
    #         if (map[i][j] != 0):
    #             print(f"{i:.0f},{j:.0f},{map[i][j]:.0f}")
    # print("DONE")

    while (1):
        ipt = input()
        if (ipt == "DONE"):
            break

        cmp = ipt.split(",")
        
        if (len(cmp) != 3):
            print ("ERROR message - format: [x,y,player]", flush=True)
            #sys.exit(84)
        
        bl = False
        try:
            x = int(cmp[0])
            y = int(cmp[1])
            p = int(cmp[2])

            if (x < 0 or y < 0):
                print ("ERROR message - X or Y needs to be positive numbers", flush=True)
                #sys.exit(84)
                bl = True
            if (p != 1 and p != 2):
                print ("ERROR message - Player must be 1 or 2", flush=True)
                #sys.exit(84)
                bl = True
        except ValueError:
            print ("ERROR message - X, Y, and the player must be ints", flush=True)
            #sys.exit(84)
            bl = True

        if (bl == False):
            map[x][y] = p
    
    tmp = noopy()
    print (f"{tmp[0]:.0f},{tmp[1]:.0f}", flush=True)

    for line in map:
        print(line)

    return

# Il faut toujours un commentaire ici
def check_hrz(player, max):
    global map
    nb = 0
    tmpspace = [[-1, -1], "UwU"]
    zeroSpace = [-1, -1]
    for i in range(len(map)):
        tmp = 0
        for j in range (len(map[i])):
            if (map[i][j] == player):
                nb += 1
            elif (map[i][j] == 0):
                if (tmp == 0):
                    tmp = 1
                    zeroSpace = [i, j]
                else:
                    if (j < len(map[i]) - 1):
                        if (map[i][j - 1] == player or map[i][j + 1] == player):
                            zeroSpace = [i, j]
                    else:
                        tmp = 1
                        nb = 0
                        zeroSpace = [i, j]
            else:
                tmp = 0
                nb = 0
            if (nb == max and tmp == 1):
                if (player == 1):
                    tmpspace = [zeroSpace, "YOU"]
                    if (max == 4):
                        return tmpspace
                    if (max == 3):
                        if (is_winning(tmpspace[0], 1, 1) == 1):
                            return tmpspace
                else:
                    tmpspace = [zeroSpace, "HIM"]
                    if (max == 3):
                        if (is_winning(tmpspace[0], 2, 1) == 1):
                            return tmpspace
                    if (max == 4):
                        return tmpspace
    return tmpspace

# Il en fallait bien un autre ici
def check_ver(player, max):
    global map
    nb = 0
    tmpspace = [[-1, -1], "UwU"]
    zeroSpace = [-1, -1]
    for j in range(len(map)):
        tmp = 0
        for i in range (len(map[j])):
            if (map[i][j] == player):
                nb += 1
            elif (map[i][j] == 0):
                if (tmp == 0):
                    tmp = 1
                    zeroSpace = [i, j]
                else:
                    if (j < len(map[i]) - 1 and map[i][j - 1] == player and map[i][j + 1] == player):
                        zeroSpace = [i, j]
                    else:
                        tmp = 1
                        nb = 0
                        zeroSpace = [i, j]
            else:
                tmp = 0
                nb = 0
            if (nb == max and tmp == 1):
                if (player == 1):
                    tmpspace = [zeroSpace, "YOU"]
                    if (max == 3):
                        if (is_winning(tmpspace[0], 1, 2) == 1):
                            return tmpspace
                    if (max == 4):
                        return tmpspace
                else:
                    tmpspace = [zeroSpace, "HIM"]
                    if (max == 3):
                        if (is_winning(tmpspace[0], 2, 2) == 1):
                            return tmpspace
                    if (max == 4):
                        return tmpspace
    return tmpspace

# Il en faut toujours un
def check_diaLR(player, max):
    global map
    nb = 0
    tmpspace = [[-1, -1], "UwU"]
    zeroSpace = [-1, -1]
    k = (len(map) - 5)
    while k >= 0:
        tmp = 0
        j = 0
        for i in range(k, len(map)):
            if (map[i][j] == player):
                nb += 1
            elif (map[i][j] == 0):
                if (tmp == 0):
                    tmp = 1
                    zeroSpace = [i, j]
                else:
                    if (i != 0 and i != len(map) - 1 and j != 0 and j != len(map) - 1 and map[i - 1][j - 1] == player and map[i + 1][j + 1] == player):
                        zeroSpace = [i, j]
                    else:
                        tmp = 1
                        nb = 0
                        zeroSpace = [i, j]
            else:
                tmp = 0
                nb = 0
            if (nb == max and tmp == 1):
                if (player == 1):
                    tmpspace = [zeroSpace, "YOU"]
                    if (max == 3):
                        if (is_winning(tmpspace[0], 1, 3) == 1):
                            return tmpspace
                    if (max == 4):
                        return tmpspace
                else:
                    tmpspace = [zeroSpace, "HIM"]
                    if (max == 3):
                        if (is_winning(tmpspace[0], 2, 3) == 1):
                            return tmpspace
                    if (max == 4):
                        return tmpspace
            j += 1
        k -= 1
    for k in range(0, (len(map) - 5)):
        tmp = 0
        i = 0
        for j in range(k, len(map)):
            if (map[i][j] == player):
                nb += 1
            elif (map[i][j] == 0):
                if (tmp == 0):
                    tmp = 1
                    zeroSpace = [i, j]
                else:
                    if (i != 0 and i != len(map) - 1 and j != 0 and j != len(map) - 1 and map[i - 1][j - 1] == player and map[i + 1][j + 1] == player):
                        zeroSpace = [i, j]
                    else:
                        tmp = 1
                        nb = 0
                        zeroSpace = [i, j]
            else:
                tmp = 0
                nb = 0
            if (nb == max and tmp == 1):
                if (player == 1):
                    tmpspace = [zeroSpace, "YOU"]
                    if (max == 3):
                        if (is_winning(tmpspace[0], 1, 3) == 1):
                            return tmpspace
                    if (max == 4):
                        return tmpspace
                else:
                    tmpspace = [zeroSpace, "HIM"]
                    if (max == 3):
                        if (is_winning(tmpspace[0], 2, 3) == 1):
                            return tmpspace
                    if (max == 4):
                        return tmpspace
            i += 1
    return tmpspace

# Et là qui voilà ? Inspecteur Gadget
def check_diaRL(player, max):
    global map
    nb = 0
    tmpspace = [[-1, -1], "UwU"]
    zeroSpace = [-1, -1]
    k = (len(map) - 5)
    while k >= 0:
        tmp = 0
        j = len(map) - 1
        i = k
        while i < len(map):
            if (map[i][j] == player):
                nb += 1
            elif (map[i][j] == 0):
                if (tmp == 0):
                    tmp = 1
                    zeroSpace = [i, j]
                else:
                    if (i != 0 and i != len(map) - 1 and j != 0 and j != len(map) - 1 and map[i - 1][j + 1] == player and map[i + 1][j - 1] == player):
                        zeroSpace = [i, j]
                    else:
                        tmp = 1
                        nb = 0
                        zeroSpace = [i, j]
            else:
                tmp = 0
                nb = 0
            if (nb == max and tmp == 1):
                if (player == 1):
                    tmpspace = [zeroSpace, "YOU"]
                    if (max == 3):
                        if (is_winning(tmpspace[0], 1, 4) == 1):
                            return tmpspace
                    if (max == 4):
                        return tmpspace
                else:
                    tmpspace = [zeroSpace, "HIM"]
                    if (max == 3):
                        if (is_winning(tmpspace[0], 2, 4) == 1):
                            return tmpspace
                    if (max == 4):
                        return tmpspace
            j -= 1
            i += 1
        k -= 1
    k = len(map) - 1
    while k >= 4:
        tmp = 0
        j = k
        i = 0
        while j >= 0:
            if (map[i][j] == player):
                nb += 1
            elif (map[i][j] == 0):
                if (tmp == 0):
                    tmp = 1
                    zeroSpace = [i, j]
                else:
                    if (i != 0 and i != len(map) - 1 and j != 0 and j != len(map) - 1 and map[i - 1][j + 1] == player and map[i + 1][j - 1] == player):
                        zeroSpace = [i, j]
                    else:
                        tmp = 1
                        nb = 0
                        zeroSpace = [i, j]
            else:
                tmp = 0
                nb = 0
            if (nb == max and tmp == 1):
                if (player == 1):
                    tmpspace = [zeroSpace, "YOU"]
                    if (max == 3):
                        if (is_winning(tmpspace[0], 1, 4) == 1):
                            return tmpspace
                    if (max == 4):
                        return tmpspace
                else:
                    tmpspace = [zeroSpace, "HIM"]
                    if (max == 3):
                        if (is_winning(tmpspace[0], 2, 4) == 1):
                            return tmpspace
                    if (max == 4):
                        return tmpspace
            j -= 1
            i += 1
        k -= 1
    return tmpspace

# return un point qui se situe au "milieu" du jeu
def find_middle():
    global map

    line1 = [-1, -1]
    line2 = [-1, -1]
    for i in range(len(map)):
        tmp = 0
        for j in range(len(map[i])):
            if (map[i][j] != 0):
                tmp += 1
        if (tmp > line1[1]):
            line1 = [i, tmp]
        if (tmp >= line2[1]):
            line2 = [i, tmp]

    column1 = [-1, -1]
    column2 = [-1, -1]
    for j in range(len(map[0])):
        tmp = 0
        for i in range(len(map)):
            if (map[i][j] != 0):
                tmp += 1
        if (tmp > column1[1]):
            column1 = [j, tmp]
        if (tmp >= column2[1]):
            column2 = [j, tmp]

    return ([int((line1[0] + line2[0])/2), int((column1[0] + column2[0])/2)])

# Check tout autour de la pos
def check_around(x, y):
    global map

    if (x - 1 >= 0 and y - 1 >= 0):
        if map[x - 1][y - 1] == 0:
            return [x - 1, y - 1]
    if (x - 1 >= 0):
        if map[x - 1][y] == 0:
            return [x - 1, y]
    if (x - 1 >= 0 and y + 1 < len(map)):
        if map[x - 1][y + 1] == 0:
            return [x - 1, y + 1]
    if (y - 1 >= 0):
        if map[x][y - 1] == 0:
            return [x, y + 1]
    if (y + 1 < len(map)):
        if map[x][y + 1] == 0:
            return [x, y + 1]
    if (x + 1 < len(map) and y - 1 >= 0):
        if map[x + 1][y - 1] == 0:
            return [x + 1, y - 1]
    if (x + 1 < len(map)):
        if map[x + 1][y] == 0:
            return [x + 1, y]
    if (x + 1 < len(map) and y + 1 < len(map)):
        if map[x + 1][y + 1] == 0:
            return [x + 1, y + 1]
    return [-1, -1]

# Return le point sur lequel jouer si pas de 4/3/2
# X et Y sont les coordonnées du point central du jeu
def play(x, y):
    global map

    tmp1 = [-1, -1]
    tmp2 = [-1, -1]
    tmp3 = [-1, -1]
    tmp4 = [-1, -1]

    if (map[x][y] == 0):
        return [x, y]
    tmp = check_around(x, y)
    if (tmp != [-1, -1]):
        return tmp

    t = 1
    while (t < (len(map) / 2)):
        for i in range (x - t, x + t):
            if (y - t) >= 0:
                if (map[i][y - t] == 1):
                    tmp1 = check_around(i, y - t)
            if ( (y + t) < len(map)):
                if (map[i][y + t] == 1):
                    tmp2 = check_around(i, y + t)
        for j in range (y - t, y + t):
            if (x - t >= 0):
                if (map[x - t][j] == 1):
                    tmp3 = check_around(x - t, j)
            if (x + t < len(map)):
                if (map[x + t][j] == 1):
                    tmp4 = check_around(x + t, j)
        if (tmp1 != [-1, -1]):
            return tmp1
        if (tmp2 != [-1, -1]):
            return tmp2
        if (tmp3 != [-1, -1]):
            return tmp3
        if (tmp4 != [-1, -1]):
            return tmp4
        t += 1
    
    return [-1, -1]

# check if you have already played on this map
def if_you():
    global map

    nb = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (map[i][j] == 1):
                nb += 1
    return nb

# check where is the only played play by the opponent
def opponent():
    global map

    for i in range(len(map)):
        for j in range(len(map[i])):
            if (map[i][j] == 2):
                return [i, j]
    
    return [-1, -1]

# Check what do we play
def noopy():
    ss = if_you()
    if (ss == 0):
        tmp = opponent()
        if (tmp == [-1, -1]):
            return [10, 10]
        if (tmp[0] - 1 >= 0):
            return [tmp[0] - 1, tmp[1]]
        return [tmp[0] + 1, tmp[1]]

    i = 4

    while (i >= 2):
        tmp = check_hrz(1, i)
        if (tmp != [[-1, -1], 'UwU']):
            return tmp[0]
        tmp = check_ver(1, i)
        if (tmp != [[-1, -1], 'UwU']):
            return tmp[0]
        tmp = check_diaRL(1, i)
        if (tmp != [[-1, -1], 'UwU']):
            return tmp[0]
        tmp = check_diaLR(1, i)
        if (tmp != [[-1, -1], 'UwU']):
            return tmp[0]

        tmp2 = check_hrz(2, i)
        if (tmp2 != [[-1, -1], 'UwU']):
            return tmp2[0]
        tmp2 = check_ver(2, i)
        if (tmp2 != [[-1, -1], 'UwU']):
            return tmp2[0]
        tmp2 = check_diaRL(2, i)
        if (tmp2 != [[-1, -1], 'UwU']):
            return tmp2[0]
        tmp2 = check_diaLR(2, i)
        if (tmp2 != [[-1, -1], 'UwU']):
            return tmp2[0]
        i-= 1

    tt = find_middle()
    return play(tt[0], tt[1])

# check for 1 line horizontally
def line_h(map, line, player):
    nb = 0
    for j in range (len(map[line])):
        if map[line][j] == player:
            nb += 1
        else:
            nb = 0
        if nb == 4:
            if (j + 1 < len(map[line]) and j - 4 >= 0):
                if (map[line][j + 1] == 0 and map[line][j - 4] == 0):
                    return 1
    return 0

# check for 1 line vertically
def line_v(map, clm, player):
    nb = 0
    for i in range (len(map)):
        if map[i][clm] == player:
            nb += 1
        else:
            nb = 0
        if nb == 4:
            if (i + 1 < len(map) and i - 4 >= 0):
                if (map[i + 1][clm] == 0 and map[i - 4][clm] == 0):
                    return 1
    return 0

# check for 1 line lr
def line_lr(map, i, j, player):
    nb = 0
    while (i < len(map) and j < len(map[i])):
        if map[i][j] == player:
            nb += 1
        else:
            nb = 0
        if nb == 4:
            if i < j:
                if (j + 1 < len(map) and j - 4 >= 0):
                    if (map[i + 1][j + 1] == 0 and map[i - 4][j - 4] == 0):
                        return 1
            else:
                if (i + 1 < len(map) and i - 4 >= 0):
                    if (map[i + 1][j + 1] == 0 and map[i - 4][j - 4] == 0):
                        return 1
        i += 1
        j += 1
    return 0

# check for 1 line rl
def line_rl(map, i, j, player):
    nb = 0
    while (i < len(map) and j >= 0):
        if map[i][j] == player:
            nb += 1
        else:
            nb = 0
        if nb == 4:
            if (i - 4 >= 0 and j + 4 < len(map)):
                if (map[i - 1][j + 1] == 0 and map[i - 4][j + 4] == 0):
                    return 1
        i += 1
        j -= 1
    return 0

# 3 gagnant ?
def is_winning(space, player, sens):
    global map
    cpy = copy_map()

    cpy[space[0]][space[1]] = player
    if (sens == 1):
        if (line_h(cpy, space[0], player) == 1):
            return 1
    if (sens == 2):
        if (line_v(cpy, space[1], player) == 1):
            return 1
    if (sens == 3):
        if (line_lr(cpy, space[0] - min(space[0]), space[1] - min(space[0]), player) == 1):
            return 1
    if (sens == 4):
        if (line_rl(cpy, space[0] - min(space[0], 10 - space[1]), space[1] + min(space[0], 10 - space[1]), player) == 1):
            return 1
    return -1

# copy map for is_winning func
def copy_map():
    global map

    cpy = []
    if (len(map) > 0):
        cpy = [[0 for i in range(len(map))] for j in range(len(map[0]))]
        for i in range (len(map)):
            for j in range (len(map[i])):
                cpy[i][j] = map[i][j]
    return cpy

# Begin keyword
def begin():
    global map

    if (len(map) != 0):
        map[int(len(map)/2)][int(len(map[0])/2)] == 1
        print (f"{len(map)/2:.0f},{len(map[0])/2:.0f}", flush=True)

# Main
if __name__ == '__main__':
    ipt = ""
    while (ipt != "END"):
        ipt = input()
        #ipt = sys.stdin.readline()
        if not ipt:
            break
        cmd = ipt.split()

        if (len(cmd) != 0):
            if (cmd[0] == "START"):
                start(cmd[1:])
            
            if (cmd[0] == "TURN"):
                turn(cmd[1:])

            if (cmd[0] == "BOARD"):
                board()

            if (cmd[0] == "a"):
                print (noopy(), flush=True)

            if (cmd[0] == "ABOUT"):
                print ("name=\"Noopy\", version=\"1.0\", author=\"Bastien&Tom\", country=\"FR\"", flush=True)
            
            if (cmd[0] == "BEGIN"):
                begin()