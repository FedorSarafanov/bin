function vdp
t=[0 1400];
y0=[-0.2553    0.0656    0.0743    0.0301];
 
[T,Y]=ode15s(@myfun, t, y0);
%plot(T,Y(:,1),'-',T,Y(:,2),'x')
plot(T,Y(:,1));
ylim([-2 2]);
%hold on;
%plot(Y(:,4),Y(:,1));

function dy = myfun(t,A)
a=0.1;
epsilon1=0.001;
epsilon2=0.1;
gamma=0.02;
omega=0.5;
alpha=5;
beta=10;
I=-0.17;
d=0.7;
%d=0;

dy = zeros(4,1);   
dy(1) = 1/epsilon1*(A(1)*(1-A(1))*(A(1)-a)-A(2)-d*A(3));
dy(2) = epsilon2*(A(1)-I);
dy(3) = A(4);
dy(4) = (gamma*(1-alpha*I+beta*A(1))-A(3)^2)*A(4)-omega^2*A(3);




