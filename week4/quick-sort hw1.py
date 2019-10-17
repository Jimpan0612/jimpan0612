#!/usr/bin/env python
# coding: utf-8

# In[39]:


#Quick-sort
#透過先訂定一個基準點來將其他數值分為大於或小於基準點，再從分割出來的兩堆數值重複取基準點的動作，重複此步驟直到所有欄位剩下一個數值無法再分割
def partition(list): 
    
    if len(list) <= 1: 
        return list #當列表的數值無法再分割時回報結果
    else:
        pivot=list[-1]  #取最後一個數為基準點
        equal=[]
        low=[]
        high=[]
    
        
        for i in list:
            if i>pivot:
                high.append(i) #取大於基準點的數值
            elif i < pivot:
                low.append(i) #取小於基準點的數值
            else:
                equal.append(i) #取相等數值
                
                
        return partition(low)+equal+partition(high) #將較小的數值放於基準點左側，將相等數值置中，將較大的數值放於基準點右側後取結果
    
#結果測試    
list1=[2,1,6,9,8,5,7] #全部正整數
list2=[9,-2,5] #正負整數交雜
list3=[-1,-3,2,-5,-1,0,-7,0,-1,2] #有同樣數值
partition(list1) 
partition(list2)
partition(list3)


# In[ ]:





# In[ ]:




