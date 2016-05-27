import sys
# import test
from MR_CannonicalCode import MR_CannonicalCode
from MR_Pattern import MR_Pattern

import copy
class util:
    def __init__(self):
        self.freq_pats_hadoop = []
        self.check_unique = dict()
        self.freq_pats = []
        self.l1vat = dict()
        self.code_to_pat = dict()
        self.l1map_v2 = dict()
        self.vid_to_lbl = dict()
        self.minsup = 1

    def reappendb(self, textfile):
        with  open(textfile) as _text:
            lines = _text.readlines()
        _string = ''.join(lines)
        lines = []
        for lin in _string.split("\n"):
            lines.append(lin.split(" "))
        #print lines
        line = iter(lines)
        temp = line.next()

        flag = 0
        tid = 0
        i = 0                               #no of graphs
        j = 1
        # print len(temp)                    4
        # print len(lines)-1                7538
#check
        while i < 2:                        # gid
            tid = int(temp[2])
            if temp[0] == 't':

                while 1:
                    temp = line.next()
                    j += 1
                    # print len(temp)

                    if (len(lines) == j):
                        flag = 1
                        break

                    if (temp[0] == 't'):
                        i += 1
                        break

                    if temp[0] == 'v':
                        self.vid_to_lbl[int(temp[1])] = int(temp[2])

                    if temp[0] == 'e':
                        v1id = int(temp[1])
                        v2id = int(temp[2])
                        v1label = self.vid_to_lbl.get(v1id)
                        v2label = self.vid_to_lbl.get(v2id)

                        # print "v1id: " + str(v1id) + " v2id: " + str(v2id) + "v1label: " + str(v1label) + " v2label: " + str(v2label)
                        if v1label <= v2label:
                            g1 = MR_Pattern(v1label, v2label, int(temp[3]))
                        else:
                            g1 = MR_Pattern(v2label, v1label, int(temp[3]))
                            temp2 = v1id
                            v1id = v2id
                            v2id = temp2

                        if g1.getCan_code() not in self.l1vat.keys():
                            # print " in if loop"
                            # print g1.getCan_code()
                            m1 = dict()
                            m1[v1id] = v2id
                            # g = MR_Pattern()
                            l = []
                            l2 = []
                            l.append(m1)
                            l2.append(l)
                            l1 = []
                            m2 = dict()
                            m2[tid] = l2

                            # occurence list
                            # print "m1 " + str(m1)
                            # print "l " + str(l)
                            # print "l2 " + str(l2)
                            # print "m2 " + str(m2)

                            self.l1vat[g1.getCan_code()] = m2
                            self.freq_pats.append(g1)
                            self.code_to_pat[g1.getCan_code()] = g1
                            g1.insert_vid_tid(tid, v1id, v2id)

                            # print "freq_pats: ", self.freq_pats
                            # print "code_to_pat", self.code_to_pat
                            # print "g1 ", g1.insert_vid_tid(tid, v1id, v2id)


                        elif self.l1vat.get(g1.getCan_code()):
                            flag2 = 0
                            if (self.l1vat.get(g1.getCan_code())).get(tid):
                                flag2 = 1

                            if flag2 == 1:
                                m1 = dict()
                                m1[v1id] = v2id
                                it1 = iter((self.l1vat.get(g1.getCan_code())).get(tid))
                                (it1.next()).append(m1)
                                (self.code_to_pat.get(g1.getCan_code())).insert_vid_hs(tid, v1id, v2id)

                            if flag2 == 0:
                                m1 = dict()
                                m1[v1id] = v2id
                                l = []
                                l1 = []
                                l.append(m1)
                                l1.append(l)
                                m2 = dict()
                                m2[tid] = l1
                                self.l1vat.get(g1.getCan_code())[tid] = l1
                                (self.code_to_pat.get(g1.getCan_code())).insert_vid_tid(tid, v1id, v2id)

                # print "self.l1vat: " + str(self.l1vat)
                # print " FSM_ vid_to_label" + str(self.vid_to_lbl)
            if flag == 1:
                break

        # print i                 ##prints no of graphs
        # print j                 ##print no of lines

        itr = iter(self.freq_pats)
        #print itr
        while True:
            try:
                t = itr.next()
                t.support = len(t.vat)
            except StopIteration:
                break

        itr = iter(self.freq_pats)
        while True:
            try:
                #print "inside while"
                t = itr.next()
                # print type(t)
                srcl = t.idtolabels.get(1)
                destl = t.idtolabels.get(2)
                # print t.can_cod[0]
                el = t.can_cod[0].get_elabel()
                itr1 = 1
                temp = 0
                if srcl != destl:
                    itr1 = 2
                while itr1 > 0:
                    if len(self.l1map_v2) == 0:
                        l1 = []
                        l1.append(el)
                        m1 = dict()
                        m1[destl] = l1
                        l2 = []
                        l2.append(m1)
                        m3 = []
                        self.l1map_v2[srcl] = l2

                        if srcl != destl:
                            l11 = []
                            l11.append(el)
                            m11 = dict()
                            m11[srcl] = l11
                            l21 = []
                            l21.append(m11)
                            m31 = dict()
                            self.l1map_v2[destl] = l21
                        itr1-=1
                        continue

                    flag1 = 0
                    flag11 = 0

                    if self.l1map_v2.get(srcl):
                        flag1 = 1

                    if flag1 == 1:
                        l2 = []
                        l2 = self.l1map_v2.get(srcl)
                        itr2 = iter(l2)
                        flag2 = 0

                        while True:
                            try:
                                Obj2 = itr2.next()
                                if ((Obj2).get(destl)):
                                    flag2 = 1
                                    break
                            except StopIteration:
                                break

                        if flag2 == 1:
                            (Obj2.get(destl)).append(el)

                        if flag2 == 0:
                            m2 = dict()
                            l1 = []
                            l1.append(el)
                            m2[destl] = l1
                            (self.l1map_v2.get(srcl)).append(m2)

                    if flag1 == 0:
                        l1 = []
                        l1.append(el)
                        m1 = dict()
                        m1[destl] = l1
                        l2 = []
                        l2.append(m1)
                        m3 = dict()
                        self.l1map_v2[srcl] = l2

                    itr1 -= 1
                    if itr1 == 1:
                        temp = srcl
                        srcl = destl
                        destl = temp

            except StopIteration:
                break

    def get_neighbors(self, nb, vlabel, adj_list):
        it = iter(self.l1map_v2.keys())

        m1 = dict()

        while True:
            try:
                obj1 = it.next()
                if vlabel != (int(obj1)):
                    continue
                it1 = iter((self.l1map_v2.get(obj1)))
                while True:
                    try:
                        obj2 = it1.next()
                        it2 = iter(obj2.keys())
                        obj3 = it2.next()
                        nbid = obj3
                        it2 = iter(obj2.get(obj3))
                        while True:
                            try:
                                m = dict()
                                o = it2.next()
                                m[nbid] = int(o)
                                nb.append(m)
                            except StopIteration:
                                break

                    except StopIteration:
                        break

            except StopIteration:
                break

    def generate_candidate(self, P):
        self.backward_extension(P)
        self.forward_extension(P)
        return

    def backward_extension(self, P):
        # print "in backward extension Right most path :", P.right_most_path
        if len(P.right_most_path) < 3:
            return
        rv = []
        for i in range(len(P.right_most_path)):
            rv.append(P.right_most_path.get(i))

        adj_list = []
        nbrs = []
        # obj1 = Object()
        # obj2 = Object()
        right_most_vertex = rv.get(len(rv) - 1)
        rv.remove(len(rv) - 1)
        rv.remove(len(rv) - 1)

        adj_list = P.get_adjlist(right_most_vertex)
        vlabel = P.idtolabels.get(right_most_vertex)
        print "FSM_ backward extension: ", vlabel, adj_list
        self.get_neighbors(nbrs, vlabel, adj_list)

        for i in range(len(rv)):
            flag = 0
            it = iter(nbrs)
            v2label_back = P.idtolabels.get(rv.get(i))
            if not P.noEdgeexist(right_most_vertex,int(rv.get(i))):
                continue

            for j in range(len(nbrs)):
                if int(nbrs.get(j).keys()[0]) == v2label_back:
                    elabel = int(nbrs.get(j).get(v2label_back))
                    cc = None

                    if v2label_back <= vlabel:
                        cc=MR_CannonicalCode(1, 2, v2label_back, elabel, vlabel)
                    else:
                        cc=MR_CannonicalCode(1, 2, vlabel, elabel, v2label_back)

                    cc_code = cc.getCan_code_()

                    p = MR_Pattern(None,None,None)
                    p=P.clone()
                    # p = copy.deepcopy(P)
                    p.addflesh_backextension(P, vlabel, elabel, v2label_back, right_most_vertex, int(rv.get(i)))

                    if not p.check_isomorphism():
                        continue

                    p.vat_intersection(P, self.l1vat.get(cc_code))

                    if p.support > 0 and (p.getCan_code() not in self.check_unique.keys()):
                        self.freq_pats_hadoop.append(p)
                        self.check_unique[p.getCan_code()] = 1


    def forward_extension(self, P):
        rv = []
        # print " forward extension right most path ", P.right_most_path
        for i in range(len(P.right_most_path)):
            rv.append(P.right_most_path[i])

        rv.sort(reverse=True)
        it = iter(rv)
        nbrs = []
        adj_list = []
        rmpsize = len(rv)
        el = 0
        prevvlabel = 0

        while True:
            try:

                extensionpoint = it.next()
                adj_list = P.get_adjlist(int(extensionpoint))
                nbrs = []
                vlabel = int((P.idtolabels.get(extensionpoint)))
                self.get_neighbors(nbrs, vlabel, adj_list)
                it1 = iter(nbrs)

                while True:
                    try:
                        obj3 = it1.next()
                        it2 = iter(obj3.keys())
                        nbrspoint = it2.next()
                        added_vlabel = nbrspoint
                        elabel = int(obj3.get(nbrspoint))
                        lastvid = P.get_lastvid()
                        # print " vlabel , elabel, added label ", vlabel, elabel, added_vlabel
                        if vlabel <= added_vlabel:
                            cc=MR_CannonicalCode(1, 2, vlabel, elabel, added_vlabel)
                        else:
                            cc=MR_CannonicalCode(1, 2, added_vlabel, elabel, vlabel)
                        cc_code = cc.getCan_code_()
                        # print " right most path of P", P.right_most_path
                        p = MR_Pattern(None, None, None)
                        p=P.clone()
                        # p = copy.deepcopy(P)
                        # print "p.rightmostpath", p.right_most_path
                        p.addflesh(P, vlabel, elabel, added_vlabel, int(extensionpoint), lastvid + 1, self.minsup)
                        # print "in FSM_ forward extension", p
                        if not p.check_isomorphism():
                            continue
                        # print " self.l1vat.get(cc_code)  ",self.l1vat.get(cc_code)
                        p.vat_intersection(P, self.l1vat.get(cc_code))
                        if p.support > 0 and (p.getCan_code() not in self.check_unique.keys()):
                            self.freq_pats_hadoop.append(p)
                            self.check_unique[p.getCan_code()] = 1
                    except StopIteration:
                        break
            except StopIteration:
                break
#
#
# if __name__=='__main__':
#     # readbi = test.reappendb("/home/saurabh/Desktop/MIRAGE_version1/sample_data/input_new.txt")
#     # #print readbi.reappendb()
#     readappendb=util()
#     readappendb.reappendb("/home/saurabh/Desktop/MIRAGE_version1/sample_data/input_new.txt")
