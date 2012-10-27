'''
Jimmy John - jim@codeeval.com - 10/26/2012


LRU Cache

Caches are a key element in scaling a system. One popular form of cache is called a Least Recently Used Cache (http://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used). Your task is to implement a cache that can be tested against a series of inputs. These actions should define an API you use for the cache object.

Your cache should store simple key/value strings of length up to 10 characters. It should also have a customizable upper bound to the number of keys that can be stored in the cache at any time. You do not have to be thread safe.

Possible Inputs:

BOUND    :  Set the upper bound. If the cache size is currently greater than this number, then extra entries must be removed following the LRU policy

SET   :  Set the value of this key

GET   :  Get the value of this key and prints to stdout.

PEEK   :  Gets the value of the key but does not mark it as being used. Prints the value to standard out.

DUMP  :  Prints the current state of the cache as a list of key/value pairs in alphabetical order by key.

 

Input Format:

First line of input contains an integer N,the number of commands.

The following N lines each describe a command.

Note: The first command will always be BOUND.

Output Format:

Print the appropriate outputs for GET , PEEK and DUMP commands. In case for GET/PEEK command if the key does not exist in the cache just output the string "NULL"(quotes are for clarity).

 

Sample Input

8
BOUND 2
SET a 2
SET b 4
GET b
PEEK a
SET c 5
GET a
DUMP

Sample Output

4
2
NULL
b 4
c 5

Constraints:

Total number of lines in input will be no more than 1,000,000(10^6)

Note: There may be DUMP commands scattered throughout the input file.

'''

import copy

class LRU(object):

    def __init__(self, max_size):
        #keeps the actual data
        self.cache = {}
        self.max_size = max_size
        #keeps track of age. head is MRU, tail is LRU
        self.tracker = []

    def _update_tracker(self, key):
        if self.tracker:

            if self.tracker[0] == key:
                return
            else:
                try:
                    self.tracker.remove(key)
                except ValueError:
                    pass

                self.tracker.insert(0, key)

        else:
            self.tracker.append(key)

    def set(self, key, value):
        if len(self.cache.keys()) >= self.max_size:
            del_key = self.tracker.pop()
            del self.cache[del_key]

        self.cache[key] = value
        self._update_tracker(key)


    def get(self, key, mark=True):
        try:
            self.cache[key]
            if mark:
                self._update_tracker(key)
            return self.cache[key]
        except KeyError:
            return 'NULL'

    def trim(self, max_size):
        self.max_size = max_size

        if len(self.cache.keys()) <= max_size:
            return
        else:
            diff = len(self.cache.keys()) - max_size
            for i in range(diff):
                del_key = self.tracker.pop()
                del self.cache[del_key]

    def dump(self):
        sorted_items = []
        tracker_copy = copy.deepcopy(self.tracker)
        tracker_copy.sort()
        for key in tracker_copy:
            sorted_items.append((key, self.cache[key]))

        return sorted_items


def main():

    lru = None
    output = []
    num_of_cmds = raw_input()
    for i in range(int(num_of_cmds)):
        input_data = raw_input()
        try:
            cmd, parameters = input_data.split(' ', 1)
        except ValueError:
            cmd = input_data

        if cmd == 'BOUND':
            max_size = int(parameters)
            if not lru:
                lru = LRU(max_size)
            else:
                lru.trim(max_size)
        else:
            if not lru:
                raise Exception, 'Incorrect input, no BOUND command seen as yet...'

            if cmd == 'SET':
                lru.set(parameters.split(' ')[0], parameters.split(' ')[1])
            elif cmd == 'GET':
                output.append(lru.get(parameters))
            elif cmd == 'PEEK':
                output.append(lru.get(parameters, False))
            elif cmd == 'DUMP':
                data = lru.dump()
                for item in data:
                    output.append('%s %s' % (item[0],item[1]))

    for element in output:
        print element



if __name__ == '__main__':
    main()

