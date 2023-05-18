#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Control import *
control=Control()

for i in range(10,-10,-1):
	control.attitude(0,0,i)
	time.sleep(0.1)
control.stop()

