# -*- coding: utf-8 -*-

import pdb
class filestream:
    def __init__(self, filename):
        self.fd = open(filename, 'r')
        self.list = []

        self.stream_index = None
        self.stream_length = None
        

    def is_char(self, char):
        lower = char.lower()
        c = lower[0]
        if c >= 'a' and c <= 'z':
            return True
        return False

    def get_one_word(self, stream):
        assert(stream != None)
        index = self.stream_index

        while (True):
            find = self.is_char(stream[index])
            if (find):
                break

            # end of stream
            if self.stream_length == (index + 1):
                return None
            index += 1


        # test, we find t at index 0
        word_begin = index

        while (True):
            find = self.is_char(stream[index])
            if (not find):
                break

            # end of stream
            if self.stream_length == (index + 1):
                return None
            index += 1

        # 'test test', we find ' ' at index 5
        word_end = index

        self.stream_index = index

        return stream[word_begin:word_end]

    def init_stream(self, stream):
        self.stream_index = 0
        self.stream_length = len(stream)

    def get_words(self, strip = False):
        stream = self.fd.read()
        stream = stream.lower()
        self.init_stream(stream)

        word = self.get_one_word(stream)
        while word != None:
            if (strip):
                if len(word) != 1:
                    if self.list.count(word) == 0:
                        self.list.append(word)
            else:
                self.list.append(word)
            word = self.get_one_word(stream)
        
        return self.list

        


