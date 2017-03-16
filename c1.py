# coding=utf-8
# python语法练习

import requests
from bs4 import BeautifulSoup

#爬豆瓣评论
def douban():
    content = requests.get('https://movie.douban.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div',{'class':'review-content'}):
        print div.text.strip()

def demo_string():
    hellostr = 'hello worlD!'
    print hellostr.capitalize()
    print hellostr.replace('worlD','coder')
    stra = '  \n\r helloworld \r\n'
    print 1, stra.lstrip()
    print 2, stra.rstrip()
    strc =  'hello w'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('w')
    print 5, hellostr + stra + strc
    print 6, len(strc)
    print 7, '-'.join(['a', 'b', 'c'])
    print 8, strc.split(' ')
    print 9, strc.find('llo')

def demo_opration():
    print 1, 3 / 2,5 * 3,4 - 1,2 * 9
    print 2, True,not True
    print 3, 1 < 2,3 > 2
    print 4, 3 << 2
    print 5, 5 | 3, 5 & 3, 5 ^ 3
    x = 2
    y = 3.3
    print x, y, type(x), type(y)

def demo_buildinfunction():
    print 1, max(2,8),min(3,5)
    print 2, len('xxx'), len([1, 2, 3])
    print 3, abs(-2)  # fabs,Math.fabs
    print 4, range(1, 10, 3)
    print 5, dir(list)
    x = 2
    print 6, eval('x + 3')
    print 7, chr(65), ord('a')
    print 8, divmod(11, 3)


def demo_controlflow():
    score = 65
    if score > 99:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'

    while score < 100:
        print score
        score += 10
    score = 65

    # for (int i = 0; i < 10; ++i)
    # continue ,break, pass
    for i in range(0, 10, 2):
        if i == 0:
            # pass:本轮什么都不做
            pass  # do_special
            # print 3, i
        if i < 5:
            continue
        print 3, i
        if i == 6:
            break

def demo_list():
    lista = [1, 2, 3]  # vector<> Arraylist
    print 1, lista
    listb = ['a', 1, 'c', 1.1]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in listb
    lista = lista + listb
    print 6, lista
    listb.insert(0, 'www')
    print 7, listb
    listb.pop(1)
    print 8, listb
    listb.reverse()
    print 9, listb
    print 10, listb[0], listb[1]
    listb.sort()
    print 11, listb
    listb.sort(reverse=True)
    print 12, listb
    print 13, listb * 2
    print 14, [0] * 14  # memset(src, 0, len)
    tuplea = (1, 2, 3) # 元组,只读的
    listaa = [1, 2, 3]
    listaa.append(4)
    print 15, listaa
    print tuplea



def add(a, b):
    return a + b
def sub(a, b):
    return a - b

# 字典(Dictionary)
# 由键和对应值成对组成。字典也被称作关联数组或哈希表。
def demo_dict():
    dicta = {4: 16, 1: 1, 2: 4, 3: 9}
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    print 3, dicta.has_key(1), dicta.has_key('3')
    # for map<int,int>::iterator it = x.begin(); it != x.end()
    for key, value in dicta.items():
        print 'key-value:', key, value
    dictb = {'+': add, '-': sub}
    print 4, dictb['+'](1, 2)
    print 5, dictb.get('-')(15, 3)
    dictb['*'] = 'x'
    print dictb
    dicta.pop(4)
    print 6, dicta
    del dicta[1]
    print 7, dicta

def demo_set():
    lista = [1, 2, 3]
    seta = set(lista)
    setb = set((2, 3, 4)) # 内含一个tuple
    print 1, seta
    print 3, seta.intersection(setb), seta & setb # 交集
    print 4, seta | setb, seta.union(setb) # 并集
    print 5, seta - setb
    seta.add('x')
    print 6, seta
    print 7, len(seta)
    print 8, seta.isdisjoint(set((1, 2))) # 是否没有交集


# 多态演示举例
class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)


class Guest(User):
    def __repr__(self):
        return 'im guest:' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid) + ' ' + self.group


def create_user(type):
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 101, 'g1')
    else:
        return Guest('gu1', 201)
        # raise ValueError('error')



if __name__ == '__main__':
    #print 'Hello world!'
    # comment
    # demo_string()
    # demo_opration()
    # demo_buildinfunction()
    # demo_controlflow()
    # demo_list()
    # demo_dict()
    # demo_set()

    #多态演示测试
    user1 = User('u1', 1)
    print user1
    admin1 = Admin('a1', 101, 'g1')
    print admin1

    print create_user('USERX')