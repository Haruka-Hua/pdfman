# this script extracts certain pages from a pdf
import pymupdf
import re
import sys

range_pattern = r"^\d+(?:-\d+)?(?:,\d+(?:-\d+)?)*$"

def append_pages(out, src_path, page_range):
    src = pymupdf.open(src_path)
    for r in page_range:
        out.insert_pdf(src, from_page = r[0], to_page = r[1])
    
def str_to_range(raw_str):
    ranges = []
    ranges_str = raw_str.split(',')
    for s in ranges_str:
        if '-' in s:
            index = s.split('-')
            lindex = int(index[0])-1
            rindex = int(index[1])-1
            ranges.append((lindex,rindex))
        else:
            index = int(s)-1
            ranges.append((index,index))
    return ranges
            

if __name__ == "__main__":
    outpath = sys.argv[1]
    out = pymupdf.open()
    index = 2
    while index < len(sys.argv):
        src_path = sys.argv[index]
        index += 1
        page_range = [(-1,-1)]
        if index < len(sys.argv):
            if re.match(range_pattern, sys.argv[index], flags=0):
                page_range = str_to_range(sys.argv[index])
                index += 1
        append_pages(out, src_path, page_range)
    out.save(outpath)