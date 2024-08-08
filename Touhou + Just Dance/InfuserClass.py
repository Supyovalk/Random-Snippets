import pickle
class infuser:
    #Should be devided into A Infuser Interface after the first draft class is complete
    #language : [[["A","B","C"],3],[["D"],2]] ->fusion of form (abc)(abc)(abc)(d)(d) [(A,B,C,D,D) is in language but (D,D,D,D,D) or (A,B,C) aren't]
    #data : {(langauge vector set):fusionobj}
    #Language word Aliases
    #Unqiue Value flag
    def __init__(self):
        self.language=[]
        self.data=[]
    def __init__(self, language, data,force_order_flag=True):
        self.language = language
        self.data = data
        self.order = force_order_flag
    def checklanguagevector(self,vector:set) -> bool:
        
        pass
    def load_infuser(self,filepath):
        #load infuser from a file using pickle
        pass
    def save_infuser(self,filepath):
        #save infuser into a file using pickle
        pass
    def modify_fusion(self,combivector,fusionobj,override_flag=False):
        #add/change fusion
        pass
    def remove_fusion(self,combivector):
        #add/change fusion
        pass
    def get_participates_fusion(self,participates):
        #get all the fusions that have all the participates
        pass
    def __len__(self):
        #return count of fusions
        pass
    def transform_all_obj(self,trans_func):
        #transform all the obj for each into a new one
        pass
s=infuser([],[])
print(s.attempt)