blog:
	pelican -t built-texts -o . -s pelicanconf.py
all:
	blog
# investigate what needs to go here
clean:
	rm *.html
