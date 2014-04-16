import sys

def usage():
        print "USAGE:"
        print sys.argv[0],"<delim>","<match>","<filename>"
        print " "
        print "This script looks for <match> in blocks surrounded by beginning of file, <delim> and EOF"
        print "Tip: this script generates delimiters for ease of use. (#####################)"

def grep(delim, str, file):
        buf=""
        found=False
        for line in file:
                if delim in line:
                        if found:
                                yield buf
                        buf=""
                        found=False
                else:
                        if str in line:
                                found=True
                        buf+=line
        if found:
                yield buf

if len(sys.argv)>3:
        file=None
        try:
                file = open(sys.argv[-1],"r")
        except:
                print "Error opening",sys.argv[-1]
                exit()
        #
        for block in grep(sys.argv[1],sys.argv[2],file):
                print block,"#####################"
else:
        usage()


