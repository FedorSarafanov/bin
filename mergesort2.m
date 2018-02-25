function b=mergesort2(a)
k=length(a);
b=[];
for i=1:k
    b=merg(b,a(i));
end
end