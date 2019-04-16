import sys, os

f = open(sys.argv[1], 'r')

for line in f:
	line = line.strip('\n')
	[a, b] = line.split('\t')
	#os.system('mv {0} {1}.md'.format(a, b))
	print '- {0}: {1}.md'.format(a.split('.md')[0], b)
f.close()
