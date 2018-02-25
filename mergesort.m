function c=mergesort(a)
n=length(a);
c=[];
if n>1
    m=round(n/2);
    m1=m+1;
    c=merg(mergesort(a(1:m)),mergesort(a(m1:n)));
else
    c=a;
end
end