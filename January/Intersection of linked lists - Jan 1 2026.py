# Intersection in Y Shaped Lists - find intersection point for 2 linked lists

class Solution:
    def intersectPoint(self, head1, head2):
        a,b=head1,head2
        while a!=b:
            a=a.next if a.next else head2
            b=b.next if b.next else head1
        return a
