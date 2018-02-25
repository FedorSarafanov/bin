ind=[];
for i=1:length(x)
    if (rem(i,3)==0)&(abs(y(i))<0.5)
        ind=[ind i];
    end
end
X=x;
Y=y;
X(ind)=[];
Y(ind)=[];

ind=[];
for i=1:length(X)
    if (rem(i,3)==0)&(abs(Y(i))<0.5)
        ind=[ind i];
    end
end
X(ind)=[];
Y(ind)=[]
