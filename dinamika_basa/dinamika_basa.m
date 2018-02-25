function dinamika_basa
                           %  Динамика дислокаций в зерне
tic
    T=500;  
    b0=3.0e-04;   
    b=b0; 

    Dx=2;  
    Dy=2; 

    cx=1; 
    cy=1;   
    h=3000;  
    N=1;
    a=0.001;   
    na=1;         
    ds=0.1;         
    Sila=0.001;  
    omega=0.04;  
    omeg=zeros(1,2); 
    n0=300;    
    qp=0;  
    qm=0; 

xdd=[0.5*Dx 0]; 
ydd=[0 0];  

xd=[0.5*Dx ]; 
yd=[0 ];


x=Dx*rand(1,N);  
y=Dy*rand(1,N);  

q1=zeros(1,T); 
q2=zeros(1,T); 
 %xj=zeros(T,n0);  yj=zeros(T,n0); bj=zeros(T,n0);

 hp = plot(x,y,'b.',x,y,'r.',0,0,'k^');
                 %mov = avifile('ex.avi','QUALITY',100)


%   Итерационный процесс
for i=1:T;          
        
     omeg=omega.*[1  0];
    [x,y]= iter(x,y,xdd,ydd,b,omeg,Sila,h);
        
                
                %  Рождение дислокаций
 xi=(Dx-2*ds).*rand(1,na)+ds;  yi=(Dy-2*ds).*rand(1,na)+ds;        
           if rem(i,2)==0
               xii=xi-ds;      yii=yi;
           else
                xii=xi+ds;     yii=yi;
           end
    x=[x xi xii];  y=[y yi yii];  bn=b0*ones(1,na);    b= [b bn -bn];   
                
      % Аннигиляция дислокаций        
     g1=find(b>0);  g2=find(b<0);
 for j=g1
     A=(x(g2)-x(j)).^2+(y(g2)-y(j)).^2;      [e,ii]=min(A);  k=g2(ii);
          if  e<a;   g1=setdiff(g1,j);   g2=setdiff(g2,k);   end;
 end
     x1=x(g1); y1=y(g1);  x2=x(g2); y2=y(g2); b1=b(g1); b2=b(g2);
     x=[x1 x2]; y=[y1 y2]; b=[b1 b2]; 

           % Накопление деформации
    kp=find(x>Dx);   if min(kp)>0;    qp=qp+length(kp);    end;
    km=find(x<0);    if min(km)>0;   qm=qm+length(km);    end;
                  q1(i)= qp;  q2(i)=qm; 

%--   Формирвание массива для сохранения                          
   nn(i)=length(y);     ki=1:nn(i);
% xj(i,ki)=x; yj(i,ki)=y;  bj(i,ki)=b;
%-------------------------------------     
           %  Сток дислокаций  
   kk=find(x<0 | x>Dx);  si=setdiff(ki,kk); x=x(si); y=y(si); b=b(si);      

        %Рост субграницы
    f1=find(abs(x1-Dx/2)<Dx/4);    f2=find(abs(x2-Dx/2)<Dx/4);
      No(i)=length(f1)-length(f2);     
      
    
    %  Динамика дислокаций (мультфильм)     
 set(hp(1),'xdata', x1,'ydata',y1, 'erase','xor','MarkerSize',14)
 set(hp(2),'xdata', x2,'ydata',y2, 'erase','xor','MarkerSize',14)
 set(hp(3),'xdata', xd,'ydata',yd, 'erase','xor','MarkerSize',12,'MarkerFaceColor','black')
 drawnow
          axis([-0.2  Dx+0.2 0 Dy]);  grid on
 %    F = getframe(gca); mov = addframe(mov,F);
end
% mov = close(mov);

toc
%========================




t=1:T; R=nn./(Dx*Dy*1e-8); 
e2=q2.*b0/Dy; e1=q1.*b0/Dy;   O=No.*b0/Dy;

figure
subplot(2,2,1)
hist(x1,40); hhi=get(gca,'Children'); set(hhi,'FaceColor','c'); axis([0 Dx 0 50 ]); 
subplot(2,2,2)
hist(x2,40) ;hhii=get(gca,'Children'); set(hhii,'FaceColor','c'); axis([0 Dx 0 50 ]); 
subplot(2,2,3)
plotyy(t,R,t,O); % axis([0 0.15 0 6e9])
subplot(2,2,4)
plot(t,e1,t,e2)



%%%%%%%%%%%%%%%%%%%%%%%%%%
function [x,y]= iter(x,y,x0,y0,b,omega,Sila,h)
N=length(y);   G=zeros(1,N);  %No=length(omega);   Go=zeros(1,No);

    for j=1:N;  
        G(j)= sum(b.*Gxy(x(j)-x,y(j)-y)); 
    end      
     Go=omega(1).*Dxy(x-x0(1),y-y0(1))+omega(2).*Dxy(x-x0(2),y-y0(2));   
     S=sinh(b.*(Sila+G+Go));     x=x+h.*S;
%============================
function f =Dxy(x,y)
b=3.0e-18;     f= - y.*x./(x.^2+y.^2+b^2);
%---------------------------------      
function f =Gxy(x,y)
b=3.0e-18;   f = x.*(x.^2-y.^2)./(x.^2+y.^2+b^2).^2;


