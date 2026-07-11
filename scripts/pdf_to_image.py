import pymupdf
from pathlib import Path
import sys

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

def src_to_image(out_dir: str, src, filename: str, page_range: list):
    for r in page_range:
        for i in range(r[0], r[1]+1):
            if i < src.page_count:
                page = src[i]
                pix = page.get_pixmap()
                out_path = Path(out_dir) / "{n}_{i}.png".format(n=filename, i=i+1)
                pix.save(out_path)

if __name__=="__main__":
    # get output directory
    if len(sys.argv)>1:
        out_dir = sys.argv[1]
    else:
        out_dir = input(">>> Output directory: ")

    # get source file path
    if len(sys.argv)>2:
        src_path = sys.argv[2]
    else:
        src_path = input(">>> Source file: ")
    src = pymupdf.open(src_path)
    filename = Path(src_path).stem

    # get page range
    if len(sys.argv)>3:
        range_str = sys.argv[3]
    else:
        range_str = input(">>> Pages to be converted: ")

    src = pymupdf.open(src_path)
    if range_str=="":
        page_range = [(0,src.page_count)]
    else:
        page_range = str_to_range(range_str)
    
    src_to_image(out_dir, src, filename, page_range)