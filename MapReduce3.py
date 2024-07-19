from mrjob.job import MRJob
from mrjob.step import MRStep

class WordCounter(MRJob):

    def configure_args(self):
        super(WordCounter, self).configure_args()

    def mapper_init(self):
        pass

    def mapper(self, _, line):
        words = line.strip().split()
        for word in words:
            yield (word.lower(), 1)

    def combiner(self, word, counts):
        yield (word, sum(counts))

    def reducer(self, word, counts):
        yield (word, sum(counts))

if __name__ == '__main__':
    WordCounter.run()
