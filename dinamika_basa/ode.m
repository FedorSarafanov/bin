function ode
    %plot(resh(45,1));
   [X,Y]=resh(45,1);
   figure
   plot(X,Y);
%    disp(z)
    ylim([0 inf]);
end


function [X,Y]=resh(alpha,k)
T=0:0.005:5;
V=10;
Vy=V*sin(alpha*pi/180);
Vx=V*cos(alpha*pi/180);
[t,y]=ode45(@(t,y) ddy(t,y,k),T,[0 Vy]);
[t,x]=ode45(@(t,x) ddx(t,x,k),T,[0 Vx]);

X=x(:,1);
Y=y(:,1);

end

function ff=f(x,y)
    ff=cos(x+y)+(3/2)*(x-y);
end


function ddy=ddy(t,y,k)
g=9.8;
%k=5;
m=1;
    ddy=[y(2); -g-k/m*y(2)];
end

function ddx=ddx(t,x,k)
g=9.8;
m=1;
    ddx=[x(2); -k/m*x(2)];
end