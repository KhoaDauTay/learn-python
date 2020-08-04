def div_num(a,b):
    try:
        return a//b
        print(div_num(2,0))
    except BaseException as be:
        print('[Error]',be)
    finally:
        print('After try/except finished')