# this script extracts certain pages from a pdf
import pymupdf
import re
import sys

range_pattern = r"^\d+(?:-\d+)?(?:,\d+(?:-\d+)?)*$"

def append_pages(out, src_path: str, page_range: list):
    """
    Append pages from `src_path` with range `page_range` to the output file.
    """
    src = pymupdf.open(src_path)
    for r in page_range:
        out.insert_pdf(src, from_page = r[0], to_page = r[1])
    
def str_to_range(raw_str: str):
    """
    Convert source page range string to a list of tuples `(lindex, rindex)`.
    """
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
    out = pymupdf.open()

    # 1. get output path
    if(len(sys.argv) >= 2):
        outpath = sys.argv[1]
    else:
        outpath = input(">>> Output path: ")

    # 2. get source list
    if(len(sys.argv) >= 3):
        source_list = sys.argv[2:]
    else:
        source_list = input(">>> PDF source: ").split()
    index = 0

    while index < len(source_list):
        src_path = source_list[index]
        index += 1
        page_range = [(-1,-1)]
        if index < len(source_list):
            if re.match(range_pattern, source_list[index], flags=0):
                page_range = str_to_range(source_list[index])
                index += 1
        append_pages(out, src_path, page_range)
    out.save(outpath)