
So the key thing to note is that the file name is the id of the document, i.e. DOCID,

so the schema you set up, ie. should put the filename (without extension) as the docid, then you can extract out the title (if the page has one),

if you can extract the base url, then put that into source. Don’t worry about the date and time.

For the content field,  you have a number of options: (1) dump in all the text in the html page.
or (2) parse the page and extract out the important blocks of text, ie. the useful information, not all the guff (headers/footers, ads, etc).

Do (1) first, then you can try something like : http://infolab.stanford.edu/~prasen9/sac05.pdf
it is likely that someone has already implemented similar algos.