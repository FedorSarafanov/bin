function c=merg(x,y)
  k=length(x);
  m=length(y);
  if (k==0) || (m==0)
    c=[x y];
  else
      if x(1)<=y(1)
        if (k==1) && (m==1)
          c=[x y];
          return
        end
        x0=x(1);
        x=x(2:k);
        c=merg(x,y);
        c=[x0 c];
      else
        if (k==1) && (m==1)
          c=[y x];
          return
        end
        y0=y(1);
        y=y(2:m);
        c=merg(x,y);
        c=[y0 c];
      end
  end
end