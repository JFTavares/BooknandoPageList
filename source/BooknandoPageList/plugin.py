#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Plugin for Sigil. Its adds page list using the plugin of inDesign BooknandoPageNum.
# This plugin was create by civodulab (ludo.bal62@gmail.com) and modified by JFTavares - Booknando Livros (@JFTavares)
# it is lincenced by GNU General Public License v3.0
# Use it, distribuite it, modify it, and give the changes to community
# 14 April 2019 - Maringá - PR - Brazil.
# Version 0.2
#
from __future__ import unicode_literals, division, absolute_import, print_function

try:
    from sigil_bs4 import BeautifulSoup
except:
    from bs4 import BeautifulSoup

import re, os


# Find number from inDesign and change to <span epub:type="pagebreak" id="page1" title="1"></span> 

def substitutePageNum(bk):  
    for (id, href) in bk.text_iter(): 
        html = bk.readfile(id) 
        # html_orig = html
        print ('File found %s:' % href)
        html = re.sub(r'<span class="pageNumber(.*?)>(.*?)</span>', r'<span epub:type="pagebreak" role="doc-pagebreak" id="page_\2" title="\2"></span>', html, flags=re.DOTALL)  
        #if not html == html_orig: 
        bk.writefile(id, html)
        #return 0


def run(bk):
    # get epub version number
    if bk.launcher_version() >= 20160102:
        epubversion = bk.epub_version()
    else:
        epubversion = BeautifulSoup(bk.get_opf(), 'lxml').find('package')['version']

    # get preferences
    prefs = bk.getPrefs()
    if prefs == {}:
        prefs['tag'] = 'span'
        prefs['attribute'] = 'epub:type'
        prefs['value'] = 'pagebreak'
        bk.savePrefs(prefs)
        prefs = bk.getPrefs()
    tag = prefs['tag']
    attribute = prefs['attribute']
    value = prefs['value']

    # get nav doc and toc.ncx ids
    nav_id = ncx_id = None
    ncx_id = bk.gettocid()

    if epubversion.startswith('3'):
        opf_soup = BeautifulSoup(bk.get_opf(), 'lxml')
        if opf_soup.find('item', {'properties' : 'nav'}) is not None:
            nav_id = opf_soup.find('item', {'properties' : 'nav'})['id']
        else:
            print('Nav document ID not found!')
                
    ncx_pagelist = '\n  <pageList>\n    <navLabel>\n      <text>Pages</text>\n    </navLabel>'
    nav_pagelist = '    <nav epub:type="page-list" id="page-list">\n      <ol>\n'
    page_targets = 0
       

    substitutePageNum(bk)


    # get all html files
    page_dic = {}
    errors = 0
    for (html_id, href) in bk.text_iter():
        html = bk.readfile(html_id)
    
        
        # load html code into BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        # find pagebreaks
        page_numbers = soup.find_all(tag, {attribute : value})
        if not page_numbers:
            print('\nNo page number targets found in ' + os.path.basename(href))
        else:
            page_targets += len(page_numbers)
            print('\n' + str(len(page_numbers)) + ' page number targets found in ' + os.path.basename(href))
        
        # add pagelist entries to pagelist
        for page_number in page_numbers:
            
            # title has priority over string
            if page_number.has_attr('title'):
                title = page_number['title']
            else:
                title = page_number.contents[0]

            # generate id, if necessary
            if not page_number.has_attr('id'):
                id = 'page' + title
            id = page_number['id']

            # check for duplicate titles/ids
            if title not in page_dic:
                page_dic[title] = os.path.basename(href + '#' + id)
            else:
                errors += 1
                page_dic[title] += ' / ' + os.path.basename(href + '#' + id)
                print('ERROR: duplicate page number found:', title, page_dic[title])
            
            # epub2
            ncx_pagelist += '''\n    <pageTarget id="{}" type="normal" value="{}">
      <navLabel>
        <text>{}</text>
      </navLabel>
      <content src="{}"/>
    </pageTarget>'''.format(id, title, title, href + '#' + id)
            
            # epub3
            if nav_id:
                nav_pagelist += '        <li>\n          <a href="{}">{}</a>\n        </li>\n'.format(href + '#' + id, title)
    
    if errors != 0:
        print('Plugin aborted because of {} duplicate page number(s).'.format(str(errors)))
        return -1
    
    # add/replace NCX pagelist section
    if page_targets:
        ncx_pagelist += '\n  </pageList>'
        if ncx_id: 
            # get ncx contents
            ncx = bk.readfile(ncx_id)
            # delete existing pagelist
            ncx = re.sub('\s*\<pageList[^>]*\>.+?\<\/pageList\>\s*', '', ncx, flags = re.DOTALL)
            # add new pagelist
            ncx = ncx.replace('</ncx>', ncx_pagelist + '\n</ncx>')
            # update ncx file
            bk.writefile(ncx_id, ncx)
            print('\n' + str(page_targets) + ' page number targets found.\nNCX file updated. ')
        else:
            print('\nNCX file couldn\'t be found and updated.')
    else:
        print('\nNo page number targets found.\nNCX file not updated')

    # add/replace NAV pagelist section
    if nav_id:
        nav_pagelist += '      </ol>\n    </nav>'
        new_pagelist = BeautifulSoup(nav_pagelist, 'html.parser')
        # get nav contents
        nav = bk.readfile(nav_id)
        nav_soup = BeautifulSoup(nav, 'html.parser')
        orig_nav_soup = str(nav_soup)
        old_page_list = nav_soup.find('nav', {'epub:type' : 'page-list'})
        if old_page_list is not None:
            old_page_list.replace_with(new_pagelist)
            #print('Existing page-list updated.')
        else:
            nav_soup.body.insert(2, new_pagelist)
            #print('New page-list section added.')
        # update nav
        if str(nav_soup) != orig_nav_soup:
            try:
                bk.writefile(nav_id, str(nav_soup.prettyprint_xhtml(indent_level=0, eventual_encoding="utf-8", formatter="minimal", indent_chars="  ")))
            except:
                bk.writefile(nav_id, str(nav_soup))
            print('NAV file updated.')
        else:
            print('NAV NOT file updated.')
            
    print('\nPlease click OK to close the Plugin Runner window.')

    return 0

def main():
    print('I reached main when I should not have\n')
    return -1

if __name__ == "__main__":
    sys.exit(main())
