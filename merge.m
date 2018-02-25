function c=merge(x,y)
  k=length(x);
  m=length(y);
  if k==0
    c=y;
  end
  if m==0
    c=x;
  end
  if x(1)<=y(1)
    if (k==1) or (m==1)
      c=[x y];
      return
    end
    x=x(2:k);
    c=merge(x,y);
    c=[x(1) c];
  else
    if (k==1) or (m==1)
      c=[x y];
      return
    end
    y=y(2:m);
    c=merge(x,y);
    c=[y(1) c];
  end
end
    