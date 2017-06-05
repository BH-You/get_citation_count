import csv


def main():
    doc_list = list()
    with open('title') as f:
        reader = csv.reader(f, delimiter='\t')
        for id, title in reader:
            doc_list.append((int(id), title))

    countlist = list()
    with open('cluster_num__count') as f:
        reader = csv.reader(f)
        for id, cit in reader:
            if cit == '':
                countlist.append((int(id), None))
            else:
                countlist.append((int(id), int(cit)))

    newcountlist = list()

    for paperid, cit in countlist:
        print(paperid, cit)
        if cit is None:
            title = get_title(paperid, doc_list)
            raw_input = int(input("Citation count of " + '"' + title + '": '))
            cit = int(raw_input)

        newcountlist.append((paperid, cit))

    with open('cluster_num__count_final', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(newcountlist)


def get_title(paperid, doc_list):
    for id, title in doc_list:
        if id == paperid:
            return title
    else:
        raise IndexError

if __name__ == '__main__':
    main()