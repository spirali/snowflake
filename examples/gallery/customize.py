
def preprocess(filename, sections):
    files = [ s.strip() for s in sections["images"].split("\n") if s.strip() != "" ]

    for n, ifile in enumerate(files):
        n += 1
        sections = {}
        sections["img"] = ifile
        sections["name"] = "Image %i" % n
        sections["prev"] = ('<a href="img%i.html">Prev</a>' % (n-1)) if n > 1 else ""
        sections["next"] = ('<a href="img%i.html">Next</a>' % (n+1)) if n < len(files) else ""
        yield ("img%i.html" % n, sections)
