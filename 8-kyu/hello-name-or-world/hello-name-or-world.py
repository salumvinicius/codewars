 
def hello(name):
    try:
        if name == "":
        return "Hello, World!"
​
        else:
            return "Hello, " + name.title() + "!"
    except:
        return "Hello World!"