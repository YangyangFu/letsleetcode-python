build:
	rm -rf letsleetcode/_build
	jb build letsleetcode/

publish:
	ghp-import -n -p -f letsleetcode/_build/html