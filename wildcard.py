import json

def wildcardProcessing(query) :
    
    final_list = []

    parts = query.split("*")

    if len(parts) == 3:
        case = 4
    elif parts[1] == '':
        case = 1
    elif parts[0] == '':
        case = 2
    elif parts[0] != '' and parts[1] != '':
        case = 3

    if case == 4:
        if parts[0] == '':
            case = 1
    
    
    f = open('permute.json')
    permuterm = json.load(f)
    f.close()

    def prefix_match(term, prefix):
        term_list = []
        for tk in term.keys():
            # if tk.startswith(prefix):
            #     term_list.append(term[tk])
            if tk.startswith(prefix):
                # print(prefix, tk)
                if term[tk] not in term_list:
                    term_list.append(term[tk])
        return term_list


    if case == 1:
        query = parts[0]
    elif case == 2:
        query = parts[1] + "$"
    elif case == 3:
        query = parts[1] + "$" + parts[0]
    elif case == 4:
        queryA = parts[2] + "$" + parts[0]
        queryB = parts[1]

    def intersection(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    if case != 4:
        final_list = prefix_match(permuterm,query)
    elif case == 4:
    # queryA Z$X
        term_listA = prefix_match(permuterm,queryA)
        #print(term_list)

        
    # queryB Y
        term_listB = prefix_match(permuterm,queryB)

        final_list = intersection(term_listA, term_listB)

    return final_list

