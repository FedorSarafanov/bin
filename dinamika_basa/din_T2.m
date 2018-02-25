                   %  Динамика дислокаций в зерне

function   dinamika_alpha
tic
   T=1500;     alpha=0;    al=alpha*(pi/180);
   omeg=zeros(1,2);
   b0=3.0e-04;   Dx=2;  Dy=2;   cx=1; cy=1;   h=2000;   hy=10;
      
   h0=0.1*Dy;  L0=Dy;     L=0:h0:Dy; aa=20;
   
   xa=0.1;  xb=0.02;    ds=0.11;        na=1;   
   
   % Тензор внешних напряжений Qij
    Sxy_a=0.001;
  Qxy=  cos(2*al).*Sxy_a;    Qxx= - sin(2*al).*Sxy_a;     Qyy=   sin(2*al).*Sxy_a;  
  Qij=[Qxy; Qxx; Qyy];
 
  omega=0.03; 
  
  z=-10:10;
  for i=1:30
     p(i,:) =z.*tan(al)+0.2.*(i-16);
  end
     p(30,:) =(z-1).*tan(pi/2+al);
  
  xd=[0.5*Dx]; yd=[0.5*Dy];
  b=[b0 -b0];   x =[0 0.1];  y=[0.5 0.5] ;  n0=300;

 qp=0;  qm=0;     qp1=0;  qm1=0;        qp2=0;  qm2=0; jj=0;
 
 q1= zeros(1,T); q2= zeros(1,T); 
 xj=zeros(T,n0);  yj=zeros(T,n0); bj=zeros(T,n0);


 D=Dx;    hf=D/27;    t=0:hf:D;   R2=2*D;   
[xf,yf]=meshgrid(t,t);
 
 hp = plot(x,y,'b.',x,y,'r.',0,0,'k^',z,p,'b:');
axis([0  Dx 0 Dy]); 
 %mov = avifile('ex.avi','QUALITY',100)
                 %   Итерационный процесс
for i=1:T;          
 % if omega <om;  omega=omega+om/T1;   end
        
 [x,y]= iter(x,y,xd,yd,b,omega,Qij,h,hy,al,Dy);
 
  nn(i)=length(y);    R(i)=nn(i)./(Dx*Dy*1e-8); 
 
 if   rem(i,T/100)==0 
     jj=jj+1;   tt(jj)=i;  
     
    [Sxy,Sx,Sy,Dxy,Dxx,Dyy,Pxy,Px,Py]= W_sis(xf,yf,xd,yd,x,y,b,omega,D,Sxy_a);
        W_s =3.*(Sxy.^2-Sx.*Sy)+ (Sx+Sy).^2;
        Wd =3.*(Dxy.^2-Dxx.*Dyy)+ (Dxx+Dyy).^2;
        W_p =3.*(Pxy.^2-Px.*Py)+ (Px+Py).^2;
        
      %  Вычисление  полной   энергии 
Ep(jj)=hf.^2.*trapz(trapz(W_p))./(8.*pi*omega^2)/4;
Es(jj)=hf.^2.*trapz(trapz(W_s))./(8.*pi*omega^2)/4;
Ed(jj)=hf.^2.*trapz(trapz(Wd))./(8.*pi*omega^2)/4;

r_s(jj)=10^(4)*R(i).^(-1/2);
r_d(jj)=D.*(Es(jj)./Ed(jj)).^(2/3);

end

   
    %  Рождение дислокаций
 xi=(Dx-2*ds).*rand(1,na)+ds;  yi=(Dy-2*ds).*rand(1,na)+ds;        
           if rem(i,2)==0
               xii=xi-ds.*cos(al);      yii=yi-ds.*sin(al);
           else
                xii=xi+ds.*cos(al);     yii=yi+ds.*sin(al);
           end
    x=[x xi xii];  y=[y yi yii];  bn=b0*ones(1,na);    b= [b bn -bn];   
                
      % Аннигиляция дислокаций        
     g1=find(b>0);  g2=find(b<0);
 for j=g1
     A=((x(g2)-x(j))./xa).^2+((y(g2)-y(j))./xb).^2;      [e,ii]=min(A);  k=g2(ii);
          if  e<1;   g1=setdiff(g1,j);   g2=setdiff(g2,k);   end;
 end
     x1=x(g1); y1=y(g1);  x2=x(g2); y2=y(g2); b1=b(g1); b2=b(g2);
     x=[x1 x2]; y=[y1 y2]; b=[b1 b2]; 

      % Накопление деформации на левой границе
  km=find(x<0);    
  for ii=km;   if b(ii)<0;   qm=qm+1;
             elseif b(ii)>0;  qm=qm-1;   end; 
  end;      q2(i)=qm.*cos(al); 
     
   % Накопление деформации на левой нижней границе
  km=find(y<0);    
  for ii=km;   if b(ii)<0;   qm1=qm1+1;
             elseif b(ii)>0;  qm1=qm1-1;   end; 
  end;      q4(i)=qm1.*sin(al); 
     
        % Накопление деформации на правой границе
 kp=find(x>Dx);   
 for ii=kp;   if b(ii)>0;   qp=qp+1;
         elseif b(ii)<0;    qp=qp-1;  end; 
 end;       q1(i)= qp.*cos(al);
 
 
     
   % Накопление деформации на правой верхней границе
 kp=find(y>Dy);   
 for ii=kp;   if b(ii)>0;   qp1=qp1+1;
         elseif b(ii)<0;    qp1=qp1-1;  end; 
 end;       q3(i)=qp1.*sin(al);
   Er(i)=b0*(q1(i) +q3(i))./Dy  ;
   El(i)=b0*(q2(i) +q4(i))./Dy  ;
 
   E3(i)=b0*(q3(i))./Dy  ;
   E4(i)=b0*(q4(i))./Dy  ;
 
 
 
 
%--   Формирвание массива для сохранения                          
 nn(i)=length(y);   ki=1:nn(i);
 %xj(i,ki)=x; yj(i,ki)=y;  bj(i,ki)=b;
 
%  Сток дислокаций  
   kk=find(x<0 | x>Dx| y<0 | y>Dy);  si=setdiff(ki,kk); x=x(si); y=y(si); b=b(si);      

      
    %Рост субграницы
    ki=1:length(y1);  
    f1=find(abs(x1-Dx/2)<aa);  f2=find(abs(x2-Dx/2)<aa);      
    si=setdiff(ki,f1); yz=y1(si); xz=x1(si);     
    No(i)=length(f1)-length(f2);     
        
    
    %  Динамика дислокаций (мультфильм)     
 set(hp(1),'xdata', x1,'ydata',y1, 'erase','xor','MarkerSize',14)
 set(hp(2),'xdata', x2,'ydata',y2, 'erase','xor','MarkerSize',14)
 set(hp(3),'xdata', xd,'ydata',yd, 'erase','xor','MarkerSize',12,'MarkerFaceColor','black')
set(hp(4),'xdata', z,'ydata',p(1), 'erase','xor')
 drawnow
          axis([0  Dx 0 Dy]);  grid off
 %    F = getframe(gca); mov = addframe(mov,F);
end
% mov = close(mov);
figure
    s1=find(x1<Dx | x1>0);       s2=find(x2<Dx | x2>0);   
    dx=0.02*Dx;  dy=0.02*Dy; %dx=0;  dy=0;
%d1=Dx/2-0.1;  d2=Dx/2+0.1; a=Dy;
%fill([d1 d1; d1 d2; d2 d2; d2 d1],[0 a; a a;a 0; 0 0],'y')
%hold on 
text(x1(s1)+dx,y1(s1)+dy,'\bf\perp','Color',[0 0 1],'Rotation',[alpha])
text(x2(s2)-dx,y2(s2)-dy,'\bf\perp','Color',[1 0 0],'Rotation',[180+alpha])
%text(0,Dy*(1+0.025),'mkm ');   text(Dx*(1+0.01),-0.035*Dy,', mkm ');
hold on
plot(xd,yd,'Marker','^','MarkerSize',10,'MarkerFaceColor','black'); hold on 
      grid on;   box on;
 axis([0 Dx 0 Dy]); 

  toc
%========================

subplot(2,2,1)
   s1=find(x1<Dx | x1>0);       s2=find(x2<Dx | x2>0);   
    dx=0.02*Dx;  dy=0.02*Dy;    % dx=0;  dy=0;
text(x1(s1)-dx,y1(s1)+dy,'\bf\perp','Color',[0 0 1],'Rotation',[alpha])
text(x2(s2)+dx,y2(s2)-dy,'\bf\perp','Color',[1 0 0],'Rotation',[180+alpha])
hold on
plot(xd,yd,'Marker','^','MarkerSize',12,'MarkerFaceColor','black'); hold on 
      grid on;   box on;
 axis([0 Dx 0 Dy]); 

subplot(2,2,2)
plot(tt,Ed,tt,Es);title('W');  %plot(tt,Ed);title('Wd')
%hist(x2,40) ;hhii=get(gca,'Children'); set(hhii,'FaceColor','c'); axis([0 Dx 0 50 ]); 

%%%%%%%%%%%%%%%%%%%%%%%%%%
function [x,y]= iter(x,y,xd,yd,b,omega,Qij,h,hi,a,Dy)
N=length(y);   
G_xy=zeros(1,N);  G_xx=zeros(1,N);  G_yy=zeros(1,N);  
  for j=1:N;  
      [Gxy,Gxx,Gyy] =disl(x(j)-x,y(j)-y,a);
      G_xy(j)=sum(b.*Gxy);
      G_xx(j)=sum(b.*Gxx);
      G_yy(j)=sum(b.*Gyy);
  end      
     
  [Dxy,Dxx,Dyy] =disclin(x-xd,y-yd,Dy);
     Sxy=omega.*Dxy+G_xy+Qij(1);  
     Sxx=omega.*Dxx+G_xx+Qij(2); 
     Syy=omega.*Dyy+G_yy+Qij(3);
     %---------------------------------------------------------------------
     
     S1=sin(2.*a).*(Syy-Sxx)./2+cos(2.*a).*Sxy;
     S_y=cos(a).^2.*(Sxx)+ sin(a).^2.*(Syy) + sin(2.*a).*Sxy;
     
     Fx=b.*S1.*cos(a);  Fy=b.*S1.*sin(a);
     Fx2=b.*S_y.*sin(a);  Fy2=-b.*S_y.*cos(a);
     
     x=x+h.*Fx+hi.*Fx2;     y=y+h.*Fy+hi.*Fy2;
%============================
function [Dxy,Dxx,Dyy] =disclin(x,y,R2)
b=3.0e-18;   r2=x.^2+y.^2+b^2; 
Dxy= - y.*x./r2;
Dxx= 0.5.*log(r2./R2)+ y.^2./r2;
Dyy= 0.5.*log(r2./R2)+ x.^2./r2;

%---------------------------------      
function [Gxy,Gxx,Gyy] =disl(x,y,a)
b=1.e-10;   r4=(x.^2+y.^2+b^2).^2;
Gxy = (x.*cos(a)+y.*sin(a)).*(x.^2-y.^2)./r4;
Gxx = - (  y.*(3.*x.^2+y.^2).*cos(a)  -  x.*(x.^2-y.^2).*sin(a)  )./r4;
Gyy = (  x.*(3.*y.^2+x.^2).*sin(a)  +  y.*(x.^2-y.^2).*cos(a)  )./r4;

%== Поля от  дисклокационной наклонной стенки ==

function [Pxy,Pxx,Pyy,Dxy,Dxx,Dyy,Sxy,Sxx,Syy]= W_sis(xi,yi,xd,yd,x,y,b,omega,D,Sila)

G=length(y);   Syy=0;Sxx=0;Sxy=0;
for j=1:G
[Gxy,Gxx,Gyy] =Disl_1(xi-x(j),yi-y(j),b(j),0);
   Syy =Syy + Gyy; Sxx =Sxx + Gxx; Sxy =Sxy + Gxy;
end
[Dxy,Dxx,Dyy] =disclin_1(xi-xd,yi-yd,omega,D);
% -- Суммарное Поле 
  Pyy =Syy+Dyy;   Pxx =Sxx+Dxx;   Pxy =Sxy+Dxy+Sila; 
  
%===== Поля от дисклокации ====
function [Gxy,Gxx,Gyy] =Disl_1(x,y,b,al)
b0=1.0e-2;   r4=(x.^2+y.^2+b0^2).^2;
Gxy = b.*(x.*cos(al)+y.*sin(al)).*(x.^2-y.^2)./r4;
Gxx = - b.*( y.*(3.*x.^2+y.^2).*cos(al) - x.*(x.^2-y.^2).*sin(al)  )./r4;
Gyy = b.*( x.*(3.*y.^2+x.^2).*sin(al) + y.*(x.^2-y.^2).*cos(al)  )./r4;

%===== Поля от дисклинации =======
function [Dxy,Dxx,Dyy] =disclin_1(x,y,omega,D)
b0=3.0e-04;   r2=x.^2+y.^2+b0^2;  R2=D^2 
Dxy= - omega.*y.*x./r2;
Dxx= omega.*(0.5.*log(r2./R2)+ y.^2./r2);
Dyy= omega.*(0.5.*log(r2./R2)+ x.^2./r2);





