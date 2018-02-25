 
       a1 =      0.7285  
       b1 =      0.4692  
       c1 =      0.9225 
       a2 =     0.07252  
       b2 =      -1.387 
       c2 =      0.4689 
       a3 =       1.001  
       b3 =     -0.3643  
       c3 =      0.9746 
       a4 =     0.07781 
       b4 =       1.418 
       c4 =      0.4373 


FF=@(x) a1*exp(-((x-b1)/c1).^2) + a2*exp(-((x-b2)/c2).^2) + a3*exp(-((x-b3)/c3).^2) + a4*exp(-((x-b4)/c4).^2)
tdfread('b_x.csv');
b=x10t;

L=28.3; %mm

%Метод мой
arr=find(abs(l)<28.3/2);
Bx1=sum(b(arr))*0.5;


%Метод не мой
Bx2=integral(FF,-28.3/2,28.3/2);
Bx22=integral(FF1,-28.3/2,28.3/2);

%Старый метод
Bx3=1.43*L;

disp(Bx1)
disp(Bx2)
disp(Bx22)
disp(Bx3)



