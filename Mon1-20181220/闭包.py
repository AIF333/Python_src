

def out(x):
    print("hahahaha")
    def inner():
        print("I  am  ", str(x))
    return inner


func=out(3)
func()
