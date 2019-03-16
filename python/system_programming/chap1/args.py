import sys

print("argc=%s" % len(sys.argv))

for i, arg in enumerate(sys.argv):
    print("arg[%d]=%s" % (i, arg))
