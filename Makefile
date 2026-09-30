# Requires Tweego with the SugarCube 2.36.1 story format installed (not vendored in this repo).
.PHONY: build validate check-js sim clean

build:
	mkdir -p dist
	tweego -f sugarcube-2 -o dist/index.html src/

validate:
	python3 tools/validate.py

check-js:
	python3 tools/extract_js.py
	node --check build/check.js

sim: check-js
	node tools/sim.js

clean:
	rm -rf build dist
