
# coding: utf-8

# In[8]:

from databaker.framework import *


# In[9]:

tabs = loadxlstabs('beatlebattle.xlsx')


# In[10]:


conversionsegments = []

# only 1 but conventions n all
for tab in tabs:
    
    obs = tab.excel_ref('B4').expand(DOWN).expand(RIGHT)
    
    beatlenames = tab.excel_ref('B3').expand(RIGHT)
    
    dimensions = [
                HDim(beatlenames, 'Name', DIRECTLY, ABOVE),
                ]
    
    conversionsegment = ConversionSegment(tab, dimensions, obs)
    conversionsegments.append(conversionsegment)
    
    


# In[11]:


# proceed to output
outputfile = 'trial_beatlesoutput.csv'
writetechnicalCSV(outputfile, conversionsegments)

