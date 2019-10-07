# PF-Prac-12
def generate_sentences(subjects, verbs, objects):
    # start writing your code here
    sentence_list = []
    for i in range(len(subjects)):

        for j in range(len(verbs)):
            for k in range(len(objects)):
                sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
                sentence_list.append(sentence)

    return sentence_list

subjects = ["I", "You"]
verbs = ["love", "play"]
objects = ["Hockey", "Football"]
print(*generate_sentences(subjects, verbs, objects))