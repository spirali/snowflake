import datetime
import os, os.path
import sys

TEMPLATE = "page.html"
OUTPUT_DIR = "out/"
DATE_TIME_FORMAT = "%Y-%m-%d"

def read_file(filename):
    with open(filename,"r") as f:
        return f.read()

def read_file_lines(filename):
    with open(filename,"r") as f:
        return list(f)

def write_file(filename, content):
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    with open(filename, "w") as f:
        f.write(content)

def init_sections():
    sections = {}
    sections["today"] = datetime.datetime.now().strftime(DATE_TIME_FORMAT)
    return sections

def parse_sections(lines):
    sections = init_sections()
    section = []
    for line in lines:
        if line.startswith("##"):
            section = []
            sections[line[2:].strip()] = section
        else:
            section.append(line)
    return sections

def replace_sections(template, sections):
    for section in sections:
        tag = "{{" + section + "}}"
        template = template.replace(tag, "".join(sections[section]))
    return template

def process_file(filename):
    if filename.endswith(".w"):
        basename = filename[:-2]
    else:
        basename = filename
    lines = read_file_lines(filename)
    template = read_file(TEMPLATE)
    output = replace_sections(template, parse_sections(lines))
    write_file(os.path.join(OUTPUT_DIR, basename + ".html"), output)

def main():
    if len(sys.argv) == 1:
        print "usage: webbuild <file>"
    else:    
        for filename in sys.argv[1:]:
            print "Processing ", filename, "..."
            process_file(filename)

if __name__ == '__main__':
    main()

