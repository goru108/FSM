from MR_CannonicalCode import MR_CannonicalCode


class MR_Pattern:
    def __init__(self, v1label, v2label, elabel):
        self.support = 0
        self.v_ids = []
        self.can_cod = []
        self.adj_list = [0]
        self.right_most_path = []
        self.vat = dict()
        self.Vsets = dict()
        self.idtolabels = dict()

        self.idtolabels[1] = v1label
        self.idtolabels[2] = v2label
        self.v_ids.append(1)
        self.v_ids.append(2)

        m1 = dict()
        m1[2] = elabel
        m2 = dict()
        m2[1] = elabel
        l1 = []
        l1.append(m1)
        l2 = []
        l2.append(m2)
        self.adj_list.append(l1)
        self.adj_list.append(l2)
        self.cc = MR_CannonicalCode(1, 2, v1label, elabel, v2label)
        self.can_cod.append(self.cc)
        self.right_most_path.append(1)
        self.right_most_path.append(2)
        self.iscannonical = True
        self.support = 1

    def getCan_code(self):
        cc = self.can_cod[0].getCan_code_()
        for i in range(1, len(self.can_cod)):
            cc = cc + ":" + self.can_cod[i].getCan_code_()
        return cc

    def insert_vid_tid(self, tid, v1id, v2id):
        s = []
        s.append(v1id)
        s.append(v2id)
        l = []
        l.append(s)
        self.Vsets[tid] = l

    def insert_vid_hs(self, tid, v1id, v2id):
        s = dict()
        s.has_key(v1id)
        s.has_key(v2id)
        (self.Vsets.get(tid)).append(s)

    def get_adjlist(self, vid):
        l = []
        it = (self.adj_list.get(vid)).iterator()
        while it.next:
            o = it.next()
            it1 = iter(o.keySet())
            o1 = it1.next()
            m = dict()
            elabel = o.get(o1)

            m.put(self.idtolabels.get(o1), elabel)
            l.add(m)
        return l

    def noEdgeexist(self, v1id, v2id):
        l = []
        it = iter(self.adj_list.get(v1id))

        while True:
            try:
                o = it.next()
                it1 = iter((o).keySet())
                o1 = it1.next()
                if (int)(o1) == v2id:
                    return False
            except StopIteration:
                break
        return True

    def get_adjlist(self,vid):
        l = []
        it = iter(self.adj_list.__getitem__(vid))
        while True:
            try:
                o = it.next()
                it1 = iter(o.keys())
                o1 = it1.next()
                m = dict()
                elabel = o.get(o1)

                m[self.idtolabels.get(o1)] = elabel
                l.add(m)
            except StopIteration:
                break

        return l

    def noEdgeexist(self,v1id, v2id):
        l = []
        it = iter(self.adj_list.get(v1id))
        while True:
            try:
                o = it.next()
                it1 = iter(o.keys())
                o1 = it1.next()

                if (int)(o1) == v2id:
                    return False
            except StopIteration:
                break

        return True

    def addflesh_backextension(self, P, vlabel, elabel, added_vlabel, v1id, v2id) :
        cc = MR_CannonicalCode()
        cc.MR_CannonicalCode(v1id, v2id, vlabel, elabel, added_vlabel)
        self.can_cod.add(cc)

        m = dict()
        m[v2id] = elabel
        self.adj_list.get(v1id).append(m)
        m1 = dict()
        m1[v1id] = elabel
        self.adj_list.get(v2id).append(m1)

        for i in range(0,len(P.right_most_path)):
            self.right_most_path.append(P.right_most_path[i])

    def getelabel(self,v1id, v2id):
        n = []
        n = self.adj_list.get(v1id)
        it = iter()
        elabel = 0
        while True:
            try:
                o = it.next()
                it1 = iter(o.keys())
                o1 = it1.next()
                if (int)(o1) == v2id :
                    elabel = (int)(o.get(o1))
                    break
            except StopIteration:
                break

        return elabel


    def check_isomorphism(self):
        ids = []
        sde = []
        dfscode = []
        srcl1 = (int)(self.idtolabels.get(1))
        destl1 = (int)(self.idtolabels.get(2))
        e = (self.getelabel(1, 2))
        new_e = self.iso_startup(int(srcl1),destl1, e, ids, sde)
        srcl = (int)(sde[0])
        destl = (int)(sde[1])
        it = iter(ids)

        while True :
            try:
                obj = it.next()
                it1 = iter(obj.keys())
                obj1 = it1.next
                gi = (int)(obj1)
                gj = (int)(obj.get(obj1))
                dfs = MR_CannonicalCode()
                dfs.mindfs(1, 2, srcl, new_e, destl, gi, gj)
                dfscode.append(dfs)

            except StopIteration:
                break

        c = dfscode[0].codes[0]
        if c.lessthan(self.can_cod[0]) :
            return False

        for i in range(0,len(dfscode)) :
            r = minimal(dfscode[i])
            if not r :
                self.iscannonical=False
                return False

        self.iscannonical = True
        return True

    def iso_startup(self,srcl, destl, e, ids, sde):
        adj_list = []
        sde.append(0, srcl)
        sde.append(1, destl)
        sde.append(2, e)
        print "v_ids size = ",len(self.v_ids)
        new_e = e

        for i in range(0,len(self.v_ids)):
            if (int)(self.idtolabels.get(self.v_ids[i])) > srcl :
                continue

            adj_list = self.get_adjlist_ids(self.v_ids[i])
            it = iter(adj_list)
            if (int)(self.idtolabels.get(self.v_ids[i])) < srcl :
                ids.clear()
                obj = it.next
                it2 = iter(obj.keys())
                obj2 = it2.next
                srcl = (int)(self.idtolabels.get(self.v_ids[i]))
                destl = (int)(self.idtolabels.get(obj2))
                new_e = (int)(obj.get(obj2))
                sde.append(0, srcl)
                sde.append(1, destl)
                sde.append(2, new_e)
                m = dict()
                m[self.v_ids[i]] = obj2
                ids.append(m)

            while True :
                try:
                    obj = it.next()
                    it2 = iter(obj.keys())
                    obj2 = it2.next()

                    if (int)(obj.get(obj2)) <= e :
                        if (int)(obj.get(obj2)) < e :
                            ids.clear()
                            destl = (int)(self.idtolabels.get(obj2))
                            new_e = (int)(obj.get(obj2))

                            sde.append(1, destl)
                            sde.append(2, new_e)
                            m = dict()
                            m[self.v_ids[i]] = obj2
                            ids.append(m)

                            continue

                except StopIteration:
                    break

            if (self.idtolabels.get(obj2)) <= destl :
                if (self.idtolabels.get(obj2)) < destl :
                    ids.clear()
                    destl = (int)(self.idtolabels.get(obj2))
                    sde.append(1, destl)

                m = dict()
                m[self.v_ids()[i]] = obj2

                ids.add(m)
        return new_e

