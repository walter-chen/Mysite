# -*- coding: utf-8 -*-
from dashboard.models import Project

class MetaData():
    source = ''
    coverage_scene = []

    avg_positive_income = 0.0
    avg_negative_income = 0.0
    def MetaData(self, source, coverage_scene, positive_income, negative_income):
        self.source = source
        self.coverage_scene = coverage_scene
        self.positive_income = positive_income
        self.negative_income = negative_income
        self.avg_positive_income = float(sum(positive_income))/(len(positive_income)*0.0000001)
        self.avg_negative_income = float(sum(negative_income))/(len(negative_income)*0.0000001)
        
    def __str__(self):
        return 'MetaData'+ self.source  
class DoubleArray(): 
    coverageScene = ''
    
