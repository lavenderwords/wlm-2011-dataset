#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 emijrp <emijrp@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
    table-files.py: it generates the table for files, with the following fields...
    
    file_id|file_name|file_user_name|file_date_taken|file_date_upload|file_size|file_width|file_height|file_monument_id|file_country
"""

import csv
import json
import re
import urllib

templateid_r = [
    re.compile(ur"(?im)\{\{\s*Béns[ _]Andorra\s*\|\s*(?:1\s*=\s*)?([^\}]+)\s*\}\}"), 
    re.compile(ur"(?im)\{\{\s*(?:Doo|Denkmalgeschütztes[ _]Objekt[ _]Österreich)\s*\|\s*(?:1\s*=\s*)?([^\}]+)\s*\}\}"), 
    re.compile(ur"(?im)\{\{\s*Onroerend[ _][Ee]rfgoed\s*\|\s*(?:1\s*=\s*)?([^\}]+)\s*\}\}"), 
    re.compile(ur"(?im)\{\{\s*Fredet[ _]bygning\s*\|\s*(?:1\s*=\s*)?([^\}]+)\s*\}\}"), 
    re.compile(ur"(?im)\{\{\s*Kultuurimälestis\s*\|\s*(?:1\s*=\s*)?([^\}]+)\s*\}\}"), 
    re.compile(ur"(?im)\{\{\s*(?:Mérimée|Merimee)\s*\|\s*(?:type\s*=\s*[^\|]*\|)?(?:1\s*=\s*)?([^\}]+)\s*\}\}"), 
    re.compile(ur"(?im)\{\{\s*Monument[ _]Hungary\s*\|\s*(?:1\s*=\s*)?([^\}]+)\s*\}\}"), 
    re.compile(ur"(?im)\{\{\s*Rijksmonument\s*\|\s*(?:1\s*=\s*)?([^\}]+)\s*\}\}"), 
    re.compile(ur"(?im)\{\{\s*Monument[ _][Nn]orge\s*\|\s*(?:1\s*=\s*)?([^\}]+)\s*\}\}"), 
    re.compile(ur"(?im)\{\{\s*Zabytek\s*\|\s*(?:1\s*=\s*)?([^\}]+)\s*\}\}"),
    re.compile(ur"(?im)\{\{\s*WLM-PT\s*\|\s*(?:1\s*=\s*)?([^\}\|]+)\s*(?:\|[^\}]*)?\s*\}\}"), 
    re.compile(ur"(?im)\{\{\s*Monument[ _]istoric\s*\|\s*(?:1\s*=\s*)?([^\}\|]+)\s*(?:\|[^\}]*)?\s*\}\}"), 
    re.compile(ur"(?im)\{\{\s*(?:Cultural[ _]Heritage[ _]Russia|Historic[ _]landmark)\s*\|\s*(?:(?:1|id)\s*=\s*)?([^\}\|]+)\s*[\}\|]"), 
    re.compile(ur"(?im)\{\{\s*BIC\s*\|\s*(?:1\s*=\s*)?([^\}\|]+)\s*[\}\|]"), 
    re.compile(ur"(?im)\{\{\s*(?:BBR|Byggnadsminne)\s*\|\s*(?:1\s*=\s*)?([^\}\|]+)\s*[\}\|]"), 
    re.compile(ur"(?im)\{\{\s*Kulturdenkmal[ _]Bremen\s*\|\s*([^\}]+)\s*\}\}"), 
]

f = open('table-files.csv', 'w')
f.write('file_id|file_name|file_user_name|file_date_taken|file_date_upload|file_size|file_width|file_height|file_monument_id|file_country\n')
f.close()

c = 0
query1 = 'http://commons.wikimedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=Category:Images_from_Wiki_Loves_Monuments_2011&gcmlimit=500&gcmnamespace=6&prop=imageinfo&iiprop=timestamp|user|size|url|metadata&iilimit=100&format=json&gcmcontinue='
query2 = 'http://commons.wikimedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=Category:Images_from_Wiki_Loves_Monuments_2011&gcmlimit=500&gcmnamespace=6&prop=revisions&rvprop=content&format=json&gcmcontinue='
gcmcontinue = 'file||'
while gcmcontinue:
    json_data1 = urllib.urlopen(query1+gcmcontinue)
    json_data2 = urllib.urlopen(query2+gcmcontinue)
    data1 = json.load(json_data1)
    data2 = json.load(json_data2)
    gen1 = ''
    if data1.has_key('query'):
        gen1 = data1['query']['pages']
    gen2 = ''
    if data2.has_key('query'):
        gen2 = data2['query']['pages']
    for pageid, properties in gen1.items():
        c += 1
        file_id = pageid
        file_name = properties["title"]
        file_user_name = properties["imageinfo"][-1]["user"]
        
        file_date_taken = ''
        if properties["imageinfo"][-1].has_key("metadata") and properties["imageinfo"][-1]["metadata"]:
            for meta in properties["imageinfo"][-1]["metadata"]:
                if meta["name"] == 'DateTimeOriginal' and meta["value"] and re.search(ur"\d\d\d\d:\d\d:\d\d \d\d:\d\d:\d\d", meta["value"]):
                    #print meta["value"]
                    file_date_taken = '%sT%sZ' % (re.sub(':', '-', meta["value"].split(' ')[0]), meta["value"].split(' ')[1])
                    break
        file_date_upload = properties["imageinfo"][-1]["timestamp"]
        file_size = properties["imageinfo"][-1]["size"]
        file_width = properties["imageinfo"][-1]["width"]
        file_height = properties["imageinfo"][-1]["height"]
        file_monument_id = ''
        #no template for luxemburg, switzerland ?
        for templateid in templateid_r:
            m = re.findall(templateid, gen2[pageid]["revisions"][0]["*"])
            if m:
                file_monument_id = m[0].strip()
                file_monument_id = re.sub(ur"[\n\r]", ur"", file_monument_id) #no newlines
                file_monument_id = re.sub(ur"(?m)(^|\|)\s*\d\s*=\s*", ur"|", file_monument_id) #no 1 = , 2  =, 3 =
                file_monument_id = re.sub(ur"\s*\|\s*", ur";", file_monument_id) #replace for Merimee and Zabytek templates that sometimes has more than 1 value...
                break
        file_country = '' #country codes http://commons.wikimedia.org/w/index.php?title=Template:Wiki_Loves_Monuments_2011&action=edit
        #|lu|1/1897}} http://commons.wikimedia.org/w/index.php?title=File:0_Clervaux_-_Ch%C3%A2teau_(1).JPG&action=edit
        m = re.findall(ur"(?i){{\s*Wiki[ _]Loves[ _]Monuments[ _]2011\s*\|\s*(?:1\s*=\s*)?(?:\{\{lc:)?([^\}\|]+)\s*[\|\}]", gen2[pageid]["revisions"][0]["*"])
        if m:
            file_country = m[0].lower().strip()
        elif re.findall(ur"(?i)\{\{\s*Selected[ _]for[ _]WLM[ _]2011[ _]CH\s*\}\}", gen2[pageid]["revisions"][0]["*"]):
            file_country = u'ch'
        #properties["imageinfo"][-1]["url"]
        
        print c, file_name, file_monument_id, file_country
        f = csv.writer(open('table-files.csv', 'a'), delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        f.writerow([file_id, file_name.encode('utf-8'), file_user_name.encode('utf-8'), file_date_taken, file_date_upload, file_size, file_width, file_height, file_monument_id.encode('utf-8'), file_country.encode('utf-8')])
    
    json_data1.close()
    json_data2.close()
    if data1.has_key('query-continue'):
        gcmcontinue = data1['query-continue']['categorymembers']['gcmcontinue'] #the same for both queries
    else:
        gcmcontinue = ''
