# import sys
class readdb():

    def __init__(self, textfile):
        self.textfile=textfile

    def readdb(self):
        with  open(self.textfile) as _text:
            lines=_text.readlines()
        _string=''.join(lines)
        lines=[]
        for lin in _string.split("\n"):
            lines.append(lin.split(" "))
        return lines



# if __name__=='__main__':
#         read = readdb("/home/saurabh/Desktop/MIRAGE_version1/sample_data/input_new.txt")
#         read.readdb()