#!/usr/bin/env python3
"""Extract the Story JavaScript passage from the twee into build/check.js, with stubs for Node.
Usage: python3 tools/extract_js.py [path-to-twee]  (run from the repo root)"""
import re, sys, os
P = sys.argv[1] if len(sys.argv) > 1 else 'src/silent-bell.twee'
t = open(P, encoding='utf-8').read()
m = re.search(r':: Story JavaScript \[script\]\n(.*?)(?=\n:: )', t, re.S)
if not m:
    sys.exit('no ":: Story JavaScript [script]" passage found in ' + P)
STUB = 'var setup={};var State={variables:{}};function random(a,b){return a+Math.floor(Math.random()*(b-a+1));}'
os.makedirs('build', exist_ok=True)
open('build/check.js', 'w', encoding='utf-8').write(STUB + '\n' + m.group(1))
print('wrote build/check.js')
