%%% calculate the extension and force of each state
%%% by WF Oct 14,2017
%%% input: decoded state sequence
%%%        force sequence
%%%        extension sequence
function [exten, forc]=ef_cal(f,e,d)
forc=zeros(max(d)+1,1);
exten=zeros(max(d)+1,1);
num=zeros(max(d)+1,1);
for i =1:length(d)
    forc(d(i)+1)=forc(d(i)+1)+f(i);
    exten(d(i)+1)=exten(d(i)+1)+e(i);
    num(d(i)+1)=num(d(i)+1)+1;
end
forc=forc./num;
exten=exten./num;
end