import os, platform, time
print('\n\x1b[1;37m[•] Checking Update...');time.sleep(0.5)
os.system('git pull')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            print("\x1b[1;92m[•] Congratulations ! Your Device Support this Tools")
            print('[•] Join Over Facebook Group First')
            os.system('xdg-open https://facebook.com/groups/351076900316263/')
            import PAK
        elif bit == '32bit':
            print("\n\x1b[1;92m[•] Congratulations ! Your Device Support this Tools")
            print('[•] Join Over Facebook Group First')
            os.system('xdg-open https://facebook.com/groups/351076900316263/')
            import PAK32
        else:
            exit('\033[1;31m[×] Connection Error')
Run()
