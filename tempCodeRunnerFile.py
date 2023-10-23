def calc():
    global place
    place = "Rom"
    name = "Le"

    print ("place in global"), "plac" in globals() 
    print ("place in local"), "plac" in locals()
    print ("name in global"), "nam" in globals() 
    print ("name in local"), "nam" in locals()
    return

place = "Berli"
print (place)
calc()