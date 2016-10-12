# -*- coding: utf-8 -*-
from dashboard.models import Project

class TowerCounter():
    district_list = ['思明区', '湖里区']
    roomType_list = ['RRU拉远', '一体化机柜']
    context = {}
    def result(self):
        for district in self.district_list:
            for roomType in self.roomType_list:
                temp = Project.objects.filter(district_id=district, room_type=roomType)
                self.context['test'][roomType] = temp
        return self.context    
                
                
