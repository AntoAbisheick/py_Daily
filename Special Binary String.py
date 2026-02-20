s = "11011000110010"

def v(string):
    if not string:
        return ""
        
    i = 0
    count = 0
    g = []
    
    for j in range(len(string)):
        if string[j] == "1":
            count += 1
        else:
            count -= 1
            
        if count == 0:
            a = string[i+1:j]
            b = v(a)
            g.append("1" + b + "0")
            i = j + 1
            
    g.sort(reverse=True)
    return ''.join(g)

print(v(s))


