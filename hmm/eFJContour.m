function exte = eFJContour(F, L, kT)
% extension x
% x = XFJCContour(F, L, S, kT, option)
%     or
% x = XFJCContour(F, L, S, kT)
%     or
% x = XFJCContour(F, L, S)
%     or
% x = XFJCContour(F, L)
%     or
% x = XFJCContour(F) %the defaults are used in this case
%
% Defaults: KT=4.14
%           ? S=8000 for 8-helix origami 
%           L=660
%           Returns x by default
%
% Calculates extension x given force F (pN), contour length L (nm),
% and stretch modulus S (pN).
%


% Default Values
if nargin < 3
    kT = 4.14;
end
% if nargin < 3
%     S = 8000;
% end
if nargin < 2
    L=20;
end
b=1.5;
S=800;
% Simplification Variables
%a=1;
%b=2*kT/(F.*L);
%c=-1;
%Solving the quadratic equation
%z1=(-b+sqrt(b^2-4*a*c))/(2*a);
%z2=(-b-sqrt(b^2-4*a*c))/(2*a);
%x=L*(z1+F./S);

exte=L.*(coth(F*b/kT)-kT./(F*b)).*(1+F/S);
% exte=exte';
end    