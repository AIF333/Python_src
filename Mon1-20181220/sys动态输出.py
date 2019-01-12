import sys,time

for i in range(8):
    # sys.stdout.write('\r%s' %('#'*i))
    # sys.stdout.flush()
    print('\r%s' %('#'*i),end='',flush=True)
    time.sleep(0.2)