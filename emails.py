import re
import os
from bs4 import BeautifulSoup
import pandas as pd

email_regex = r'[\w.-]+@[\w.-]+'

for roots, dirs, files in os.walk('./html'):
    for name in files:
        if not name.startswith('.'):
            filepath = os.path.join(roots, name)
            content = open(filepath)
            soup = BeautifulSoup(content, "lxml")
            text = soup.get_text()
            emails = re.findall(email_regex,text)
            df = pd.DataFrame(data=emails)
            filename = name.strip('.html') + '_emails.csv'
            df.to_csv(os.path.join('./output',filename),index=False,header=False)
            if not os.path.exists('./processed_files'):
                os.makedirs('./processed_files')
            os.rename(filepath,os.path.join('./processed_files', name))


