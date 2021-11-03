class Shashki(): 
    def recordingMoves(self, x1, y1, motion, x2, y2, f: str, i):
        f = open(f, 'a')
        f.write(str(i))
        f.write('. ')
        if(chet != 0 and chet != 1):
            f.write('damki ')
        f.write(motion)
        f.write(' походил c ')
        f.write(str(x1))
        f.write(' ')
        f.write(str(y1))
        f.write(' на ')
        f.write(str(x2))
        f.write(' ')
        f.write(str(y1))
        f.write(' \n')
        f.close()
    def mot(self, f):  
        f = open(f, 'r')  
        motion = f.read(1)
        f.close() 
        return motion  
    def change(self, m, chet, x1, y1, x2, y2):
        if(chet == 2 and x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0):
            return 1
        m[x1][y1], m[x2][y2] = m[x2][y2], m[x1][y1]
        if(chet == 1):
            m[int((x1 + x2) / 2)][int((y1 + y2) / 2)] = '0'
        if(chet == 2):
            m[x2 - 1][y2 - 1] = '0'
        if(chet == 3):
            m[x2 + 1][y2 - 1] = '0'
        if(chet == 4):
            m[x2 - 1][y2 + 1] = '0'
        if(chet == 5):
            m[x2 + 1][y2 + 1] = '0'
        return 0
    def readFromFile(self, f):  
        m = [0] * 8  
        f = open(f, 'r')  
        f.read(2) 
        for i in range(8): 
            m[i] = list(f.readline().split()) 
        f.close() 
        return m 
 
    def getNextTurn(self, m, motion):
        chet = 0
        i = 0
        j = 0
        #B
        if(motion == 'b'):
            for i in range(7): # проверяем по диагонали справа есть ли фишка для того чтобы съесть
                for j in range(7):
                    if( j != 6) and ( j != 7) and ( i != 6) and ( i != 7): # снизу
                        if(m[i][j] == 'B'):
                            k = 1
                            while((i + k) < 7 and (j + k) < 7): #дамка
                                if((m[i + k][j + k] == 'w' or m[i + k][j + k] == 'W') and m[i + k + 1][j + k + 1] != '0'):
                                    break
                                if((m[i + k][j + k] == 'w' or m[i + k][j + k] == 'W') and m[i + k + 1][j + k + 1] == '0'):
                                    chet = 2
                                    return chet, i, j, i + k + 1, j + k + 1
                                k = k + 1
                        if(m[i + 1][j + 1] == 'w') and (m[i][j] == motion) and (m[i + 2][j + 2] == '0'):#обычная
                            chet = 1
                            return chet, i, j, i + 2, j + 2
 
                    if( j != 6) and ( j != 7) and ( i != 0) and ( i != 1): # сверху
                        if(m[i][j] == 'B'): #дамка
                            k = 1
                            while((i - k) > 0 and (j + k) < 7):
                                if((m[i - k][j + k] == 'w' or m[i - k][j + k] == 'W') and m[i - k - 1][j + k + 1] != '0'):
                                    break
                                if((m[i - k][j + k] == 'w' or m[i - k][j + k] == 'W') and m[i - k - 1][j + k + 1] == '0'):
                                    chet = 3
                                    return chet, i, j, i - k - 1, j + k + 1
                                k = k + 1
                        if(m[i - 1][j + 1] == 'w') and (m[i][j] == motion) and (m[i - 2][j + 2] == '0'):#обычная
                            #print(i, j, 'ходит', i - 2, j + 2, 'сожрал')
                            chet = 1
                            return chet, i, j, i - 2, j + 2
 
            j = 1
            for i in range(7): # проверяем по диагонали слева есть ли фишка для того чтобы съесть
                for j in range(7):
                    if(j != 0) and (j != 1) and ( i != 6) and ( i != 7):#снизу
                        if(m[i][j] == 'B'):#дамка
                            k = 1
                            while((i + k) < 7 and (j - k) > 0):
                                if((m[i + k][j - k] == 'w' or m[i + k][j - k] == 'W') and m[i + k + 1][j - k - 1] != '0'):
                                    break
                                if((m[i + k][j - k] == 'w' or m[i + k][j - k] == 'W') and m[i + k + 1][j - k - 1] == '0'):
                                    chet = 4
                                    return chet, i, j, i + k + 1, j - k - 1
                                k = k + 1
                        if(m[i + 1][j - 1] == 'w') and (m[i][j] == motion) and (m[i + 2][j - 2] == '0'):#обычная
                            #print(i, j, 'ходит', i + 2, j - 2, 'сожрал')
                            chet = 1
                            return chet, i, j, i + 2, j - 2
 
                    if(j != 0) and (j != 1) and ( i != 0) and ( i != 1):#сверху
                        if(m[i][j] == 'B'):#дамка
                            k = 1
                            while((i - k) > 0 and (j - k) > 0): 
                                if((m[i - k][j - k] == 'w' or m[i - k][j - k] == 'W') and m[i - k - 1][j - k - 1] == '0'):
                                    break
                                if((m[i - k][j - k] == 'w' or m[i - k][j - k] == 'W') and m[i - k - 1][j - k - 1] == '0'):
                                    chet = 5
                                    return chet, i, j, i - k - 1, j - k - 1
                                k = k + 1
                        if(m[i - 1][j - 1] == 'w') and (m[i][j] == motion) and (m[i - 2][j - 2] == '0'):
                            #print(i, j, 'ходит', i - 2, j - 2, 'сожрал')
                            chet = 1
                            return chet, i, j, i - 2, j - 2
 
            j = 0
            if(chet == 0):
                for i in range(8): # проверяем по диагонали справа есть ли фишка
                    for j in range(8):
                        if(j != 7) and (i != 7):#обычный
                            if(m[i][j] == 'B'):
                                k = 1
                                while((i + k) < 8 and (j + k) < 8):
                                    if(m[i + k][j + k] == '0'):
                                        return chet, i, j, i + k, j + k
                                    k = k + 1
                            if(m[i + 1][j + 1] == '0') and (m[i][j] == motion):
                                return chet, i, j, i + 1, j + 1
                        if(j != 7 and i != 0):
                            if(m[i][j] == 'B'):
                                k = 1
                                while((i - k) >= 0 and (j + k) < 8):
                                    if(m[i - k][j + k] == '0'):
                                        return chet, i, j, i - k, j + k
                                    k = k + 1
 
                j = 1
                for i in range(8): # проверяем по диагонали cлева есть ли фишка
                    for j in range(8):
                        if(j != 0) and (i != 7):
                            if(m[i][j] == 'B'):
                                k = 1
                                while((i + k) < 8 and (j - k) >= 0):
                                    if(m[i + k][j - k] == '0'):
                                        return chet, i, j, i + k, j - k
                                    k = k + 1
                            if(m[i + 1][j - 1] == '0') and (m[i][j] == motion):
                                return chet, i, j, i + 1, j - 1
                        if(j != 0 and i != 0):
                            if(m[i][j] == 'B'):
                                k = 1
                                while((i - k) >= 0 and (j - k) >= 0):
                                    if(m[i - k][j - k] == '0'):
                                        return chet, i, j, i - k, j - k
                                    k = k + 1
        #W
        if(motion =='w'):
            for i in range(7): # проверяем по диагонали справа есть ли фишка для того чтобы съесть
                for j in range(7):
                    if( j != 6) and ( j != 7) and ( i != 6) and ( i != 7): # снизу
                        if(m[i][j] == 'W'): #дамка
                            k = 1
                            while((i + k) < 7 and (j + k) < 7):
                                if((m[i + k][j + k] == 'b' or m[i + k][j + k] == 'B') and m[i + k + 1][j + k + 1] != '0'):
                                    break
                                if((m[i + k][j + k] == 'b' or m[i + k][j + k] == 'B') and m[i + k + 1][j + k + 1] == '0'):
                                    chet = 2
                                    return chet, i, j, i + k + 1, j + k + 1
                                k = k + 1
                        if(m[i + 1][j + 1] == 'b') and (m[i][j] == motion) and (m[i + 2][j + 2] == '0'):
                            #print(i, j, 'ходит', i + 2, j + 2, 'сожрал')
                            chet = 1
                            return chet, i, j, i + 2, j + 2
 
                    if( j != 6) and ( j != 7) and ( i != 0) and ( i != 1): # сверху
                        if(m[i][j] == 'W'): #дамка
                            k = 1
                            while((i - k) > 0 and (j + k) < 7):
                                if((m[i - k][j + k] == 'b' or m[i - k][j + k] == 'B') and m[i - k - 1][j + k + 1] != '0'):
                                    break
                                if((m[i - k][j + k] == 'b' or m[i - k][j + k] == 'B') and m[i - k - 1][j + k + 1] == '0'):
                                    chet = 3
                                    return chet, i, j, i - k - 1, j + k + 1
                                k = k + 1
                        if(m[i - 1][j + 1] == 'b') and (m[i][j] == motion) and (m[i - 2][j + 2] == '0'):
                            #print(i, j, 'ходит', i - 2, j + 2, 'сожрал')
                            chet = 1
                            return chet, i, j, i - 2, j + 2
 
            j = 1
            for i in range(7): # проверяем по диагонали слева есть ли фишка для того чтобы съесть
                for j in range(7):
                    if(j != 0) and (j != 1) and ( i != 6) and ( i != 7):
                        if(m[i][j] == 'W'):#дамка
                            k = 1
                            while((i + k) < 7 and (j - k) > 0):
                                if((m[i + k][j - k] == 'b' or m[i + k][j - k] == 'B') and m[i + k + 1][j - k - 1] != '0'):
                                    break
                                if((m[i + k][j - k] == 'b' or m[i + k][j - k] == 'B') and m[i + k + 1][j - k - 1] == '0'):
                                    chet = 4
                                    return chet, i, j, i + k + 1, j - k - 1
                                k = k + 1
                        if(m[i + 1][j - 1] == 'b') and (m[i][j] == motion) and (m[i + 2][j - 2] == '0'):
                            #print(i, j, 'ходит', i + 2, j - 2, 'сожрал')
                            chet = 1
                            return chet, i, j, i + 2, j - 2
 
                    if(j != 0) and (j != 1) and ( i != 0 ) and ( i != 1):
                        if(m[i][j] == 'W'):#дамка
                            k = 1
                            while((i - k) > 0 and (j - k) > 0): 
                                if((m[i - k][j - k] == 'b' or m[i - k][j - k] == 'B') and m[i - k - 1][j - k - 1] == '0'):
                                    break
                                if((m[i - k][j - k] == 'b' or m[i - k][j - k] == 'B') and m[i - k - 1][j - k - 1] == '0'):
                                    chet = 5
                                    return chet, i, j, i - k - 1, j - k - 1
                                k = k + 1
                        if(m[i - 1][j - 1] == 'b') and (m[i][j] == motion) and (m[i - 2][j - 2] == '0'):
                            #print(i, j, 'ходит', i - 2, j - 2, 'сожрал')
                            chet = 1
                            return chet, i, j, i - 2, j - 2
 
            j = 0
            if(chet == 0):
                for i in range(8): # проверяем по диагонали справа есть ли фишка
                    for j in range(8):
                        if( j != 7) and (i != 0):
                            if(m[i - 1][j + 1] == '0') and (m[i][j] == motion): 
                                #print(i, j, 'ходит', i - 1, j + 1)
                                return chet, i, j, i - 1, j + 1
                j = 1
                for i in range(8): # проверяем по диагонали cлева есть ли фишка
                    for j in range(8):
                        if(j != 0) and (i != 0):
                            if(m[i - 1][j - 1] == '0') and (m[i][j] == motion):
                                #print(i, j, 'ходит', i - 1, j - 1)
                                return chet, i, j, i - 1, j - 1
        i = 0 
        j = 0
        chet = 2
        return chet, i, j, i, j
    def writeToFile(self, x1, y1, x2, y2, motion, m):
        #m[x1][y1], m[x2][y2] = m[x2][y2], m[x1][y1]
        #x1, y1 = x2, y2
        #if(chet == 1):
         #   m[int((x1 + x2) / 2)][int((y1 + y2) / 2)] = '0'
        f = open('3W_with_damki.txt', 'w') #аттрибут a - будет открывать файл на дозапись, w - на перезапись
        i = 0
        j = 0
        #if(proverka == 1):
          #  f.write('G\n')
           # f.write(motion)
        #if(proverka == 0):
        if(motion == 'w'):
            f.write('b')
        if(motion == 'b'):
            f.write('w')
        f.write('\n')
        for i in range(8):
            for j in range(8):
                f.write(m[i][j])
                f.write(' ')
            f.write('\n')
        f.close()
    #def __init__(self, f: str): 
     #   self.f = f 
      #  self.motion = mot(self.f) 
       # self.m = readFromFile(self.f) 
        #self.chet, self.x1, self.y1, self.x2, self.y2 = x.getNextTurn() 
 
proverka = 0
i = 0
while(proverka == 0):
    i = i + 1
    x = Shashki()
    motion = x.mot('3W_with_damki.txt')
    m = x.readFromFile('3W_with_damki.txt')
    сhet = 0
    chet, x1, y1, x2, y2 = x.getNextTurn(m, motion)
    proverka = 0
    proverka = x.change(m, chet, x1, y1, x2, y2)
    if(proverka == 0):
        x.recordingMoves(x1, y1, motion, x2, y2, 'chekers.txt', i)
    if(chet != 0 and chet != 1 and proverka != 1):
        print('damki')
    print(x1, y1, motion, x2, y2)
    x.writeToFile(x1, x2, y1, y2, motion, m)
    #print(m)
print('Проиграли', motion,)
f = open('chekers.txt', 'a')
f.write(motion)
f.write('  G A M E  O V E R \n')
f.close()