import glob

def make_link(url, content):
	return "<a href='%s'/>%s</a>" % (url, content)

@tag
def menu(sections):
	sections = [ read_sections(fname) for fname in glob.glob("*.w") ]
	sections.sort(key=lambda s: int(s["position_in_menu"]))
	lines = [ make_link(output_filename(s["__filename__"]), s["title"]) for s in sections ]
	return "\n".join(lines)
