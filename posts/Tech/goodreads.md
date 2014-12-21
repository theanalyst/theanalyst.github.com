Title: 2014 Year in Books, using Goodreads, pandas & Hy
Date: 2014-12-21
Tags: Hy, Goodreads, Pandas, Kindle
Author: Abhishek L
Category: Tech

As 2014 is coming to a close, I thought it would be a nice time to
review the year as far as reading was concerned. Since I track the
books I read using Goodreads, I felt it would be an interesting
experiment to see some numbers from Goodreads. Though Goodreads
provides an api, it doesn't seem to be directly useful to get some
numbers from a user account (I could be wrong here). Fortunately, an
export to csv option is provieded in the account which helps in our
favor.

For any kind of data analysis in python, [pandas][1] is a brilliant
library. Also it does most of the heavy lifting as far as processing
csv files are concerned. Since [Hy][2] works wherever python works, I
thought it would be an interesting experiment to use Hy to parse the
data.

To start with reading csv is a simple call to pandas' `read_csv`
function.

    :::hylang
	(import pandas
        [numpy :as np]
        [matplotlib.pyplot :as plt]
        [seaborn :as sns])

    (defn parse-csv [filepath kwargs]
	  (apply pandas.read_csv [filepath] kwargs))

Now taking out only the column's we're interested in & filtering out
the data from only a particular year can be done by

	:::hylang
    (defn books-in-year [dataframe year]
	  (let [[day1 (fn [y] (+ (str y) "-01-01"))]]
        (slice (. dataframe ix) (day1 year) (day1 (inc year)))))

`ix` returns the index of dataframe, since we'll be indexing by date
read, this allows us to select the required range, by simply selecting
a date range from the beginning of the year to the next year.

[1]: http://pandas.pydata.org
[2]: http://hylang.org
