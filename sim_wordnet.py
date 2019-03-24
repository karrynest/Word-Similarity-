#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, csv
import nltk

from nltk.corpus import wordnet
from nltk.corpus import wordnet_ic

from setting import *

nltk.download('wordnet')
nltk.download('wordnet_ic')

def sim_wordnet(wordpairs, filename):
    brown_ic = wordnet_ic.ic('ic-brown.dat')
    semcor_ic = wordnet_ic.ic('ic-semcor.dat')

    WORDNET_DIR=os.path.join(RESULT_DIR, "wordnet")

    pathfile=open(os.path.join(WORDNET_DIR,"path_"+filename),'w',newline='')
    pathwriter=csv.writer(pathfile)

    wupfile=open(os.path.join(WORDNET_DIR,"wup_"+filename),'w',newline='')
    wupwriter=csv.writer(wupfile)

    lchfile=open(os.path.join(WORDNET_DIR,"lch_"+filename),'w',newline='')
    lchwriter=csv.writer(lchfile)

    resfile=open(os.path.join(WORDNET_DIR,"res_"+filename),'w',newline='')
    reswriter=csv.writer(resfile)

    jcnfile=open(os.path.join(WORDNET_DIR,"jcn_"+filename),'w',newline='')
    jcnwriter=csv.writer(jcnfile)

    linfile=open(os.path.join(WORDNET_DIR,"lin_"+filename),'w',newline='')
    linwriter=csv.writer(linfile)

    resultfiles=[pathfile, wupfile, lchfile, resfile, jcnfile, linfile]
    resultwriters=[pathwriter, wupwriter, lchwriter, reswriter, jcnwriter, linwriter]

    for wordpair in wordpairs:
        synsets1=wordnet.synsets(wordpair[0])
        synsets2=wordnet.synsets(wordpair[1])

        path_sim = -100
        wup_sim = -100
        lch_sim = -100

        res_sim = -100
        jcn_sim = -100
        lin_sim = -100


        for tmpword1 in synsets1:
            for tmpword2 in synsets2:
                if tmpword1.pos() == tmpword2.pos():
                    try:
                        path_sim=max(path_sim,tmpword1.path_similarity(tmpword2))
                    except Exception as e:
                        print(tmpword1, tmpword2)
                        print("path: "+str(e))

                    try:
                        wup_sim=max(wup_sim,tmpword1.wup_similarity(tmpword2))
                    except Exception as e:
                        print(tmpword1, tmpword2)
                        print("wup: "+str(e))

                    try:
                        lch_sim=max(lch_sim,tmpword1.lch_similarity(tmpword2))
                    except Exception as e:
                        print(tmpword1, tmpword2)
                        print("lch: "+str(e))

                    try:
                        res_sim=max(res_sim,tmpword1.res_similarity(tmpword2,brown_ic))
                    except Exception as e:
                        print(tmpword1, tmpword2)
                        print("res: "+str(e))

                    try:
                        jcn_sim=max(jcn_sim,tmpword1.jcn_similarity(tmpword2,brown_ic))
                    except Exception as e:
                        print(tmpword1, tmpword2)
                        print("jcn: "+str(e))

                    try:
                        lin_sim=max(lin_sim,tmpword1.lin_similarity(tmpword2,semcor_ic))
                    except Exception as e:
                        print(tmpword1, tmpword2)
                        print("lin: "+str(e))

        path_result=(wordpair[0], wordpair[1], path_sim)
        wup_result=(wordpair[0], wordpair[1], wup_sim)
        lch_result=(wordpair[0], wordpair[1], lch_sim)
        res_result=(wordpair[0], wordpair[1], res_sim)
        jcn_result=(wordpair[0], wordpair[1], jcn_sim)
        lin_result=(wordpair[0], wordpair[1], lin_sim)

        results=[path_result, wup_result, lch_result, res_result, jcn_result, lin_result]

        for i in range(len(resultwriters)):
            writer = resultwriters[i]
            writer.writerow(results[i])

    for resultfile in resultfiles:
        resultfile.close()
