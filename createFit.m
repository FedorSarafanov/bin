% tdfread('/home/lab/neiro/data/img2.tsv','\t')
% [xData, yData] = prepareCurveData(x, y2);
% ft = fittype( 'smoothingspline' );
% [fitresult, gof] = fit( xData, yData, ft );
% 
%x=0:0.001:0.89;
% y=fitresult(x);
%y=fittedmodel4(x);

fid = fopen('/home/lab/neiro/data/berst_matlab.tsv', 'wt+');
fprintf(fid, 'x\ty\n','');
for i=1:1:length(X)
    fprintf(fid, '%g\t%g\n', [X(i) Y(i)]);
end
fclose(fid);