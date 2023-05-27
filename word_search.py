# Write your solution here
def find_words(search_term: str):
    words = []
    with open("words.txt") as file:
        for word in file:
            words.append(word.strip())


    found = []
    if search_term[-1] == "*":
        for word in words:
            if word.startswith(search_term[:-1]):
                found.append(word)

    elif search_term[0] == "*":
        for word in words:
            if word.endswith(search_term[1:]):
                found.append(word)

    elif "." in search_term:

        for word in words:
            is_found = True
            i = 0
            if len(word) != len(search_term):
                continue
            for char in search_term:
                if char != ".":
                    if char == word[i]:
                        i +=1
                        continue
                    else:
                        is_found = False
                        break
                elif char == ".":
                    i += 1
            if is_found:
                found.append(word)
    else:
        if search_term in words:
            found.append(search_term)

    return found


