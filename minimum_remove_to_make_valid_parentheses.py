arr = [ "(ABC(B)))", "(A(BC(B))", "(AB(C(B)))"]

# first remove access closed string
# if excess open brancket then remove them

for _arr in arr:
    processed_str = ""
    final_result = ""
    open_count = 0

    # remove excess closed bracket
    for char in _arr:
        if char == '(':
            open_count = open_count + 1;
        elif char == ')':
            if open_count > 0:
                open_count = open_count - 1;
            else:
                # excess closed string
                continue

        processed_str = processed_str + char

        
    # remove excess open bracket from behind, since begining open brackert handles closed brancket
    for char in processed_str[::-1]:
        if char == '(' and open_count > 0:
            open_count = open_count - 1;
            continue
            
        final_result = final_result + char

    print "For array: %s"%_arr
    print "Cleaned Arrat: %s"%final_result[::-1]
    print "Min remove count: %d"%(len(_arr) - len(final_result))
