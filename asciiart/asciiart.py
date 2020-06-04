#!/usr/bin/python3

class MegaNimation():
    """Basic animations generators"""

    def moving_object(self, obj, path=80):
        try:
            where_am_i = 0
            while where_am_i <= path and where_am_i + len(obj) <= path:
                to_print = "{}{}".format(" "*where_am_i, obj)
                yield to_print
                where_am_i += 1

        except AttributeError:
            print("Path must be integer, obj must be str")
    
    def moving_object_in_ether(self, obj, ether, path=80):
        #remplissage de l'ether
        background = ""
        while len(background) < path:
            background += ether
        
        # Shrink background if > path
        background = background[:path]

        # yield de l'ether
        yield background
        # yield du message
        i = 0
        while i <= path and i + len(obj) <= path:
            start = background[0:i]
            mid = obj
            end = background[i+1+len(obj):]
            yield start + mid + end
            i += 1

    def waiving(self, obj='_.~"~.', path=80):
        i = 0
        mess = ""

        while i <= path and i + len(obj) <= path:
            new_char = obj[i%len(obj)]
            mess += new_char
            yield mess
            i += 1
    
    def scrolling(self, obj, path):
        before = ""
        background = r"."*path

        yield background
        i = 0
        while i <= path:
            if i >= len(obj):
                # obj complètement sorti
                before = background[0:i]
                text = obj
            else:
                text = obj[len(obj)-i:]

            before = background[0:i-len(obj)]
            after = background[(len(before)-1 + len(text)-1):] 

            yield before + text + after
            i += 1
        