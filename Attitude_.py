#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Control import *
control=Control()

for i in range(15):
    control.attitude(0,0,i)

control.stop()

