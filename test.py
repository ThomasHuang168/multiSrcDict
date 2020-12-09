import re, os

def splitCantoSylTone(Phone):
    return re.findall(r"([a-z]+)([1-6])", Phone)

from multiSrcDict import multiSrcDict

from multiSrcDict.dict_util import load_dict, line2KeyValue_tab, line2KeyValue_space, line2KeyValue_tab_before_space, line2KeyValue_tab_before_slash, search_by_char

base_path = "test"
_dict_n2L = os.path.join(base_path, "Dictionary", "number2LETTER")
_dict_p2l = os.path.join(base_path, "Dictionary", "punctuation2letter")

dicts = {
    "n2L" : load_dict(_dict_n2L, line2KeyValue_tab_before_slash, start_from_line=0),
    "p2l" : load_dict(_dict_p2l, line2KeyValue_tab_before_space, start_from_line=0),
}
from datetime import datetime
now =  datetime.now()
date_time = now.strftime("%Y%m%d_%H%M%S_")
LD = multiSrcDict(dicts, {"n2L": search_by_char, "p2l": search_by_char},out_stat_name=os.path.join(base_path, "records", "{}multi_dict".format(date_time)))

def translate(word):
    jyutping = LD.translate(word)
    jyutping_list = jyutping.split("-")
    jyutping_result = list()
    for j_i, j_ in enumerate(jyutping_list):
        jyutping_result.append(j_)
    return "".join(jyutping_result)

def main():
    string2transcribed = "12 2 3 4 789456 ,. , ? /. ?."
    transcribeList = string2transcribed.split(" ")
    for w in transcribeList:
        t_w = translate(w)
        if None is not t_w:
            print (t_w + "\n")

if __name__=="__main__":
    main()
