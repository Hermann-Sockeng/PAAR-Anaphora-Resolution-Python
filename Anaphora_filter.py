#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""                     
                 
Created on Wed Jun  7 09:17:29 2023

@author: Hermann Sockeng,   Email: hermannsockeng@gmail.com
"""
from termcolor import colored


class anaphora_filter:
    
    
    
    """
        

        Parameters
        ----------
        tokenized_sent : string
            Sentence obtained from the tokenized text.
        tokenized_words : list
           List of words & pontuation obtained from the tokenized text.

        Returns
        -------
        List of PA tokens.

    """
    def __init__(self, sent_tok, word_tok):
        self.sent_tok = sent_tok
        self.word_tok = word_tok
 
#texthier = 'Beim Museumsfest und Internationalen Museumstag konnten die zahlreichen Besucher sich hiervon überzeugen.' 
#texth = 'Hiervon entfielen 83,3 Prozent auf Schmutzwasser sowie 16,7 Prozent auf Niederschlag.'         
    def Da_or_Hier_PA_classifier(self,
                                 Da_pa,
                                 sent,
                                 antecedent,
                                 last_sent,
                                 Wsart_list = ['dass','ob','wer',
                                               'wen','wem','wessen',
                                               'wo','wohin','woher',
                                               'was','wie','wie lange', 
                                               'wie oft','wie viel',
                                               'warum','weshalb','wieso', 
                                               'weswegen','wozu','welche']):
        '''
        

        Parameters
        ----------
        Da_pa : string
            da or hier pronominal adverb in the sentence sent.
        sent : list of string
            current sentence.
        antecedent : string
            Antecedent of the sentence sent.
        last_sent : string
            Last sentence in the text.
        Wsart_list : list , optional
            DESCRIPTION. The default is ['dass','ob','wer',                                               'wen','wem','wessen',                                               'wo','wohin','woher',                                               'was','wie','wie lange',                                               'wie oft','wie viel',                                               'warum','weshalb','wieso',                                               'weswegen','wozu','welche'].

        Returns
        -------
        Da or Hier PA classification (anaphora or cataphora)

        '''

        


        ana_color = 'cyan'
        cata_color = 'black'
        ana_pa = colored(Da_pa, ana_color, attrs=['reverse', 'blink'])
        cata_pa = colored(Da_pa, cata_color, attrs=['reverse', 'blink'])
        text_antecedent = colored(antecedent, ana_color, attrs=['reverse', 'blink'])
        anaphora = colored("anaphora", ana_color, attrs=['reverse', 'blink'])
        cataphora = colored("cataphora", cata_color, attrs=['reverse', 'blink'])
        
        #print(text)
        wordtok = self.word_tok
        # Position of the Da-hier in the word tokenized sentence
        Da_pa_index = wordtok.index(Da_pa)

        # number of tokens betwen the pronominal adverb and ","  & ":"
        
        wsart_set = set(Wsart_list)
        token_after_pa = wordtok[Da_pa_index+1:-1]
        
        if ',' in token_after_pa:
            n_tokens_pa_coma  = len(wordtok[Da_pa_index+1 : wordtok[Da_pa_index:].index(',')])
        else:
            pass
                
        
        if ':' in token_after_pa:
            n_tokens_pa_two_pt = len(wordtok[Da_pa_index+1 : wordtok[Da_pa_index:].index(':')])   
        else:
            pass
            

        wsart = list(wsart_set.intersection(set(token_after_pa)))
        n_elt = len(wsart)
        
       # if ":" in token_after_pa
        if (n_elt != 0 and len(wordtok[Da_pa_index+1 : wordtok.index(wsart[0])]) <= 4) or  (',' in token_after_pa and n_tokens_pa_coma < 2) or (':' in token_after_pa and n_tokens_pa_two_pt < 2):
               
        #for wsart in Wsart_list:
            #if wsart in wordtok[Da_pa_index+1:] and len(wordtok[Da_pa_index+1 : wordtok.index(wsart)]) <= 4:
            print(f"The Da-/Hier- PA {cata_pa} in the sentence:\n {[sent]} is a {cataphora}.\n \n")
        else:
            
            if antecedent != last_sent:
                print(f"The Da-/Hier- PA {ana_pa} in the sentence:\n {[sent]} is an {anaphora} with antecedent the sentence:\n {text_antecedent} \n \n")
            else:
                print(f"The Da-/Hier- PA {ana_pa} in the sentence:\n {[sent]} is an {anaphora} without specific antecedent. \n \n")
                
            

#textd = "Menschen müssen wieder mehr Sorge dafür tragen, dass der Körper Entspannung findet", meint Psychotherapeut Soljan.             
    def Wo_PA_classifier(self, Wo_pa, sent):
        """
        

        Parameters
        ----------
        Wo_pa : string
            The Wo-PA Pronominal Adverb (PA).

        Returns
        -------
        Classified Wo-PA as Anaphora or Cataphora in part of the Pronominal Anaphora Averbial Resolution.

        """
        ana_color = 'cyan'
        cata_color = 'black'
        color_ana_pa = colored(Wo_pa, ana_color, attrs=['reverse', 'blink'])
        color_cata_pa = colored(Wo_pa, cata_color, attrs=['reverse', 'blink'])
        anaphora = colored("anaphora", ana_color, attrs=['reverse', 'blink'])
        cataphora = colored("cataphora", cata_color, attrs=['reverse', 'blink'])
        
        sentence = self.word_tok
        Wo_pa_position = sentence.index(Wo_pa)
        # All what precede the PA
        antecedent = [sentence[:Wo_pa_position]]
        
        # Method to untokenized the antecedent of the wo-pa
        def untokenize(data):
            for tokens in data:
                yield ' '.join(tokens)


    #data = [['this', 'is', 'a', 'sentence'], ['this', 'is', 'a', 'sentence', '2']]
        untokenized_antecedent = list(untokenize(antecedent))
        untok_ant = colored(untokenized_antecedent, ana_color, attrs=['reverse', 'blink'])
        if sentence[0] == Wo_pa:
            print(f"The Wo-PA {color_cata_pa} in the sentence: {[sent]} is a {cataphora}.\n \n")
        elif sentence[Wo_pa_position-1] == ',':
            print(f"The Wo_PA {color_ana_pa} in the sentence: {[sent]} is an {anaphora} with antecedent:\n {untok_ant}\n \n")
        else:
            pass
            #print(f"Something wrong with PA in the sentence: {[sent]}! Make sure that this sentence is right!\n \n")

           
                
        
        
                    
        