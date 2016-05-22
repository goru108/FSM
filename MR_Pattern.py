from MR_CannonicalCode import MR_CannonicalCode

""" Finds the MR Pattern"""
class MR_Pattern:
    def __init__(self, v1label, v2label, elabel):
        self.support = 0
        self.v_ids = []
        self.can_cod = []
        self.adj_list = []
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
                if int(o1) == v2id:
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

                if int(o1) == v2id:
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
                if int(o1) == v2id :
                    elabel = int(o.get(o1))
                    break
            except StopIteration:
                break

        return elabel

    def get_adjlist_ids(self,vid):
        l = []
        it = iter(self.adj_list.get(vid))

        while True:
            try:
                o = it.next()
                it1 = iter(o.keys())
                o1 = it1.next()
                m = dict()
                elabel = o.get(o1)
                m[o1]=elabel
                l.append(m)
            except StopIteration:
                break
        return l

    def clone(self) :
        obj = MR_Pattern()
        for i in range(0,len(self.v_ids)):
            obj.self.v_ids.append(self.v_ids[i])

        it = iter(self.idtolabels.keys())
        it1 = iter(self.idtolabels.values())
        while True :
            try:
                o1 = it.next()
                o2 = it1.next()
                obj.idtolabels[o1] = o2
            except StopIteration:
                break

        it3 = iter(self.adj_list.keys())

        while True :
            try:
                o1 = it3.next()
                it = iter(self.adj_list.get(o1))
                l = []
                while True :
                    try:
                        o = it.next()
                        it1 = iter(o.keys())
                        o2 = it1.next()
                        m = dict()
                        elabel = (o.get(o2))
                        vlabel = o2
                        m[vlabel] = elabel
                        l.append(m)
                    except StopIteration:
                        break
                obj.adj_list[o1] = l
            except StopIteration:
                break
        obj.vat = dict()
        obj.iscannonical = True

        for i in range(0,len(self.can_cod)) :
           obj.can_cod.append(self.can_cod[i])

        obj.support = self.support
        return obj


    def check_isomorphism(self):
        ids = []
        sde = []
        dfscode = []
        srcl1 = int(self.idtolabels.get(1))
        destl1 = int(self.idtolabels.get(2))
        e = (self.getelabel(1, 2))
        new_e = self.iso_startup(int(srcl1),destl1, e, ids, sde)
        srcl = int(sde[0])
        destl = int(sde[1])
        it = iter(ids)

        while True :
            try:
                obj = it.next()
                it1 = iter(obj.keys())
                obj1 = it1.next
                gi = int(obj1)
                gj = int(obj.get(obj1))
                dfs = MR_CannonicalCode()
                dfs.mindfs(1, 2, srcl, new_e, destl, gi, gj)
                dfscode.append(dfs)

            except StopIteration:
                break

        c = dfscode[0].codes[0]
        if c.lessthan(self.can_cod[0]) :
            return False

        for i in range(0,len(dfscode)) :
            r = self.minimal(dfscode[i])
            if not r :
                self.iscannonical=False
                return False

        self.iscannonical = True
        return True

    def minimal(self,new_code):
        if len(self.can_cod) == len(new_code.codes) :
            return True
        lastadded = new_code.codes[len(new_code.codes) - 1]
        is_last_fwd = (lastadded.v1id < lastadded.v2id) # denotes if last edge in new_code was a fwd edge
        if is_last_fwd :
            last_vid = lastadded.v2id
        else:
            last_vid = lastadded.v1id # vid to which edge shall be added
        last_vid_g = new_code.gid(last_vid)
        e = 0
        adj_list = self.get_adjlist_ids(last_vid_g)
        code_index = len(new_code.codes)

        rmp = new_code.right_most_path

        # first try to add BACK EDGE
        back_vid = last_vid
        if is_last_fwd : # add the farthest back edge you find
            last_back_vid = -1
        else: #add a back edge only if it 's after the last back edge present
            last_back_vid = lastadded.v2id

        it = iter(adj_list)
        while True:
            try:
                rmvaddindex = len(rmp) - 3
                obj1 = it.next()
                it1 = iter(obj1.keys())
                obj2 = it1.next()
                neibor = (int(obj2))
            while rmvaddindex >= 0 :
                if int(rmp[rmvaddindex]) == new_code.cid(neibor):
                    break

                if (int(rmp[rmvaddindex])) < new_code.cid(neibor):
                    rmvaddindex = 0

            if rmvaddindex < 0 :
                continue

            if (new_code.cid(neibor) < back_vid and new_code.cid(neibor) > last_back_vid): # self vertex is farthest one seen so far
            #  a valid back edge must end at a vertex after last_back_vid
                back_vid = new_code.cid(neibor)
                e = int(obj1.get(obj2))

        if back_vid != last_vid : # valid back edge found
            lblv1=int(self.idtolabels.get(new_code.gid(last_vid)))
            lblv2=(int(self.idtolabels.get(new_code.gid(back_vid))))
            c = MR_CannonicalCode(last_vid, back_vid, lblv1, e, lblv2)

            if c.lessthan(self.can_cod[code_index]):
                #print("decision at back-edge: new tuple is more minimal")
                return False

            if (self.can_cod[code_index]).lessthan(c) :
            #print("decision at back-edge: current tuple is more minimal")
                return True
            else:
                new_code.codes.add(c)
                # no changes to  new_code's rmp, nor to the cid-gid mappings since back edge implies both vertices were already present in it
                #print("size of new_code inside back = " + len(new_code.codes))
                return self.minimal(new_code)
                # print("size of new_code inside back 2 = " + len(new_code.codes))

        # try to add a FWD EDGE how to: find  the  deepest outgoing edge, and among all such edges find the minimal one, i.e.least edge - label + least dest - label
        fwd_found = False
        last_vid = rmp[len(rmp)- 1]
        new_vids = []
        #equivalent minimal vertices whose minimality has to be checked recursively
        e = 99999
        dest_v = 99999
        extensionpoint = 0
        for i in range(len(rmp)-1,-1) :
            extensionpoint = int(rmp[i])
            del adj_list[:]
            adj_list = self.get_adjlist_ids(new_code.gid(extensionpoint))
            it = iter(adj_list)
            while True:
                try:
                    obj1 = it.next()
                    it1 = iter(obj1.keys())
                    obj2 = it1.next()
                    possibleextension = (int(obj2))

                    if new_code.cid(possibleextension) != -1 :
                        continue

                    possibleextensionElabel = int(obj1.get(obj2))

                    if possibleextensionElabel <= e:
                        # minimal edge
                        #print "possibleextension = " , possibleextension
                        curr_lbl = int(self.idtolabels.get(possibleextension))

                        if possibleextensionElabel < e :
                        # new minimal edge found
                            del new_vids[:]
                            e=possibleextensionElabel
                            dest_v=curr_lbl


                        if curr_lbl <= dest_v :
                            # minimal dest label
                            if curr_lbl < dest_v :
                                del new_vids[:]
                                dest_v=curr_lbl

                            new_vids.append(possibleextension)
                except StopIteration:
                    break

            if not new_vids:
                #fwd extension found at self level
                fwd_found=True
                break

        if not fwd_found :
            #no fwd edge extension could be found i.e.all fwd edges have been added so self code is minimal
            # cout << "Isomorphism decision at fwd-edge: all edges exhausted" << endl
            return True

        #print "extensionpoint = " , extensionpoint , "added with =" , (last_vid + 1)
        c = MR_CannonicalCode(extensionpoint, last_vid + 1, self.idtolabels.get(new_code.gid(extensionpoint)), e,self.idtolabels.get(new_vids[0]))
        if c.lessthan((MR_CannonicalCode)(self.can_cod[code_index])) :
            #new edge is more minimal
            return False
        if self.can_cod[code_index].lessthan(c) :
            #current tuple is more minimal
            return True

        #check minimality against each new code
        for i in range(0,len(new_vids)) :
            #CAN_CODE next_code = new_code
            next_code = new_code.clone(extensionpoint)
            #mindfs next_code = new_code
            gi = next_code.gid(extensionpoint)
            gj = int(new_vids[i])

            next_code.append(c, gi, gj)
            next_code.append_rmp(extensionpoint, last_vid + 1)

            if not self.minimal(next_code) :
                return False

        return True


    def iso_startup(self,srcl, destl, e, ids, sde):
        adj_list = []
        sde.append(0, srcl)
        sde.append(1, destl)
        sde.append(2, e)
        print "v_ids size = ",len(self.v_ids)
        new_e = e

        for i in range(0,len(self.v_ids)):
            if int(self.idtolabels.get(self.v_ids[i])) > srcl :
                continue

            adj_list = self.get_adjlist_ids(self.v_ids[i])
            it = iter(adj_list)
            if int(self.idtolabels.get(self.v_ids[i])) < srcl :
                del ids[:]
                obj = it.next
                it2 = iter(obj.keys())
                obj2 = it2.next
                srcl = int(self.idtolabels.get(self.v_ids[i]))
                destl = int(self.idtolabels.get(obj2))
                new_e = int(obj.get(obj2))
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

                    if int(obj.get(obj2)) <= e :
                        if int(obj.get(obj2)) < e :
                            del ids[:]
                            destl = int(self.idtolabels.get(obj2))
                            new_e = int(obj.get(obj2))

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
                    destl = int(self.idtolabels.get(obj2))
                    sde.append(1, destl)

                m = dict()
                m[self.v_ids()[i]] = obj2

                ids.add(m)
        return new_e

    def fwd_intersect(self, P, evat1, evat2, cand_vat, is_fwd_chain, rmp_index, new_edge_state, gid, l2_eq):
        swap_vids = False # flag to denote if vids in evat_v2  should be swapped before appending to boolean
        l2_swap = False   # flag to denote if vids in v1 should be swapped before insertion to vat self occurs in the special case when l2_eq = 1
        v1 = 0
        v2 = 0
        v3 = 0
        v4 = 0
        i = 0
        j = 0
        k = 0
        offset_v1 = 0
        off = -1
        for i in range(0, len(evat1)):
            v1 = int((evat1[i]).keys()[0])
            v2 = int((evat1[i]).get(v1))

            for j in range(0, len(evat2)):
                v3 = int((evat2[j]).keys()[0])
                v4 = int(evat2[j].get(v3))
    
                if new_edge_state == 0: # both vertex labels of new edge are same
                    if l2_eq:
                        if v2 == v3: 
                            swap_vids=False
                            l2_swap=False
                        elif v2 == v4 :
                            swap_vids=True
                            l2_swap=False
                        elif v1 == v3:
                            swap_vids=False
                            l2_swap=True
                        elif v1 == v4 :
                            swap_vids=True
                            l2_swap=True
                        else:
                            continue

                    else:
                        if is_fwd_chain :
                            if v2 != v3:
                                if v2 != v4 :   # none of the vids in v2 matches
                                    continue
                                else:
                                    swap_vids = True

                            else:
                                swap_vids = False
                        else:
                            if v1 != v3:
                                if v1 != v4 :  # none of the vids in v2 matches
                                    continue
                                else:
                                    swap_vids = True
                            else:
                                swap_vids = False

                else:
                    if new_edge_state - 1 == 0:
                        swap_vids = False
                    if new_edge_state - 1 == 1:
                        swap_vids = True
                    if l2_eq :
                        if not swap_vids:
                            if v1 != v3 :
                                if v2 != v3:
                                    continue
                                else:
                                    l2_swap = False
                            else:
                                l2_swap = True
                        else:
                            if (v1 != v4):
                                if (v2 != v4):
                                    continue
                                else:
                                    l2_swap = False
                            else:
                                l2_swap = True
                    else:
                        if (is_fwd_chain):
                            if (swap_vids and v2 != v4):
                                continue
                            if (not swap_vids and v2 != v3):
                                continue
                        else:
                            if (swap_vids) :
                                return
                            if (v1 != v3):
                                continue


                if (not swap_vids):
                    m = dict()
                    m[v3] = v4

                    if not P.is_new_vertex_modified(v4, gid, offset_v1)
                        continue
                else:
                    m = dict()
                    m[v4] = v3
                    if not P.is_new_vertex_modified(v3, gid, offset_v1):
                        continue
                    
                if (rmp_index == 0):
                    if (self.Vsets.isEmpty()):
                        self.copy_vids_tid(P, gid, offset_v1)
                    elif self.Vsets.get(gid) == null:
                        self.copy_vids_tid(P, gid, offset_v1)
                    else:
                        self.copy_vids_hs(P, gid, offset_v1)
                    off +=1

                if (rmp_index > 0 and self.vat.isEmpty()):
                    self.copy_vats_entry(P, rmp_index, gid, l2_swap, i, offset_v1)
                    off +=1
                elif (rmp_index > 0):
                    self.copy_vats_entry(P, rmp_index, gid, l2_swap, i, offset_v1)
                    off +=1

                new_occurrence = dict()
                key = 0
                value = 0
                if not l2_eq :
                    if is_fwd_chain :
                        key = v2
                    else:
                        key = v1
                else:
                    if not l2_swap:
                        key = v2
                    else:
                        key = v1

                if swap_vids:
                    value = v3
                else:
                    value = v4

                new_occurrence[key] = value
                if not is_fwd_chain :
                    if (self.vat.containsKey(gid)):
                        self.vat.get(gid)[0].append(new_occurrence)
                        self.insert_vid(gid, off, key)
                        self.insert_vid(gid, off, value)
                    else:
                        l = []
                        l.append(new_occurrence)
                        l2 = []
                        m2 = dict()
                        l2.append(l)
                        m2[gid] = l2
                        self.vat[gid]= l2
                        self.insert_vid(gid, off, key)
                        self.insert_vid(gid, off, value)

                else:
                    if len(self.vat.get(gid)) == rmp_index :
                        l = []
                        l.append(new_occurrence)
                        self.vat.get(gid).append(l)
                        self.insert_vid(gid, off, key)
                        self.insert_vid(gid, off, value)
                    else:
                        (self.vat.get(gid))[rmp_index].append(new_occurrence)
                        self.insert_vid(gid, off, key)
                        self.insert_vid(gid, off, value)

                    
    def is_new_vertex_modified(self,vid, gid, offset):
        if self.Vsets.get(gid)[offset].contains(vid) :
            return False
        return True


    def vat_intersection(self, P, vat2):
        is_fwd_chain = False # flag to denote whether edge appended by intersection is at the root (which is when flag=0)
        cand_vat = []
        l2_eq = (len(self.v_ids)==3) and ((self.idtolabels.get(1))==(self.idtolabels.get(2))) # special case in evat intersection for L-2 with first edge with equal vertex labels
        new_edge_state=-1 # flag to denote if the new edge to be added has same labeled vertices, of the form A-A (flag=0) or is of the form  A-B (flag=1)
        #  or is not canonical at all, of the form B-A (flag=2) evat intersection needs to take self into account

        back_idx=-1
        rvid =(self.right_most_path[len(self.right_most_path)-1])
    	edge_vid=-1  # vid of the other vertex (other than rvid) connected to rvid as to form the new edge

        degree = len(self.adj_list.get(rvid))

        if degree>1 :
      		is_fwd=False  #last edge was fwd edge only if outdegree of last vid=1
    	else:
      		is_fwd=True

        if is_fwd:
            edge_vid=int(self.right_most_path[len(self.right_most_path)-2])

            if edge_vid==1:  # rvid is attached to the root
                is_fwd_chain=False
            else :
                is_fwd_chain=True

        else :
            edge_vid=int(((self.adj_list.get(rvid))[degree-1]).keys()[0])

			# now determine the index of edge_vid on rmp of candidate. self is used by back_intersect.
            # TO DO: self is currently a linear search through rmp, is there a more efficient way??

            for i in range(0, len(self.right_most_path)) :
                if int((self.right_most_path[i])) ==edge_vid :
                    back_idx=i
                    break

      		if back_idx==-1:
                 return

	    if is_fwd:
      		rmp_index=len(self.right_most_path)-2
        else:
            rmp_index=len(self.right_most_path)-1

        if (int(self.idtolabels.get(edge_vid))) == int(self.idtolabels.get(rvid)):
      	    new_edge_state=0
        else:
            if is_fwd:
				if int(self.idtolabels.get(edge_vid)) > int(self.idtolabels.get(rvid)) :
                    new_edge_state=2
                else:
                    new_edge_state=1
            else:
				if int(self.idtolabels.get(rvid)) > int(self.idtolabels.get(edge_vid))
        			new_edge_state=2
                else:
					new_edge_state=1
        		#new_edge_state=(self.idtolabels.get(rvid)> self.idtolabels.get(edge_vid)+1

		i=0
        j=0
        g1id=0
        g2id=0
        support=0
        get_val=0

        Pvatgid = []
        vat2gid = []

        for i1 in range(0,len(P.vat.keys())):
			Pvatgid.append(P.vat.keys()[i1])

		for i1 in range(0, len(vat2.keyS())) :
			vat2gid.append(vat2.keys()[i1])

		Pvatgid.sort()
        vat2gid.sort()

        while i<len(Pvatgid) and j< len(vat2gid) :
			g1id = Pvatgid.get(i)
			g2id = vat2gid.get(j)

			if g1id < g2id:
				i +=1
				continue
			if g1id > g2id :
				j +=1
				continue
			evat1 = []
			evat2 = []

			evat2 = vat2.get(g1id)[0]

			if not is_fwd:
				evat1=P.vat.get(g1id)[rmp_index-1]
            else :
                if is_fwd_chain:
					evat1=P.vat.get(g1id)[rmp_index-1]
                else:
					evat1=P.vat.get(g1id)[0]

			if is_fwd:
				fwd_intersect(P, evat1, evat2, cand_vat, is_fwd_chain, rmp_index, new_edge_state, g1id, l2_eq)
     		else
	  			back_intersect(P, evat1, evat2, cand_vat, new_edge_state, back_idx, g1id)
    		i++
			j++

	self.support = len(self.vat)

