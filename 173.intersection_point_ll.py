class Solution:
    
    def intersetPoint(self,head1,head2):
        #code here
        d1 = head1
        d2 = head2
        
        while(d1!=d2):
            if(d1==None):
                d1 = head2
            else:
                d1=d1.next
                
            if(d2==None):
                d2 = head1
            else:
                d2 = d2.next
        
        return d1.data
