import datetime
import os, os.path
import sys

TEMPLATE = "page.html"
OUTPUT_DIR = "out/"
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"

custom_tags = []

# Decorators -----------------------------------------
def tag(function):
    custom_tags.append((function.__name__, function))
    return function

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

def init_sections(sections):
    sections["today"] = datetime.datetime.now().strftime(DATE_FORMAT)
    sections["now"] = datetime.datetime.now().strftime(TIME_FORMAT)
           
    for tag_name, tag_function in custom_tags:
        sections[tag_name] = tag_function(sections)

    return sections

def parse_sections(lines, init = True):
    sections = {}
    if init:
        sections = init_sections(sections)

    section = []
    name = "__nosection__"
    for line in lines:
        if line.startswith("##"):
            sections[name] = "".join(section).strip()
            section = []
            name = line[2:].strip()
        else:
            section.append(line)

    sections[name] = "".join(section)
    sections[name].strip()
    return sections

def replace_sections(template, sections):
    for section in sections:
        tag = "{{" + section + "}}"
        template = template.replace(tag, "".join(sections[section]))
    return template

def read_sections(filename, init = False):
    lines = read_file_lines(filename)
    sections =  parse_sections(lines, init)
    sections[ "__filename__" ] = filename
    return sections

def output_filename(filename):
    if filename.endswith(".w"):
        basename = filename[:-2]
    else:
        basename = filename
    return basename + ".html"

def process_file(filename):
    template = read_file(TEMPLATE)
    output = replace_sections(template, read_sections(filename, True))
    write_file(os.path.join(OUTPUT_DIR, output_filename(filename)), output)

def main():
    if len(sys.argv) == 1:
        print "usage: snowflake <file>"
    else:    
        for filename in sys.argv[1:]:
            print "Processing ", filename, "..."
            process_file(filename)

if __name__ == '__main__':
    if os.path.isfile("customize.py"):
        execfile("customize.py")
    main()
