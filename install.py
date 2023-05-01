#!/usr/bin/env python3
from pathlib import Path
STEVE=Path(__file__).absolute().parent

if not STEVE==Path.home()/'.__STEVE__':
    print( 'can install only to ~/.__STEVE__' )
    exit()

MAGIC='#magic_python_98745'

def fix(name):
    target=Path.home()/name
    proxy=STEVE/('.dots/dot%s' % name)
    target.touch()
    proxy.touch()

    head=[]
    head.append( 'export STEVE=%s' % STEVE )
    head.append( 'source %s' % proxy )
    length = max( map(len,head) ) + 5
    head = [ line.ljust( length ) + MAGIC for line in head ]

    body = target.read_text().split('\n')
    body = [line for line in body if line.find(MAGIC) == -1 ]
    text = '\n'.join(head + body)
    target.write_text(text)

    print( 'updated %s' % target )

fix('.bashrc')
fix('.profile')

