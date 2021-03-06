#!/usr/bin/env python
#===================================================================================
#description     : Methods for features exploration                                =
#author          : Shashi Narayan, shashi.narayan(at){ed.ac.uk,loria.fr,gmail.com})=                                    
#date            : Created in 2014, Later revised in April 2016.                   =
#version         : 0.1                                                             =
#===================================================================================


class Feature_Nov27:

    def get_split_feature(self, split_tuple, parent_sentence, children_sentence_list, boxer_graph):
        # Calculating iLength
        #iLength = boxer_graph.calculate_iLength(parent_sentence, children_sentence_list)
        # Get split tuple pattern
        split_pattern = boxer_graph.get_pattern_4_split_candidate(split_tuple)
        #split_feature = split_pattern+"_"+str(iLength)
        split_feature = split_pattern
        return split_feature

    def get_drop_ood_feature(self, ood_node, nodeset, main_sent_dict, boxer_graph):
        ood_word = boxer_graph.extract_oodword(ood_node, main_sent_dict)
        ood_position = boxer_graph.nodes[ood_node]["positions"][0] # length of positions is one
        span = boxer_graph.extract_span_min_max(nodeset)
        boundaryVal = "false"
        if ood_position <= span[0] or ood_position >= span[1]:
            boundaryVal = "true"
        drop_ood_feature = ood_word+"_"+boundaryVal
        return drop_ood_feature

    def get_drop_rel_feature(self, rel_node, nodeset, main_sent_dict, boxer_graph):
        rel_word = boxer_graph.relations[rel_node]["predicates"]
        rel_span = boxer_graph.extract_span_for_nodeset_with_rel(rel_node, nodeset)
        drop_rel_feature = rel_word+"_"
        if len(rel_span) <= 2:
            drop_rel_feature += "0-2"
        elif len(rel_span) <= 5:
            drop_rel_feature += "2-5"
        elif len(rel_span) <= 10:
            drop_rel_feature += "5-10"
        elif len(rel_span) <= 15:
            drop_rel_feature += "10-15"
        else:
            drop_rel_feature += "gt15"
        return drop_rel_feature
        
    def get_drop_mod_feature(self, mod_cand, main_sent_dict, boxer_graph):
        mod_pos = int(mod_cand[0])
        mod_word = main_sent_dict[mod_pos][0]
        #mod_node = mod_cand[1]
        drop_mod_feature = mod_word
        return drop_mod_feature 

class Feature_Init:

    def get_split_feature(self, split_tuple, parent_sentence, children_sentence_list, boxer_graph):
        # Calculating iLength
        iLength = boxer_graph.calculate_iLength(parent_sentence, children_sentence_list)
        # Get split tuple pattern
        split_pattern = boxer_graph.get_pattern_4_split_candidate(split_tuple)
        split_feature = split_pattern+"_"+str(iLength)
        return split_feature

    def get_drop_ood_feature(self, ood_node, nodeset, main_sent_dict, boxer_graph):
        ood_word = boxer_graph.extract_oodword(ood_node, main_sent_dict)
        ood_position = boxer_graph.nodes[ood_node]["positions"][0] # length of positions is one
        span = boxer_graph.extract_span_min_max(nodeset)
        boundaryVal = "false"
        if ood_position <= span[0] or ood_position >= span[1]:
            boundaryVal = "true"
        drop_ood_feature = ood_word+"_"+boundaryVal
        return drop_ood_feature

    def get_drop_rel_feature(self, rel_node, nodeset, main_sent_dict, boxer_graph):
        rel_word = boxer_graph.relations[rel_node]["predicates"]
        rel_span = boxer_graph.extract_span_for_nodeset_with_rel(rel_node, nodeset)
        drop_rel_feature = rel_word+"_"+str(len(rel_span))
        return drop_rel_feature
        
    def get_drop_mod_feature(self, mod_cand, main_sent_dict, boxer_graph):
        mod_pos = int(mod_cand[0])
        mod_word = main_sent_dict[mod_pos][0]
        #mod_node = mod_cand[1]
        drop_mod_feature = mod_word
        return drop_mod_feature 

