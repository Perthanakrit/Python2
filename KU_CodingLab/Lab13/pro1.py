def namelist(names):
    if len(names) < 1:
        return ""
    txt = ""
    if len(names) >= 2:
        names.insert(len(names) - 1,"&")
        txt = ", ".join(names)
        txt = txt.replace(", &,", " &")
    else:
        txt = names[0]
        
    return txt

print( namelist(['Peter']) )
print( namelist(['Bart', 'Viola']) )
print( namelist(['Bart', 'Viola', 'Peter', 'Nostel']) )
print( namelist([]) == '' )