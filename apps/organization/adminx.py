__author__ = 'Ting'
__date__ = '2018/1/29 16:55'

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'image', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
