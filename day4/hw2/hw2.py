import sys
import collections
import heapq

class Wikipedia:

    # Initialize the graph of pages.
    def __init__(self, pages_file, links_file):

        # A mapping from a page ID (integer) to the page title.
        # For example, self.titles[1234] returns the title of the page whose
        # ID is 1234.
        self.titles = {}

        # A set of page links.
        # For example, self.links[1234] returns an array of page IDs linked
        # from the page whose ID is 1234.
        self.links = {}

        # Read the pages file into self.titles.
        with open(pages_file, encoding='utf-8') as file:
            for line in file:
                (id, title) = line.rstrip().split(" ")
                id = int(id)
                assert not id in self.titles, id
                self.titles[id] = title
                self.links[id] = []
        print("Finished reading %s" % pages_file)

        # Read the links file into self.links.
        with open(links_file, encoding='utf-8') as file:
            for line in file:
                (src, dst) = line.rstrip().split(" ")
                (src, dst) = (int(src), int(dst))
                assert src in self.titles, src
                assert dst in self.titles, dst
                self.links[src].append(dst)
        print("Finished reading %s" % links_file)
        print()



    def find_most_popular_pages(self):
        old_page_rank = {} # 元のページランク p
        new_page_rank = {} # 更新後のページランク c
        converge = 0.001
        length = len(self.titles)

        for node in self.titles:
            old_page_rank[node] = 1
            new_page_rank[node] = 0

        sum_page_rank = sum(old_page_rank.values())

        diff = 100
        while diff > converge:
            diff = 0
            for node in self.titles:
                new_page_rank[node] += 0.15
                if not self.links[node]:
                    score = (old_page_rank[node] * 0.85) / length
                    for node in self.titles:
                        new_page_rank[node] += score
                else:
                    score = (old_page_rank[node] * 0.85) / len(self.links[node])
                    for child in self.links[node]:
                        new_page_rank[child] += score
            assert round(sum(new_page_rank.values())) == sum_page_rank

            for node in self.titles:
                diff += (old_page_rank[node] - new_page_rank[node]) ** 2
            if diff <= converge:
                break

            for node in self.titles:
                old_page_rank[node] = new_page_rank[node]
                new_page_rank[node] = 0

        top_pages = heapq.nlargest(10, old_page_rank.items(), key=lambda x: x[1])
        for id, score in top_pages:
            print(f'ID: {id}, popular: {score}')


        pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: %s pages_file links_file" % sys.argv[0])
        exit(1)

    wikipedia = Wikipedia(sys.argv[1], sys.argv[2])
    # wikipedia.find_longest_titles()
    # wikipedia.find_most_linked_pages()
    # wikipedia.find_shortest_path("渋谷", "小野妹子")
    wikipedia.find_most_popular_pages()