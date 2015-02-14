blog:
	pelican -t built-texts -o . -s pelicanconf.py
all:
	blog
clean:
	rm *.html  # investigate what exactly needs to be done here
