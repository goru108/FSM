class MR_CannonicalCode:
    def __init__(self, id1, id2, l1, e, l2):
        self.v1id = id1
        self.v2id = id2
        self.v1label = l1
        self.v2label = l2
        self.elabel = e

    def lessthan(self, c2):
        is_fwd= self.v1id < self.v2id
        rhs_is_fwd = c2.v1id < c2.v2id

        if not is_fwd and rhs_is_fwd:
            return True
        if not is_fwd and (not rhs_is_fwd) and (self.v2id<c2.v2id):
            return True

        if (not is_fwd) and (not rhs_is_fwd) and (self.v2id==c2.v2id) and (self.elabel<c2.elabel):
            return True

        if is_fwd and  rhs_is_fwd and self.v1id>c2.v1id:
            return True

        if is_fwd and  rhs_is_fwd and self.v1id==c2.v1id and self.v1label<c2.v1label:
            return True

        if  is_fwd and  rhs_is_fwd and self.v1id==c2.v1id and self.v1label==c2.v1label and self.elabel < c2.elabel:
            return True

        if  is_fwd and  rhs_is_fwd and self.v1id==c2.v1id and self.v1label==c2.v1label and self.elabel == c2.elabel and self.v2label<c2.v2label:
            return True

        return False

    def getCan_code_(self):
        can_cod = self.v1id
        can_cod = "{0}_{1}".format(can_cod, self.v2id)
        can_cod = "{0}_{1}".format(can_cod,self.v1label)
        can_cod = "{0}_{1}".format(can_cod,self.elabel)
        can_cod = "{0}_{1}".format(can_cod,self.v2label)
     #  print can_cod
        return can_cod


    def get_elabel(self):
        return self.elabel


class mindfs:

    def __init__(self, id1, id2, l1, e, l2, gi, gj):
        c = MR_CannonicalCode(id1,id2,l1,e,l2)
        self.right_most_path = []
        self.right_most_path.append(id1)
        self.right_most_path.append(id2)
        self.gid_to_cid = []
        self.cid_to_gid = []
        m1 = dict()
        m1[gi] = id1
        m2 = dict()
        m2[gj] = id2
        self.gid_to_cid.append(m1)
        self.gid_to_cid.append(m2)
        m3 = dict()
        m3[id1] = gi
        m4 = dict()
        m4[id2] = gj
        self.cid_to_gid.append(m3)
        self.cid_to_gid.append(m4)
        self.codes = []
        self.codes.append(c)



    def append(self, c, gi, gj) :
        self.codes.append(c)
        m1 = dict()
        m1[gi] =  c.v1id
        m2 = dict()
        m2[gj] = c.v2id
        self.gid_to_cid.append(m1)
        self.gid_to_cid.append(m2)
        m3 = dict()
        m3[c.v1id] = gi
        m4 = dict()
        m4[c.v2id] = gj
        self.cid_to_gid.append(m3)
        self.cid_to_gid.append(m4)

    def append_rmp(self,extensionpoint,lastv):
        temp = []
        index = 0
        i = 0
        for i in range(0, len(self.right_most_path)):
            temp.append(self.right_most_path.get(i))
            if (self.right_most_path[i]) == extensionpoint :
                break
        del self.right_most_path[:]
        temp.append(lastv)
        self.right_most_path + temp
        index = i + 1

    
    def gid(self,cid):
        it = iter(self.cid_to_gid)
        while True:
            try:
                obj1 = it.next()
                it1 = iter(obj1.keys())
                obj2 = it1.next()
                if cid == (int(obj2)):
                    return obj1.get(obj2)
            except StopIteration:
                break
        return -1

    def cid(self,gid):
        it = iter(self.gid_to_cid)
        while True:
            try:
                obj1 = it.next()
                it1 = iter(obj1.keys())
                obj2 = it1.next()
                if gid == obj2:
                    return (int(obj1.get(obj2)))
            except StopIteration:
                break
        return -1
