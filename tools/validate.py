#!/usr/bin/env python3
"""Validate silent-bell.twee: links, macro balance, JS syntax, companion/NPC references.
Usage: python3 tools/validate.py [path-to-twee]  (run from the repo root)"""
import re, sys, subprocess, tempfile, os
P = sys.argv[1] if len(sys.argv) > 1 else 'src/silent-bell.twee'
t = open(P, encoding='utf-8').read()
errs = []
names = set(re.findall(r'^:: (.+?)(?: \[[^\]]*\])?$', t, re.M))
pats = [r'\[\[(?:[^\]|]*\|)?([^\]]+)\]\]', r'<<goto "([^"]+)">>', r'win:"([^"]+)"',
        r'<<move "([^"]+)"', r'joinlink "[^"]+" "[^"]+" "([^"]+)"', r'\$checkpoint to "([^"]+)"']
for p in pats:
    for x in re.findall(p, t):
        if x not in names: errs.append('missing passage: ' + x)
for nm, body in re.findall(r'^:: (.+?)(?: \[[^\]]*\])?\n(.*?)(?=\n\n:: |\Z)', t, re.S | re.M):
    for mac in ['if', 'for', 'link', 'capture', 'widget']:
        o = len(re.findall(r'<<%s[ >`]' % mac, body)); c = len(re.findall(r'<</%s>>' % mac, body))
        if o != c: errs.append('macro imbalance in %s: <<%s>> %d open, %d close' % (nm, mac, o, c))
    if '**' in body: errs.append('markdown bold in ' + nm + ' (use <b>)')
    if re.search(r'"cha"|"str"|"dex"|"con"|"int"', body): errs.append('old attribute code in ' + nm)
js = re.search(r':: Story JavaScript \[script\]\n(.*?)(?=\n:: )', t, re.S).group(1)
f = tempfile.NamedTemporaryFile('w', suffix='.js', delete=False); f.write(js); f.close()
r = subprocess.run(['node', '--check', f.name], capture_output=True, text=True)
if r.returncode: errs.append('JS syntax: ' + r.stderr[:300])
os.unlink(f.name)
comp = set(re.findall(r'^  (\w+): \{ name:', js.split('setup.npcs')[0], re.M))
npcs = set(re.findall(r'^  (\w+): \{ name:', js.split('setup.npcs')[1], re.M)) if 'setup.npcs' in js else set()
for x in re.findall(r'(?:talklink) "(\w+)"', t):
    if x not in npcs: errs.append('talklink to unknown NPC: ' + x)
for x in re.findall(r'joinlink "(\w+)"', t):
    if x not in comp: errs.append('joinlink to unknown companion: ' + x)
for hub, ids in re.findall(r'(\w+): \[((?:"\w+",? ?)+)\]', js.split('setup.hubRoster')[1].split('};')[0]):
    for i in re.findall(r'"(\w+)"', ids):
        if i not in comp: errs.append('hubRoster %s has unknown companion %s' % (hub, i))
print('%d passages' % len(names))
print('\n'.join(errs) if errs else 'OK: no problems found')
sys.exit(1 if errs else 0)
