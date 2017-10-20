%% calculate contour of protein
%% by Fei, Oct 14, 2017
function c=pcontour(e,f)
pp=0.5;
pd=1;
ld=16*0.676; %contour length of DNA linker
lo=441.5;% length of 8helex
%an_ratio=0.6666;
%l0=[2.99 2.99 2.99 2.99 2.99 0]';
xp=XWLCContour(f,pp,80000);
%xd=XWLCContour(f,ld,1800);
xd=eFJContour(f,ld);
%xo=XFJContour(f,lo);
ep=e-2*xd-2*lo;
figure;
plot(ep)
% ep=e-2*xo*lo
c=ep./xp
c=c-c(length(e));