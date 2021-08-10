import os
import re
import sys
import glob
import errno
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

contagemhtmlinicial = 0

contagemhtml = open('contagem2.csv','w')

for root, dirpath, fname in os.walk('Z:\\'):
    for name in fname:
        if re.match(r'\d+_\d+_\d+_\d+', name):
            if name.endswith('.html'):
                path = os.path.join(root, name)
                try:
                    with open(path) as f: # No need to specify 'r': this is the default.
                        soup = BeautifulSoup(f,'lxml')
                        
                        table = soup.findAll("table")[1]
                        row_marker = 0
                        for row in table.findAll('tr')[1::2]:
                            #parsingmline.writelines('<tr>')
                            column_marker = 0
                            #htdoc.writelines(str(row))
                            columns = row.findAll('td')
                            for column in columns:
                                #parsingmline.writelines('<td>')
                                #new_table.iat[row_marker,column_marker] = column.get_text()
                                #htdoc.writelines(str(column.get_text())+ 'Ä')
                                print(str(column.get_text()+ '&'))
                                #parsingmline.writelines(str(column.get_text()+ '&'))
                                #htdoc.writelines('Ú')
    
                                column_marker += 1   
                                
                        table2 = soup.findAll("table")[2]
                        row_marker2 = 0                    
                        for row2 in table2.find_all('tr')[1::2]:
                            column_marker2 = 0
                            
                            columns2 = row2.find_all('td')
                            for column2 in columns2:
                                #parsingmline.writelines('<td>')
                                #new_table2.iat[row_marker2, column_marker2] = column2.get_text()
                                #htdoc.writelines(str(column2.get_text())+'Ú')
                                #htdoc.writelines('Ú')
                                print(str(column2.get_text())+'&')
                                #parsingmline.writelines(str(column2.get_text()+ '&'))
                                column_marker2 += 1
                        
                        try:
                            table3 = soup.findAll("table")[3]
                            row_marker3 = 0                    
                            for row3 in table3.find_all('tr')[1::2]:
                                column_marker3 = 0
                                
                                columns3 = row3.find_all('td')
                                for column3 in columns3:
                                    #parsingmline.writelines('<td>')
                                    #new_table2.iat[row_marker2, column_marker2] = column2.get_text()
                                    #htdoc.writelines(str(column2.get_text())+'Ú')
                                    #htdoc.writelines('Ú')
                                    print(str(column3.get_text())+'&')
                                    #parsingmline.writelines(str(column2.get_text()+ '&'))
                                    column_marker3 += 1

                            table4 = soup.findAll("table")[4]
                            row_marker4 = 0                    
                            for row4 in table4.find_all('tr')[1::2]:
                                column_marker4 = 0
                                
                                columns4 = row4.find_all('td')
                                for column4 in columns4:
                                    #parsingmline.writelines('<td>')
                                    #new_table2.iat[row_marker2, column_marker2] = column2.get_text()
                                    #htdoc.writelines(str(column2.get_text())+'Ú')
                                    #htdoc.writelines('Ú')
                                    print(str(column4.get_text())+'&')
                                    #parsingmline.writelines(str(column2.get_text()+ '&'))
                                    column_marker4 += 1
                            
                        except:
                            print('arquivo com apenas duas tabelas')
                        else:
                            pass
                except IOError as exc:
                    if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
                        raise # Propagate other kinds of IOError.    
                
                contagemhtmlinicial += 1
                contagemhtml.writelines(str(f)+'\n')    
                print(name)

print(contagemhtmlinicial)  
contagemhtml.flush()
contagemhtml.close()