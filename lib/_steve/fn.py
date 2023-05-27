#!/usr/bin/env python3
from pathlib import Path
import argparse

def walk(folder : Path, depth : int):
    for path in folder.glob('*'):
        yield path
        if path.is_dir() and not depth==0:
            yield from walk(path, depth-1)

