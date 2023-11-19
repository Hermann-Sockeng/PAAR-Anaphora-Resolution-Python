#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:17:29 2023

@author: Hermann Sockeng,   Email: hermannsockeng@gmail.com
"""
#import re


def find_pa(tokenized_sent):
            
    """
        

        Parameters
        ----------
        tokenized_sent : list
            List of sentence obtained from the tokenized text.
        tokenized_words : list
           List of words & pontuation obtained from the tokenized text.

        Returns
        -------
        Set of PA in the sentence.
    """
    
    Sixty_PA = {'daran', 'hieran', 'woran' ,'darauf', 'hierauf', 'worauf', 'daraus',
                'hieraus', 'woraus', 'dabei', 'hierbei', 'wobei', 'dadurch', 'hierdurch',
                'wodurch', 'dafür', 'hierfür', 'wofür', 'dagegen', 'hiergegen', 'wogegen',
                'dahinter', 'hierhinter', 'wohinter', 'darin','hierin', 'worin', 'darein',
                'hierein', 'worein', 'damit', 'hiermit', 'womit', 'danach', 'hiernach',
                'wonach', 'daneben', 'hierneben', 'woneben', 'darüber', 'hierüber', 'worüber',
                'darum', 'hierum', 'worum', 'darunter', 'hierunter', 'worunter', 'davon',
                'hiervon', 'wovon', 'davor', 'hiervor', 'wovor', 'dazu', 'hierzu', 'wozu',
                'dazwischen', 'hierzwischen', 'wozwischen'}

    Sixty_PA_Cap = {pa.capitalize() for pa in Sixty_PA}

    Sixty_PA = Sixty_PA.union(Sixty_PA_Cap)
    
    pa_set = set(tokenized_sent).intersection(Sixty_PA)
    pa_list = list(pa_set)
    
    return pa_list
    

    
            
        