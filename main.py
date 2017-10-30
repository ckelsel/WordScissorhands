# -*- coding: utf-8 -*-


import sys
import io
import filestream

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python main.py filename"
    else:
        stream = filestream.filestream(sys.argv[1])
        list = stream.get_words(True)
        
        save_file = open("out.txt", "w")
        for word in list:
            save_file.write(word + "\n")
        save_file.close()
