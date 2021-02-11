import ptvsd

if __name__ == "__main__":
    print "mytest-ptvsd: Enable debugger"
    ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)
    print "mytest-ptvsd: Waiting debugger..."
    ptvsd.wait_for_attach()
    print "mytest-ptvsd: Debugger connected"

    # start enigma2
    # use execfile instead of import, because of import lock:
    # https://blog.sqreen.com/freeze-python-str-encode-threads/
    execfile('/usr/lib/enigma2/python/mytest.py')
