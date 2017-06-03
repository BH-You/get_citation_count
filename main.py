import csv
import os
import subprocess


def main():
    count_list = dict()
    with open('title') as f:
        for line in f:
            cluster_num, title = line.split(' ', 1)
            if cluster_num not in count_list:
                num_citation = google_scholar_search(title[:-1])
                count_list[cluster_num] = num_citation
                with open('citation_count', 'a+') as w:
                    writer = csv.writer(w)
                    writer.writerow([cluster_num, num_citation])
    print(len(count_list))


def google_scholar_search(title):
    proc = subprocess.run(['python3', 'scholar.py', '--csv-header', '-s', '"' + title + '"'], check=True,
                          stdout=subprocess.PIPE)
    return get_citation_count(proc.stdout.decode('utf-8'), title)


def get_citation_count(stdout, title):
    reader = csv.reader(stdout.splitlines(), delimiter="|")
    header = next(reader)
    title_idx = header.index('title')
    num_citations_idx = header.index('num_citations')
    title_citation_list = list()
    for doc in reader:
        title_citation_list.append((doc[title_idx], doc[num_citations_idx]))
        if doc[title_idx].lower() == title.lower():
            return doc[num_citations_idx]
    else:
        for i in range(len(title_citation_list)):
            print(i, title_citation_list[i])
        try:
            num = int(input("Choose proper title for " + '"' + title + '": '))
            title_citation = title_citation_list[num]
            return title_citation[1]
        except:
            print(num, "is not integer in range")
            return None


if __name__ == '__main__':
    if not os.path.isfile('scholar.py'):
        subprocess.run(['curl', '-O', 'https://raw.githubusercontent.com/ckreibich/scholar.py/master/scholar.py'])

    main()
