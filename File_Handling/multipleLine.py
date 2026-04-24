l = ["hello\n", "this is an example\n", "of\n", "writing multiple lines\n"]

f = open("multipleLine.txt", 'w')
f.writelines(l)
f.close()
