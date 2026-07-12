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

def extract_image(out_dir: str, src, filename: str, page_range: list):
    imgcnt = 0
    for r in page_range:
        for i in range(r[0],r[1]+1):
            if i < src.page_count:
                page = src[i]
                img_list = page.get_images()
                for img_info in img_list:
                    img = src.extract_image(img_info[0])
                    imgout = open(Path(out_dir) / "{n}_{cnt}.{ext}".format(n=filename, cnt=imgcnt+1 ,ext=img["ext"]), "wb+")
                    imgout.write(img["image"])
                    imgout.close()
                    imgcnt += 1
    print("Extracted {} images.".format(imgcnt))

if __name__ == "__main__":
    # 1. get output directory
    if len(sys.argv)>1:
        out_dir = sys.argv[1]
    else:
        out_dir = input(">>> Output directory: ")
    
    # 2. get source path
    if len(sys.argv)>2:
        src_path = sys.argv[2]
    else:
        src_path = input(">>> Source path: ")
    
    # 3. get page range
    if len(sys.argv)>3:
        range_str = sys.argv[3]
    else:
        range_str = input(">>> Pages to extract: ")

    src = pymupdf.open(src_path)
    if range_str=="":
        page_range = [(0,src.page_count)]
    else:
        page_range = str_to_range(range_str)
    filename = Path(src_path).stem
    extract_image(out_dir,src,filename,page_range)