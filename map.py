# public void map(NullWritable key, Text value, OutputCollector<Text, BytesWritable> output, Reporter reporter) throws IOException
# 			{
# 				FSDataInputStream currentStream
#     			        BufferedReader currentReader
# 				FileSystem fs
# 				Text map_key = new Text()
# 				Text map_value = new Text()
# 				Path path = new Path(value.toString())
# 				fs = path.getFileSystem(conf)
# 				currentStream = fs.open(path)
#       			currentReader = new BufferedReader(new InputStreamReader(currentStream))
#
#
# 				Util_functions func1 = new Util_functions()
# 				func1.readDB_VAT_L1map(currentReader)

#from pyspark import SparkContext as sc
import MR_CannonicalCode
import MR_Pattern
import FSM_
from MR_Serialize import MR_Serialize
from MRStats import MRStats
def map():
    func1 = FSM_.util()
    func1.reappendb("/home/saurabh/Desktop/input_new1.txt")
    Serial = dict()
    for i in range(len(func1.freq_pats)):
        serial = MR_Serialize()
        serial.pattern = func1.freq_pats[i]
        # print func1.l1vat.get(func1.freq_pats[i].getCan_code()).keys()
        serial.pattern.support = len(func1.l1vat.get(func1.freq_pats[i].getCan_code()).keys())
        serial.pattern.vat = (func1.l1vat.get(func1.freq_pats[i].getCan_code()))
        serial.l1map_v2 = func1.l1map_v2
        serial.l1vat = func1.l1vat
        Serial[func1.freq_pats[i].getCan_code()] = serial

        # print serial.l1map_v2, serial.l1vat, serial.pattern.support, serial.pattern.vat
    return Serial

def mapperminer(serial):
    for k,v in serial.iteritems():
        func1 =FSM_.util()
        print "key, ", k , "value ", v
        print "v.l1vat", v.l1vat
        func1.l1vat = v.l1vat
        print "vl1map_v2", v.l1map_v2
        func1.l1map_v2 = v.l1map_v2
        P = v.pattern
        func1.generate_candidate(P)
        mapperminerouput=dict()
        print "freq_pats", func1.freq_pats
        for i in range(len(func1.freq_pats_hadoop)):
            if len(func1.freq_pats_hadoop[i].can_cod) == len(P.can_cod):
                continue

            key1 = func1.freq_pats_hadoop[i].getCan_code()
            Serial_ = MR_Serialize()
            Serial_.pattern = func1.freq_pats_hadoop[i]
            Serial_.l1map_v2 = func1.l1map_v2
            Serial_.l1vat = func1.l1vat
            sup = int(Serial_.pattern.support)
            # print " mapper miner ", sup, Serial_.l1vat
            mapperminerouput[key1] = (Serial_, sup)
        # print mapperminerouput
        func1.l1map_v2.clear()
        func1.l1vat.clear()
        func1.check_unique.clear()
        return mapperminerouput

def reducerminer(mapperoutput, minsup, mrstats):
    reduceroutput=dict()
    for k, v in mapperoutput.iteritems():
        support = 0
        support+=v[1]
        # print "support ", support, "min", minsup
        if support>= minsup:
            reduceroutput[k]=v[0]
            mrstats.NUMBER_OF_PATTEN_EXTENDED +=1
            mrstats.NUMBER_OF_PATTEN += 1
    # print "reducer miner ", reduceroutput
    return reduceroutput

if __name__ == '__main__':
    # print "runing fsm"
    mrstats = MRStats()
    intialoutput = map()
    iteration = 0
    minsup=1
    reducerinput = dict()
    mapperinput = dict()
    print  "initial ", intialoutput
    while True:
        if iteration==0:
            reducerinput = mapperminer(intialoutput)
            mapperinput = reducerminer(reducerinput, minsup, mrstats)
        else:
            print "mapper input ", iteration, reducerinput
            reducerinput = mapperminer(mapperinput)
            mapperinput = reducerminer(reducerinput, minsup, mrstats)
        if mrstats.NUMBER_OF_PATTEN_EXTENDED == 0:
            break
        mrstats.NUMBER_OF_PATTEN_EXTENDED = 0
        iteration+=1
        print "iteration ", iteration, mrstats.NUMBER_OF_PATTEN

