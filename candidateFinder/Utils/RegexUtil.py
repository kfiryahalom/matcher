import difflib

class RegexUtil:

    # Util that Gives socre by most relevant text match to pattren
    # Example Result for title 'Softwear Engineer'
    #           
    #Softwear Engineer    1.000
    #QA Engineer          0.643
    #Front-End            0.231
    #Manual QA            0.154
    #VP Product           0.148
    #VP R&D               0.087
    #CFO                  0.000
    def get_match_ratio(list, pattren):
        s = difflib.SequenceMatcher()

        s.set_seq2(pattren)
        full = []
        for job_title in list:
            s.set_seq1(job_title)
            full.append((s.ratio(), job_title))
        full.sort(reverse=True)
        for score, job_title in full:
            print ("{:20} {:.3f}".format(job_title, score))
        
        return full

    def get_top_match_ratio(list, pattren):
        res = RegexUtil.get_match_ratio(list, pattren)[0][0]
        return res
