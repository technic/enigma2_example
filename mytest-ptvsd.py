from __future__ import print_function
import ptvsd

if __name__ == "__main__":
    print("mytest-ptvsd: Enable debugger")
    ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)
    print("mytest-ptvsd: Waiting debugger...")
    ptvsd.wait_for_attach()
    print("mytest-ptvsd: Debugger connected")
    import mytest  # start enigma2
 