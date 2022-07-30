import os, platform
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            import BD
        elif bit == '32bit':
            import BD32
Run()