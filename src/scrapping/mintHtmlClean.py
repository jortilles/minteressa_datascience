# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 19:20:28 2016

@author: jortilles
"""

import re


class MintHtmlClean:

        
    def clean( self, html ):
        
               
        
        res = html.replace('\n', ' ').replace('\r', '').replace( '\t',' ').replace('  ', ' ' ) 
        #scripts 
        
        res = re.sub('(<script).*^(<script).*(script>)',' ',res) 
        
        #styles
        res = re.sub('(<style).*^(<style)(style>)',' ',res) 
        print html 
       # print "\n\n\n", res   
        
        
        return res
    

            
