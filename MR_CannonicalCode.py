
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

        if not is_fwd and  rhs_is_fwd:
          return True
        if not is_fwd and (not rhs_is_fwd) and (self.v2id<c2.v2id):
          return True

        if (not is_fwd) and (not rhs_is_fwd) and (self.v2id==c2.v2id) and (self.elabel<c2.elabel):
          return True

        if  is_fwd and  rhs_is_fwd and self.v1id>c2.v1id:
          return True

        if  is_fwd and  rhs_is_fwd and self.v1id==c2.v1id and self.v1label<c2.v1label:
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


class mindfs:

	def __init__(self, id1, id2, l1, e, l2, gi, gj):
		c = MR_CannonicalCode(id1,id2,l1,e,l2)
		right_most_path = []
		right_most_path.append(id1)
		right_most_path.append(id2)
		gid_to_cid = []
		cid_to_gid = []
		m1 = dict()
		m1[gi] = id1
		m2 = dict()
		m2[gj] = id2
		gid_to_cid.append(m1)
		gid_to_cid.append(m2)
		m3 = dict()
		m3[id1] = gi
		m4 = dict()
		m4[id2] = gj
		cid_to_gid.append(m3)
		cid_to_gid.append(m4)
		codes = []
		codes.append(c)
