import pandas as pd 
import numpy as np 
import requests # For getting the HTML file
import lxml # For reading the table in the HTML file
import xlrd # For reading and writing Excel files from python

# The URL we need to scrape
url = 'http://mnregaweb4.nic.in/netnrega/FTO/ResponseDetailStatusReport.aspx?lflag=&flg=W&page=s&state_name=MADHYA+PRADESH&state_code=17&district_name=AGAR-MALWA&district_code=1751&fin_year=2016-2017&typ=R&mode=B&source=national&Digest=mRrYMJ/BWPQRbL5KdQ/yqQ'
html = requests.get(url).content

# read_html gies list of all tables in the HTML file, in pandas format
df_lists = pd.read_html(html)
df = df_lists[3] # The 4th table is what we are concerned with - it's the one with all the information

# Extracting column names from test output format file, to ensure uniformity in final output format
df_excel = pd.read_excel('epod_test_output.xlsx')
df.columns = df_excel.columns
df.drop([0], inplace=True)

# Saving the file to excel
df.to_excel('sansiddh_epod_test_output.xlsx', index=False)