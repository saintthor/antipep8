# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:49:18 2016

@author: thor
"""   

import tokenize


def Convert( path ):
    "convert py source from pep8 to pretty style"
    tokens = []

    with file( path ) as f:
        LastToken = ( -1, '', ( 0, 0 ), ( 0, 0 ), '' )
        delta = 0

        for tk in tokenize.generate_tokens( f.readline ):
            # print tk, delta
            NewDelta = 0
            head = tk[:2]
            if head == ( 4, '\n' ):
                delta = 0
            elif head == ( 51, '(' ):
                if LastToken[:2] == ( 51, '(' ):
                    delta -= 1
                NewDelta = 1
            elif head == ( 51, ')' ):
                if LastToken[:2] == ( 51, '(' ):
                    delta -= 1
                elif LastToken[:2] != ( 51, ')' ):
                    delta += 1
            elif head == ( 51, '{' ):
                NewDelta = ( 1, 0 )[LastToken[:2] == ( 51, '{' )]
            elif head == ( 51, '}' ):
                delta += ( 1, -1 )[LastToken[:2] == ( 51, '{' )]
            elif head in (( 51, '=' ), ( 51, '==' )) and LastToken[3][1] == tk[2][1]:
                delta += 1

            if LastToken[:2] in (( 51, '=' ), ( 51, '==' )) and LastToken[3][1] == tk[2][1]:
                delta += 1

            if tk[2][1] - LastToken[3][1] > 1:
                if delta > 0:
                    delta -= 1
                NewDelta = 0

            LastToken = tk

            if delta != 0:
                tk = head + (( tk[2][0], tk[2][1] + delta ), ( tk[3][0], tk[3][1] + delta ), tk[4] )
            delta += NewDelta
            tokens.append( tk )

    with file( path, 'w' ) as f:
        LastPos = LastLine = 0
        for tk in tokens:
            if tk[2][0] > LastLine:
                LastPos = 0
                LastLine = tk[2][0]
            # print LastPos, tk
            f.write( ' ' * ( tk[2][1] - LastPos ))
            f.write( tk[1] )
            LastPos = tk[3][1]


if __name__ == '__main__':
    #Convert( 'AntiPEP8.py' )
    import os
    for path in filter( None, os.popen( "find -name '*.py'" ).read().split( '\n' )):
        Convert( path )
        print path, ' is pretty now.'
