%% functionnme: function description
% function  [Bx1,Bx2,Bx3]= f(L)

% ������������� �������� ������

a1 = 1.428;%  (1.425, 1.43)
b1 = -0.2581;%  (-0.2927, -0.2235)
c1 = 25.06;%  (25, 25.11)
FF=@(x)  a1.*exp(-((x-b1)./c1).^2);
tdfread('b_x.csv');
b=x10t;

% L=28.3; %mm
global L;

%����� ���
arr=find(abs(l)<L/2);
Bx1=sum(b(arr))*0.5;


%����� �� ���
Bx2=integral(FF,-L/2,L/2);

%������ �����
Bx3=1.43*L;

disp(['�����:'])
disp(Bx1)
disp(['��������:'])
disp(Bx2)
disp(['���������:'])
disp(Bx3)

% end

