function c=merge2(x,y)
    lx=length(x);
    ly=length(y);
    ix=1;iy=1;ic=1;
    c=zeros(1,lx+ly);
    while ((ix<=lx) && (iy<=ly))
        if x(ix)<y(iy)
            c(ic)=x(ix);
            ix=ix+1;
        else
            c(ic)=y(ic);
            iy=iy+1;
        end
    end
end
    