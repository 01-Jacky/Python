def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)

def greet_me(job='123', time='999', **kwargs,):
    if kwargs:
        for key, value in kwargs.items():
            print("%s == %s" %(key,value))
    print(job)
    print(time)

# test_var_args('yasoob','python','eggs','test')
greet_me(time='456',job='111', name="yasoob", thing="the thing")

